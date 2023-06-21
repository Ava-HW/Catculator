def calculate_size(age, weight):
    if age > 32 and age != 32:
        raise ValueError("Your cat is older than 32 weeks")
    else:
        size = int(round((weight/age)*32, 2))
        return size



def calculate_age(age):
    try:
        if age <= 6:
                return round((age*19) / 3  + 1)
        if age > 6:
                return round((age-6)*4 + 40)
    except ValueError:
        raise ValueError("Please enter an interger")



def calculate_bmi(rib, leg):
    bmi = (rib / 0.7062 - leg) /0.9156 - leg
    if bmi < 15:
        message = "underweight"
    if 29.9 >= bmi >= 15:
        message = "normal weight"
    if 29.9 < bmi < 42:
        message = "overweight"
    if bmi >= 42:
        message = "obese"
    return [round(bmi), message]

def header():
    print("=====================================================")
    print("============== WELCOME TO CATCULATOR ================")
    print("=====================================================")

def display_menu():
    print(f"\n")
    print("=============== Select a Catculator! ===============")
    print("= 1 - How big will my kitten get?                  =")
    print("= 2 - How old is my cat in human years?            =")
    print("= 3 - Is my cat overweight?                        =")
    print("= Q - Quit                                         =")
    print("================ ᨐᵉᵒʷ ᨐᵉᵒʷ ᨐᵉᵒʷ ᨐᵉᵒʷ ===============")
    print(f"\n")

def thanks():
    print(f"\n")
    print("==== Thanks for using Catculator! =====")
    print(f"\n")



def main():
    header()
    while True:
        quit = False
        display_menu()
        choice = input("Choose a calculator: ").strip()
        if choice == "1":
            while True:
                age = input("How old is your kitten in weeks? ").strip()
                if age.upper() =="Q":
                    quit = True
                    break
                elif age.isnumeric() == False:
                        print("Please enter a whole positive number!!")
                elif int(age) > 32:
                        print("Your cat is older than 32 weeks, which is when they become an adult! Press Q to exit")
                else:
                    age = int(age)
                    break
            while True:
                if quit == True:
                    break
                weight = input("How much does your kitten weigh in grams? ").upper().replace("G", "").strip()
                if weight.upper()== "Q":
                    quit = True
                    break
                elif weight.isnumeric()== False:
                    print("Please enter a whole positive number!")
                else:
                    weight = int(weight)
                    break
            if quit == False:
                print(f"Your kitten will grow to {calculate_size(age, weight)} grams.")
        if choice == "2":
            while True:
                age = input("How old is your cat in years? ").strip()
                if age.upper()=="Q":
                    break
                elif age.isnumeric == False:
                    print("Please enter a whole positive number!")
                    continue
                else:
                    age= int(age)
                    print(f"Your cat's age in human years is {calculate_age(age)} years old.")
                    break
        if choice == "3":
            while True:
                rib = input("What is the circumference of your cat's rib cage in centimeters? ").upper().replace("CM", "").strip()
                if rib.upper()=="Q":
                    quit = True
                    break
                if rib.isnumeric()==False:
                    print("Please enter a whole positive number!")
                else:
                    rib= int(rib)
                    break
            while True:
                if quit == True:
                    break
                leg = input("What is the distance from your cat's back knee to their ankle in centimeters? ").upper().replace("CM", "").strip()
                if leg.upper()=="Q":
                    quit=True
                    break
                elif leg.isnumeric() == False:
                    print("Please enter a whole positive number!")
                else:
                    leg= int(leg)
                    break
            if quit == False:
                print(f"Your cat's BMI is {calculate_bmi(rib, leg)[0]}. This means that they are {calculate_bmi(rib, leg)[1]}.")
        if choice.upper().strip() == "Q":
            thanks()
            break
        if input("Press enter to return to the main menu or Q to quit: ").upper().strip() == "Q":
            thanks()
            break




if __name__ == "__main__":
    main()
