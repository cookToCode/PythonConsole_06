#cookToCode

#This program introduces "functions" | functions are a great way to break up code into smaller chuncks

#This program will ask the user how many * and calculate the calories and how long it will take to jog/run the calories off

#variable library
bigMac = 0
medFry = 0
smallShake = 0
calories = 0
jog = 0
run = 0


#These blocks of code are called "functions"
# the syntax is "def 'name'():"  <----the "def" lets the code know that this is a function and the () holds the parameters

#This gets the input info of how many of each product the user consumed
def gatherInfo():   #Becuase the () are empty, that means this function doesn't need anything to run
    print('For every question, please only answer whole numbers. No one eats half of a Big Mac.......\n\n\n')
    bigMac = int(input("How many Big Mac's did you eat? "))
    medFry = int(input("\nHow many orders of medium fries did you eat? "))
    smallShake = int(input("\nHow many small shakes did you drink? "))
    calConversion(bigMac, medFry, smallShake)#<----Functions can be called within functions
    #The above function has parameters that need to be set
    #This means that the function "calConversion" is specifically looking for three different variables
    #For the sake of simplicity, i have named the parameters the same as the variables
    #This is something you may not want to have turn into a habbit as it can get super confusing in big projects

#This will convert the food to calories
def calConversion(bigMac, medFry, smallShake):#The words in the () are called parameters | They don't need to relate to the variables that are going into it
    bigMac = bigMac*563
    medFry = medFry*378
    smallShake = smallShake*530
    calories = bigMac+medFry+smallShake
    #This portion converts calories to how many hours it will take to burn them
    #rounded to the nearest tenths place
    jog = round(calories/398, 1)
    run = round(calories/557, 1)
    print(f'\n\nIn total, you consumed {calories} calories.\n')
    print(f'It will take {jog} hours to burn off {calories} calories while jogging.\n')
    print(f'It will take {run} hours to burn off {calories} calories while running.\n')


gatherInfo()    #<---This is how you call a function





