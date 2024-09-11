# Define constants
TAX_RATE = 0.21  # 21% tax
TIP_RATE = 0.15  # 15% tip

# Get user input for the cost of the meal and extract the number
input_str = input("Please enter the cost (format 'Cost of the meal: xy.wz'): ")
meal_cost = float(input_str.split(":")[1].strip())  # Extracting the numeric part from input

# Calculate tax and tip
tax = meal_cost * TAX_RATE
tip = meal_cost * TIP_RATE

# Calculate total cost
total = meal_cost + tax + tip

# Display the results rounded to 3 decimal places
print(f"Tax: {tax:.3f} , Tip: {tip:.3f} , Total: {total:.3f}")
