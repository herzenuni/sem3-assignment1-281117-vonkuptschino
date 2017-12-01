
def digitsSum(num):
	num = str(num)
	sum = 0
	for i in num:
		sum += int(i) ** 2
	return sum

def usinp():
	n = int(input("input the number of digits: "))
	res = []
	for i in range((10 ** (n - 1)), (10 ** n)):
		if digitsSum(i) % 17 == 0:
			res.append(i)
	print("{}-digit nums which sum of powered digits is devisible by 17:\n {}". format(n, res))
	

if __name__ == "__main__":
	usinp()