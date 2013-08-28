import os
import rethinkdb as r

print os.getenv('MASTER_IP')
print os.getenv('MASTER_PORT')
print os.getenv('SLAVE2_IP')
print os.getenv('SLAVE2_PORT')

print 'connecting and listing databases'

conn = r.connect(os.getenv('MASTER_IP'), os.getenv('MASTER_PORT')).repl()
print r.db_list().run(conn)
print conn.host

print 'creating database'

r.db_create('python_tutorial').run(conn)

print 'creating table'

r.db('python_tutorial').table_create('heroes').run(conn)

print 'inserting heroes'
r.db('python_tutorial').table('heroes').insert({
      "hero": "Wolverine", 
      "name": "James 'Logan' Howlett", 
      "magazine_titles": ["Amazing Spider-Man vs. Wolverine",
      "Avengers", "X-MEN Unlimited", "Magneto War", "Prime"],
      "appearances_count": 98
    }).run(conn)

print "doing stuff on the second slave..."
conn2 = r.connect(os.getenv('SLAVE2_IP'), 28015).repl()
print conn2.host
print r.db_list().run(conn2)
result = r.db('python_tutorial').table('heroes').run(conn2)
for i in result:
  print i
