QUERIES MONGODB
===============================================================================

All MongoDB Queries have been enlisted in a "copy and paste"-ready format below



QUERY Q1
===============================================================================

JavaScript file which searches for UserID with index and without index.
var date1 =  Date.now();
use shardDB;
db.ehuser.find({UserID: 56076262});
var date2 =  Date.now();
print ("Elapsed time without index(ms)");
print(date2-date1);
print("creating index on UserId")
db.ehuser.createIndex({UserID:1});
var date2 = Date.now()
db.ehuser.find({UserID: 56076262});
print("Elapsed time with index(ms)");
print(Date.now()-date2);

Output

MongoDB shell version: 3.2.4
connecting to: test
switched to db shardDB
{ "_id" : 56076262, "UserID" : 56076262, "UserStatus" : "Active", "UserStartDate" : "2014-02-11", "Gender" : "Male", "BirthDate" : 
"1959-08-25", "EducationName" : "unknown", "AssetName" : "ehc016", "CampaignDescription" : "unknown", "SegmentName" : "Default Segment",
 "GenderPreference" : "Female", "IncomeLevelName" : "$40000 to $60000", "UserNumberofMarriages" : 2, "UserChildren" : 3, "UserSmoke" : "2", 
 "Promotion" : "unknown", "PPR" : "Basic PPR", "LocaleSite" : ".AU", "TransactionAmount" : 311.4, "City" : "Hillston", "ZipCode" : "2675", 
 "State" : "New South Wales", "country" : "Australia  " }
Elapsed time without index (ms)
3906
creating index on UserId
{
"raw" : {
"replicaSet2/10.0.225.58:27000,10.0.225.58:27001,10.0.225.58:27002" : {
"createdCollectionAutomatically" : false,
"numIndexesBefore" : 1,
"numIndexesAfter" : 2,
"ok" : 1,
"$gleStats" : {
"lastOpTime" : Timestamp(1461266438, 1),
"electionId" : ObjectId("7fffffff0000000000000003")
}
}
},
"ok" : 1
}
{ "_id" : 56076262, "UserID" : 56076262, "UserStatus" : "Active", "UserStartDate" : "2014-02-11", "Gender" : "Male", "BirthDate" : "1959-08-25", 
"EducationName" : "unknown", "AssetName" : "ehc016", "CampaignDescription" : "unknown", "SegmentName" : "Default Segment", "GenderPreference" :
 "Female", "IncomeLevelName" : "$40000 to $60000", "UserNumberofMarriages" : 2, "UserChildren" : 3, "UserSmoke" : "2", "Promotion" : "unknown",
 "PPR" : "Basic PPR", "LocaleSite" : ".AU", "TransactionAmount" : 311.4, "City" : "Hillston", "ZipCode" : "2675", "State" : "New South Wales", 
 "country" : "Australia  " }
Elapsed time with index (ms)
3
Bye



QUERY Q2
===============================================================================

Searching tables ehUser (single node collection) and ehUserShard (sharded collection)
JavaScript file
var date1 =  Date.now();
use shardDB;
db.ehuser.find({ZipCode: "92880"}).count();
var date2 =  Date.now();
print ("Elapsed time without Sharding");
print(date2-date1);
var date2 = Date.now();
db.ehuserShard.find({ZipCode: "92880"}).count();
print("Elapsed time with Sharding");
print(Date.now()-date2);

Output
MongoDB shell version: 3.2.4
connecting to: test
switched to db shardDB
936
Elapsed time without Sharding
7217
936
Elapsed time with Sharding
2
Bye



QUERY Q3
===============================================================================

Using Aggregations
JavaScript file
var date1 =  Date.now();
use shardDB;
var date2 =  Date.now();
db.ehuser.aggregate([{$group: { _id: "$Gender", total: {$sum:1}}}])
print ("Elapsed time without Sharding");
print(date2-date1);
var date2 = Date.now();
db.ehuserShard.aggregate([{$group: { _id: "$Gender", total: {$sum:1}}}])
print("Elapsed time with Sharding");
print(Date.now()-date2);

Output
MongoDB shell version: 3.2.4
connecting to: test
switched to db shardDB
{ "_id" : "Female", "total" : 4683501 }
{ "_id" : "Male", "total" : 4369857 }
Elapsed time without Sharding
10602
{ "_id" : "Female", "total" : 4683501 }
{ "_id" : "Male", "total" : 4369857 }
Elapsed time with Sharding
8392
Bye



QUERY Q4
===============================================================================

