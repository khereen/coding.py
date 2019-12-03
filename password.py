i = 3
password = 'abc123'
while True:
	pwd = input('pls enter pass:')
	if pwd == password:
		print ('done')
		break
	else:
		i = i - 1
		print('wrong pass, you still have', i, 'chance')
		if i == 0:
			break