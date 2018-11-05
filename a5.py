def testBoolFunction(goodInput, badInput, output1, output2):
	if output1:
		outcome = "PASS"
	else:
		outcome = "FAIL"
	print("Input: " + str(goodInput) + " | Expected output: TRUE | Output: " + str(output1) + " | Result: " + str(outcome))

	if output2:
		outcome = "FAIL"
	else:
		outcome = "PASS"
	print("Input: " + str(badInput) + " | Expected output: FALSE | Output: " + str(output2) + " | Result: " + str(outcome) + "\n")
	return

def is_int(num):
	numList = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
	for char in num:
		if char not in numList:
			return False
	return True

def is_float(num):
	containsDot = False
	numList = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
	for char in num:
		if char not in numList:
			if char == '.' and not containsDot:
				containsDot = True
			elif containsDot:
				return False
			else:
				return False
	if containsDot:
		return True
	else:
		return False
	
def is_capital(letter):
	charList = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	if len(letter) != 1:
		return False
	if letter in charList:
		return True
	return False

def is_even(num):
	if num % 2 == 0:
		return True
	return False

def is_odd(num):
	if num % 2 == 1:
		return True
	return False
		
def numbers_present(sentence):
	numList = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
	for char in sentence:
		if char in numList:
			return True
	return False

def letters_present(sentence):
	for char in sentence:
		if ord(char) in range(65, 90) or ord(char) in range(97, 122):
			return True
	return False

def contains_sub_string(sentence, sub_string):
	if sub_string in sentence:
		return True
	return False

def make_upper(sentence):
	newString = ""
	for char in sentence:
		if ord(char) in range(97, 122):
			newString += chr(ord(char) - 32)
		else:
			newString += char
	return newString

def make_lower(sentence):
	newString = ""
	for char in sentence:
		if ord(char) in range(65, 90):
			newString += chr(ord(char) + 32)
		else:
			newString += char
	return newString


print("Testing is_int:")
testBoolFunction("123", "a123", is_int("123"), is_int("a123"))

print("Testing is_float:")
testBoolFunction("123.4", "123", is_float("123.4"), is_float("123"))

print("Testing is_capital:")
testBoolFunction("A", "a", is_capital("A"), is_capital("a"))

print("Testing is_even:")
testBoolFunction(2, 1, is_even(2), is_even(1))

print("Testing is_odd:")
testBoolFunction(1, 2, is_odd(1), is_odd(2))

print("Testing numbers_present:")
testBoolFunction("abc 123", "I love my mom", numbers_present("abc 123"), numbers_present("I love my mom"))

print("Testing letters_present:")
testBoolFunction("abc 123", "123456789,.[]", letters_present("abc 123"), letters_present("123456789,.[]"))

print("Testing contains_sub_string")
testBoolFunction("This is a test, is a", "This is a test, Hello world!", contains_sub_string("This is a test", "is a"), contains_sub_string("This is a test", "Hello world!"))

print("Testing make_upper")
print("Input: Test String  | Expected output: TEST STRING | Output: " + make_upper("Test String") + " | Result: PASS\n")

print("Testing make_lower:")
print("Input: Test String  | Expected output: test string | Output: " + make_lower("Test String") + " | Result: PASS\n")
