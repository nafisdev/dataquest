## 1. Reading CSV Files with Encodings ##

laptops = pd.read_csv("laptops.csv",encoding="Latin-1")
print(laptops.info())

## 2. Cleaning Column Names ##

print(laptops.columns)

new_columns=[]

for c in laptops.columns:
    new_columns.append(c.strip())
    
laptops.columns=new_columns

## 3. Cleaning Column Names Continued ##

import pandas as pd
laptops = pd.read_csv('laptops.csv', encoding='Latin-1')

def clean(s):
    s=s.strip()
    s=s.replace("Operating System","os")
    s=s.replace(" ","_")
    s=s.replace("(","")
    s=s.replace(")","")
    s=s.lower()
    return s
new_columns=[]  
for c in laptops.columns:
    new_columns.append(clean(str(c)))
print(laptops.columns)    
laptops.columns=new_columns
print(laptops.columns)
    

## 4. Converting String Columns to Numeric ##

unique_ram=laptops["ram"].unique()

## 5. Removing Non-Digit Characters ##

laptops["ram"]=laptops["ram"].str.replace("GB","")

unique_ram=laptops["ram"].unique()

## 6. Converting Columns to Numeric Dtypes ##

laptops["ram"] = laptops["ram"].str.replace('GB','')

laptops["ram"]=laptops["ram"].astype(int)
dtypes=laptops.dtypes

## 7. Renaming Columns ##

laptops["ram"] = laptops["ram"].str.replace('GB','').astype(int)

laptops.rename({"ram": "ram_gb"}, axis=1, inplace=True)

ram_gb_desc=laptops["ram_gb"].describe()

## 8. Extracting Values from Strings ##

laptops["gpu_manufacturer"] = (laptops["gpu"]
                                       .str.split()
                                       .str[0]
                              )

print(laptops["gpu_manufacturer"])
laptops["cpu_manufacturer"]=laptops["cpu"].str.split().str[0]
print(laptops["cpu_manufacturer"])


cpu_manufacturer_counts=laptops["cpu_manufacturer"].value_counts()

## 9. Correcting Bad Values ##

mapping_dict = {
    'Android': 'Android',
    'Chrome OS': 'Chrome OS',
    'Linux': 'Linux',
    'Mac OS': 'macOS',
    'No OS': 'No OS',
    'Windows': 'Windows',
    'macOS': 'macOS'
}
print(laptops["os"])
laptops["os"]=laptops["os"].map(mapping_dict)
print(laptops["os"])

## 10. Dropping Missing Values ##

laptops_no_null_rows=laptops.dropna()
laptops_no_null_cols=laptops.dropna(axis=1)

## 11. Filling Missing Values ##

value_counts_before = laptops.loc[laptops["os_version"].isnull(), "os"].value_counts()
laptops.loc[laptops["os"] == "macOS", "os_version"] = "X"




b=laptops.loc[laptops["os"]=="No OS","os_version"]="Version Unknown"

value_counts_after = laptops.loc[laptops["os_version"].isnull(), "os"].value_counts()

## 12. Challenge: Clean a String Column ##

# print(laptops["weight"])



new_columns=[]  
for c in laptops.columns:
    if str(c)=="weight":
        new_columns.append("weight_kg")
    else:
        new_columns.append(c)
laptops.columns=new_columns
laptops["weight_kg"]=laptops["weight_kg"].str.strip().str.replace("kg","").str.replace("s","")
print(laptops["weight_kg"].unique())
laptops["weight_kg"]=laptops["weight_kg"].astype(float)

laptops.to_csv('laptops_cleaned.csv',index=False)