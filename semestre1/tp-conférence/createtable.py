import sqlite3

conn = sqlite3.connect('cours.db')

c = conn.cursor()

# Create table
c.execute("""
CREATE TABLE IF NOT EXISTS prof(
     id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
     prof TEXT
)
""")
# Insert a row of data
# c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

# Save (commit) the changes
conn.commit()

conn.close()
