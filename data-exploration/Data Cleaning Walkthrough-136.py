## 4. Reading in the Data ##

import pandas as pd
data_files = [
    "ap_2010.csv",
    "class_size.csv",
    "demographics.csv",
    "graduation.csv",
    "hs_directory.csv",
    "sat_results.csv"
]
data = {}

for i in data_files:
    k=i.split('.')[0]
    data[k]=pd.read_csv('schools/'+i)
    print(i.split('.')[0])

## 5. Exploring the SAT Data ##

print(data['sat_results'].head())

## 6. Exploring the Remaining Data ##

for i in data.keys():
    print(data[i].head())

## 8. Reading in the Survey Data ##

all_survey=pd.read_csv('schools/survey_all.txt',delimiter='\t',encoding='windows-1252')
d75_survey=pd.read_csv('schools/survey_d75.txt',delimiter='\t',encoding='windows-1252')


survey=pd.concat([all_survey,d75_survey], axis=0)
print(survey.head())

## 9. Cleaning Up the Surveys ##

survey['DBN']=survey['dbn'].copy()
cl=["DBN", "rr_s", "rr_t", "rr_p", "N_s", "N_t", "N_p", "saf_p_11", "com_p_11", "eng_p_11", "aca_p_11", "saf_t_11", "com_t_11", "eng_t_11", "aca_t_11", "saf_s_11", "com_s_11", "eng_s_11", "aca_s_11", "saf_tot_11", "com_tot_11", "eng_tot_11", "aca_tot_11"]

survey=survey[cl]

data['survey']=survey

## 11. Inserting DBN Fields ##

print(data.keys())
hs_directory=data['hs_directory']

hs_directory['DBN']=hs_directory['dbn']

padded_csd=data['class_size']["CSD"].apply(lambda x:str(x).zfill(2))
data['class_size']["DBN"]=padded_csd+data['class_size']["SCHOOL CODE"]
print(data['class_size'].head())

## 12. Combining the SAT Scores ##

sat_results=data['sat_results']
sat_results['SAT Math Avg. Score']= pd.to_numeric(sat_results['SAT Math Avg. Score'],errors="coerce")


sat_results['SAT Critical Reading Avg. Score']= pd.to_numeric(sat_results['SAT Critical Reading Avg. Score'],errors="coerce")
sat_results['SAT Writing Avg. Score']= pd.to_numeric(sat_results['SAT Writing Avg. Score'],errors="coerce")

sat_results['sat_score']=sat_results['SAT Critical Reading Avg. Score']+sat_results['SAT Writing Avg. Score']+sat_results['SAT Math Avg. Score']

print(sat_results['sat_score'].head())

## 13. Parsing Geographic Coordinates for Schools ##

import re
re.findall("\(.+\)", "1110 Boston Road\nBronx, NY 10456\n(40.8276026690005, -73.90447525699966)")

def extract(elem):
    return re.findall("\(.+\)", elem)[0].split(',')[0][1:-1]

print(extract("1110 Boston Road\nBronx, NY 10456\n(40.8276026690005, -73.90447525699966)"))
hs_directory=data['hs_directory']
hs_directory['lat']=hs_directory['Location 1'].apply(extract)
print(hs_directory['lat'].head())

## 14. Extracting the Longitude ##

import re

def extract(elem):
    return re.findall("\(.+\)", elem)[0].split(',')[1][0:-2]

print(extract("1110 Boston Road\nBronx, NY 10456\n(40.8276026690005, -73.90447525699966)"))
hs_directory=data['hs_directory']
hs_directory['lon']=hs_directory['Location 1'].apply(extract)
print(hs_directory['lon'].head())

hs_directory['lat']=pd.to_numeric(hs_directory['lat'],errors='coerce')
hs_directory['lon']=pd.to_numeric(hs_directory['lon'],errors='coerce')
print(hs_directory.head())