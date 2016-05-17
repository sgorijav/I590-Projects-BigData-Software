QUERIES CASSANDRA
===============================================================================

All Cassandra Queries have been enlisted in a "copy and paste"-ready format below



QUERY Q10
===============================================================================

select unixtimestampOf(now()) from system.local;
select * from eh.ehuser where userid = 55576857;
select unixtimestampOf(now()) from system.local;

Output
unixtimestampOf(now())
------------------------
	1461801799815
(1 rows)
	userid   | assetname | birthdate                | campaigndescription | city      | country       | ...
----------+-----------+--------------------------+---------------------+-----------+---------------+------
	55576857 |   unknown | 1972-05-12 16:00:00+0000 |             unknown | Cleveland | 	United States | ...
	unixtimestampOf(now())
	------------------------
	1461801799850
	(1 rows)

	Time Elapsed: 35 ms (with 4 node cluster)
	Time Elapsed:  37 ms (with standalone cluster)

	
	
Query Q11
===============================================================================

select unixtimestampOf(now()) from system.local;
select count(*) from eh.ehuser where zipcode = '20001';
select unixtimestampOf(now()) from system.local;

Output
unixtimestampOf(now())
------------------------
1461801580638

(1 rows)

count
-------
2034

(1 rows)

unixtimestampOf(now())
------------------------
1461801581007

(1 rows)

Time Elapsed: 369 ms (with 4 node cluster)
Time Elapsed:  821 ms (with standalone cluster)



QUERY Q12
===============================================================================

Update Query
	select unixtimestampOf(now()) from system.local;
	UPDATE eh.ehuser SET CampaignDescription = 'Testing'  where userid = 55576857;
	select unixtimestampOf(now()) from system.local;
	cqlsh> SOURCE 'test.cql'

	Output
	unixtimestampOf(now())
	------------------------
	1461802063377
	(1 rows)
	unixtimestampOf(now())
	------------------------
	1461802063381
	(1 rows)

Time Elapsed: 4 ms (with 4 node cluster)
Time Elapsed:  4 ms (with standalone cluster)

