# Contents of src/main.py

from auth import Auth

def main():
    auth = Auth()
    print("Welcome to the Authentication System")
    
    while True:
        action = input("Choose an action: [login/logout/exit]: ").strip().lower()
        
        if action == "login":
            username = input("Enter username: ")
            password = input("Enter password: ")
            if auth.login(username, password):
                print("Login successful!")
            else:
                print("Login failed. Please check your credentials.")
        
        elif action == "logout":
            auth.logout()
            print("You have been logged out.")
        
        elif action == "exit":
            print("Exiting the application.")
            break
        
        else:
            print("Invalid action. Please try again.")

if __name__ == "__main__":
    main()