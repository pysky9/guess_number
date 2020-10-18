import random
r = random.randint(1, 100)
i = 0
while True :
	i += 1
	num = eval(input("請猜一個數字: "))
	if num == r :
		print(f'你猜了{i}次')
		print("終於猜對了")
		break
	elif num > r :
		print("猜錯了，你的數字比答案大")
	elif num < r :
		print("猜錯了，你的數字比答案小")