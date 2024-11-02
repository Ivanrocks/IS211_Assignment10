import sqlite3
def create_database():
    # Create or connect to the pets.db database
    connection = sqlite3.connect('pets.db')
    cursor = connection.cursor()
    cursor.execute('''
    DROP TABLE IF EXISTS person;
    ''')
    # Create the person table
    cursor.execute('''
    CREATE TABLE person (
        id INTEGER PRIMARY KEY,
        first_name TEXT,
        last_name TEXT,
        age INTEGER
    );
    ''')
    cursor.execute('''
        DROP TABLE IF EXISTS pet;
        ''')
    # Create the pet table
    cursor.execute('''
    CREATE TABLE pet (
        id INTEGER PRIMARY KEY,
        name TEXT,
        breed TEXT,
        age INTEGER,
        dead INTEGER
    );
    ''')

    # Create the person_pet table
    cursor.execute('''
        DROP TABLE IF EXISTS person_pet;
        ''')
    cursor.execute('''
    CREATE TABLE person_pet (
        person_id INTEGER,
        pet_id INTEGER,
        FOREIGN KEY (person_id) REFERENCES person (id),
        FOREIGN KEY (pet_id) REFERENCES pet (id)
    );
    ''')

    # Commit changes and close the connection
    connection.commit()
    connection.close()

def load_data():
    # Connect to the pets.db database
    connection = sqlite3.connect('pets.db')
    cursor = connection.cursor()

    # Insert data into the person table
    persons = [
        (1, 'James', 'Smith', 41),
        (2, 'Diana', 'Greene', 23),
        (3, 'Sara', 'White', 27),
        (4, 'William', 'Gibson', 23),
    ]
    cursor.executemany('INSERT INTO person VALUES (?, ?, ?, ?);', persons)

    # Insert data into the pet table
    pets = [
        (1, 'Rusty', 'Dalmation', 4, 1),
        (2, 'Bella', 'Alaskan Malamute', 3, 0),
        (3, 'Max', 'Cocker Spaniel', 1, 0),
        (4, 'Rocky', 'Beagle', 7, 0),
        (5, 'Rufus', 'Cocker Spaniel', 1, 0),
        (6, 'Spot', 'Bloodhound', 2, 1),
    ]
    cursor.executemany('INSERT INTO pet VALUES (?, ?, ?, ?, ?);', pets)

    # Insert data into the person_pet table
    person_pets = [
        (1, 1),
        (1, 2),
        (2, 3),
        (2, 4),
        (3, 5),
        (4, 6),
    ]
    cursor.executemany('INSERT INTO person_pet VALUES (?, ?);', person_pets)

    # Commit changes and close the connection
    connection.commit()
    connection.close()

if __name__ == '__main__':
    try:
        print("Creating Database.............")
        create_database()
        print("Database created successfully.")
        print("Loading data into Database............")
        load_data()
        print("Data Loaded successfully.")
    except Exception as e:
        print("Error: ", e)




