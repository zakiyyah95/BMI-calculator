height = float(input("Enter your height in meters. "))

weight = float(input("Enter your weight in kilograms. "))


bmi = round(weight / height ** 2)
if bmi < 18.5:
    print(f"Your bmi is {bmi}, you have a normal weight.")
elif bmi < 25:
    print(f"Your bmi is {bmi}, you are over weight.")
elif bmi < 30:
    print(f"Your bmi is {bmi}, you are obese.")
else:
    print(f"Your bmi is {bmi}, you are clinically obese.")