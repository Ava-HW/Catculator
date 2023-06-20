# Catculator
### Video Demo: 

## __Welcome to Catculator!__

This project provides three cat-related calculators:
 
* [Main menu](#main-menu)  
* [Preventing cat-a-strophic cacluations](#errors)  
* [Feline like making a grand escape? ](#quit)  
* [Calculator 1: How big will my kitten get?](#size)     
* [Calculator 2: How old is my cat in human years?](#years)    
* [Calculator 3: Is my cat overweight?](#weight)    
* [Acknowledgements](#thanks)

<a name="main-menu"></a>
## __1. Main Menu__

The user is presented with a menu showing the options for the different calculators. 

![image of the menu](https://github.com/Ava-HW/CS50p-final-project/assets/126925721/31404501-b53b-462f-85cd-0f3a8902baac)

If a user inputs something not on the menu, the program will re-prompt them to select a calculator. 

<a name="errors"></a>
## __2. Preventing cat-a-strophic cacluations__
The calculators are designed to give you a purrfect results every time. This is achieved by: 
* using [xxxxx] so whitespace doesn't affect how the program processes input
* ensuring calculations only proceed if a user enteres apositive whole numbers. If any other kinds of input is entered, the program prompts the use to try again [in accordance with loop].  

<a name="quit"></a>
## __3. Feline like making a grand escape?__
If a user inputs 'Q' while using a calculator, the program will invite them to press 'enter' to return to the main menu or 'Q' to quit the program. Is the return to the main menu.

If the user inputs 'Q' when presented with the main menu, the program will exit and display a thank you message. 

![image](https://github.com/Ava-HW/CS50p-final-project/assets/126925721/514f0d73-ee38-4691-81fe-4b633f3fcd6b)

If a user inputs Q while using a calculator, the program will display the option to quit completely or continue by pressing enter. If the user enters neither Q nor enter, the program will return to the main menu anyway. 

<a name="size"></a>
## 4. Calculator 1: How big will my kitten get?

This calculator takes two inputs from the user, how old their kitten is in weeks, and how much their kitten weighs in kgs. If the user inputs something that is not an interger, the program will re-prompt them until they enter a valid input or select Q to quit. 

If the given age in weeks is more than 32, the program will display a message saying that their cat is now an adult. 

![Message saying that the user's cat is an adult](https://github.com/Ava-HW/CS50p-final-project/assets/126925721/ebd610d5-99d6-41e1-93a8-a4fa45e071f8)

##### Example usage

![image of calculator 1 usage](https://github.com/Ava-HW/CS50p-final-project/assets/126925721/cfe77183-f335-4d57-b110-12f2c6ef16c6)

<a name="years"></a>
## 2. How old is my cat in human years?

This calculator takes one input from the user, their cat's age in years. The program will output how old their cat is in human years. 

#### Example usage

![image](https://github.com/Ava-HW/CS50p-final-project/assets/126925721/4ac2b414-cb21-438e-8f93-701b521ac1ba)

<a name="weight"></a>
## 3. Is my cat overweight?

This calculator takes two inputs from the user- the circumfrence of their cat's ribcage in cm, and the distance from their cat's back knee to their ankle in cm. The program will accept input if the user adds "cm" or " cm" onto the end of their input. If the user doesn't enter a valid input, the program will reprompt them. 

The program returns the cat's BMI, and if the user's cat is underweight, normal weight, overweight or obese. 

#### Example usage

![image of calculator 3](https://github.com/Ava-HW/CS50p-final-project/assets/126925721/7a29eda0-03d7-4cdc-a551-37e34951d308)

<




## __Installation__

Install with pip:

$ pip install -r requirements.txt

<a name="thanks"></a>
## __Acknowledgements__

Formula for How big will my kitten get calculator: [Calculator on Omnicalculator](https://www.omnicalculator.com/biology/how-big-will-my-cat-get)

Formula for How old is my cat in human years calculator: [Calculator on Omnicalculator](https://www.omnicalculator.com/biology/cat-age)

Formula for Is my cat overweight calculator: [Calculator on Omnicalculator](https://www.omnicalculator.com/biology/cat-bmi)







