import csv

outfiles = ['insert_data1.sql', 'insert_data2.sql', 'insert_data3.sql', 'insert_data4.sql', 'insert_data5.sql']

relations = ['data1', 'data2', 'data3', 'data4', 'data5']

# +
#relat = 'match'    #loop
# -

import os.path
for outfile in outfiles:
    if(os.path.isfile(outfile)): 
        file = open(outfile,"r+")
        file. truncate(0)
        file. close()

'''
for i in range(5):
    old_qu = 'delete from '
    relat = relations[i]
    qu = old_qu
    qu = qu + relat + ';'
    outfile = outfiles[i]
    with open(outfile, 'a') as f:
        print(qu, file=f)
    #print(qu)
'''

# +




# -

for i in range(5):
    relat = relations[i]
    with open(relat + '.csv', newline='') as csvfile:
        stud = csv.DictReader(csvfile)
        old_qu = 'insert into ' + 'covid' + ' values ('
        
        for row in stud:
            qu = old_qu
            for key, value in row.items():
                if(value == 'NULL'):
                    qu = qu + 'null,'
                else:
                    qu = qu + '\'' + value + '\'' + ','
                    
            qu = qu[:-1] + ');'
            
            outfile = outfiles[i]
            with open(outfile, 'a') as f:
                print(qu, file=f)
            #print(qu)















