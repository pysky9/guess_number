import random
r = random.randint(1, 100)
while True :
	num = eval(input("請猜一個數字: "))
	if num == r :
		print("終於猜對了")
		break
	elif num > r :
		print("猜錯了，你的數字比答案大")
	elif num < r :
		print("猜錯了，你的數字比答案小")