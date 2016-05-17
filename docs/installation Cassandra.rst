Installation
===============================================================================

Installation commands/instructions for installing Cassandra are listed here.
Cassandra Cluster will be installed based on DataStax Enterprise 4.8.


Prerequisites
-------------------------------------------------------------------------------

* Java 6 or later is required before installing Cassandra. 
You can check java version using following command.
$> Java –version
java version "1.8.0_66"
Java(TM) SE Runtime Environment (build 1.8.0_66-b17)
Java HotSpot(TM) 64-Bit Server VM (build 25.66-b17, mixed mode)

If you don’t find Java, you need to install java latest version first before
 proceeding to Cassandra installation. It also good to set JAVA_HOME environment 
 variable and add JAVA_HOME/bin directory to the PATH variable on operating 
 system if it’s not part of the path.

* Cassandra Enterprise is available for Linux and Mac operating system. 
If you are using Windows, You may download DataStax community edition, 
which is available for download on DataStax website.

You can download DataStax enterprise from the following web site for Linux and
 Mac OS.
http://www.planetcassandra.org/cassandra/

The community edition is available for download on http://www.planetcassandra.org/
 cassandra/, which works for Windows as well.

Create Directories for Data, Commit Logs and Cache with required disk space as
mentioned in the above section. Make sure all the directories created have read 
and write permissions to Cassandra user under which you are going to install and 
run Cassandra instance.


Installation of Cassandra
-------------------------------------------------------------------------------

•	Go to the folder where you downloaded Datastax enterprise Cassandra and run
 the following command.
$> chmod +x DataStaxEnterprise-4.5.x-linux-x64-installer.run
•	Run the following command to initiate Cassandra installation.
$> sudo ./DataStaxEnterprise-4.5.x-linux-x64-installer.run
  
 	This command start installing Cassandra in the GUI mode if your operating system 
	has GUI enabled.
To install Cassandra in text mode add the “--mode text” at the end of the above command.
•	The following screen appears when you run the above command. 
 
•	Select on “I Accept agreement” and click next
 
•	In the below screen type the installation path where you want to install the binaries. 
If you are installing it as root, select ‘Update the system’ and enter IP address of the node.
 
•	Click next 
 

•	Enter the name of the cluster and seeds. If it is standalone installation, just leave local IP 
as seed. If you are adding it as a new node to cluster, you need to give 1 or more other node IPs within
 the cluster. It’s not advisable to give all the node IPs of the cluster or just one other node’s IP address.
 The good rule is the number of the nodes mentioned in the seed can be equal to the Replication Factor.
 When the node starts first time, it learns about the cluster from the nodes mentioned in the Seed parameter.
 Gossip protocol uses this information to communicate with other nodes.

You also need to choose Node Type whether it is Cassandra, Search Node or Analytic node. Analytic node comes
 with Spark enabled and Search Node comes with SOLR integrated. You can run few nodes with analytic mode or 
 Search mode and rest with Cassandra type.

•	Enter super user name and password. This is important when you enable password authentication. 
You need to login with this user to create other users.
 

•	If you chose to install it as in Analytic mode, then you need to choose Spark only or Spark + Hadoop
 integrated. 
 

•	Enable vnodes if you are using Cassandra node and disable vnodes if you are installing this node as
 an Analytic node or Search node.

Enter IP address of the current node as listen address and RPC address.

•	In this screen below, enter the directories you created for Data, Commit Log, Caches directory and log
 directory.

•	Enter the port numbers to communicate with Cassandra data.
 
•	If you want to install DataStax agent on this node, enter IP address of the node. 
The data monitored through this agent can be visualized using DataStax Ops center.
 
•	Now we are ready to install the Cassandra instance and just click on next and then click on finish on the next screen.
 
Using Cassandra
To start Cassandra instance, go to dse directory where you installed the Cassandra software and type in the following command. 
The following command start Cassandra instance.
$>bin/dse Cassandra 	
To start Cassandra in the analytical mode (spark), use the following command.
$>bin/dse Cassandra –t
To get the status of the Cassandra instance, use nodetool utility as below.
