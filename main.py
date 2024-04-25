def calculate_bmi(weight, height):
    """Calculate BMI based on weight and height."""
    bmi = weight / (height ** 2)
    return bmi

def classify_bmi(bmi):
    """Classify BMI into categories."""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def main():
    print("Welcome to the BMI Calculator!")
    
    # Repeat the process until the user wants to exit
    while True:
        try:
            # Get user input for weight and height
            weight = float(input("Enter your weight in kilograms (kg): "))
            height = float(input("Enter your height in meters (m): "))
            
            # Calculate BMI
            bmi = calculate_bmi(weight, height)
            
            # Classify BMI
            category = classify_bmi(bmi)
            
            # Display the result
            print(f"Your BMI is {bmi:.2f}. You are in the '{category}' category.")
            
            # Ask the user if they want to calculate again
            again = input("Do you want to calculate another BMI? (yes/no): ").strip().lower()
            if again != 'yes':
                break
        
        except ValueError:
            print("Invalid input. Please enter numeric values for weight and height.")
            continue

    print("Thank you for using the BMI Calculator. Goodbye!")

if __name__ == "__main__":
    main()
