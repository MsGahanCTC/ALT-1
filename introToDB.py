import sqlite3

# Step 1: Connect to the database (creates school.db if it doesn't exist)
conn = sqlite3.connect("school.db")

# Step 2: Create a cursor object
cursor = conn.cursor()

# Step 3: Create a students table using raw SQL
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    age INTEGER,
    grade REAL
)
""")

# Step 4: Insert sample records
cursor.execute("""
INSERT INTO students (first_name, age, grade) 
VALUES ('Cian', 17, 88.5)
""")

cursor.execute("""
INSERT INTO students (first_name, age, grade) 
VALUES ('Siobhán', 16, 92.0)
""")

# Step 5: Save (commit) changes to disk
conn.commit()

# Step 6: Query and display the data
cursor.execute("SELECT * FROM students")
records = cursor.fetchall()

print("--- Student Roster ---")
for student in records:
    print(f"ID: {student[0]} | Name: {student[1]} | Age: {student[2]} | Grade: {student[3]}%")

# Step 7: Close the connection
conn.close()
