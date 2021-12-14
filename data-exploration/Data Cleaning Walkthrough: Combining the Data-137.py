## 3. Condensing the Class Size Dataset ##

class_size=data["class_size"]

class_size=class_size[class_size['GRADE '].str.contains('09-12',na=False)]

class_size=class_size[class_size['PROGRAM TYPE'].str.contains('GEN ED',na=False)]


print(class_size.head())

## 5. Computing Average Class Sizes ##

import numpy as np


class_size=class_size.groupby('DBN').agg(np.mean)


class_size.reset_index(inplace=True)

data['class_size']=class_size
print(data['class_size'].head())

## 7. Condensing the Demographics Dataset ##

demographics=data["demographics"]

demographics=demographics[demographics["schoolyear"]==20112012]


data["demographics"]=demographics

## 9. Condensing the Graduation Dataset ##

graduation=data['graduation']

graduation=graduation[graduation['Demographic']=='Total Cohort']

graduation=graduation[graduation['Cohort']=='2006']
data['graduation']=graduation

print(data['graduation'].head())

## 10. Converting AP Test Scores ##

cols = ['AP Test Takers ', 'Total Exams Taken', 'Number of Exams with scores 3 4 or 5']

ap_2010=data['ap_2010']
for i in cols:
    ap_2010[i]=pd.to_numeric(ap_2010[i],errors='coerce')
data['ap_2010']=ap_2010

## 12. Performing the Left Joins ##

combined = data["sat_results"]

combined=combined.merge(ap_2010,on='DBN', how='left')
combined=combined.merge(graduation,on='DBN', how='left')

print(combined.head())

combined.shape

## 13. Performing the Inner Joins ##

combined=combined.merge(class_size,on='DBN', how='inner')
combined=combined.merge(demographics,on='DBN', how='inner')
combined=combined.merge(survey,on='DBN', how='inner')
combined=combined.merge(data['hs_directory'],on='DBN', how='inner')


print(combined.head())

combined.shape

## 15. Filling in Missing Values ##

m=combined.mean()
combined=combined.fillna(m)
combined=combined.fillna(0)
print(combined.head())

## 16. Adding a School District Column for Mapping ##

def ext(elem):
    return elem[0:2]



combined['school_dist']=combined['DBN'].apply(ext)

print(combined['school_dist'].head())