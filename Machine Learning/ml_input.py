import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy import stats
import csv

# dict to hold column names from dataset
# and more descriptive names for the user
stat_desc = {'FG':'Field Goals Made', 'FGA':'Field Goals Attempted', '3P':'3 Pointers Made', 
			 '3PA':'3 Pointers Attempted', 'FT':'Free Throws Made', 'FTA':'Free Throws Attempted', 
			 'OR':'Offensive Rebounds', 'DR':'Defensive Rebounds', 'OEFF':'Offensive Effeciency',
			 'DEFF':'Defensive Efficiency', 'TOT':'Total Rebounds', 'A':'Assists', 'PF':'Number of Personal Fouls',
			 'ST':'Steals', 'TO TO':'Total Turnovers', 'POSS':'Possessions', 'PACE':'Pace', 'BL':'Blocks', 
			 'PTS':'Points', 'rest_days_adj':'Number of Rest Days', 'opp_fgpct':'Oppenents Field Goal Percentage',
			 'Opp_OR':"Opponent's Offensive Rebounds", 'Opp_DR':"Opponent's Defensive Rebounds",
			 'close':'Close Range Shots', 'long-range':'Long Range Shots', 'mid-range':'Mid Range Shots'}


df = pd.DataFrame()

def take_user_input(stat_desc):
	'''function that allows the user to input their own data,
	   outputs a csv of their inputs, plus a dataframe'''
	print("Input your own team's stats and test them with the predictive model.")
	print("Let's get started.")
	
	global df
	
	stat_dict = {}

	# for each key in the stat_desc dict, ask the user for the value
	for key in stat_desc:
		iter_dict = {}
		print(stat_desc[key])
		user_input = input()
		iter_dict[key] = float(user_input)
		stat_dict.update(iter_dict)

	# write the dict to csv for further use
	with open('user_input.csv', 'w') as f:
		w = csv.DictWriter(f, stat_dict.keys())
		w.writeheader()
		w.writerow(stat_dict)
	
	# return a dataframe for further data manipulation
	df = pd.DataFrame.from_csv('user_input.csv').reset_index()
	
	return df

def generate_stats(df):
	'''function accepts a dataframe as input,
	and generates further advanced NBA statistics for
	modeling'''
	
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

	cols = ['PTS', '3P', 'Opp_DR', 'DEFF', 'OEFF', 'FTA',
			'FT', 'Opp_OR', 'FGA', '3PA','FG', 'index']

	df.drop(cols,axis=1,inplace=True)
	df.to_csv('user_input_adj.csv')
	return df

take_user_input(stat_desc)
generate_stats(df)