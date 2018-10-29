for ii in range(0,5):
	print("Hello World!")

for ii in range(0,101):
	print("Hello student " + str(ii) + "!")

number = 50

while number >=  0:
	print(str(number))
	number -= 1

while True:
	number = int(input("Input a number between 25 and 50:  "))
	if number <= 50:
		if number >= 25:
			print("Good job")
			break

character = 'A'

while True:
	character = str(input("Input a lowercase character:  "))
	if character[0].islower():
		if len(character) == 1:
			print("Good job")
			break

for ii in range (1,6):
	for jj in range (1,6):
		number = ii * jj
		print(str(number) + " ", end='')
		if len(str(number)) == 1:
			print(" ", end='')
	print("\n")

correct = 0

while correct != 3:
	number = input("Input a number NOT between 25 and 50:  ")
	if str(number).isdigit():
		if int(number) > 50 or int(number) < 25:
			print(str(number))
			correct += 1
		
		
