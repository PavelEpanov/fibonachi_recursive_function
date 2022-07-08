def main():
	x = int(input("X: "))
	fibonachi = fib(x)
	print(fibonachi)


def fib(x):

	if x == 0 or x == 1:
		return 1
	else:
		return fib(x -1) + fib(x - 2)

main()