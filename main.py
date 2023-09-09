num = 7
num = int(input("enter a number:"))
factorial = 1
if num < 0:
  print("it is a not factorial")
elif num == 0:
  print("the factorial of 0is1")
else:
  for i in range(1, num + 1):
    factorial = factorial * i
  print("the factorial of", num, "is", factorial)
