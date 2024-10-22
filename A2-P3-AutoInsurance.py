#Program 3 – Auto Insurance
#Write a program that computes monthly insurance according to the provided schedule. 

#Student #: W0491583
#Student Name: Brayden Creese

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)

    #init total cost of the monthly insurance
    totalCost = 0


    # getting user input checking for just male or female as the input
    while True:
        gender = input("Are you 'Male' or 'Female': ").lower()
        if gender in ['Male', 'Female']:
            break
        else:
            print("Invalid Input! Please enter a valid gender.")

    # getting all other user input and checking for invalid inputs
    while True:
        try:
            age = int(input("Enter your age: "))
            break
        except ValueError:
            print("Invalid Input! Please enter a valid number for your age.")

    while True:
        try:
            vehiclePrice = float(input("Enter the price of the vehicle: "))
            break
        except ValueError:
            print("Invalid Input! Please enter a valid number for the price of the vehicle.")


    # calcs for inputs. cheking gender, age, and cost of the vehicle
    if gender == 'Male':
        if 15 <= age < 25:
            totalCost = (0.25 * vehiclePrice) / 12
        elif 25 <= age < 40:
            totalCost = (0.17 * vehiclePrice) / 12
        elif 40 <= age < 70:
            totalCost = (0.10 * vehiclePrice) / 12
    elif gender == 'Female':
        if 15 <= age < 25:
            totalCost = (0.20 * vehiclePrice) / 12
        elif 25 <= age < 40:
            totalCost = (0.15 * vehiclePrice) / 12
        elif 40 <= age < 70:
            totalCost = (0.10 * vehiclePrice) / 12


    # displaying outputs to the user
    print(f"Your monthly insurance will be ${totalCost:.2f}") 

    # YOUR CODE ENDS HERE

main()