print("1 = Yes, 0 = No\n")

student = int(input("Are you a student at OSU? 1 for yes, 0 for no\n"))

if student == 1:
	print("You are a student. Good job.\n")
elif student == 0:
	print("You are not a student.\n")
else:
	print("You answered incorrectly somehow.\n")

number = int(input("Input a number between 0 and 50\n"))

if number < 25:
	print(str(number) + " is less than 25\n")
elif number > 25: 
	print(str(number) + " is greater than 25\n")
else:
	print("Your number is 25\n")

surname = raw_input("What is your last name?\n")

kyllo = ['a', 'u', 'w', 'v', 'x', 'y', 'z']
shivers = ['o', 'p', 'q', 'r', 's', 't']
white = ['e', 'f', 'g', 'h', 'i', 'j']
worley = ['k', 'l', 'm', 'n']
rosenzweig = ['b', 'c', 'd']

done = 0

while done == 0:

	for letter in kyllo:
		if surname[0] == letter:
			print("Your advisor is Sarah Kyllo\n")
			done = 1

	for letter in shivers:
		if surname[0] == letter:
			print("Your advisor is Shannon Shivers\n")
			done = 1

	for letter in white:
		if surname[0] == letter:
			print("Your advisor is Michelle White\n")
			done = 1

	for letter in worley:
		if surname[0] == letter:
			print("Your advisor is Aaron Worley\n")
			done = 1

	for letter in rosenzweig:
		if surname[0] == letter:
			print("Your advisor is Julia Rosenzweig\n")
			done = 1

	if done == 0:
		print("Your last name doesn't start with a letter so you don't have an advisor.\nSorry.\n")
	done = 1

grade = int(input("Enter a nubmer between 0 and 100\n"))

if grade > 100:
	print("You got extra credit somehow\n")
elif grade > 90:
	print("You got an A\n")
elif grade > 80:
	print("You got a B\n")
elif grade > 70:
	print("You got a C\n")
elif grade > 60:
	print("You got a D\n")
elif grade > 0:
	print("You got an F\n")
else:
	print("How in god's name did you get a negative grade\n")

firstword = raw_input("Input a word\n")
secondword = raw_input("Input a second word\n")

words = [firstword, secondword]
words.sort()

if words[0][0] == words[1][0]:
	print("Both your words start with the same letter\n")
else:
	print(words[0] + " comes before " +  words[1] +  " in the alphabet.\n")

foodchoice = int(input("Hamburger or Hotdog? 1 for burger, 0 for hotdog\n"))
if foodchoice == 1:
	cheese = int(input("Do you want cheese? 1 for yes 0 for no\n"))
	if cheese == 1:
		print("You ordered a hamburger with cheese.")
	else:
		print("You ordered a hamburger without cheese. How boring.")
elif foodchoice == 0:
	mustard = int(input("Do you want mustard? 1 for yes 0 for no\n"))
	if mustard == 1:
		print("You ordered a hotdog with mustard")
	else:
		print("You ordered a hotdog without mustard")
else:
	print("Bro did you really get to the end of the program and NOT order anything?")









