import random

r = random.randint(1,100)
while True:
	num = input('guess no.:')
	num = int(num)
	if num == r:
		print('well done')
		break
	elif num > r:
		print('more than')
	elif num < r:
		print('less than')