height=float(input('enter height in cm\n'))
weight=int(input('enter weight in kg:\n'))


BMI=float(weight/(height**2))
print(f"You BMI is {BMI}")

if BMI<=20.6:
    print("You are underweight.")
elif BMI<=23.9:
    print("You are healthy.")
elif BMI<=26.7:
    print("You are overweight.")
elif BMI<=69.9:
    print("You are obese.")
else:
    print("you are clinically obese")
