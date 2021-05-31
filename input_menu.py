ConstString = """
[1]Add a Student
[2]Delete a Student
[3]Look Up Student Record
[4]Exit/Quit
"""


def menu():
	ans = True
	while ans:
		print(ConstString)
		ans = input("What would you like to do? ")
		if ans == "1":
			print("\nStudent Added")
		elif ans == "2":
			print("\n Student Deleted")
		elif ans == "3":
			print("\n Student Record Found")
		elif ans == "4":
			print("\n Goodbye")
			ans = None
		else:
			print("\n Not Valid Choice Try again")


def login():

	# 初始用户名密码
	account_info = {'uname': 'abc', 'pwd': '123'}
	# 可以试3次
	time = 3

	print("-- 登录 --")
	while True:
		# 获取用户登录输入的用户名和密码
		uname = input("请输入用户名:")
		pwd = input("请输入密码:")

		# 判断用户名等于初始用户名 并且密码等于初始密码
		if uname==account_info['uname'] and pwd==account_info['pwd']:
			print("登录成功!")
			# 如果登录成功使用break语句退出while循环
			break
		else:
			# 如果错误，让可以试的次数减去1
			time=time-1
			print("用户名或者密码错误")
			print("您还有{}次机会".format(time))

			if time < 1:
				# 如果三次机会用完提示登录失败，退出while循环
				print("登录失败!")
				break


if __name__ == '__main__':
	menu()
