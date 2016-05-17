Installation
===============================================================================

Installation commands/instructions for installing MongoDB are listed here.


Installation of MongoDB using DevOps Tools
-------------------------------------------------------------------------------

1)	Create cookbooks for 3 main parts of MongoDB
Mongod
Mongos
Mongocfg

2)	Create the following folders in each cookbook
chef - Revision 20376: /trunk/cookbooks/mongod

..
attributes/
files/
recipes/
templates/

3)	Under the attributes create common.yaml which contains all the variables and values.
# this is where common attributes go which are shared across all environments
# mostly things like roleuser, deployment dir, etc.
app_name: mongod
deploy_dir: mongo
role_user: mongod

base_dir: /data/svc/mongo

conf_file: /data/svc/mongo/conf/mongod.conf
sysconf_file: /etc/sysconfig/mongod
db_dir: /data/svc/mongo/db
log_dir: /data/svc/mongo/log/
log_file: /data/svc/mongo/log/mongod.log
#storage_engine: mmapv1
storage_engine: wiredTiger

logappend: true

days_to_keep_logs: 7

4)	Create another file called hosts.yaml and add the following code
mongod-shard1:
  replica_set: replicaSet1
  node_group: "mongod-shard1"

mongod-shard2:
  replica_set: replicaSet2
  node_group: “mongod-shard2"

mongod-shard3:
  replica_set: replicaSet3
  node_group: "mongod-shard3"

mongod-shard4:
  replica_set: replicaSet4
  node_group: "mongod-shard4"

5)	Under Recipes, Create a ruby file called default.rb
require 'nv_helpers'
class Chef::Recipe
  include NvHelpers::NodeGroupHelper
end

# Make sure we have the appropriate users
localuser "mongod" do
  action :add
end

localuser "munin" do
  action :add
end

#####################
# Dependencies
#####################
#Install MongoDB
script "install modeling packages" do
  interpreter "bash"
  user "root"
  code <<-EOH
    yum install mongodb-org-3.2.6  -y 
    
  EOH
end

include_recipe "base::default"

#####################
# ulimit
#####################

ulimit_types = %W(hard soft)
item_types = %W(nofile nproc)
ulimit_types.each do |ulimit_type|
  item_types.each do |item_type|
    eharmonyops_limitsconf "mongod-#{item_type}-#{ulimit_type}" do
      target "mongod"
      type ulimit_type
      item item_type
      value "8192"
      action :add
    end
  end
end

#item_types = %W(memlock)
#ulimit_types.each do |ulimit_type|
#  item_types.each do |item_type|
#    eharmonyops_limitsconf "mongod-#{item_type}-#{ulimit_type}" do
#      target "mongod"
#      type ulimit_type
#      item item_type
#      value "64"
#      action :add
#    end
#  end
#end

# NOTE: munin-node uses port 4949, which needs to be open on the
# monitored system, so the agent can access this data source.
# See http://mms.10gen.com/help/install.html#hardware-monitoring-with-munin-node.
yum_package "munin-node"

# Disable separate init script for munin-node: we will launch it manually
# from the init script installed by this cookbook.
script "disable munin-node at startup" do
    interpreter "bash"
    user "root"
    code "chkconfig munin-node off"
end

#####################
# Post-Install Cleanup
#####################

script "post-install cleanup" do
  interpreter "bash"
  user "root"
  code <<-EOH
  chmod a+r  #{node[:config]['base_dir']}/bin/*.js
  chmod a+rx #{node[:config]['base_dir']}/bin/*.sh
  chkconfig --del mongod
  if [ -f /etc/init.d/mongod ]; then rm /etc/init.d/mongod; fi
  EOH
end

#####################
# Cron Section
#####################

# Log Rotate
cron "Daily rotation of mongod logs." do
    user node[:config][:role_user]
    minute "0"
    hour "0"
    command "#{node[:config]['base_dir']}/bin/logrotate.sh"
end


6)	Under template add scripts to create sharding and replicaset which was explained in original installation document.
logrotate.sh
rs_add_secondaries.js
rs_get_primary.js
rs_get_primary.sh
rs_initiate.js
rs_set_primary.js
rs_set_primary.sh

7)	Add mongo configuration file with following code.
#replica set
<% if node[:config][node[:service]] && node[:config][node[:service]].has_key?('replica_set') %>
replSet=<%= node[:config][node[:service]]['replica_set'] %>
<% end %>

#where to log
logpath=<%= node[:config]['log_file'] %>

#log overwritten or appended to
logappend=<%= node[:config]['logappend'] %>

#fork and run in background
fork=true

#path to data files
dbpath=<%= node[:config]['db_dir'] %>

storageEngine=<%= node[:config]['storage_engine'] %>

