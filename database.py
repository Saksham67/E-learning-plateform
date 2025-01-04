import sqlite3

def create_database():
    conn = sqlite3.connect('college_app.db')
    cursor = conn.cursor()

    # Create Users Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            role TEXT DEFAULT 'student',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    # Create Courses Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS courses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            course_name TEXT UNIQUE NOT NULL
        )
    ''')
    # Create Study Materials Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS study_materials (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            course_id INTEGER NOT NULL,
            material_type TEXT NOT NULL,
            material_name TEXT NOT NULL,
            material_link TEXT NOT NULL,
            FOREIGN KEY (course_id) REFERENCES courses (id)
        )
    ''')
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_database()
    print("Database and tables created!")
