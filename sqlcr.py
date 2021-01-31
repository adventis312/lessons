import sqlite3

conn = sqlite3.connect('mybase.db')
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS "registers" (
name	TEXT,
register NUMERIC NOT NULL,
variable TEXT PRIMARY KEY,
value NUMERIC NOT NULL);
  """)
conn.commit()
