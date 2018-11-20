def getList(nums):
	while True:
		number = str(input("Input a number. Input a non-number to stop:  "))
		for dig in number:
			if dig not in "1234567890":
				print("List complete\n")
				return
		nums.append(number)

def compare(list1, list2):
	if len(list1) == len(list2):
		print("Same length: TRUE")
	else:
		print("Same length: FALSE")
	sum1 = 0
	sum2 = 0
	common = []
	for val in list1:
		sum1 += int(val)
		if val in list2 and val not in common:
			common.append(val)
	for val in list2:
		sum2 += int(val)
	if sum1 == sum2:
		print("Same sum: TRUE")
	else:
		print("Same sum: FALSE")
	if len(common) > 0:
		print("Common values: ", end = '')
		for val in common:
			print(str(val) + "  ", end ='')
	else:
		print("No common values")
	return

def main():
	list1 = [] 
	list2 = []
	getList(list1)
	getList(list2)
	compare(list1, list2)
	print("")
	return

main()
