def no_of_different_suits(cards):
  a_set = set()
  for i in cards:
    if i  in range(0,12):
      a_set.add(1)
    elif i  in range(13, 25):
      a_set.add(2)
    elif i in range(26, 38):
      a_set.add(3)
    elif i  in range(39, 51):
      a_set.add(4)
  return len(a_set)


def check_in_sequence_or_not(cards):
  a = list()
  for x in cards:
  	a.append(x%13)
  a.sort()
  return True if(a[1]-a[0] == 1 and a[2]-a[1] == 1) else False

def check_if_three_of_a_kind(cards):
  return True if(len(set(x%13 for x in cards )) == 1) else False

def check_if_same_suit_or_not(cards):
  """
  Returns True in case all cards lie in same suit.
  """
  a_set = set()
  for i in cards:
    if i in range(0,12):
      a_set.add(1)
    elif i not in range(13, 25):
      a_set.add(2)
    elif i not in range(26, 38):
      a_set.add(3)
    elif i not in range(39, 51):
      a_set.add(4)
  return True if(len(a_set) == 1) else False


def return_ranking(cards):
  """
  Returns ranking of set of cards, the lower the better.
  Using Referance given on : https://en.wikipedia.org/wiki/Teen_patti#Ranking_of_hands

  Order from highest to lowest, Ranking writtern in brackets:

  - Three of a kind (1)
  - Three consecutive cards of the same suit. (2)
  - Three consecutive cards not all in the same suit (3)
  - All the 3 cards are of same suit (4)
  - Two cards of the same rank. (5)
  - No pair (6)

  """
  # Three of the same cards.
  if check_if_three_of_a_kind(cards):
    return 1
  # Three consecutive cards of the same suit.
  elif check_if_same_suit_or_not(cards) and check_in_sequence_or_not(cards):
    return 2
  # Three consecutive cards not all in the same suit.
  elif (check_in_sequence_or_not(cards) == True and no_of_different_suits(cards) == 3):
    return 3
  # All the 3 cards are of same suit.
  elif no_of_different_suits(cards) == 1:
    return 4
  # Two cards of the same rank.
  elif len(set(x%13 for x in cards )) == 2:
    return 5
  else:
  # No pair (high card)
    return 6

#---------------Above all functions decide ranking


# sends the position of player
def who_wins(ranking, player_one, player_two):
	if(ranking == 1):
		return player_one if (a[player_one][0]%13 < a[player_two][0]%13) else player_two

	if(ranking == 2):
		# print(a[player_one])
		a1 = sorted(a[player_one])

		a1 = a1[0]%13
		a2 = sorted(a[player_two])
		a2 = a2[0]%13
		return player_one if (a1 <= a2) else player_two

	if(ranking == 3):
		a1 = list()
		a2 = list()
		for x in a[player_one]:
			a1.append(x%13)
		for x in a[player_two]:
			a2.append(x%13)
		a1.sort()
		a1 = a1[0]
		a2.sort()
		a2 = a2[0]
		return player_one if (a1 <= a2) else player_two

	if(ranking == 4):
		"""
		 If two players both have flushes, the player with the high card wins; if they match, then the next highest card is compared, then the third card if needed. If two players have the same card values, then the hands are ranked by suit, with spades first and clubs last.
		 """
		a1 =list()
		a2 = list()
		for x in a[player_one]:
			a1.append(x%13)
		for x in a[player_two]:
			a2.append(x%13)
		a1.sort()
		a2.sort()

		# if(a1 == a2):
			#todo

		for i in range(0,3):
			if(a1[i] < a2[i]):
				return player_one
			elif(a1[i] > a2[i]):
				return player_two

		# print(a[player_one][0], a[player_two][0])
		if (a[player_one][0] <=25 and a[player_one][0] >=13):
			return player_one
		elif (a[player_two][0] <=25 and a[player_two][0] >=13):
			return player_two
		elif (a[player_one][0] <=12 and a[player_one][0] >=0):
			return player_one
		elif (a[player_two][0] <=12 and a[player_two][0] >=0):
			return player_two
		elif (a[player_one][0] <=38 and a[player_one][0] >=26):
			return player_one
		elif (a[player_two][0] <=38 and a[player_two][0] >=26):
			return player_two
		elif (a[player_one][0] <=51 and a[player_one][0] >=39):
			return player_one
		elif (a[player_two][0] <=51 and a[player_two][0] >=39):
			return player_two


	if(ranking == 5):
		"""
		Two cards of the same rank. Between two pairs, the one with the higher value is the winner. If the pairs are of equal value, the value of the third card decides the winner. Therefore the lowest pair is 2-2-3 and the highest is A-A-K.
		"""
		a1 = list()
		a2 = list()
		for x in a[player_one]:
		 	a1.append(x%13)
		for x in a[player_two]:
		 	a2.append(x%13)

		a1.sort()
		a2.sort()
		# todo case when all three of both player are same but diff suit
		if(a1[1] == a2[1]):
			diff1 = a1[0] if a1[0] != a1[1] else a1[2]
			diff2 = a2[0] if a2[0] != a2[1] else a2[2]

			return player_one if(diff1 < diff2) else player_two
		else:
			return player_one if(a1[1] < a2[1]) else player_two

	if(ranking == 6):
		"""
		If two players share a common high card, then rest of the cards are compared based upon their values.
		"""
		a1 = list()
		a2 = list()
		for x in a[player_one]:
		 	a1.append(x%13)

		for x in a[player_two]:
		 	a2.append(x%13)

		a1.sort()
		a2.sort()

		for i in range(0,3):
			if(a1[i] < a2[i]):
				return player_one
			elif(a1[i] > a2[i]):
				return player_two
		return player_one
		#Todo when all cards are same but from different suit

a =  list(list())
def run_in(argument):

	args = list()
	sett = set()

	for x in argument:
		args.append(int(x))
		sett.add(int(x))


	if(min(args)< 0 or max(args) > 52):
		# "Error! Value exceeds allowed range 0-51"
		return -1
	elif(len(sett) != len(args)):
		# "Duplicate value detected!"
		return -2

	final_args = list()
	cleann = list()
	for idx, x in enumerate(args):
		cleann.append(x)
		if((idx+1)%3 == 0):
			final_args.append(cleann)
			cleann = []

	global a
	a = final_args

	# print(a)

	ranking_list = list()
	for index,x in enumerate(a):
		value = return_ranking(x)
		ranking_list.append((value, index))

	# print(ranking_list)
	ranking_list = sorted(ranking_list,key=lambda x: x[0])
	# print "---"
	# print(ranking_list)
	best_ranking = ranking_list[0][0]
	# print(best_ranking)
	# print "---"
	# print(who_wins(best_ranking,4,3))
	comp = list()

	for  val in ranking_list:
		if(val[0] == best_ranking):
			comp.append(val[1])


	if(len(comp) == 1):
		curr_winner = comp[0]
	else:
		curr_winner = comp[0]
		for i in comp:
			# print(i, curr_winner,best_ranking)
			curr_winner = who_wins(best_ranking, i, curr_winner)

	return curr_winner+1

if __name__ == "__main__":
	# a = list({0,14,28})
	# in_sequence_or_not(a)
	print ("asas")