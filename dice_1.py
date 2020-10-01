from random import randint

def turn(score, user):
	''' Function helps in thrwoing dice for player '''
	s = randint(1, 6)
	if score + s > 10:
		agg = score
		print("\n{}: Your turn exceeds Final Value..!! So, your score is only {}\n".format(user, agg))
	else:
		agg = snk_ldr(user, score, s)
		print("\n{} : Your turn score is {}. Total score is {}\n".format(user, s, agg))
	return agg

def snk_ldr(player, move, sub_t):
	''' Function helps in predicting up-moves or down-moves ''' 
	snake, ladder = {5:2, 7:3, 9:1}, {1:3, 2:4}
	if move+sub_t in snake:
		print("\t\t\t\t Alas! {} you are caught by a snake at {}... and lost {} of your score".format(player,move+sub_t, snake[move+sub_t]))
		return move+sub_t - snake[move+sub_t]
	elif move+sub_t in ladder:
		print("\t\t\t\t Hurray! {} you got a ladder at {}... and moved-up {} of your score".format(player,move+sub_t, ladder[move+sub_t]))
		return move+sub_t + ladder[move+sub_t]
	else:
		return move+sub_t

def dice_throw(p1, p2):
	''' Function helps in validating winner '''
	total1, total2 = 0, 0
	print("\t\t\t\t*** Hello.... {} and {}. Welcome to Snake & Ladder scenario ***\n".format(p1, p2))
	while total1 != 10 and total2 != 10:
		if(input("{} it's your turn..".format(p1))) == 'Y':
			total1 = turn(total1, p1)
			if total1 == 10:
			    break
		else:
			print("\nYou made an uneven throw!!\n")
		
		if(input("{} it's your turn..".format(p2))) == 'Y':
			total2 = turn(total2, p2)
			print("="*120+"\n")
			if total2 == 10:
			    break
		else:
			print("\nYou made an uneven throw!!\n")
		
	if total1 == 10:
		return "\t\t\t"+"***** {} you have won the game... Celebrate *****".format(p1)
	elif total2 == 10:
		return "\t\t\t"+"******* {} you have won the game... Celebrate *******".format(p2)


u1 = input("\nEnter Player1 Name : ")
u2 = input("Enter Player2 Name : ")
x = dice_throw(u1, u2)
print(x)


