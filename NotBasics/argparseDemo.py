import argparse
import sys

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('--x', type=float, default=1.0,
						help='First number')
	parser.add_argument('--y', type=float, default=1.0,
						help='First number')
	parser.add_argument('--op', type=str, default='add',
						help='Operation(add, sub, mul, div)')
	args = parser.parse_args()
	sys.stdout.write(str(calc(args)))

def calc(args):
	if args.op == 'add':
		return args.x + args.y
	elif args.op == 'sub':
		return args.x - args.y
	elif args.op == 'mul':
		return args.x * args.y
	elif args.op == 'div':
		return args.x / args.y
		
if __name__ == "__main__":
	main()