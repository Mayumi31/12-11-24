import sqlite3
from random import randint
import random
import string
import datetime

# Data Randomizer Class
class DataRandomizer:
    def __init__(self):
        self.first_names = ["John", "Jane", "Alex", "Emily", "Chris", "Katie"]
        self.last_names = ["Smith", "Doe", "Johnson", "Williams", "Brown", "Davis"]
        self.domains = ["example.com", "mail.com", "random.org", "test.com"]
        self.cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]
        self.countries = ["USA", "Canada", "UK", "Australia", "Germany"]

    def random_name(self):
        return f"{random.choice(self.first_names)} {random.choice(self.last_names)}"

    def random_email(self):
        name_part = ''.join(random.choices(string.ascii_lowercase, k=5))
        domain = random.choice(self.domains)
        return f"{name_part}@{domain}"

    def random_phone(self):
        return f"+1-{random.randint(100, 999)}-{random.randint(100, 999)}-{random.randint(1000, 9999)}"

    def random_date(self, start_year=1990, end_year=2023):
        start_date = datetime.date(start_year, 1, 1)
        end_date = datetime.date(end_year, 12, 31)
        random_date = start_date + datetime.timedelta(days=random.randint(0, (end_date - start_date).days))
        return random_date

    def random_address(self):
        street_num = random.randint(100, 9999)
        street_name = ''.join(random.choices(string.ascii_uppercase, k=6))
        city = random.choice(self.cities)
        country = random.choice(self.countries)
        return f"{street_num} {street_name} St, {city}, {country}"

# Database Setup
def setup_database():
    conn = sqlite3.connect("random_data.db")
    cursor = conn.cursor()
    # Create table if it doesn't exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS users
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                      name TEXT,
                      email TEXT,
                      phone TEXT,
                      dob TEXT,
                      address TEXT)''')
    conn.commit()
    conn.close()

# Insert Randomized Data into the Database
def insert_random_data(data_randomizer, num_entries=5):
    conn = sqlite3.connect("random_data.db")
    cursor = conn.cursor()
    
    for _ in range(num_entries):
        name = data_randomizer.random_name()
        email = data_randomizer.random_email()
        phone = data_randomizer.random_phone()
        dob = data_randomizer.random_date().isoformat()  # Convert date to ISO format for storage
        address = data_randomizer.random_address()
        
        cursor.execute("INSERT INTO users (name, email, phone, dob, address) VALUES (?, ?, ?, ?, ?)",
                       (name, email, phone, dob, address))
    
    conn.commit()
    conn.close()
    print(f"Inserted {num_entries} random entries into the database.")

# Retrieve and display data
def display_data():
    conn = sqlite3.connect("random_data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    conn.close()

# Main Program
if __name__ == "__main__":
    data_randomizer = DataRandomizer()
    setup_database()
    insert_random_data(data_randomizer, num_entries=10)  # Insert 10 random entries
    display_data()  # Display the data
