#Simple calculator created by Python

#Funtion to add two numbers
def add(numbuer_1, number_2):
	return number_1 + number_2

#Funtion to subtract two numbers
def subtract(number_1, number_2):
	return number_1 - number_2
 
#Funtion to Multiply two numbers
def multiply(number_1, number_2):
	return number_1 * number_2

#Funtion to divide two numbers
def divide(number_1, number_2):
	return number_1 / number_2

print("Select your mathmatical operation -\n" \
	"+. Addition\n" \
	"-. Subtraction\n" \
	"*. Multiplication\n" \
	"/. Division\n")

#Take the users pick
select = input("Select operations from +, -, *, / :")

number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))


if select == '+':
	print(number_1, "+", number_2, "=",
		add(number_1, number_2))
elif select == '-':
	print(number_1, "-", number_2, "=",
		subtract(number_1, number_2))
elif select == '*':
	print(number_1, "*",  number_2, "=",
		multiply(number_1, number_2))
elif select == '/':
	print(number_1, "/", number_2, "=",
		divide(number_1, number_2))
else:
	print("Invalid input, please try again.")
