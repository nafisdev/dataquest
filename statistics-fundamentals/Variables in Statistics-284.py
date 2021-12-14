## 2. Quantitative and Qualitative Variables ##

import pandas as pd
wnba = pd.read_csv('wnba.csv')

variables = {'Name': '', 'Team': '', 'Pos': '', 'Height': '', 'BMI': '',
             'Birth_Place': '', 'Birthdate': '', 'Age': '', 'College': '', 'Experience': '',
             'Games Played': '', 'MIN': '', 'FGM': '', 'FGA': '',
             '3PA': '', 'FTM': '', 'FTA': '', 'FT%': '', 'OREB': '', 'DREB': '',
             'REB': '', 'AST': '', 'PTS': ''}
variables['Name']='qualitative'
variables['Team']='qualitative'
variables['Pos']='qualitative'
variables['Height']='quantitative'
variables['BMI']='quantitative'
variables['Birth_Place']='qualitative'
variables['Birthdate']='quantitative'
variables['Age']='quantitative'
variables['College']='qualitative'
variables['Experience']='quantitative'
variables['Games Played']='quantitative'
variables['MIN']='quantitative'
variables['FGM']='quantitative'
variables['FGA']='quantitative'
variables['3PA']='quantitative'
variables['FTM']='quantitative'
variables['FTA']='quantitative'
variables['FT%']='quantitative'
variables['OREB']='quantitative'
variables['DREB']='quantitative'
variables['REB']='quantitative'
variables['AST']='quantitative'
variables['PTS']='quantitative'

## 4. The Nominal Scale ##

nominal_scale=['Team','College','Birth_Place','Pos','Name']
nominal_scale=sorted(nominal_scale)

## 5. The Ordinal Scale ##

question1=True
question2=False
question3=False
question4=True
question5=False
question6=False

## 7. The Difference Between Ratio and Interval Scales ##

interval=sorted(['Weight_deviation','Birthdate'])
ratio=sorted(['15:00','3P%','3PA',  'AST', 'Age', 'BLK', 'BMI', 'DD2', 'DREB', 'Experience', 'FG%', 'FGA', 'FGM', 'FT%', 'FTA', 'FTM','Games Played', 'Height', 'MIN', 'OREB','PTS','REB', 'STL', 'TD3',  'TO', 'Weight'])

## 9. Discrete and Continuous Variables ##

ratio_interval_only = {'Height':'continuous', 'Weight': 'continuous', 'BMI': 'continuous', 'Age': 'continuous', 'Games Played': 'discrete', 'MIN': 'continuous', 'FGM': 'discrete',
                       'FGA': 'discrete', 'FG%': 'continuous', '3PA': 'discrete', '3P%': 'continuous', 'FTM': 'discrete', 'FTA': 'discrete', 'FT%': 'continuous',
                       'OREB': 'discrete', 'DREB': 'discrete', 'REB': 'discrete', 'AST': 'discrete', 'STL': 'discrete', 'BLK': 'discrete', 'TO': 'discrete',
                       'PTS': 'discrete', 'DD2': 'discrete', 'TD3': 'discrete', 'Weight_deviation': 'continuous'}

## 10. Real Limits ##

bmi = {21.201: [21.2005,21.2015],
 21.329: [21.3285,21.3295],
 23.875: [23.8745,23.8755],
 24.543: [24.5425,24.5435],
 25.469: [25.4685,25.4695]}