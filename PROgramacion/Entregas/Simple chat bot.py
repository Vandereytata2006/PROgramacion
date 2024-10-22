# Start the chatbot conversation
def Willfredo():
    # Try-except block to handle potential exceptions
    try:
        # Ask the user for their name
        name = input("How you doin' my friend? I'm Willfredo and I'm here to chat with you! What's your name? ")
        
        # Confirm the name input
        print(f"Nice to meet you, {name}!")
        
       # Keep asking for the date of birth until the format is correct
        while True: 
            dob = input("Could you tell me your date of birth? (Format: DD/MM/YYYY) ")
        
            # Check if the format is correct (length 10 and '/' in correct positions)
            if len(dob) == 10 and dob[2] == '/' and dob[5] == '/':
                print("Date of birth format looks correct!")
                break  # Exit the loop if the format is correct
            else:
                print("Oops! The date format seems incorrect. Please enter it as DD/MM/YYYY.")
    
        
        # Ask the user for their hobbies
        hobbies = input("What are your hobbies? ")
        
        # Display all the gathered information back to the user
        print("\nThank you for the information!")
        print(f"Your name is {name}, you were born on {dob}, and your hobbies are: {hobbies}.")
    
    # Handle any unexpected errors
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the chatbot function to start the conversation
Willfredo()
