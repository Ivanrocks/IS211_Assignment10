import sqlite3
import sys
from os import system


def connect_to_db():
    """
        Establishes a connection to the 'pets.db' SQLite database. If the database
        file does not exist, it will be created. Returns a cursor object for executing SQL commands.

        Returns:
            sqlite3.Cursor: Cursor object to interact with the database.
        """
    # Create or connect to the pets.db database
    connection = sqlite3.connect('pets.db')
    cursor = connection.cursor()
    return cursor

def fetch_data(personID, con):
    """
        Fetches and displays data for a person and their associated pets based on the given person ID.

        Args:
            personId (int): ID of the person whose data to fetch.
            con (sqlite3.Cursor): Cursor object to interact with the database.

        Returns:
            None
        """
    ID = str(personID)
    personData = con.execute(
        'SELECT * FROM person WHERE id = ?',
        ID
    ).fetchall()
    petData = con.execute('''
        SELECT p.id, p.name, p.breed, p.age, p.dead 
        FROM pet AS p 
        JOIN person_pet AS pt ON p.id = pt.pet_id 
        WHERE pt.person_id = ?
        ''',ID

    ).fetchall()
    # Check if person data was retrieved
    if personData:
        # Unpack the personData tuple to get individual attributes
        id, firstName, lastName, age = personData[0]
        print(f"Name: {firstName} {lastName}, Age: {age}")

        if petData:
            # Check if any pets were found for the person
            print("Pets Found:")

            for pet in petData:
                id, name, breed, age, dead = pet
                print(f"Pet: Name: {name}, breed: {breed}, age: {age}, dead: {dead}  ")

        else:
            # Display message if no pets are associated with the person
            print("No pets found")
    else:
        # Display an error if no person was found for the given ID
        print("Error: Could not find the provided ID:", personID )


if __name__ == "__main__":
    """
        Main program block that initiates database connection, and prompts the user
        for a person ID. Based on the input, it retrieves and displays the person's
        details along with their pets. Input '-1' to exit the program.
    """
    print("Running query_pets.py")
    # Establish database connection
    con = connect_to_db()

    # Initialize a flag to control the loop
    keepAsking = True

    # Start a loop to continually ask for a person ID until the user decides to exit
    while keepAsking:
        try:
            # Prompt user to enter a Person ID and convert it to an integer

            personID = int(input("Enter a Person ID: "))
        except ValueError:
            # Display an error message if input is not a valid integer
            print("Enter a valid number")
            personID = 0

        # If the user enters -1, exit the loop and close the program
        if personID == -1:
            print("Exiting..............")
            keepAsking = False
            con.close()

        else:
            # Fetch and display data for the entered person ID
            fetch_data(personID,con)

