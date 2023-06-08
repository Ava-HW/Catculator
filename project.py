def calculate_size(age, weight):
    if int(age) > 32:
        return("Your cat is older than 32 weeks- that's when they become an adult!")
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
        display_menu()
        choice = input("Choose a calculator: ").strip()
        if choice == "1":
            while True:
                age = input("How old is your kitten in weeks? ").strip()
                if age.isnumeric() == False:
                    print("Please enter a number!")
                else:
                    age = int(age)
                    break
            while True:
                weight = input("How much does your kitten weigh in kgs? ").strip()
                if weight.isnumeric()== False:
                    print("Please enter a number!")
                else:
                    weight = int(age)
                    break
            print(f"Your cat's bmi is {calculate_size(age, weight)[0]}. This means they are {calculate_size(age, weight)[0]}.")
        if choice == "2":
            while True:
                age = input("How old is your cat? ").strip()
                if age.isnumeric == False:
                    print("Please enter a number!")
                else:
                    age= int(age)
                    print(f"Your cat's age in human years is {calculate_age(age)} years old.")
                    break
        if choice == "3":
            while True:
                rib = input("What is the circumfrence of your cat's rib cage? ").strip()
                if rib.isnumeric()==False:
                    print("Please enter a number!")
                else:
                    rib= int(rib)
                    break
            while True:
                leg = input("What is the distance from your cat's back knee to their ankle? ").strip()
                if leg.isnumeric() == False:
                    print("Please enter a number! ")
                else:
                    leg= int(leg)
                    break
            print(f"Your cat's BMI is {calculate_bmi(rib, leg)[0]}. This means that they are {calculate_bmi(rib, leg)[1]}.")
        if choice.upper().strip() == "Q":
            thanks()
            break
        if input("Press enter to continue: ").upper == "Q":
            thanks()
            break




if __name__ == "__main__":
    main()
