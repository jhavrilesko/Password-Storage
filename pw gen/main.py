from database_manager import (
    initialize_database,
    register_user,
    verify_user,
    add_password,
    get_user_id,
    get_passwords,
    delete_account
)
from pwgen import generate_password

def main():
    initialize_database()
    print("Welcome to the Password Manager!")
    
    while True:
        print("\nOptions:")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            username = input("Enter a username: ").strip()
            password = input("Enter a password: ").strip()
            if register_user(username, password):
                print("Registration successful!")
            else:
                print("Username already exists. Try another.")

        elif choice == "2":
            username = input("Enter your username: ").strip()
            password = input("Enter your password: ").strip()
            if verify_user(username, password):
                print(f"\nWelcome back, {username}!")
                user_id = get_user_id(username)
                while True:
                    print("\nOptions:")
                    print("1. Add a new password")
                    print("2. Display stored passwords")
                    print("3. Delete account")
                    print("4. Logout")
                    user_choice = input("Enter your choice: ").strip()

                    if user_choice == "1":
                        service = input("Enter the service name: ").strip()
                        generated_password = generate_password()
                        add_password(user_id, service, generated_password)
                        print(f"Password for {service} added: {generated_password}")

                    elif user_choice == "2":
                        passwords = get_passwords(user_id)
                        if passwords:
                            print("\nStored passwords:")
                            for service, password in passwords:
                                print(f"Service: {service}, Password: {password}")
                        else:
                            print("No passwords stored.")

                    elif user_choice == "3":
                        confirm = input("Are you sure you want to delete your account? (yes/no): ").strip().lower()
                        if confirm == "yes":
                            delete_account(user_id)
                            print("Account deleted.")
                            break

                    elif user_choice == "4":
                        print("Logged out.")
                        break

                    else:
                        print("Invalid choice. Try again.")

            else:
                print("Invalid credentials. Try again.")

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
