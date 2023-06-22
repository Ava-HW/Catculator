# Catculator
### Video Demo: 

## __Welcome to Catculator!__

This project provides three cat-related calculators.
 
* [Main menu](#main-menu)  
* [Preventing cat-a-strophic calculations](#errors)  
* [Feline like making a grand escape? ](#quit)  
* [Calculator 1: How big will my kitten get?](#size)     
* [Calculator 2: How old is my cat in human years?](#years)    
* [Calculator 3: Is my cat overweight?](#weight)
* [Installation](#requirements)   
* [Acknowledgements](#thanks)

<a name="main-menu"></a>
## __1. Main Menu__

The user is presented with a menu showing the options for the different calculators. 

![image of the menu](https://github.com/Ava-HW/CS50p-final-project/assets/126925721/31404501-b53b-462f-85cd-0f3a8902baac)

If a user inputs something not on the menu, the program will prompt them again. 

<a name="errors"></a>
## __2. Preventing cat-a-strophic calculations__
The calculators are designed to give you a purrfect results every time. This is achieved by: 
* using strip() so whitespace doesn't affect how the program processes input
* ensuring calculations only proceed if a user enters a positive whole number. If any other kind of input is entered, the program prompts the user to try again and displays a message.  

<a name="quit"></a>
## __3. Feline like making a grand escape?__
If a user inputs 'Q' while using a calculator, the program will invite them to press 'enter' to return to the main menu or 'Q' to quit the program.    

If the user inputs 'Q' when presented with the main menu, the program will exit and display a thank you message. 

![image](https://github.com/Ava-HW/CS50p-final-project/assets/126925721/514f0d73-ee38-4691-81fe-4b633f3fcd6b)


<a name="size"></a>
## 4. Calculator 1: How big will my kitten get?

This calculator takes two inputs from the user, how old their kitten is in weeks, and how much their kitten weighs in grams. 

If the given age in weeks is more than 32, the program will display a message saying that their cat is now an adult. 

![adult cat message](https://github.com/Ava-HW/CS50p-final-project/assets/126925721/8394e604-2daa-45f1-a858-372e2791d14c)

#### Example usage

![size example](https://github.com/Ava-HW/CS50p-final-project/assets/126925721/6800bf92-cf5e-4104-818c-600a3977e60b)

<a name="years"></a>
## 5. Calculator 2: How old is my cat in human years?

This calculator takes one input from the user, their cat's age in years. The program will output how old their cat is in human years. 

#### Example usage

![age example](https://github.com/Ava-HW/CS50p-final-project/assets/126925721/ef763a99-4138-4563-9800-e00e688937e1)

<a name="weight"></a>
## 6. Calculator 3: Is my cat overweight?

This calculator takes two inputs from the user: the circumfrence of their cat's ribcage in cm, and the distance from their cat's back knee to their ankle in cm. The program will accept input if the user adds "cm" or " cm" onto the end of their input. 

The program returns the cat's BMI, and if the user's cat is underweight, normal weight, overweight or obese. 

#### Example usage

![bmi example](https://github.com/Ava-HW/CS50p-final-project/assets/126925721/7667c92a-e56a-4555-87cf-a3657a452d80)

<a name="requirements"></a>
## __Installation__

Install with pip:

$ pip install -r requirements.txt

<a name="thanks"></a>
## __Acknowledgements__

All of the formulas used in this program were sourced from Omnicalcualtor

Formula for How big will my kitten get calculator: [Calculator on Omnicalculator](https://www.omnicalculator.com/biology/how-big-will-my-cat-get)

Formula for How old is my cat in human years calculator: [Calculator on Omnicalculator](https://www.omnicalculator.com/biology/cat-age)

Formula for Is my cat overweight calculator: [Calculator on Omnicalculator](https://www.omnicalculator.com/biology/cat-bmi)







