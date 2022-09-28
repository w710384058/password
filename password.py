password = 'a123456'
times=3
while times>0:
	password_input = input('請輸入密碼: ')
	times = times - 1
	if password_input == password:
		print('登入成功')
		break
	else:
		if times>0:
			print('密碼錯誤!你還有',times,'次機會')
