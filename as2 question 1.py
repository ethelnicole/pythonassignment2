import sqlite3


def manage_sqlite_database():
    try:
        # 1. Connect to the database (creates the file 'example.db' if it doesn't exist)
        # Using ':memory:' instead of a filename will create a temporary database in RAM
        connection = sqlite3.connect("example.db")

        # 2. Create a cursor object to execute SQL commands
        cursor = connection.cursor()

        # 3. Create a table
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS employees (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                department TEXT,
                salary REAL
            )
        """
        )
        print("Table 'employees' successfully verified/created.")

        # 4. Insert data using parameterized queries (prevents SQL injection)
        sample_data = [
            ("Alice Smith", "Engineering", 85000.00),
            ("Bob Jones", "Marketing", 62000.00),
            ("Charlie Brown", "Human Resources", 55000.00),
        ]

        # executemany allows inserting multiple records efficiently at once
        cursor.executemany(
            """
            INSERT INTO employees (name, department, salary) 
            VALUES (?, ?, ?)
        """,
            sample_data,
        )

        # Commit (save) the changes permanently to the database
        connection.commit()
        print(f"{len(sample_data)} records successfully inserted.")

        # 5. Retrieve and print data from the table
        cursor.execute("SELECT id, name, department, salary FROM employees")

        # Fetch all rows returned by the query
        rows = cursor.fetchall()

        print("\n--- Employee Records ---")
        for row in rows:
            print(
                f"ID: {row[0]} | Name: {row[1]} | Department: {row[2]} | Salary: ${row[3]:,.2f}"
            )

    except sqlite3.Error as error:
        print(f"An error occurred while working with SQLite: {error}")

    finally:
        # 6. Ensure the connection is always closed properly
        if connection:
            connection.close()
            print("\nDatabase connection closed.")


if __name__ == "__main__":
    manage_sqlite_database()
