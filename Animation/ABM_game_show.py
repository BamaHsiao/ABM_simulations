# https://matplotlib.org/stable/users/explain/animations/animations.html
# https://www.geeksforgeeks.org/how-to-create-animations-in-python/
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.artist import Artist
import numpy as np
import random

moves_dic = {1:'Rock', 2:'Paper', 3:'Scissors', 4:'Lizard', 5:'Spock'}
gestures = {
    "Rock": {"wins": ["Scissors", "Lizard"], "winning_points": 1, "losing_points": -1},
    "Paper": {"wins": ["Rock", "Spock"], "winning_points": 2, "losing_points": -2},
    "Scissors": {"wins": ["Paper", "Lizard"], "winning_points": 3, "losing_points": -3},
    "Lizard": {"wins": ["Spock", "Paper"], "winning_points": 4, "losing_points": -4},
    "Spock": {"wins": ["Scissors", "Rock"], "winning_points": 5, "losing_points": -5}
}

tick_time = 50
frame_list = []
scores = [0, 0]
palette = ['blue', 'red', 'green', 'darkorange', 'maroon', 'black']

def generate_animation(player1_moves, player2_moves, title_str, tick_time):

	round_num = len(player1_moves)
	
	figure, ax = plt.subplots() # figsize=(16,8)
	plt.title(title_str, fontsize = 20)
	plt.axhline(y=0, color='r', linestyle='-')
	# Setting limits for x and y axis
	ax.set_xlim(0, round_num)
	ax.set_ylim(-round_num, round_num)
	# Since plotting a single graph
	line,  = ax.plot(0, 0) 
	
	# how many ticks
	
	ticks, score_dif = [], []

	def animation_function(i):
		global frame_list, score1, score2
		
		action01 = player1_moves[i]
		action02 = player2_moves[i]
		s1, s2 = 0, 0
		if action02 in gestures[action01]['wins']:
			s1 = gestures[action01]['winning_points']
			s2 = gestures[action02]['losing_points']
		elif action01 in gestures[action02]['wins']:
			s1 = gestures[action01]['losing_points']
			s2 = gestures[action02]['winning_points']
		scores[0] += s1
		scores[1] += s2 
		s1 = "+" + str(s1) if s1>0 else str(s1)
		s2 = "+" + str(s2) if s2>0 else str(s2)
		
		
		for f in frame_list: Artist.remove(f)
		# actions 
		f1 = plt.text(round(0.1*round_num), round(0.5*round_num), action01, fontsize = 20, color='maroon')
		f2 = plt.text(round(0.8*round_num), round(0.5*round_num), action02, fontsize = 20, color='maroon')
		f3 = plt.text(round(0.5*round_num), round(0.5*round_num), "vs", fontsize = 20, color='darkorange')
		# winning/losing scores
		f4 = plt.text(round(0.2*round_num), round(0.65*round_num), s1, fontsize = 15, color='red')
		f5 = plt.text(round(0.9*round_num), round(0.65*round_num), s2, fontsize = 15, color='red')
		# cumulative scores
		f6 = plt.text(round(0.1*round_num), round(0.8*round_num), "P 1: "+str(scores[0]), fontsize = 15, color='purple')
		f7 = plt.text(round(0.8*round_num), round(0.8*round_num), "P 2: "+str(scores[1]), fontsize = 15, color='purple')
		# round number
		f8 = plt.text(round(0.4*round_num), round(0.8*round_num), "Round: " + str(i+1), fontsize = 15, color='blue')
		
		ticks.append(i)
		score_dif.append(scores[0] - scores[1])
		line.set_xdata(ticks)
		line.set_ydata(score_dif)
		
		if i+1==round_num: 
			win_msg = "player 1 win!" if scores[0]>scores[1] else "player 2 win!"
			f9 = plt.text(round(0.25*round_num), round(0.3*round_num), win_msg, fontsize = 30, color='red')
			frame_list = [f1, f2, f3, f4, f5, f6, f7, f8, f9]
		else:
			frame_list = [f1, f2, f3, f4, f5, f6, f7, f8]
		return line,
	
	# fargs = (frame_list, scores),
	animation = FuncAnimation(figure,
							  func = animation_function,
							  frames = np.arange(0, round_num, 1), 
							  interval = tick_time,
							  repeat = False)
	plt.show()
	return



round_num = 200
player1_moves = []
player2_moves = []
for i in range(round_num): player1_moves.append( moves_dic[random.randint(1, 5)] )
for i in range(round_num): player2_moves.append( moves_dic[random.randint(1, 5)] )
title_str = "Random vs Random"
generate_animation(player1_moves, player2_moves, title_str, tick_time)