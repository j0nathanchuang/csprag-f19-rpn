#!/bin/bash/env python3
import readline
import sys
import operator

def red(skk): print("\033[91m {}\033[00m" .format(skk)) #red for negatives
def green(skk): print("\033[92m {}\033[00m" .format(skk)) #green for positives

#hashtable
operators = {
	'+': operator.add,
	'-': operator.sub,
	'*': operator.mul,
	'/': operator.floordiv,
	'%': operator.mod,
	'^': operator.pow,
}

def calculate(arg):
	stack = list()
	for token in arg.split():
		try:
			value = int(token)
			stack.append(value)
		except ValueError:
			function = operators[token]
			arg2 = stack.pop()
			arg1 = stack.pop()
			result = function(arg1, arg2)
			stack.append(result)
		#print(stack)
	if len(stack) != 1:
		raise TypeError
	return stack.pop()

def main():
	try:
		while True:
			result = calculate(input("\033[1;36;40m INPUT: "))
			print((lambda: green(result), lambda: red(result)) [result < 0] ())
	except ValueError:
		print("Input two integers then an operation")
		sys.exit()
	except EOFError:
		print("You terminated the program")
		sys.exit()
	except TypeError:
		print("Malformed input: input two integers then an operation")
		sys.exit()
	except:
		print("An error occured...")
		sys.exit()
	return

if __name__ == '__main__':
	main()
