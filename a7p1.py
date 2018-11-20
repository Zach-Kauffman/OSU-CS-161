def getNames(names):
	while True:
		name = str(input("Input 0 to stop\nInput a name:  "))
		if name == '0':
			return
		for char in name:
			if char not in "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM":
				print("Bad input\n")
				name = ''
				break
		if name != '':
			names.append(name)
	return

def parseNames(names, letters):
	for x in range(26):
		for name in names:
			for char in name:
				if chr(65+x) == char or chr(97+x) == char:
					letters[x] += 1
	return				

def printLetters(letters):
	letter = 0
	for val in letters:
		if val > 0:
			print(chr(letter + 65) + " - " + str(val))
		letter += 1
	return

def main():
	names = []
	getNames(names)
	letters = []
	for x in range(26):
		letters.append(0)
	parseNames(names, letters)
	printLetters(letters)
	return

main() 
