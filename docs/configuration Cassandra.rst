Configuration
===============================================================================

Configuration commands/instructions for Cassandra are listed here.


Steps to Configure Cassandra
-------------------------------------------------------------------------------

I.	Installing and Setup Cassandra as 4 node cluster and standalone.
Separate document attached.

II.	Connect to stand alone and multi node cluster and execute following script to create key space.
CREATE KEYSPACE eh
WITH replication = {
'class' : 'SimpleStrategy',
'replication_factor' : 3
};

III.	Create table called ehuser within eh tablespace.
CREATE TABLE ehuser
(   UserID bigint Primary Key,
UserStatus varchar,
UserStartDate timestamp,
Gender varchar,
Birthdate timestamp,
EducationName varchar,
Assetname varchar,
CampaignDescription varchar,
SegmentName varchar,
GenderPreference varchar,
IncomeLevelName varchar,
UserNumberofmarriages int,
userchildren int,
usersmoke int,
promotion varchar,
PPR varchar,
LocaleSite varchar,
TransactionAmount decimal,
City varchar,
zipcode varchar,
state varchar,
country varchar
);
--Create Index on ehuser table zipcode.
create index on ehuser(zipcode);

IV) Import data from csv file.

COPY eh.ehuser ( UserID, UserStatus,UserStartDate,Gender,Birthdate,EducationName,Assetname,CampaignDescription,
SegmentName,GenderPreference,IncomeLevelName,UserNumberofmarriages,userchildren,usersmoke,promotion,PPR,LocaleSite,
TransactionAmount,City,zipcode,state,country) FROM '/home/srao/ehuser.csv' DELIMITED WITH '"';

Output on multi node cluster:
Processed: 7994294 rows; Rate:    2202 rows/s; Avg. rate:   15683 rows/s
7994294 rows imported from 1 files in 8 minutes and 29.751 seconds (0 skipped).
Output on standalone cluster:
Processed: 7994294 rows; Rate:    1203 rows/s; Avg. rate:   8683 rows/s
7994294 rows imported from 1 files in 15 minutes and 34.472 seconds (0 skipped).
