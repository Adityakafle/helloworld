def greet_user(name):
    """Function to greet the user."""
    print(f"Hello, {name}! Welcome to the Simple Greeting Application.")

def main():
    """Main function to run the application."""
    print("Welcome ..... to the Simple Greeting Application!")
    user_name = input("Please enter your name: ")
    greet_user(user_name)

if __name__ == "__main__":
    main()
