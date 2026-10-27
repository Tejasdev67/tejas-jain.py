def guess_the_number():
    print("====================================")
    print("Welcome to the Number Guessing Game!")
    print("====================================")
    print("I am thinking of a number between 1 and 100.")
    
    # The secret number is now hardcoded to 45
    secret_number = 45
    attempts = 0
    
    while True:
        user_input = input("\nEnter your guess (1-100) or type 'exit' to quit: ").strip()
        
        # Allow the user to gracefully exit the loop
        if user_input.lower() == 'exit':
            print(f"Game over! The correct number was {secret_number}. See you next time!")
            break
            
        # Error handling: Check if the input is actually a valid whole number
        if not user_input.isdigit():
            print("❌ Invalid input! Please enter a valid whole number between 1 and 100.")
            continue
            
        # Convert valid string input to integer
        guess = int(user_input)
        
        # Error handling: Check if the number is within the defined boundary
        if guess < 1 or guess > 100:
            print("❌ Out of bounds! Your guess must be between 1 and 100.")
            continue
            
        # Increment the attempt counter after passing input validation
        attempts += 1
        
        # Check the logic conditions
        if guess== 54:
            print("⇄the number is opposite of 54")
        elif guess== 46:
            print("🤏too close to the number")
        elif guess == 44:
            print("🤏too close to the number")
        
        elif guess ==(47-100) and guess <secret_number:
            print("📉 Too low! Try a higher number.")
        elif guess > secret_number:
            print("📈 Too high! Try a lower number.")
        else:
            print(f"\n🎉 Congratulations! You guessed the number {secret_number} correctly!")
            print(f"🏆 Total attempts: {attempts}")
            break

# This line ensures the game runs immediately when you execute the script
if __name__ == "__main__":
    guess_the_number()

