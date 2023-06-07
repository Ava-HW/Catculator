def calculate_size(weight, age):
    if int(age) > 32:
        raise ValueError
    else:
        size = round((int(weight) / int(age) )*32, 2)
        return size



def calculate_age(age):
    if int(age) <= 6:
        return (int(age)*19) / 3  + 1
    if int(age) > 6:
        human = (int(age)-6)*4 + 40
        return round(human)
    
def calculate_bmi(rib, leg):
    rib = int(rib)
    leg = int(leg)
    bmi = (rib / 0.7062 - leg) /0.9156 - leg
    bmi = round(bmi, 2)
    if bmi < 15:
        message = "underweight"
    if 29.9 >= bmi and bmi > 15:
        message = "normal weight"
    if 29.9 < bmi < 42:
        message = "overweight"
    if bmi >= 42:
        message = "obese"
    return [bmi, message]

def display_menu():
    print(f"\n")
    print("==== Select a Catculator! ====")
    print("1 - How big will my kitten get calculator")
    print("2 - How old is my cat in human years calculator")
    print("3 - Is my cat overweight calculator")    
    print("Q - Quit")
    print("=== ᨐᵉᵒʷ ᨐᵉᵒʷ ᨐᵉᵒʷ ᨐᵉᵒʷ ===")
    print(f"\n")

def thanks():
    print(f"\n")
    print("==== Thanks for using Catculator! =====")
    print(f"\n")

def header():
    print("=======================================")
    print("======== WELCOME TO CATCULATOR ========")
    print("=======================================")

def main():
    header()
    while True:
        try:
            display_menu()
            choice = input("Choose a calculator: ").strip()
            if choice == "1":
                while True:
                    age = input("How old is your kitten in weeks? ").strip()
                    if int(age) > 32:
                        print("Your cat is older than 32 weeks- that's when your pet becomes an adult! ")
                    if age.isnumeric() == False:
                        print("Please enter a number!")
                    else:
                        break
            if choice == "2":
                while True:
                    age = input("How old is your cat in years? ").strip()
                    if age.isnumeric == False:
                        print("Please enter a number!")
                    else:
                        print(f"Your cat is {round(calculate_age(age))} years old in human years")
                        break
            if choice == "3":
                while True:
                    rib = input("Your cat's rib cage circumfrence in cm: ").replace("cm", "").strip()
                    if rib.isnumeric()== False:
                        print("Please enter a number!")
                    else:
                        break
                while True:
                    leg = input("Distance from your cat's back knee to ankle in cm: ").replace("cm", "").strip()
                    if leg.isnumeric()==False:
                        print('Please enter a number!')
                    else:
                        break
                print(f"Your cat's BMI is {calculate_bmi(rib, leg)[0]}. This means that they are {calculate_bmi(rib, leg)[1]}")
            if choice.upper() == "Q":
                thanks()
                break
            if input("Press enter to continue: ").upper == "Q":
                thanks()
                break
            else:
                continue
        except ValueError:
            print("Please enter a number!")
            continue



if __name__ == "__main__":
    main()