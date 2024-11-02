# IS211_Assignment10
IS211_Assignment10
# Pets Database Query Script

This script is a command-line application to interact with the `pets.db` SQLite database. It allows users to look up a person’s details and their associated pets by entering a person ID. The program displays the person’s name, age, and their pets’ details if available. If the person has no pets, an appropriate message is displayed.

## Files

- `pets.db`: The SQLite database file containing `person`, `pet`, and `person_pet` tables.
- `query_pets.py`: The main Python script that connects to `pets.db` and retrieves data.

## Table Structure in `pets.db`

For this script to work, the database `pets.db` must have the following tables and relationships:

1. **person**: Stores data about individuals.
   - `id`: Integer, primary key
   - `first_name`: Text, first name of the person
   - `last_name`: Text, last name of the person
   - `age`: Integer, age of the person

2. **pet**: Stores data about pets.
   - `id`: Integer, primary key
   - `name`: Text, name of the pet
   - `breed`: Text, breed of the pet
   - `age`: Integer, age of the pet
   - `dead`: Integer, flag indicating if the pet is alive (0 for alive, 1 for deceased)

3. **person_pet**: Stores the relationship between a person and their pet(s).
   - `person_id`: Integer, foreign key referencing `person(id)`
   - `pet_id`: Integer, foreign key referencing `pet(id)`

## Requirements

- **Python 3**
- **SQLite3**

## Script Structure

### `connect_to_db()`

This function:
- Establishes a connection to the `pets.db` database.
- Returns a cursor object, which allows executing SQL commands on the database.

### `fetch_data(personID, con)`

This function:
- Takes in a `personID` (integer) and a `con` (cursor object).
- Queries the `person` table for details on the person with the specified ID.
- If a match is found, it retrieves the person’s details (name and age) and prints them.
- It also retrieves and displays any associated pets from the `pet` table, showing the pet’s name, breed, age, and whether the pet is alive or deceased.
- If no pets are found for a person, it displays "No pets found."
- If the person ID is invalid, it displays "Error: Could not find the provided ID."

### Main Program

The main block:
- Connects to the database.
- Continuously prompts the user to enter a person ID to look up.
- If the user enters `-1`, the program exits.

## Usage

1. Run the script from the command line:
   ```bash
   python query_pets.py

# Contributor
Ivan Martinez
