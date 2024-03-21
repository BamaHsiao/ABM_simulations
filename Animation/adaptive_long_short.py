# https://matplotlib.org/stable/users/explain/animations/animations.html
# https://www.geeksforgeeks.org/how-to-create-animations-in-python/
from matplotlib import pyplot as plt
import matplotlib.animation as animation
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
	global scores
	round_num = len(player1_moves)
	x_limit, y_limit = round_num, round_num//2
	
	figure, ax = plt.subplots() # figsize=(16,8)
	plt.title(title_str, fontsize = 20)
	plt.axhline(y=0, color='r', linestyle='-')
	# Setting limits for x and y axis
	ax.set_xlim(0, x_limit)
	ax.set_ylim(-y_limit, y_limit)
	# Since plotting a single graph
	line,  = ax.plot(0, 0) 
	
	# how many ticks
	
	ticks, score_dif = [], []
	
	scores[0] = 0
	scores[1] = 0

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
		
		#print( "round ", i, "\t scores: ", scores, "\t", s1, s2 )
		
		for f in frame_list: Artist.remove(f)
		# actions 
		f1 = plt.text(round(0.1*x_limit), round(0.5*y_limit), action01, fontsize = 20, color='maroon')
		f2 = plt.text(round(0.8*x_limit), round(0.5*y_limit), action02, fontsize = 20, color='maroon')
		f3 = plt.text(round(0.5*x_limit), round(0.5*y_limit), "vs", fontsize = 20, color='darkorange')
		# winning/losing scores
		f4 = plt.text(round(0.2*x_limit), round(0.65*y_limit), s1, fontsize = 15, color='red')
		f5 = plt.text(round(0.9*x_limit), round(0.65*y_limit), s2, fontsize = 15, color='red')
		# cumulative scores
		f6 = plt.text(round(0.1*x_limit), round(0.8*y_limit), "P 1: "+str(scores[0]), fontsize = 15, color='purple')
		f7 = plt.text(round(0.8*x_limit), round(0.8*y_limit), "P 2: "+str(scores[1]), fontsize = 15, color='purple')
		# round number
		f8 = plt.text(round(0.4*x_limit), round(0.8*y_limit), "Round: " + str(i+1), fontsize = 15, color='blue')
		
		ticks.append(i)
		score_dif.append(scores[0] - scores[1])
		line.set_xdata(ticks)
		line.set_ydata(score_dif)
		
		if i+1==round_num: 
			win_msg = "player 1 win!" if scores[0]>scores[1] else "player 2 win!"
			f9 = plt.text(round(0.25*x_limit), round(0.3*y_limit), win_msg, fontsize = 30, color='red')
			frame_list = [f1, f2, f3, f4, f5, f6, f7, f8, f9]
		else:
			frame_list = [f1, f2, f3, f4, f5, f6, f7, f8]
		return line,
	
	# fargs = (frame_list, scores),
	ani = FuncAnimation(figure,
							  func = animation_function,
							  frames = np.arange(0, round_num, 1), 
							  interval = tick_time,
							  repeat = False)
	plt.grid() 
	plt.show()
	#with open("/Users/xiaoyao/Desktop/Programming/python_workspace/TurinTech/myvideo.html", "w") as f:
		#HTML(anim.to_html5_video())
	writervideo = animation.FFMpegWriter(fps=60)
	ani.save('/Users/xiaoyao/Desktop/Programming/python_workspace/TurinTech/random_vs_random.mp4', writer=writervideo)
	plt.close() 
	return

### startegy
import random
import pandas as pd

