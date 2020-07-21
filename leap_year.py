 = int(input("Enter a year"))

 def leap_year(a):
     return (lambda a: "This is a leap year" if (a % 4 == 0) and (a % 100 != 0) or (a % 400 == 0) else "This is not a leap year")(a)

     result = leap_year(a)

     print(result)

