## 1. Storing Data ##

content_ratings=['4+', '9+', '12+', '17+']
nums=[4433, 987, 1155, 622]
content_rating_numbers=[content_ratings,nums]

## 2. Dictionaries ##

content_ratings={'4+': 4433, '9+': 987, '12+': 1155, '17+': 622}
print(content_ratings)

## 3. Indexing ##

content_ratings = {'4+': 4433, '9+': 987, '12+': 1155, '17+': 622}


over_9= content_ratings['9+']
over_17=content_ratings['17+']

print(over_9)
print(over_17)

## 4. Alternative Method of Creating a Dictionary ##

content_ratings={}
content_ratings={'4+': 4433, '9+': 987, '12+': 1155, '17+': 622}
over_12_n_apps=content_ratings['12+']

## 5. Key-Value Pairs ##

d_1={'key_1': 'first_value', 
 'key_2': 2,
 'key_3': 3.14,
 'key_4': True,
 'key_5': [4,2,1],
 'key_6': {'inner_key' : 6}
 }
error=True

## 6. Checking for Membership ##

content_ratings = {'4+': 4433, '9+': 987, '12+': 1155, '17+': 622}

is_in_dictionary_1='9+' in content_ratings
is_in_dictionary_2=987 in content_ratings

if '17+' in content_ratings:
    result="It exists"
    print(result)

## 7. Counting with Dictionaries ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)
content_ratings={"4+":0,"9+":0,"12+":0,"17+":0}


for each in apps_data[1:]:
    c_rating=each[10]
    content_ratings[c_rating]+=1
print(content_ratings)

## 8. Finding the Unique Values ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)
content_ratings={}
a1={"4+":0,"9+":0,"12+":0,"17+":0}

a=['4+','9+', '12+', '17+']#list(a1.keys())
for each in apps_data[1:]:
    c_rating=each[10]
    if c_rating in list(content_ratings.keys()):
        content_ratings[c_rating]+=1
    else:
        content_ratings[c_rating]=1
print(content_ratings)

## 9. Proportions and Percentages ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)
genre_counting={}

for each in apps_data[1:]:
    genre=each[11]
    if genre in list(genre_counting.keys()):
        genre_counting[genre]+=1
    else:
        genre_counting[genre]=1
print(genre_counting)

## 10. Looping over Dictionaries ##

content_ratings = {'4+': 4433, '12+': 1155, '9+': 987, '17+': 622}
total_number_of_apps = 7197
for each in content_ratings:
    content_ratings[each]=(content_ratings[each]/7197)*100
    
percentage_17_plus=content_ratings['17+']
percentage_15_allowed=100-percentage_17_plus

## 11. Keeping the Dictionaries Separate ##

content_ratings = {'4+': 4433, '12+': 1155, '9+': 987, '17+': 622}
total_number_of_apps = 7197

c_ratings_proportions={}
c_ratings_percentages={}

for key in content_ratings:
    proportion=content_ratings[key]/total_number_of_apps
    c_ratings_proportions[key] = proportion
    c_ratings_percentages[key] = proportion*100
print(c_ratings_proportions)
print(c_ratings_percentages)

## 12. Frequency Tables for Numerical Columns ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)
data_sizes=[]
for each in apps_data[1:]:
    size=float(each[2])
    data_sizes.append(size)
    
min_size=min(data_sizes)
max_size=max(data_sizes)