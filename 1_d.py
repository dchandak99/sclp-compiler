import psycopg2, config

def connect():
	""" returns connection to datadata """
	# TODO: use variables from config file as connection params
	conn = psycopg2.connect(host=config.host, port=config.port, dbname=config.name, user=config.user, password=config.pswd)
	
	return conn

	#pass

def exec_query(conn, sql):
	""" Executes sql query and returns header and rows """
	# TODO: create cursor, get header from cursor.description, and execute query to fetch rows.

	curr = conn.cursor()

	try:
		curr.execute(sql)
		#conn.commit()

	except Exception as sqle:
		print("Could not execute query ", sqle)
		conn.rollback()

	# header = list(map(lambda x: x[0], curr.description))    
	# rows = curr.fetchall()	

	# for depth in curr:
	# 	print(depth[0], depth[1])
	# header = [desc[0] for desc in curr.description]
	# #rows = [desc[1:] for desc in curr.description]

	# #print(curr.description)
	# #print(curr.fetchall)

	# rows = []
	# for row in curr:
	# 	rows.append(row)


	# return (header, rows)

	#pass

if __name__ == "__main__":

	from sys import argv
	import config
	import datetime
	import csv

	#print (config.name)


	#qu1 = "copy covid FROM '/home/devansh/Desktop/IITB_Semesters/Sem_6/CS387/Lab4/outlab/data_into_5/" 
	relations = ['data1', 'data2', 'data3', 'data4', 'data5']
	#qu2 = "' DELIMITER ',' CSV "
	times = []

	#query = argv[1]
	try:
		#conn = connect()
		#(header, rows) = exec_query(conn, query)
		#print(",".join([str(i) for i in header]))
		#for r in rows:
		#	print(",".join([str(i) for i in r]))

		for i in range(5):
			conn = connect()
			exec_query(conn, "delete from covid")
			conn.close()

			#time1
			with open(relations[i] + ".csv") as csvfile:
				stud = csv.DictReader(csvfile)
				old_qu = 'insert into ' + 'covid' + ' values ('
				#conn = connect()
				conn = connect()
				curr = conn.cursor()
				t1 = datetime.datetime.now()

				j = 0
				for row in stud:
					qu = old_qu

					for key, value in row.items():
						
						if(value == 'NULL'):
							qu = qu + 'null,'
						else:
							qu = qu + '\'' + value + '\'' + ','
					
					qu = qu[:-1] + ');'

					#print(str(j) + "\t" + qu)
					curr.execute(qu)

					j = j + 1

				conn.commit()
				t2 = datetime.datetime.now()
				conn.close()

				delta = t2-t1

				print("Time for inserting " + relations[i] + ".csv (in milliseconds) = " + str(delta.total_seconds() * 1000))
				times.append(delta)



		for i in range(5): 
			print("Time for inserting " + relations[i] + ".csv (in milliseconds) = " + str(times[i].total_seconds() * 1000))

		#conn.close()
	except Exception as err:
		print("ERROR %%%%%%%%%%%%%%%% \n", err)
