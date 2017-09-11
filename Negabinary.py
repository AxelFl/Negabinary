while 1:
	number = input("Type a negabinary number here: ")
	try:
		number = int(number)
		break
	except ValueError:
		pass

total = 0
loop = 0

for char in str(number)[::-1]:
	if char == "1":
		total += (-2) ** loop
	elif char == "0":
		pass
	else:
		print("You enterned an invalid number")
		quit()
	loop += 1

print(total)



