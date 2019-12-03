import random

r = random.randint(1,10)
count = 0
while True:
	count +=1 #count = count +1
	num = input('guess no.:')
	num = int(num)
	if num == r:
		print('well done')
		print('this is your', count , 'chance')
		break
	elif num > r:
		print('more than')
	elif num < r:
		print('less than')
	print('this is your', count , 'chance')