Total transaction amount by State
JavaScript
var date1 =  Date.now();
use shardDB;
db.ehuser.aggregate([{$group: { _id: "$State", total: {$sum:"$TransactionAmount"}}}])
var date2 =  Date.now();
print ("Elapsed time without Sharding");
print(date2-date1);
var date2 = Date.now();
db.ehuserShard.aggregate([{$group: { _id: "$State", total: {$sum:"$TransactionAmount"}}}])
print("Elapsed time with Sharding");
print(Date.now()-date2);

Output
connecting to: test
switched to db shardDB
{ "_id" : "Rond�nia", "total" : 1526.66 }
{ "_id" : "Amap�", "total" : 89.85000000000001 }
{ "_id" : "Rio Grande do Norte", "total" : 1870.51 }
{ "_id" : "Acre", "total" : 1884.31 }
{ "_id" : "Saskatchewan", "total" : 800295.9699999952 }
{ "_id" : "S�o Paulo", "total" : 321064.67999999906 }
{ "_id" : "Quebec", "total" : 1665700.2099999397 }
{ "_id" : "Wyoming", "total" : 498106.2200000022 }
{ "_id" : "North Carolina", "total" : 5815878.11000058 }
{ "_id" : "Virginia", "total" : 6311491.6100007845 }
{ "_id" : "North Dakota", "total" : 663825.3200000011 }
{ "_id" : "Maryland", "total" : 4386950.230000222 }
{ "_id" : "Par�", "total" : 2865.66 }
{ "_id" : "Louisiana", "total" : 2296820.3399999663 }
{ "_id" : "Missouri", "total" : 3621338.8800001466 }
{ "_id" : "Colorado", "total" : 5594285.050000535 }
{ "_id" : "Massachusetts", "total" : 5235623.3900004625 }
{ "_id" : "Ohio", "total" : 7135260.650000854 }
{ "_id" : "New Hampshire", "total" : 1176530.0799999805 }
{ "_id" : "Alaska", "total" : 593867.6100000007 }
Type "it" for more
Elapsed time without Sharding
11637
{ "_id" : "Northwest Territories", "total" : 30925.93 }
{ "_id" : "Manitoba", "total" : 776246.520000001 }
{ "_id" : "Maranh�o", "total" : 1170.03 }
{ "_id" : "Queensland", "total" : 7751408.17999993 }
{ "_id" : "Louisiana", "total" : 2296820.340000008 }
{ "_id" : "Par�", "total" : 2865.66 }
{ "_id" : "Maryland", "total" : 4386950.2299999315 }
{ "_id" : "Colorado", "total" : 5594285.049999884 }
{ "_id" : "Minas Gerais", "total" : 36275.009999999995 }
{ "_id" : "Minnesota", "total" : 4197512.209999935 }
{ "_id" : "Cear�", "total" : 7395.169999999999 }
{ "_id" : "Virginia", "total" : 6311491.609999865 }
{ "_id" : "North Dakota", "total" : 663825.3199999997 }
{ "_id" : "Michigan", "total" : 5907904.079999886 }
{ "_id" : "Rio Grande do Norte", "total" : 1870.5099999999998 }
{ "_id" : "Idaho", "total" : 876120.9900000016 }
{ "_id" : "Maine", "total" : 811228.1400000013 }
{ "_id" : "Nova Scotia", "total" : 428647.9299999994 }
{ "_id" : "Arkansas", "total" : 1385623.5700000052 }
{ "_id" : "Tennessee", "total" : 3924091.389999965 }
Type "it" for more
Elapsed time with Sharding
8971
bye


QUERY Q5
===============================================================================

Update Performance
JavaScript
var date1 =  Date.now();
use shardDB;
db.ehuser.update({UserID: 11111111},{ZipCode: "92880", TransactionAmount: 340});
var date2 =  Date.now();
print(date2-date1);
db.ehuserShard.update({"_id" : ObjectId("571a6fbba6b64d6da6aa5583")},{UserID:22222222,ZipCode: "67654", TransactionAmount: 34});
print(Date.now()-date2);

Output
MongoDB shell version: 3.2.4
connecting to: test
switched to db shardDB
WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 })
2
WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 })
2
Bye


QUERY Q6
===============================================================================

Insert Performance
JavaScript
var date1 =  Date.now();
use shardDB;
db.ehuser.insert({  "UserID" : 11111111, "UserStatus" : "Active", "UserStartDate" : "2015-10-03", "Gender" : "Female", "BirthDate" :
 "1991-04-05", "EducationName" : "High School", "AssetName" : "ehc016", "CampaignDescription" : "unknown", "SegmentName" : 
 "Default Segment", "GenderPreference" : "Male", "IncomeLevelName" : "Less than $20000", "UserNumberofMarriages" : 0,
 "UserChildren" : 3, "UserSmoke" : "2", "Promotion" : "unknown", "PPR" : "Basic PPR", "LocaleSite" : ".COM", "TransactionAmount" : 
 0, "City" : "Hiltons", "ZipCode" : "24251", "State" : "Virginia", "country" : "United States" });
