from random import randint

def dice_throw(u1, u2):
	''' Function helps in thrwoing dice for player '''
	ts, tv = 0, 0
	print("Hello.... {} and {}. Welcome to Number Guessing Game!!".format(u1, u2))
	while ts < 10 and tv < 10:
		if(input("Throw Dice for Player1: ")) == 'Y':
			s = randint(1,6)
			ts+=s
			if ts < 10:
				print("{} : You got a {}\nYour score is {}".format(u1, s, ts))
			elif ts == 10:
				print("***{} : You scored a {}***".format(u1, ts))
				break
			else:
				print("\t\t{} exceeds optimal Value".format(s))			
				ts-=s
		if(input("Throw Dice for Player2: ")) == 'Y':
			v = randint(1,6)
			tv+=v
			if tv < 10:
				print("{} : You got a {}\nYour score is {}\n".format(u2, v, tv))
			elif tv == 10:
				print("***{} : You scored a {}***".format(u2, tv))
				break
			else:
				print("\t\t{} exceeds optimal Value".format(v))
				tv-=v
	if ts == 10:
		return "S has won the Game!"
	elif tv == 10:
		return "V has won the Game!"


u1 = input("Enter Player1 Name : ")
u2 = input("Enter Player2 Name : ")
x = dice_throw(u1, u2)
print(x)






