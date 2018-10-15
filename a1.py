import math

a = .6666666666666
b = -.75

cosSol = math.cos(a)
sinSol = 2 * math.sin(a)
tanSol = math.tan(b)
logSol = math.log10(55)
lnSol = math.log(60)

print("cos(2/3) = " + str((cosSol)))
print("2sin(2/3) = " + str(sinSol))
print("tan(-3/4) = " + str(tanSol))
print("log(55) = " + str(logSol))
print("ln(60) = " + str(lnSol))
print("")
print("")

x = math.log(15)
b = math.log(2)
megalog = x / b

print("log base 2 of 15:")
print("ln(x) = " + str(x))
print("ln(b) = " + str(b))
print("ln(x) / ln(b) = " + str(megalog))

print("")

x = math.log(40)
b = math.log(4)
megalog = x / b

print("log base 4 of 40:")
print("ln(x) = " + str(x))
print("ln(b) = " + str(b))
print("ln(x) / ln(b) = " + str(megalog))

print("")
print("")

xvalues = [1, 10, 100]
for x in xvalues:
	print("For X = " + str(x))
	print("")
	power = math.sin(x)
	answer = 3 ** power
	print("sin(" + str(x) + ") = " + str(power))
	print("3 ^ " + str(power) + " = " + str(answer))
	print("")
	square = x * x + 1
	log = math.log(square, 2)
	print(str(x) + "^2 + 1 = " + str(square))
	print("Log base 2 of " + str(square) + " = " + str(log))
	print("")
	print("")
