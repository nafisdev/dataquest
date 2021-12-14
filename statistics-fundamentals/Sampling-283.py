## 3. Populations and Samples ##

question1 = 'population'
question2 = 'population'
question3 = 'sample'
question4 = 'population'
question5 = 'sample'

## 4. Sampling Error ##

import pandas as pd
wnba = pd.read_csv('wnba.csv')

# print(wnba.head())

# print(wnba.tail())

parameter=(wnba['Games Played'].max())

statistic=(wnba.sample(random_state=1)['Games Played'].max())
sampling_error=parameter-statistic

## 5. Simple Random Sampling ##

import pandas as pd
import matplotlib.pyplot as plt

wnba = pd.read_csv('wnba.csv')

li=[]
for i in range(0,100):
    li.append(wnba['PTS'].sample(n=10,random_state=i).mean())
    
plt.scatter(x=range(1,101),y=li)
plt.axhline(y = wnba['PTS'].mean())
plt.show()

## 7. Stratified Sampling ##

wnba["npg"]=wnba["PTS"]/wnba["Games Played"]

li=[]
li.append(wnba[wnba['Pos']=='F'])
li.append(wnba[wnba['Pos']=='G'])
li.append(wnba[wnba['Pos']=='C'])
li.append(wnba[wnba['Pos']=='G/F'])
li.append(wnba[wnba['Pos']=='F/C'])
d={}
for i in li:
    # print()
    d[i.iloc[0,:]['Pos']]=i['npg'].sample(10,random_state=0).mean()
    
position_most_points=max(d, key=d.get)
    

## 8. Proportional Stratified Sampling ##

li=[]

li.append(wnba[wnba["Games Played"]<=12])

li.append(wnba[(wnba["Games Played"]>12) & (wnba["Games Played"]<=22)])

li.append(wnba[wnba["Games Played"]>22])
d=[]
for j in range(0,100):
    d.append(pd.concat([li[0]['PTS'].sample(1,random_state=j),li[1]['PTS'].sample(2,random_state=j),
    li[2]['PTS'].sample(7,random_state=j)], ignore_index=True).mean())
    
# position_most_points=max(d, key=d.get)
plt.scatter(x=range(1,101), y=d)
plt.axhline(wnba['PTS'].mean())
plt.show()

## 10. Cluster Sampling ##

# print(pd.Series(wnba['Team'].unique()).sample(4, random_state = 0))
li=[]
li.append(pd.DataFrame(wnba[wnba['Team']=='PHO']))
li.append(pd.DataFrame(wnba[wnba['Team']=='IND']))
li.append(pd.DataFrame(wnba[wnba['Team']=='MIN']))
li.append(pd.DataFrame(wnba[wnba['Team']=='ATL']))

df=pd.concat(li)

sampling_error_height=wnba['Height'].mean()-df['Height'].mean()

sampling_error_BMI=wnba['BMI'].mean()-df['BMI'].mean()

sampling_error_age=wnba['Age'].mean()-df["Age"].mean()

sampling_error_points=wnba['PTS'].mean()-df['PTS'].mean()