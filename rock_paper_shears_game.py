#!/usr/bin/env python3
import random



def game():
	player_input = str(input('Please select choice (rock, paper or shears) or write QUIT for exit the game:')).lower()
	av_choices = ['rock', 'paper', 'shears']
	player_point = 0
	comp_point = 0

	def game_info_output(game: str, player_inp: str, comp_inp: str, player_p: int, comp_p: int):
		return '{}! \n\
			Your choice is {}\n\
			Comp choice is {}.\n\
			Player point = {} \n\
			Comp point ={}'.\
			format(game, player_inp, comp_inp, player_p, comp_p)

	while (player_input != 'QUIT'):

		if player_point == 3:
			print("You are WIN !")
			break
		elif comp_point == 3:
			print('Game over! You are Loss !')
			break

		comp_choice = random.choice(av_choices)

		if player_input == comp_choice:
			print(game_info_output('Draw', player_input, comp_choice, player_point, comp_point))
		elif player_input == 'rock':
			if comp_choice == 'paper':
				comp_point += 1
				print(game_info_output('Los', player_input, comp_choice, player_point, comp_point))
			elif comp_choice == 'shears':
				player_point += 1
				print(game_info_output('Win', player_input, comp_choice, player_point, comp_point))
		elif player_input == 'paper':
			if comp_choice == 'shears':
				comp_point += 1
				print(game_info_output('Los', player_input, comp_choice, player_point, comp_point))
			elif comp_choice == 'rock':
				player_point += 1
				print(game_info_output('Win', player_input, comp_choice, player_point, comp_point))
		elif player_input == 'shears':
			if comp_choice == 'rock':
				comp_point += 1
				print(game_info_output('Los', player_input, comp_choice, player_point, comp_point))
			elif comp_choice == 'paper':
				player_point += 1
				print(game_info_output('Win', player_input, comp_choice, player_point, comp_point))

		if player_point == 3 or comp_point == 3:
			pass
		else:
			player_input = str(input('Please select choice (rock, paper or shears) or write QUIT for exit the game:')).lower()

if __name__ == '__main__':
	game()