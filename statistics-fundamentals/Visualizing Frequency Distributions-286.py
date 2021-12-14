## 2. Bar Plots ##

wnba['Exp_ordinal'].value_counts().iloc[[3,0,2,1,4]].plot.bar()
plt.show()
print(wnba['Exp_ordinal'].unique())

## 3. Horizontal Bar Plots ##

wnba['Exp_ordinal'].value_counts().iloc[[3,0,2,1,4]].plot.barh(title = 'Number of players in WNBA by level of experience')

## 4. Pie Charts ##

wnba['Exp_ordinal'].value_counts().plot.pie()

## 5. Customizing a Pie Chart ##

import matplotlib.pyplot as plt
# wnba['Pos'].value_counts().plot.pie(figsize = (6,6))
# plt.ylabel('')


# wnba['Pos'].value_counts().plot.pie(figsize = (6,6), autopct = '%.1f%%')

wnba['Exp_ordinal'].value_counts().plot.pie(title="Percentage of players in WNBA by level of experience",figsize = (6,6), autopct = '%.2f%%')
plt.ylabel('')

## 6. Histograms ##

wnba['PTS'].plot.hist()

## 7. The Statistics Behind Histograms ##

from numpy import arange
wnba['Games Played'].describe()
wnba['Games Played'].plot.hist()

## 9. Binning for Histograms ##

wnba['Games Played'].plot.hist(range = (1,32), bins = 8, title= "The distribution of players by games played")
plt.xlabel( "Games played")

## 10. Skewed Distributions ##

wnba['AST'].plot.hist()
wnba['FT%'].plot.hist()

assists_distro='right skewed'
ft_percent_distro='left skewed'

## 11. Symmetrical Distributions ##

wnba['Age'].plot.hist()
# wnba['Height'].plot.hist()
# wnba['MIN'].plot.hist()

normal_distribution='Height'