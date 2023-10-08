# Initialize variables
daily_goal = []
water_intake = 0

user_input = input("What's your daily water intake goal (in glasses)? ")
daily_goal.append(float(user_input))

# Loop to track water intake
while water_intake < daily_goal[0]:  # Compare with the first element of daily_goal
    print(f"Daily water intake: {water_intake} out of {daily_goal[0]} glasses")

    try:
        intake = float(input("Enter the number of glasses you drank today (or 0 to quit): "))

        # Check if the input is valid
        if intake < 0:
            print("Invalid input. Please enter a non-negative number.")
            continue

        # Update water intake count
        water_intake += intake

        # Check if the daily goal is reached
        if water_intake >= daily_goal[0]:
            print("You've reached your daily goal 🥳!")
        else:
            print(f"Keep going! you've {daily_goal[0]-water_intake} of glass left")

    except ValueError:
        print("Invalid input. Please enter a number.")

print("Goodbye!")