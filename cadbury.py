m = int(input())
n= int(input())
p = int(input())
q = int(input())

def main():
	count = 0
	for i in range(m,n+1):
		for j in range(p,q+1):
			count += compute(i,j)
			
	import sys
	sys.stdout.write(str(count))

def compute(l,b):
	ch = 0
	while True:
		if l >= b:
			ch += l//b
			l = l%b
			if l == 0:
				return ch
		elif  b > l:
			ch += b//l
			b = b%l
			if b == 0:
				return ch

main()