var date2 =  Date.now();
print(date2-date1);
db.ehuserShard.insert({  "UserID" : 22222222, "UserStatus" : "Active", "UserStartDate" : "2015-10-03", "Gender" : "Female", "BirthDate" : 
"1991-04-05", "EducationName" : "High School", "AssetName" : "ehc016", "CampaignDescription" : "unknown", "SegmentName" : "Default Segment",
 "GenderPreference" : "Male", "IncomeLevelName" : "Less than $20000", "UserNumberofMarriages" : 0, "UserChildren" : 3, "UserSmoke" : "2", 
 "Promotion" : "unknown", "PPR" : "Basic PPR", "LocaleSite" : ".COM", "TransactionAmount" : 0, "City" : "Hiltons", "ZipCode" : "24251",
 "State" : "Virginia", "country" : "United States" });
print(Date.now()-date2);

Output
MongoDB shell version: 3.2.4
connecting to: test
switched to db shardDB
WriteResult({ "nInserted" : 1 })
3
WriteResult({ "nInserted" : 1 })
2
Bye


QUERY Q7
===============================================================================

Delete Performance
var date1 =  Date.now();
use shardDB;
db.ehuser.remove({UserID: 11111111});
var date2 =  Date.now();
print(date2-date1);
db.ehuserShard.remove({UserID: 22222222});
print(Date.now()-date2);

Output
MongoDB shell version: 3.2.4
connecting to: test
switched to db shardDB
WriteResult({ "nRemoved" : 1 })
2
WriteResult({ "nRemoved" : 1 })
1
Bye


QUERY Q8
===============================================================================

Checking MapReduce performance
JavaScript
var date1 =  Date.now();
use shardDB;
db.ehuser.mapReduce(function() { emit(this.Promotion,this.TransactionAmount);},function(key,values) { return Array.sum(values)}, { query: { }, out: "order_totals"})
var date2 =  Date.now();
db.order_totals.find()
print ("Elapsed time without Sharding");
print(date2-date1);
var date2 = Date.now();
db.ehuserShard.mapReduce(function() { emit(this.Promotion,this.TransactionAmount);},function(key,values) { return Array.sum(values)}, { query: { }, out: "order_totals"})
print("Elapsed time with Sharding");
print(Date.now()-date2);
db.order_totals.find()

