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

![image](https://github.com/Ava-HW/CS50p-final-project/assets/126925721/bcde1cf3-a86e-419c-9627-9b270579f19a)

If a user inputs something not on the menu, the program will re-prompt them to select a calculator. If a user inputs Q, the program will exit. 

#### __Calculator 1 - How big will my kitten get calculator__

This calculator takes two inputs from the user, how old their kitten is in weeks, and how much their kitten weighs in kgs. If the user inputs something that is not an interger, the program will re-prompt them until they enter a valid input or select Q to quit. 

If the given age in weeks is more than 32, the program will display a message saying that their cat is now an adult. 

![image](https://github.com/Ava-HW/CS50p-final-project/assets/126925721/ebd610d5-99d6-41e1-93a8-a4fa45e071f8)

##### Example usage

![image](https://github.com/Ava-HW/CS50p-final-project/assets/126925721/4ecd9bba-5eb0-4e84-bb6d-5b0a5f981e56)

#### __Catculator 2- How old is my cat in human years?__

This calculator takes one input from the user, their cat's age in years. The program will output how old their cat is in human years. If the user doesn't enter an interger, the program will re-prompt them until they enter a valid input or quit. 

##### Example usage

![image](https://github.com/Ava-HW/CS50p-final-project/assets/126925721/72d6f722-ddec-42dd-9d0a-1f4dbd17ef6e)



