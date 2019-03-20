import sqlite3


conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()
for i in range(5):
    cursor.execute('INSERT INTO front_institution VALUES(?, ?, ?, ?, ?, ?)',(5+i, u'XF', 10000059, u'new one', u'added', u'University '+str(5+i)))
conn.commit()