Output
MongoDB shell version: 3.2.4
connecting to: test
switched to db shardDB
{
"result" : "order_totals",
"timeMillis" : 61448,
"counts" : {
"input" : 9053358,
"emit" : 9053358,
"reduce" : 94976,
"output" : 26
},
"ok" : 1
}
{ "_id" : "12M $198.7 / 1M $29.95", "value" : 356532.0700000085 }
{ "_id" : "6M $138.96 / 1M $29.95", "value" : 169249.62999999808 }
{ "_id" : "6M $143.76 / 6M $140.95", "value" : 1044256.6800000274 }
{ "_id" : "One month link for AU Price Experiences", "value" : 0 }
{ "_id" : "One month link for CA Price Experiences", "value" : 387297.8800000119 }
{ "_id" : "One month link for GB Price Experiences", "value" : 0 }
{ "_id" : "One month link for US Price Experiences", "value" : 2588843.7699999674 }
{ "_id" : "promo COUPONCABINAAA : 6M $143.76 / 140.95", "value" : 5298.820000000001 }
{ "_id" : "promo COUPONCABINBBB : 12M $198.7 / 29.95", "value" : 1390.9 }
{ "_id" : "promo COUPONCACTUSBBB : 12M $198.7 / 29.95", "value" : 2155.2400000000002 }
{ "_id" : "promo COUPONWINNERAAA : 6M $143.76 / 140.95", "value" : 7523.780000000005 }
{ "_id" : "promo COUPONWINNERBBB : 12M $198.7 / 29.95", "value" : 643.7 }
{ "_id" : "promo DEALNEWSAAA : 6M $143.76 / 140.95", "value" : 17176.519999999997 }
{ "_id" : "promo DEALTAKERAAA : 6M $143.76 / 140.95", "value" : 2150.7799999999997 }
{ "_id" : "promo DEALTAKERBBB : 12M $198.7 / 29.95", "value" : 427.35 }
{ "_id" : "promo ODATINGMATCHESAAA : 6M $143.76 / 140.95", "value" : 71033.90999999999 }
{ "_id" : "promo ODATINGMATCHESBBB : 12M $198.7 / 29.95", "value" : 8569.569999999998 }
{ "_id" : "promo OFFERSAAA : 6M $143.76 / 140.95", "value" : 152310.5099999998 }
{ "_id" : "promo OFFERSBBB : 12M $198.7 / 29.95", "value" : 6803.689999999997 }
{ "_id" : "promo PROCODEAAA : 6M $143.76 / 140.95", "value" : 249141.76000000184 }
Type "it" for more
Elapsed time without Sharding
61457
{
"result" : "order_totals",
"counts" : {
"input" : NumberLong(9053358),
"emit" : NumberLong(9053358),
"reduce" : NumberLong(95017),
"output" : NumberLong(26)
},
"timeMillis" : 28316,
"timing" : {
"shardProcessing" : 28294,
"postProcessing" : 21
},
"shardCounts" : {
"replicaSet1/10.0.225.57:27000,10.0.225.57:27001,10.0.225.57:27002" : {
"input" : 3374544,
"emit" : 3374544,
"reduce" : 35357,
"output" : 23
},
"replicaSet2/10.0.225.58:27000,10.0.225.58:27001,10.0.225.58:27002" : {
"input" : 2170839,
"emit" : 2170839,
"reduce" : 22785,
"output" : 25
},
"replicaSet3/10.0.225.59:27000,10.0.225.59:27001,10.0.225.59:27002" : {
"input" : 1901959,
"emit" : 1901959,
"reduce" : 20029,
"output" : 23
},
"replicaSet4/10.0.225.60:27000,10.0.225.60:27001,10.0.225.60:27002" : {
"input" : 1606016,
"emit" : 1606016,
"reduce" : 16822,
"output" : 20
}
},
"postProcessCounts" : {
"replicaSet2/10.0.225.58:27000,10.0.225.58:27001,10.0.225.58:27002" : {
"input" : NumberLong(91),
"reduce" : NumberLong(24),
"output" : NumberLong(26)
}
},
"ok" : 1
}
Elapsed time with Sharding
28318
{ "_id" : "12M $198.7 / 1M $29.95", "value" : 356532.06999999855 }
{ "_id" : "6M $138.96 / 1M $29.95", "value" : 169249.63000000047 }
{ "_id" : "6M $143.76 / 6M $140.95", "value" : 1044256.6800000139 }
{ "_id" : "One month link for AU Price Experiences", "value" : 0 }
{ "_id" : "One month link for CA Price Experiences", "value" : 387297.8799999977 }
{ "_id" : "One month link for GB Price Experiences", "value" : 0 }
{ "_id" : "One month link for US Price Experiences", "value" : 2588843.769999993 }
{ "_id" : "promo COUPONCABINAAA : 6M $143.76 / 140.95", "value" : 5298.82 }
{ "_id" : "promo COUPONCABINBBB : 12M $198.7 / 29.95", "value" : 1390.8999999999999 }
{ "_id" : "promo COUPONCACTUSBBB : 12M $198.7 / 29.95", "value" : 2155.24 }
{ "_id" : "promo COUPONWINNERAAA : 6M $143.76 / 140.95", "value" : 7523.78 }
{ "_id" : "promo COUPONWINNERBBB : 12M $198.7 / 29.95", "value" : 643.7 }
{ "_id" : "promo DEALNEWSAAA : 6M $143.76 / 140.95", "value" : 17176.520000000004 }
{ "_id" : "promo DEALTAKERAAA : 6M $143.76 / 140.95", "value" : 2150.7799999999997 }
{ "_id" : "promo DEALTAKERBBB : 12M $198.7 / 29.95", "value" : 427.35 }
{ "_id" : "promo ODATINGMATCHESAAA : 6M $143.76 / 140.95", "value" : 71033.90999999995 }
{ "_id" : "promo ODATINGMATCHESBBB : 12M $198.7 / 29.95", "value" : 8569.57 }
{ "_id" : "promo OFFERSAAA : 6M $143.76 / 140.95", "value" : 152310.50999999983 }
{ "_id" : "promo OFFERSBBB : 12M $198.7 / 29.95", "value" : 6803.689999999999 }
{ "_id" : "promo PROCODEAAA : 6M $143.76 / 140.95", "value" : 249141.75999999995 }
Type "it" for more
Bye


QUERY Q9
===============================================================================