choices = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
counter_moves = {
    'Rock': ['Paper', 'Spock'], 
    'Paper': ['Scissors', 'Lizard'], 
    'Scissors': ['Rock', 'Spock'], 
    'Lizard': ['Rock', 'Scissors'], 
    'Spock': ['Paper', 'Lizard']
}
payoffs = {
    'Rock': 3, 'Paper': 2, 'Scissors': 1, 'Lizard': 4, 'Spock': 5
}
# Outcomes from the perspective of the first choice
outcomes = {
    ('Rock', 'Scissors'): 'win', ('Rock', 'Lizard'): 'win',
    ('Paper', 'Rock'): 'win', ('Paper', 'Spock'): 'win',
    ('Scissors', 'Paper'): 'win', ('Scissors', 'Lizard'): 'win',
    ('Lizard', 'Spock'): 'win', ('Lizard', 'Paper'): 'win',
    ('Spock', 'Scissors'): 'win', ('Spock', 'Rock'): 'win'
}
class Strategy:
    def next_move(self, history):
        raise NotImplementedError
class AdaptiveStrategy(Strategy):
    def __init__(self, player_1_2=1, memory_length=10):
        self.player = player_1_2
        self.memory_length = memory_length
    
    def next_move(self, history):
        # If it's the first move, or no history is available, choose randomly
        if not history:
            return random.choice(choices)
        
        # Count the frequency of the opponent's moves
        if self.player==1:
            opponent_moves = [it[1] for it in history]
        else:
            opponent_moves = [it[0] for it in history]
        if len(opponent_moves)>self.memory_length:
            opponent_moves = opponent_moves[-self.memory_length:]
        move_frequency = {move: opponent_moves.count(move) for move in choices}
        
        # Find the opponent's most frequent move
        most_frequent_move = max(move_frequency, key=move_frequency.get)
        
        # Based on the opponent's most frequent move, decide our move
        # The strategy here is to beat the most frequent move of the opponent
        return random.choice( counter_moves[most_frequent_move] )
# generate moves for each player
def simulate_round(strategy1, strategy2, history):
    move1 = strategy1.next_move(history)
    move2 = strategy2.next_move(history)
    # Determine outcome and update scores
    if (move1, move2) in outcomes: 
        return move1, move2, +payoffs[move1], -payoffs[move2]
    elif move1 == move2:
        return move1, move2, 0, 0
    else:
        return move1, move2, -payoffs[move1], +payoffs[move2] 

def run_simulation(strategy1, strategy2, num_rounds=100):
    history = []
    scores = [0, 0]  # [strategy1_score, strategy2_score]
    for _ in range(num_rounds):
        m1, m2, s1, s2 = simulate_round(strategy1, strategy2, history)
        scores[0] += s1
        scores[1] += s2
        history.append( (m1, m2, s1, s2) )
        # Update history and scores
    return history, scores 


total = [0, 0, 0]
player1_scores, player2_scores = [], []
for times in range(1):
       num_rounds = 1000
       lst = [ 
              ("AdaptiveStrategy", AdaptiveStrategy(2, 10))
              ]
       strategy1 = AdaptiveStrategy(1, num_rounds)
       (name, strategy2) = lst[0]
       #print( "RandomStrategy vs", name )
       history, scores = run_simulation(strategy1, strategy2, num_rounds)
       #print("scores: player 1 vs player 2, ", scores)
       if scores[0]>scores[1]: total[0] += 1
       elif scores[0]<scores[1]: total[1] += 1
       else: total[2] += 1
       player1_scores.append( scores[0] )
       player2_scores.append( scores[1] )
df = pd.DataFrame()
df[ 'score1' ] = player1_scores
df[ 'score2' ] = player2_scores
total, df['score1'].mean(), df['score2'].mean(), df['score1'].std(), df['score2'].std()


round_num = 1000
player1_moves = list(map(lambda x:x[0], history))
player2_moves = list(map(lambda x:x[1], history))
#for i in range(round_num): player1_moves.append( moves_dic[random.randint(1, 5)] )
#for i in range(round_num): player2_moves.append( moves_dic[random.randint(1, 5)] )
title_str = "Adaptive Long vs Short Memory"
generate_animation(player1_moves, player2_moves, title_str, tick_time)

