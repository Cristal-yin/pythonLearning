'''
一段小程序

'''
# constant 常量
username = 'cristal'
password = '123456'

print('please input your username:')
username_user = input()
print('please input your password:')
password_user = input()


if username == username_user and password == password_user:
    print('success')

else: 
    print("fail")