JavaScript file
var date1 =  Date.now();
use shardDB;
db.ehuser.mapReduce(function() { emit(this.State,1);},function(key,values) { return Array.sum(values)}, { query: { }, out: "order_totals"})
var date2 =  Date.now();
db.order_totals.find()
print ("Elapsed time without Sharding");
print(date2-date1);
var date2 = Date.now();
db.ehuserShard.mapReduce(function() { emit(this.State,1);},function(key,values) { return Array.sum(values)}, { query: { }, out: "order_totals"})
print("Elapsed time with Sharding");
print(Date.now()-date2);
db.order_totals.find()

Output
MongoDB shell version: 3.2.4
connecting to: test
switched to db shardDB
{
"result" : "order_totals",
"timeMillis" : 55939,
"counts" : {
"input" : 9053358,
"emit" : 9053358,
"reduce" : 736332,
"output" : 100
},
"ok" : 1
}
{ "_id" : "Acre", "value" : 68 }
{ "_id" : "Alabama", "value" : 98001 }
{ "_id" : "Alagoas", "value" : 236 }
{ "_id" : "Alaska", "value" : 14790 }
{ "_id" : "Alberta", "value" : 96356 }
{ "_id" : "Amap�", "value" : 71 }
{ "_id" : "Amazonas", "value" : 583 }
{ "_id" : "Arizona", "value" : 117703 }
{ "_id" : "Arkansas", "value" : 56022 }
{ "_id" : "Australian Capital Territory", "value" : 13583 }
{ "_id" : "Bahia", "value" : 1410 }
{ "_id" : "British Columbia", "value" : 87254 }
{ "_id" : "California", "value" : 695818 }
{ "_id" : "Cear�", "value" : 895 }
{ "_id" : "Colorado", "value" : 102874 }
{ "_id" : "Connecticut", "value" : 64529 }
{ "_id" : "Delaware", "value" : 18758 }
{ "_id" : "District of Columbia", "value" : 18892 }
{ "_id" : "Distrito Federal", "value" : 1568 }
{ "_id" : "Esp�rito Santo", "value" : 723 }
Type "it" for more
Elapsed time without Sharding
55950
{
"result" : "order_totals",
"counts" : {
"input" : NumberLong(9053358),
"emit" : NumberLong(9053358),
"reduce" : NumberLong(737461),
"output" : NumberLong(100)
},
"timeMillis" : 26345,
"timing" : {
"shardProcessing" : 26322,
"postProcessing" : 23
},
"shardCounts" : {
"replicaSet1/10.0.225.57:27000,10.0.225.57:27001,10.0.225.57:27002" : {
"input" : 3374544,
"emit" : 3374544,
"reduce" : 274764,
"output" : 100
},
"replicaSet2/10.0.225.58:27000,10.0.225.58:27001,10.0.225.58:27002" : {
"input" : 2170839,
"emit" : 2170839,
"reduce" : 176843,
"output" : 100
},
"replicaSet3/10.0.225.59:27000,10.0.225.59:27001,10.0.225.59:27002" : {
"input" : 1901959,
"emit" : 1901959,
"reduce" : 154923,
"output" : 100
},
"replicaSet4/10.0.225.60:27000,10.0.225.60:27001,10.0.225.60:27002" : {
"input" : 1606016,
"emit" : 1606016,
"reduce" : 130831,
"output" : 100
}
},
"postProcessCounts" : {
"replicaSet2/10.0.225.58:27000,10.0.225.58:27001,10.0.225.58:27002" : {
"input" : NumberLong(400),
"reduce" : NumberLong(100),
"output" : NumberLong(100)
}
},
"ok" : 1
}
Elapsed time with Sharding
26348
{ "_id" : "Acre", "value" : 68 }
{ "_id" : "Alabama", "value" : 98001 }
{ "_id" : "Alagoas", "value" : 236 }
{ "_id" : "Alaska", "value" : 14790 }
{ "_id" : "Alberta", "value" : 96356 }
{ "_id" : "Amap�", "value" : 71 }
{ "_id" : "Amazonas", "value" : 583 }
{ "_id" : "Arizona", "value" : 117703 }
{ "_id" : "Arkansas", "value" : 56022 }
{ "_id" : "Australian Capital Territory", "value" : 13583 }
{ "_id" : "Bahia", "value" : 1410 }
{ "_id" : "British Columbia", "value" : 87254 }
{ "_id" : "California", "value" : 695818 }
{ "_id" : "Cear�", "value" : 895 }
{ "_id" : "Colorado", "value" : 102874 }
{ "_id" : "Connecticut", "value" : 64529 }
{ "_id" : "Delaware", "value" : 18758 }
{ "_id" : "District of Columbia", "value" : 18892 }
{ "_id" : "Distrito Federal", "value" : 1568 }
{ "_id" : "Esp�rito Santo", "value" : 723 }
Type "it" for more
Bye





