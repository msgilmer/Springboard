# Here is the code for the bonus exercise
# Run as python json_to_sql.py json_file, table_name (as strings)
# e.g. python json_to_sql.py author-results.json author
import sys
import json

#json_file = sys.argv[0]
#table_name = sys.argv[1]

#with open('author-results.json') as f: 
# For some, some reason the above causes error
# Therefore, change the file below and the table
# name for a different json file.
with open('author-results.json') as f:
    data = json.load(f) # Getting an error here for some reason

col_names = list(data[0].keys())
command = "CREATE TABLE IF NOT EXISTS {} (".format('author')
#command = "CREATE TABLE IF NOT EXISTS {} (".format(table_name)
command += "\n          {} text PRIMARY KEY,".format(col_names[0])
for name in col_names[1:-1]:

    command += "\n            {} text DEFAULT '',".format(name)
command += "\n            {} text DEFAULT ''".format(col_names[-1])
command += ") WITHOUT ROWID;"
print(command)

import sqlite3
conn = sqlite3.connect('./db.sqlite3')
cur = conn.cursor()
cur.execute(command)

cur.execute("SELECT name from sqlite_master WHERE type='table'")
print(cur.fetchall())

# Now load the data
product_sql = "INSERT INTO {} ({}) VALUES ({})".format('author', ', '.join(col_names), ', '.join(['?'] * len(col_names)))
for datum in data:
    record = []
    for name in col_names:
        record.append(datum[name])
    cur.execute(product_sql, record)

cur.execute("SELECT name FROM author LIMIT 10;")
print(cur.fetchall())
