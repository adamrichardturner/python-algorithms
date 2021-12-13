def bmi(weight, height):
    index = weight / (height ** 2)
    if index <= 18.5:
        return "Underweight"
    elif index <= 25.0:
        return "Normal"
    elif index <= 30.0:
        return "Overweight"
    else:
        return "Obese"

print(bmi(50, 1.80)) # Underweight
print(bmi(80, 1.80)) # Normal
print(bmi(90, 1.80)) # Overweight