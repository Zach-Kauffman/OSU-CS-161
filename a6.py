def BtD(num):
	dec = 0
	digit = len(str(num)) - 1
	for char in num:
		dec +=  int(char) * (2 ** int(digit))
		digit -= 1	
	return dec

def DtB(num):
	num = int(num) + 1
	bina = ''
	digit = 0
	chars = []
	while num - 2 ** digit > 0:
		chars += '0'
		digit += 1
	while num > 0:
		while num - 2 ** digit > 0:
			digit += 1
		num -= 2 ** (digit - 1)
		chars[digit - 1] = '1'
		digit = 0
	for io in range(0, len(chars)):
		bina += chars[len(chars) - io - 1]
	return bina

def HtD(num):
	dec = 0
	digit = len(str(num)) - 1
	for char in str(num):
		if ord(char) in range(30,39):
			dec += int(char) * (16 ** digit)
		if ord(char) in range(41,46):
			dec += int(ord(char) - 31) * (16 ** digit)
		digit -= 1
	return int(str(num), 16)	

def DtH(num):
	hexa = hex(int(num))
	return hexa

choice = -1

while str(choice) != "5":
	choice = str(input("1. Bin to Dec\n2. Dec to Bin\n3. Hex to Dec\n4. Dec to Hex\n5. Quit\n\n:"))
	if str(choice) == "5":
		break

	num = 0
	go = 0

	while go != 1:
		if choice in range (3,4): 
			print("Please use capital letters for Hex\n")
		num = input("Number: ")
		if choice in range (1,2):
			for char in str(num):
				if ord(char) not in range(30, 39):
					go = 1
		go = 1
	print("----")
	if str(choice) == "1":
		print(str(num) + " bin to " + str(BtD(num)) + " dec\n")
	if str(choice) == "2":
		print(str(num) + " dec to " + str(DtB(num)) + " bin\n")
	if str(choice) == "3":
		print(str(num) + " hex to " + str(HtD(num)) + " dec\n")
	if str(choice) == "4":
		print(str(num) + " dec to " + str(DtH(num)) + " hex\n")
	

print("Goodbye")
