 in range(1, 101):
     if (i % 5 == 0) and (i % 3 == 0):
             i = "FizzBuzz"
	             FizzBuzz.append(i)
		         elif i % 3 == 0:
			         i = "Fizz"
				         Fizz.append(i)
					     elif i % 5 == 0:
					             i = "Buzz"
						             Buzz.append(i)
							         elif not(i % 5 == 0 or i % 3 == 0):
								         Numbers.append(i)


									 print(FizzBuzz)
									 print(Buzz)
									 print(Fizz)
									 print(Numbers)
