Name=input("What is your Name:")
Weight=float(input("What is your Weight in Kg?"))
Height=float(input("What is your Height in metres?"))
BMI=Weight/(Height*Height)
if BMI<=18.5:
    print(f"Your BMI is {BMI} which means you are Underweight")
elif BMI<=24.9:
      print(f"Your BMI is {BMI} which means you are Normal")
elif BMI<=29.9:
      print(f"Your BMI is {BMI} which means you are Overweight")
else:
    print(f"Your BMI is {BMI} You are Obese")