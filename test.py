import os
import rethinkdb as r

conn = r.connect(os.getenv('MASTER_IP'), os.getenv('MASTER_PORT')).repl()
print r.db_list().run(conn)
print conn.host
r.db_create('python_tutorial').run(conn)
conn.db('python_tutorial').table_create('heroes').run()
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
