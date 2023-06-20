x=10
y=20
if x<y:
    print("TRUE")
else:
    print("FALSE")

if x>y | y < 50:
    print("TRUE")
else:
    print("FALSE")

marks= 90
if marks< 40:
    print("E")
elif marks < 50:
    print("D")
elif marks< 60:
    print("C")
elif marks < 70:
    print("B")
else:
    print("A")


#Implement a betti9ng game where the user is required to enter any number
# from 1-4 and win something or lose depending on the number entered
bettingNumber = 0
if bettingNumber ==1:
    print("You lost")
elif bettingNumber== 2:
    print("You won a cow")
elif bettingNumber== 3:
    print("You won a car")
elif bettingNumber == 4:
    print("You won a trip to Kenya")
else:
    print("Please enter a number from 1-4 to bet")
#Implement the logic to calculate the BMI of any user.
#Henceforth , display the results as either:
# 1.Underweight 2.Normal weight 3.Overweight 4.Obese
#Use the formula BMI = weight in Kgs divide by height in metres squared

#Use the scale:
        #18 and below-----Underweight
        #18.1------29-----Normal weight
        #29.1------34-----Overweight
        #34.1 and above-----Obese
height=1.84
weight=85
BMI=weight/(height*height)
if BMI<=18:
    print("Underweight")
elif BMI >18 and BMI <=29:
    print("Normal weight")
elif BMI >29 and BMI <=34:
    print("Overweight")
else:
    print("Obese")




