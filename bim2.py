def calculate_bmi(weight, height):
  bmi = weight / (height * height)
  return bmi
weight = 75
height = 1.75
bmi = calculate_bmi(weight, height)
print(bmi)
