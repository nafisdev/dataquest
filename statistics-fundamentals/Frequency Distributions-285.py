## 1. Simplifying Data ##

import pandas as pd

pd.options.display.max_rows = 200
pd.options.display.max_columns = 50


df=pd.read_csv("wnba.csv")

print(df.shape)
# print(df)
print(df['Height'].value_counts())

## 2. Frequency Distribution Tables ##

wnba = pd.read_csv('wnba.csv')

freq_distro_pos=df['Pos'].value_counts()
freq_distro_height=df['Height'].value_counts()

## 4. Sorting Tables for Ordinal Variables ##

def make_pts_ordinal(row):
    if row['PTS'] <= 20:
        return 'very few points'
    if (20 < row['PTS'] <=  80):
        return 'few points'
    if (80 < row['PTS'] <=  150):
        return 'many, but below average'
    if (150 < row['PTS'] <= 300):
        return 'average number of points'
    if (300 < row['PTS'] <=  450):
        return 'more than average'
    else:
        return 'much more than average'
    
wnba['PTS_ordinal_scale'] = wnba.apply(make_pts_ordinal, axis = 1)

# Type your answer below

pts_ordinal_desc=wnba['PTS_ordinal_scale'].value_counts().iloc[[4,3,0,2,1,5]]

## 5. Proportions and Percentages ##

wnba = pd.read_csv('wnba.csv')

proportion=wnba['Age'].value_counts(normalize=True)
proportion_25=proportion[25]
percentage_30=proportion[30]*100
percentage_over_30=sum( [proportion[i] for i in range(30,37)])*100
percentage_below_23=sum( [proportion[i] for i in range(21,24)])*100

## 6. Percentiles and Percentile Ranks ##

from scipy.stats import percentileofscore


wnba = pd.read_csv('wnba.csv')

percentile_rank_half_less=(percentileofscore(a = wnba['Games Played'], score = 17, kind = 'weak'))
percentage_half_more=100-percentileofscore(a = wnba['Games Played'], score = 17, kind = 'weak')

## 7. Finding Percentiles with pandas ##

wnba = pd.read_csv('wnba.csv')


age_upper_quartile=wnba['Age'].describe()[6]

age_middle_quartile=wnba['Age'].describe()[5]

age_95th_percentile=wnba['Age'].describe(percentiles = [.95]).iloc[5]
question1=True
question2=False
question3=True

## 8. Grouped Frequency Distribution Tables ##

wnba = pd.read_csv('wnba.csv')

grouped_freq_table = wnba["PTS"].value_counts(bins = 10).sort_index(ascending=False)/143*100

## 10. Readability for Grouped Frequency Tables ##

wnba = pd.read_csv('wnba.csv')

intervals = pd.interval_range(start = 0, end = 600, freq = 60)
print(len(intervals))
gr_freq_table = pd.Series([0,0,0,0,0,0,0,0,0,0], index = intervals)
print(gr_freq_table)



for value in wnba['PTS']:
    for interval in intervals:
        if value in interval:
            gr_freq_table.loc[interval] += 1
            break
print(gr_freq_table)

gr_freq_table_10=gr_freq_table