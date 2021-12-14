## 2. What's a Good Metric? ##

ans1="no"

ans21="no"
ans22="yes"

## 3. Introduction to the Net Promoter Score ##

def categorize(elem):
    if elem<=6:
        return "Detractor"
    elif elem<9:
        return "Passive"
    else:
        return "Promoter"

## 4. Net Promoter Score ##

import pandas as pd
import numpy as np

df = pd.read_csv("nps.csv", parse_dates=["event_date"])

df["yearmonth"]=df["event_date"].dt.strftime('%Y%m').astype('int')
df['category']=df['score'].apply(categorize)

nps=df.pivot_table(index=['yearmonth'],columns='category', aggfunc=np.size, values='score')

nps["total_responses"]=nps.sum(axis=1)

nps['nps']=(nps['Promoter']-nps["Detractor"])/nps["total_responses"]
nps['nps']=(nps['nps']*100).astype('int')

print(df.info())

## 6. Customer Churn ##

import pandas as pd

subs = pd.read_csv('muscle_labs.csv',parse_dates=['end_date','start_date'])
subs["churn_month"]=subs["end_date"].astype('datetime64[ns]').dt.strftime('%Y%m').astype('int')



monthly_churn=subs.loc[:,['id','churn_month']].groupby(['churn_month']).count()
monthly_churn['total_churned']=monthly_churn['id']
monthly_churn=monthly_churn.loc[:,['total_churned']]
print(monthly_churn)

## 7. Date Wrangling ##

years = list(range(2011,2015))
months = list(range(1,13))
yearmonths = [y*100+m for y in years for m in months]
yearmonths = yearmonths[:-1]

churn = pd.DataFrame({"yearmonth": yearmonths})

churn=churn.merge(monthly_churn, left_on='yearmonth',right_index=True, how='left')

churn.fillna(0,inplace=True)
churn['total_churned']=churn["total_churned"].astype('int')

## 8. Churn Rate ##

from datetime import datetime
from datetime import timedelta


def nrows(ind):
    time_change = timedelta(days=1)
    # print(datetime.strptime(str(ind),'%Y%m').replace(day=1)-time_change)
    # print(ind)
    # print(datetime.strptime(str(ind),'%Y%m').replace(day=1))
    # sub1=subs[subs["start_date"]<datetime.strptime(str(ind),'%Y%m').replace(day=1)]
    # sub1=sub1[sub1["end_date"]>(datetime.strptime(str(ind),'%Y%m').replace(day=1)-time_change)]
    
    sub1=subs[subs["start_date"]<datetime.strptime(str(ind),'%Y%m')]
    sub1=sub1[sub1["end_date"]>=datetime.strptime(str(ind),'%Y%m')]
    
    return(sub1.shape[0])



churn['total_customers']=churn['yearmonth'].apply(nrows)

churn['churn_rate']=churn['total_churned']/churn['total_customers']


churn['yearmonth'] = [str(x) for x in churn.loc[:, 'yearmonth']]
print(churn.info())
arange = __import__("numpy").arange
Ellipse = __import__("matplotlib").patches.Ellipse
ax = churn.plot(x="yearmonth", y="churn_rate", figsize=(12,6), rot=45, marker=".")
start, end = ax.get_xlim()
ax.get_xticks()
ax.set_xticks(arange(2, end, 3))
ax.set_xticklabels(yearmonths[2::3])
circle = Ellipse((35, churn.loc[churn.yearmonth == "201312", "churn_rate"].iloc[0]),
                 5, 0.065, color='sandybrown', fill=False
                   )
ax.add_artist(circle)
ax.xaxis.label.set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.get_legend().remove()