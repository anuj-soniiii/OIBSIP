# We take a input from user of weight in kilogram.
weight = float(input("Enter Your Weight :"))

# Now we take a input from user of height in meter.
height = float(input("Enter your height :"))

# Now we will calculate our BODY MASS INDEX with this formula.
bmi = weight / (height)**2

#In this step we will print our bmi. 
print(bmi)

#Now we categories bmi result.
if bmi <= 18.5:
       print("You are underweight")

elif 18.5 < bmi <= 24.9:
       print("You are Healthy Weight")

elif 25 < bmi <= 29.9:
       print("You are Overweight ")

else:
       print("You are Obese")
