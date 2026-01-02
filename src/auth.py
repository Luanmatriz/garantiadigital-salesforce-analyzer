from simple_salesforce import Salesforce
from dotenv import load_dotenv
import os

load_dotenv()

class Auth:
    def __init__(self):
        self.users = {}  # A simple dictionary to store user credentials

    def register(self, username, password):
        if username in self.users:
            return False  # User already exists
        self.users[username] = password
        return True  # Registration successful

    def login(self, username, password):
        if username in self.users and self.users[username] == password:
            return True  # Login successful
        return False  # Invalid credentials

    def logout(self):
        # Logic for logout can be implemented here
        pass

def validate_credentials(username, password):
    # Simple validation logic
    return isinstance(username, str) and isinstance(password, str) and len(password) > 0