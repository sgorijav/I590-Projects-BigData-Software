Configuration
===============================================================================

Configuration commands/instructions for MongoDB are listed here.

Setting up Mongodb ReplicaSets
We created 3 instances of mongod processes on each node that makes it as 3 node Replicaset. 
The following commands start 3 mongod processes on each server and add it to Replicaset.
	$> sudo ./bin/mongod --config  conf/mongo.conf --replSet replicaSet1
	$> sudo ./bin/mongod --config  conf/mongo1.conf --replSet replicaSet1
	$> sudo ./bin/mongod --config  conf/mongo2.conf --replSet replicaSet1

Go to Mongo shell and issue following Javascript commands to add 3 mongod instances into Replicaset.
	$> mongo ltnosql1n1:27000
	Mongo> cfg = {
                  '_id':'replicaSet1',
                  'members':[
                        {'_id':0, 'host': '10.0.225.60:27000'},
                        {'_id':1, 'host': '10.0.225.60:27001'},
                        {'_id':2, 'host': '10.0.225.60:27002'}
                  ]
              }

	Mongo> rs.initiate(cfg)
                
Repeat above for other 3 ReplicaSets called ReplicaSet2, ReplicaSet3 and ReplicaSet4. 
We are planning to create 4 Shard cluster.
Creating MongoDB Sharding Cluster
1)	Create directories to hold Mongodb configuration database.
2)	Issue the following command which creates Mongodb configuration database.
	$> sudo ./bin/mongod --configsvr --dbpath  /data/mongodb/con1/db --port 25000 --	
	logpath  /data/mongodb/logs/config.log –fork
3)	The following command creates mongos instance from where we can access Mongodb sharded cluster.
	$> mongos --configdb 10.0.225.57:25000 --logpath  /data/mongodb/logs/ mongos.log –fork
4)	Now access mongos instance by issuing following commands.

$> mongo 
	Mongos> 	sh.addShard("replicaSet1/10.0.225.57:27000,10.0.225.57:27001,10.0.225.57:27002")
	Mongos> 	sh.addShard(“replicaSet2/10.0.225.58:27000,10.0.225.58:27001,10.0.225.58:27002”)
	Mongos> 	sh.addShard(“replicaSet3/10.0.225.59:27000,10.0.225.59:27001,10.0.225.59:27002”)
	Mongos>sh.addShard(“replicaSet4/10.0.225.60:27000,10.0.225.60:27001,10.0.225.60:27002”	)
	mongos> sh.status()
--- Sharding Status --- 
	  sharding version: {
	"_id" : 1,
	"minCompatibleVersion" : 5,
	"currentVersion" : 6,
	"clusterId" : ObjectId("5702e230ebaaae6e5bffecc0")
	}
	  shards:
	{  "_id" : "replicaSet1",  "host" : 	"replicaSet1/10.0.225.57:27000,10.0.225.57:27001,10.0.225.57:27002" }
	{  "_id" : "replicaSet2",  "host" : 	"replicaSet2/10.0.225.58:27000,10.0.225.58:27001,10.0.225.58:27002" }
	{  "_id" : "replicaSet3",  "host" : 	"replicaSet3/10.0.225.59:27000,10.0.225.59:27001,10.0.225.59:27002" }
	{  "_id" : "replicaSet4",  "host" : 	"replicaSet4/10.0.225.60:27000,10.0.225.60:27001,10.0.225.60:27002" }
	  active mongoses:
	"3.2.4" : 1
	  balancer:
	Currently enabled:  yes
	Currently running:  no
	Failed balancer rounds in last 5 attempts:  0
	Migration Results for the last 24 hours: 
		No recent migrations
	  databases:
	{  "_id" : "loans",  "primary" : "replicaSet2",  "partitioned" : true }
	{  "_id" : "shardDB",  "primary" : "replicaSet2",  "partitioned" : true }
		shardDB.ehuserShard
			shard key: { "UserID" : "hashed" }
			unique: false
			balancing: true
			chunks:
			replicaSet1	11
			replicaSet2	10
			replicaSet3	12
			replicaSet4	10
			too many chunks to print, use verbose if you want to force print
	{  "_id" : "test",  "primary" : "replicaSet1",  "partitioned" : false }
	{  "_id" : "MatchMaker",  "primary" : "replicaSet4",  "partitioned" : false }

So far we installed MongoDB, created Replicasets and configured 4 Shard cluster. 
Now we are ready to create databases, collections, import data and do our performance testing.
Creating Database and enabling tables for Sharding
	Create and enable shardDB for Sharding.
	Mongos> use shardDB
	Mongos> sh.enableSharding("shardDB")
	Mongos> sh.shardCollection("shardDB.ehuserShard", {UserID: "hashed"}, false)

Importing dataset and populating 2 collections called ehuser and ehuserShard.
We have collected around 10 million user data with 4.2GB in total size for performance testing.
	-bash-4.1$ ls -lth ehuserjson.json
	-rw-r--r-- 1 srao ehuser 4.2G Apr 12 12:06 ehuserjson.json

Use mongoimport command that comes with MongoDB to import data from JSON file to MongoDB tables.
	$> sudo ./bin/mongoimport -d shardDB -c ehUser --type json --file 	/home/srao/ehuserjson.json
	$> sudo ./bin/mongoimport -d shardDB -c ehUserShard --type json --file 	/home/srao/ehuserjson.json

Once data is imported, connect to mongos instances and check the data.
	mongos> use shardDB
	switched to db shardDB
	mongos> db.ehuser.count()
	9053360
	mongos> db.ehuserShard.count()
	9053360
	mongos> db.ehuserShard.getShardDistribution()
The following output will be displayed in which the collection is sharded and data is distributed onto 4 servers.

	Shard replicaSet1 at replicaSet1/10.0.225.57:27000,10.0.225.57:27001,10.0.225.57:27002
 	data : 1.71GiB docs : 3374544 chunks : 11
	 estimated data per chunk : 159.88MiB
	 estimated docs per chunk : 306776

	Shard replicaSet2 at replicaSet2/10.0.225.58:27000,10.0.225.58:27001,10.0.225.58:27002
	 data : 1.1GiB docs : 2170839 chunks : 10
	 estimated data per chunk : 113.14MiB
	 estimated docs per chunk : 217083

Shard replicaSet3 at replicaSet3/10.0.225.59:27000,10.0.225.59:27001,10.0.225.59:27002
 	data : 991.26MiB docs : 1901959 chunks : 12
 	estimated data per chunk : 82.6MiB
 	estimated docs per chunk : 158496

Shard replicaSet4 at replicaSet4/10.0.225.60:27000,10.0.225.60:27001,10.0.225.60:27002
	 data : 837.01MiB docs : 1606016 chunks : 10
	 estimated data per chunk : 83.7MiB
	 estimated docs per chunk : 160601

Totals
	 data : 4.6GiB docs : 9053358 chunks : 43
	 Shard replicaSet1 contains 37.27% data, 37.27% docs in cluster, avg obj size on shard : 546B
	 Shard replicaSet2 contains 23.97% data, 23.97% docs in cluster, avg obj size on shard : 546B
	 Shard replicaSet3 contains 21% data, 21% docs in cluster, avg obj size on shard : 546B
	 Shard replicaSet4 contains 17.73% data, 17.73% docs in cluster, avg obj size on shard : 546B
