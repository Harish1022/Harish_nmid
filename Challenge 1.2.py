#1.2 Write a program that determines whether a year entered by the user is a leap year or not using ifelif-else statements.
year = int(input("Enter a year: "))
if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print(year, "is a leap year")
    else:
      print(year, "is not a leap year")
  else:
    print(year,"is a leap year")
else:
  print(year,"is not a leap year")
  