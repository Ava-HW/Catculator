# Catculator
### Video Demo: 

### __Description__

This project provides the user with three cat-related calculators, to figure out a cat's BMI, what a cat's age in human years is, and how big a kitten will get. 

### __Requirements__

All requirements for this project are contained in requirements.txt- these can be installed by running ```pip install -r requirements.txt```.

### __Usage__

Users can press Q to quit at anytime, including while using a calculator. If the user inputs Q while using a calculator, the program will return to the main menu. Whitespace doesn't affect how the program processes input. 

#### __Main Menu__

The user is presented with a menu showing the options for the different calculators. 

![Catculator main menu](https://github.com/Ava-HW/CS50p-final-project/assets/126925721/bcde1cf3-a86e-419c-9627-9b270579f19a)

If a user inputs something not on the menu, the program will re-prompt them to select a calculator. If a user inputs Q, the program will exit. 

#### __1 - How big will my kitten get?__

This calculator takes two inputs from the user, how old their kitten is in weeks, and how much their kitten weighs in kgs. If the user inputs something that is not an interger, the program will re-prompt them until they enter a valid input or select Q to quit. 

If the given age in weeks is more than 32, the program will display a message saying that their cat is now an adult. 

![Message saying that the user's cat is an adult](https://github.com/Ava-HW/CS50p-final-project/assets/126925721/ebd610d5-99d6-41e1-93a8-a4fa45e071f8)

##### Example usage

![Example of calculator 1](https://github.com/Ava-HW/CS50p-final-project/assets/126925721/35bcb8ce-e44e-4a15-9588-45ea70d59ee7)

#### __2 - How old is my cat in human years?__

This calculator takes one input from the user, their cat's age in years. The program will output how old their cat is in human years. If the user doesn't enter an interger, the program will re-prompt them until they enter a valid input or quit. 

##### Example usage

![Example of calculator 2](https://github.com/Ava-HW/CS50p-final-project/assets/126925721/8d0b174e-2148-4a31-ad11-e77d036fa0d4)

#### __3 - Is my cat overweight?__

This calculator takes two inputs from the user- the circumfrence of their cat's ribcage in cm, and the distance from their cat's back knee to their ankle in cm. The program will accept input if the user adds "cm" or " cm" onto the end of their input. If the user doesn't enter a valid input, the program will reprompt them. 

The program returns the cat's BMI, and if the user's cat is underweight, normal weight, overweight or obese. 

##### Example usage

![Example of calculator 3](https://github.com/Ava-HW/CS50p-final-project/assets/126925721/350bf287-0764-4276-a7ee-ceedb7d77ec5)

#### __Q - Quit__

If the user inputs Q when presented with the main menu, the program will exit and display a thank you message. 

![image](https://github.com/Ava-HW/CS50p-final-project/assets/126925721/514f0d73-ee38-4691-81fe-4b633f3fcd6b)

If a user inputs Q while using a calculator, the program will display the option to quit completely or continue by pressing enter. If the user enters neither Q nor enter, the program will return to the main menu anyway. 

### __Acknowledgements__

Formula for How big will my kitten get calculator: [Calculator on Omnicalculator](https://www.omnicalculator.com/biology/how-big-will-my-cat-get)

Formula for How old is my cat in human years calculator: [Calculator on Omnicalculator](https://www.omnicalculator.com/biology/cat-age)

Formula for Is my cat overweight calculator: [Calculator on Omnicalculator](https://www.omnicalculator.com/biology/cat-bmi)







