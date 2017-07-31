import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy import stats
import csv

stat_desc = {'FG':'Field Goals Made', 'FGA':'Field Goals Attempted', '3P':'3 Pointers Made', 
			 '3PA':'3 Pointers Attempted', 'FT':'Free Throws Made', 'FTA':'Free Throws Attempted', 
			 'OR':'Offensive Rebounds', 'DR':'Defensive Rebounds',
			 'TOT':'Total Rebounds', 'A':'Assists', 'PF':'Number of Personal Fouls',
			 'ST':'Steals', 'TO TO':'Total Turnovers', 'BL':'Blocks', 'PTS':'Points', 
			 'opp_fgpct':'Oppenents Field Goal Percentage', 'Opp_OR':"Opponent's Offensive Rebounds", 
			 'Opp_DR':"Opponent's Defensive Rebounds", 'opp_FG':"Opponent's Made Field Goals", 
			 'opp_FGA':"Opponent's Attempted Field Goals", 'opp_FTA':"Opponent's Attempted Free Throws", 
			 'opp_TO TO':"Opponenet's Total Turnovers", "Opp_pts":"Opponent's Points"}

df2 = pd.DataFrame.from_csv('user_input.csv')
df2.reset_index(inplace=True)


def take_user_adjustment(stat_desc, df):
	'''function to allow the user to adjust various stats by a
	percentage of their choosing.'''

	print("Adjust team stats by a chosen percentage")	
	print("Let's get started.")
	
	# adjust user input to percentage, and update dataframe
	for key in stat_desc:
		df_column = key
		print(stat_desc[key])
		
		while True:
			try:
				user_input = float(input())
				break
			except ValueError:
				print("Please enter a number.")
		adjustment_val = ((float(user_input) / 100) + 1)
		df[df_column] = df[df_column] * adjustment_val

	return df

def generate_stats(df):
	'''function accepts a dataframe as input,
	and generates further advanced NBA statistics for
	modeling'''

	df.loc[:, 'POSS'] = (df['FGA'] + (0.44 * df['FTA']) + df['TO TO'] - df['OR'])
	df.loc[:, 'Opp_poss'] = (df['opp_FGA'] + (0.44 * df['opp_FTA']) + df['opp_TO TO'] - df['Opp_OR'])
	
	df.loc[:, 'OEFF'] = (100 * (df['PTS'] / df['POSS']))

	df.loc[:, 'DEFF'] = (100 * (df['Opp_pts'] / df['Opp_poss']))

	df['points_per_poss'] = ((df['PTS'] / (df['FGA'] + 
                        (0.44 * df['FTA']))) * 
                        ((df['FGA'] + 
                        (0.44 * df['FTA'])) / df['POSS']))

	df['true_shooting_%'] = ((0.5 * df['PTS']) / (df['FGA'] + 0.44 * df['FTA']))

	df['Off_reb_minus_TO'] = (df['OR'] - df['TO TO'])

	df.loc[:, 'TO_rate'] = df['TO TO'] / df['POSS']

	df.loc[:, 'off_reb_pct'] = df['OR'] / (df['Opp_OR'] + df['Opp_DR'])

	df.loc[:, 'free_throw_pct_of_FGA'] = df['FTA'] / df['FGA']

	df.loc[:, 'free_throw_pct'] = df['FT'] / df['FTA']

	df.loc[:, 'FG_pct'] = df['FG'] / df['FGA']

	df['made_FG_poss'] = df['FG'] / df['POSS']

	df['attempted_FG_poss'] = df['FGA'] / df['POSS']

	df['total_rebounds_poss'] = df['TOT'] / df['POSS'] 

	df['3P_pct'] = df['3P'] / df['3PA']

	df['3_point_pct_of_fga'] = df['3PA'] / df['FGA']
	df['close_pct_of_fga'] = df['close'] / df['FGA']
	df['long_range_pct_of_fga'] = df['long-range'] / df['FGA']
	df['mid_range_pct_of_fga'] = df['mid-range'] / df['FGA']
	df.reset_index(inplace=True)

	cols = ['PTS', '3P', 'Opp_DR', 'FTA', 'FT', 'Opp_OR', 'FGA', '3PA','FG', 'index','Opp_pts',
			'opp_FTA', 'opp_TO TO', 'opp_FTA', 'opp_FG', 'opp_FGA', 'Opp_poss']

	df.drop(cols,axis=1,inplace=True)
	df.to_csv('user_input_adj.csv')
	return df

take_user_adjustment(stat_desc, df2)
df2 = generate_stats(df2)