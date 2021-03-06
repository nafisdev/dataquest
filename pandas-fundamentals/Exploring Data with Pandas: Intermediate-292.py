## 1. Introduction ##

import pandas as pd
# read the data set into a pandas dataframe
f500 = pd.read_csv("f500.csv", index_col=0)
f500.index.name = None

# replace 0 values in the "previous_rank" column with NaN
f500.loc[f500["previous_rank"] == 0, "previous_rank"] = np.nan


f500_selection=f500[["rank","revenues","revenue_change"]].head(5)

## 2. Reading CSV files with pandas ##

import pandas as pd
# read the data set into a pandas dataframe
f500 = pd.read_csv("f500.csv")

f500.loc[f500["previous_rank"] == 0, "previous_rank"] = np.nan

## 3. Using iloc to select by integer position ##

fifth_row=f500.iloc[4]
company_value=f500["company"].iloc[0]

## 4. Using iloc to select by integer position continued ##

first_three_rows=f500.iloc[:3]
first_seventh_row_slice=f500.iloc[[0,6],:5]

## 5. Using pandas methods to create boolean masks ##

li=f500.loc[:,"previous_rank"].isnull()
null_previous_rank=f500.loc[li,["company","rank","previous_rank"]]

## 6. Working with Integer Labels ##

null_previous_rank = f500[f500["previous_rank"].isnull()]

top5_null_prev_rank=null_previous_rank.iloc[:5]

## 7. Pandas Index Alignment ##

previously_ranked=f500.loc[f500["previous_rank"].notnull()]


rank_change=previously_ranked.loc[:,"previous_rank"]-previously_ranked.loc[:,"rank"]
f500["rank_change"]=rank_change

## 8. Using Boolean Operators ##

large_revenue=f500["revenues"]>100000

negative_profits=f500["profits"]<0


combined=large_revenue & negative_profits

big_rev_neg_profit=f500.loc[combined]

## 9. Using Boolean Operators Continued ##

b=f500.loc[:,"country"]=="Brazil"
u=f500.loc[:,"country"]=="Venezuela"
brazil_venezuela=f500.loc[b|u]


t=f500["sector"]=="Technology"
c=f500["country"]!="USA"
tech_outside_usa=f500.loc[ t& c ].head(5)

## 10. Sorting Values ##

selected_rows = f500[f500["country"] == "Japan"]



sorted_rows = selected_rows.sort_values("employees", ascending=False)
top_japanese_employer=sorted_rows.iloc[0].loc["company"]

## 11. Using Loops with pandas ##

top_employer_by_country={}

cou=f500["country"].unique()

for c in cou:
    selected_rows = f500[f500["country"] == c]
    sorted_rows = selected_rows.sort_values("employees", ascending=False)
    top_japanese_employer=sorted_rows.iloc[0].loc["company"]
    top_employer_by_country[c]=top_japanese_employer

## 12. Challenge: Calculating Return on Assets by Country ##

top_roa_by_sector={}

cou=f500["sector"].unique()
f500["roa"]=f500["profits"]/f500["assets"]
for c in cou:
    selected_rows = f500[f500["sector"] == c].sort_values("roa", ascending=False)
    top_roa_by_sector[c]=selected_rows.iloc[0].loc["company"]
    