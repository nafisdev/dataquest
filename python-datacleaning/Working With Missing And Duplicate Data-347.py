## 1. Introduction ##

shape_2015=happiness2015.shape
shape_2016=happiness2016.shape
shape_2017=happiness2017.shape

## 2. Identifying Missing Values ##

missing_2016=happiness2016.isnull().sum()
missing_2017=happiness2017.isnull().sum()

## 3. Correcting Data Cleaning Errors that Result in Missing Values ##

happiness2017.columns = happiness2017.columns.str.replace('.', ' ').str.replace('\s+', ' ').str.strip().str.upper()
happiness2015.columns = happiness2015.columns.str.replace('.', ' ').str.replace('\s+', ' ').str.strip().str.upper().str.replace('(', '').str.replace(')', '')

happiness2016.columns = happiness2016.columns.str.replace('.', ' ').str.replace('\s+', ' ').str.strip().str.upper().str.replace('(', '').str.replace(')', '')


combined = pd.concat([happiness2015, happiness2016, happiness2017], ignore_index=True)
missing=combined.isnull().sum()

## 4. Visualizing Missing Data ##

import seaborn as sns
combined_updated = combined.set_index('YEAR')
sns.heatmap(combined_updated.isnull(), cbar=False)
regions_2017=combined[combined["YEAR"]==2017]
regions_2017=regions_2017.loc[:,"REGION"]
missing=regions_2017.isnull().sum()

## 5. Using Data From Additional Sources to Fill in Missing Values ##

combined=combined.merge(regions,how="left", on="COUNTRY")
combined=combined.drop('REGION_x', axis=1)
missing=combined.isnull().sum()

## 6. Identifying Duplicates Values ##

combined["COUNTRY"]=combined["COUNTRY"].str.upper().str.strip()


dups = combined.duplicated(['COUNTRY', 'YEAR'])
combined[dups]

## 7. Correcting Duplicates Values ##

combined['COUNTRY'] = combined['COUNTRY'].str.upper()
dups = combined.duplicated(['COUNTRY', 'YEAR'])
combined[dups]
combined=combined.drop_duplicates(subset=['COUNTRY' ,'YEAR'])

## 8. Handle Missing Values by Dropping Columns ##

columns_to_drop = ['LOWER CONFIDENCE INTERVAL', 'STANDARD ERROR', 'UPPER CONFIDENCE INTERVAL', 'WHISKER HIGH', 'WHISKER LOW']



combined=combined.drop(columns=columns_to_drop)
missing=combined.isnull().sum()

## 9. Handle Missing Values by Dropping Columns Continued ##

combined.notnull().sum().sort_values()

combined=combined.dropna(thresh=159,axis=1)
missing=combined.isnull().sum()

## 11. Handling Missing Values with Imputation ##

sorted = combined.set_index('REGION').sort_values(['REGION', 'HAPPINESS SCORE'])
sns.heatmap(sorted.isnull(), cbar=False)


happiness_mean=combined["HAPPINESS SCORE"].mean()
combined["HAPPINESS SCORE UPDATED"]=combined["HAPPINESS SCORE"].fillna(happiness_mean)

## 12. Dropping Rows ##

combined=combined.dropna()
missing=combined.isnull().sum()