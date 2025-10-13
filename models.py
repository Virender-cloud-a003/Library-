from db import app, get_db  # use get_db() instead of mysql

def create_tables():
    with app.app_context():  # ensure Flask app context
        cur = get_db().cursor()
        
        # Books table
        cur.execute('''
            CREATE TABLE IF NOT EXISTS books(
                id INT AUTO_INCREMENT PRIMARY KEY,
                title VARCHAR(100),
                author VARCHAR(100),
                status VARCHAR(20) DEFAULT 'Available'
            )
        ''')
        
        # Members table
        cur.execute('''
            CREATE TABLE IF NOT EXISTS members(
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100),
                email VARCHAR(100)
            )
        ''')
        
        # Borrow table
        cur.execute('''
            CREATE TABLE IF NOT EXISTS borrow(
                id INT AUTO_INCREMENT PRIMARY KEY,
                book_id INT,
                member_id INT,
                borrow_date DATE,
                return_date DATE,
                FOREIGN KEY (book_id) REFERENCES books(id),
                FOREIGN KEY (member_id) REFERENCES members(id)
            )
        ''')
        
        get_db().commit()
        cur.close()
        print("Tables created successfully!")

if __name__ == "__main__":
    create_tables()
