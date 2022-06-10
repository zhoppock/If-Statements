food = ""
foodcal = 0

food = input("What food would you like to eat? ")
foodCal = int(input("How many calories is it? "))

if foodCal > 400:
    print (food, "is not that healthy!")
elif foodCal > 250:
  print (food, "is not that bad on occasion!")
else:
   print (food, "is a healthy option!")
print ("Enjoy that", foodCal, "calorie", food + "!")