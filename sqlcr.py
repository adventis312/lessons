import sqlite3
import time
#    real_time = time.strftime('%y-%m-%d %H:%M:%S')
real_time = time.strftime('S')
#    создание таблици db
conn = sqlite3.connect('mybase.db')
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS registers (
time TEXT);
""")
conn.commit()
while True:
    time = [real_time]
    cur.executemany("INSERT INTO registers VALUES (?);", time)
    conn.commit()