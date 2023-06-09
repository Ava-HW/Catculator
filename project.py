def calculate_size(age, weight):
    if int(age) > 32:
        raise ValueError
    else:
        size = round((int(weight) / int(age) )*32, )
        return size



def calculate_age(age):
    if int(age) <= 6:
            return int((int(age)*19) / 3  + 1)
    if int(age) > 6:
            return int((int(age)-6)*4 + 40)



def calculate_bmi(rib, leg):
    bmi = (int(rib) / 0.7062 - int(leg)) /0.9156 - int(leg)
    bmi = round(bmi, 2)
    if bmi < 15:
        message = "underweight"
    if 29.9 >= bmi >= 15:
        message = "normal weight"
    if 29.9 < bmi < 42:
        message = "overweight"
    if bmi >= 42:
        message = "obese"
    return [bmi, message]

def header():
    print("=====================================================")
    print("============== WELCOME TO CATCULATOR ================")
    print("=====================================================")

def display_menu():
    print(f"\n")
    print("=============== Select a Catculator! ===============")
    print("= 1 - How big will my kitten get calculator        =")
    print("= 2 - How old is my cat in human years calculator  =")
    print("= 3 - Is my cat overweight calculator              =")
    print("= Q - Quit                                         =")
    print("================ ᨐᵉᵒʷ ᨐᵉᵒʷ ᨐᵉᵒʷ ᨐᵉᵒʷ ===============")
    print(f"\n")

def thanks():
    print(f"\n")
    print("==== Thanks for using Catculator! =====")



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
                        print("Please enter a number!")
                elif int(age) > 32:
                        print("Your cat is older than 32 weeks- that's when they become an adult! Press Q to exit")
                        quit = True
                else:
                    age = int(age)
                    break
            while True:
                if quit == True:
                    break
                weight = input("How much does your kitten weigh in kgs? ").strip()
                if weight.upper()== "Q":
                    quit = True
                    break
                elif weight.isnumeric()== False:
                    print("Please enter a number!")
                else:
                    weight = int(age)
                    break
                if quit == False:
                    print(f"Your kitten will grow to {calculate_size(age, weight)} kgs.")
        if choice == "2":
            while True:
                age = input("How old is your cat? ").strip()
                if age.upper()=="Q":
                    break
                elif age.isnumeric == False:
                    print("Please enter a number!")
                else:
                    age= int(age)
                    print(f"Your cat's age in human years is {calculate_age(age)} years old.")
                    break
        if choice == "3":
            while True:
                rib = input("What is the circumfrence of your cat's rib cage in cm? ").upper().replace("CM", "").strip()
                if rib.upper()=="Q":
                    quit = True
                    break
                if rib.isnumeric()==False:
                    print("Please enter a number!")
                else:
                    rib= int(rib)
                    break
            while True:
                if quit == True:
                    break
                leg = input("What is the distance from your cat's back knee to their ankle? ").upper().replace("CM", "").strip()
                if leg.upper()=="Q":
                    break
                elif leg.isnumeric() == False:
                    print("Please enter a number! ")
                else:
                    leg= int(leg)
                    break
            if quit == False:
                print(f"Your cat's BMI is {calculate_bmi(rib, leg)[0]}. This means that they are {calculate_bmi(rib, leg)[1]}.")
                break
        if choice.upper().strip() == "Q":
            thanks()
            break
        if input("Press enter to continue or Q to quit: ").upper().strip() == "Q":
            thanks()
            break




if __name__ == "__main__":
    main()
