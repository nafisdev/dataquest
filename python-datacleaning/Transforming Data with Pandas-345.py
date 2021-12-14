## 1. Introduction ##

mapping = {'Economy (GDP per Capita)': 'Economy', 'Health (Life Expectancy)': 'Health', 'Trust (Government Corruption)': 'Trust' }

happiness2015=happiness2015.rename(mapping, axis=1)

## 2. Apply a Function Element-wise Using the Map and Apply Methods ##

def label(element):
    if element > 1:
        return 'High'
    else:
        return 'Low'
    
    
economy_impact_map=happiness2015['Economy'].map(label)
economy_impact_apply=happiness2015['Economy'].apply(label)

equal=economy_impact_map.equals(economy_impact_apply)

## 3. Apply a Function Element-wise Using the Map and Apply Methods Continued ##

def label(element , x):
    if element > x:
        return 'High'
    else:
        return 'Low'
economy_impact_apply = happiness2015['Economy'].apply(label,x=0.8)

## 4. Apply a Function Element-wise to Multiple Columns Using Applymap Method ##

def label(element):
    if element > 1:
        return 'High'
    else:
        return 'Low'
economy_apply = happiness2015['Economy'].apply(label)
factors = ['Economy', 'Family', 'Health', 'Freedom', 'Trust', 'Generosity']

factors_impact=happiness2015[factors].applymap(label)

## 5. Apply Functions along an Axis using the Apply Method ##

def v_counts(col):
    num=col.value_counts()
    den=col.size
    return num/den
    # if pd.isna(num['Low']):
    #     num['Low']=0
    # if pd.isna(num['High']):
    #     num['High']=0
    # s=num['Low']+num['High']
    # if (s!=0):
    #     num['Low']=(num['Low']/s)*100
    #     num['High']=(num['High']/s)*100
    # return num
v_counts_pct1 = factors_impact.apply(pd.value_counts)
v_counts_pct = factors_impact.apply(v_counts)

a=factors_impact["Economy"].value_counts()
a[0]=98
print(a)

## 6. Apply Functions along an Axis using the Apply Method Continued ##

factors = ['Economy', 'Family', 'Health', 'Freedom', 'Trust', 'Generosity', 'Dystopia Residual']


def percentages(col):
    div=col/happiness2015['Happiness Score']
    div*=100
    return div


factor_percentages=happiness2015[factors].apply(percentages)

## 7. Reshaping Data with the Melt Function ##

main_cols = ['Country', 'Region', 'Happiness Rank', 'Happiness Score']
factors = ['Economy', 'Family', 'Health', 'Freedom', 'Trust', 'Generosity', 'Dystopia Residual']


melt=pd.melt(happiness2015,id_vars=main_cols,value_vars=factors)


melt['Percentage']=round((melt["value"]*100)/melt['Happiness Score'],2)

## 8. Challenge: Aggregate the Data and Create a Visualization ##

melt = pd.melt(happiness2015, id_vars = ['Country', 'Region', 'Happiness Rank', 'Happiness Score'], value_vars= ['Economy', 'Family', 'Health', 'Freedom', 'Trust', 'Generosity', 'Dystopia Residual'])
melt['Percentage'] = round(melt['value']/melt['Happiness Score'] * 100, 2)


pv_melt=melt.pivot_table(index='variable',values='value')

pv_melt.plot(kind='pie',legend=False, y= 'value')