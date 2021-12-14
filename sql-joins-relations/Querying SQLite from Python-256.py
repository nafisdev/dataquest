## 3. Connecting to the Database ##

import sqlite3
conn=sqlite3.connect('jobs.db')

## 6. Creating a Cursor and Running a Query ##

import sqlite3
conn = sqlite3.connect("jobs.db")
cursor = conn.cursor()

query = "select major from recent_grads;"
cursor.execute(query)
majors = cursor.fetchall()
print(type(results))
print(majors[0:3])

## 8. Fetching a Specific Number of Results ##

import sqlite3
conn = sqlite3.connect("jobs.db")
cursor = conn.cursor()
five_results=cursor.execute("select Major , Major_category from recent_grads").fetchmany(5)

## 9. Closing the Database Connection ##

conn = sqlite3.connect("jobs.db")
conn.close()

## 10. Practice ##

conn = sqlite3.connect("jobs.db")
cursor = conn.cursor()

query = "select major from recent_grads order by Major desc;"
cursor.execute(query)
reverse_alphabetical = cursor.fetchall()
conn.close()