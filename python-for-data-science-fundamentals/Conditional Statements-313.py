## 1. If Statements ##

# INITIAL CODE
opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

free_apps_ratings = []
for row in apps_data[1:]:
    rating = float(row[7])
    price = float(row[4])
    if(price==0.0):
        free_apps_ratings.append(rating)
avg_rating_free=sum(free_apps_ratings)/len(free_apps_ratings)
    # Complete the code from here

## 2. Booleans ##

a_price = 0
if(a_price ==0):
    print("This is free")
if(a_price==1):
    print("This is not free")

## 3. The Average Rating of Non-free Apps ##

# INITIAL CODE
opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

non_free_apps_ratings = []
for row in apps_data[1:]:
    rating = float(row[7])
    price = float(row[4])   
    if price != 0.0:
        non_free_apps_ratings.append(rating)
    
avg_rating_non_free = sum(non_free_apps_ratings) / len(non_free_apps_ratings)

## 4. The Average Rating of Gaming Apps ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

non_games_ratings=[]
for each in apps_data[1:]:
    rating = float(each[7])
    genre = str(each[11])
    if(genre!="Games"):
        non_games_ratings.append(rating)
avg_rating_non_games=sum(non_games_ratings)/len(non_games_ratings)
        

## 5. Multiple Conditions ##

# INITIAL CODE
opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

free_games_ratings = []
for row in apps_data[1:]:
    rating = float(row[7])
    price = float(row[4])
    genre = row[11]
    if(genre=="Games" and price==0):
        free_games_ratings.append(rating)

avg_rating_free_games=sum(free_games_ratings)/len(free_games_ratings)
    # Complete code from here

## 6. The or Operator ##

# INITIAL CODE
opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

games_social_ratings = []
for row in apps_data[1:]:
    rating = float(row[7])
    genre = row[11]
    if(genre== "Social Networking" or genre =="Games"):
        games_social_ratings.append(rating)

avg_games_social=sum(games_social_ratings)/len(games_social_ratings)# Complete code from here

## 7. Combining Logical Operators ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

free_games_social_ratings = []
non_free_games_social_ratings = []
for row in apps_data[1:]:
    rating = float(row[7])
    genre = row[11]
    price = float(row[4])
    
    if (genre == 'Social Networking' or genre == 'Games') and price == 0:
        free_games_social_ratings.append(rating)
    if (genre == 'Social Networking' or genre == 'Games') and price != 0:
        non_free_games_social_ratings.append(rating)
avg_free = sum(free_games_social_ratings) / len(free_games_social_ratings)
avg_non_free = sum(non_free_games_social_ratings) / len(non_free_games_social_ratings)
# Non-free apps (average)

## 8. Comparison Operators ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)
n_apps_more_9=0
n_apps_less_9=0
free_games_social_ratings=[]
for row in apps_data[1:]:
    rating = float(row[7])
    genre = row[11]
    price = float(row[4])
    
    if price > 9:
        free_games_social_ratings.append(rating)
        n_apps_more_9+=1
    if price < 9:
        n_apps_less_9+=1
avg_rating = sum(free_games_social_ratings) / len(free_games_social_ratings)

## 9. The else Clause ##

# INITIAL CODE
opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

for app in apps_data[1:]:
    price = float(app[4])
    
    if price == 0:
        app.append("free")
    else:
        app.append("non-free")
apps_data[0].append("free_or_not")

## 10. The elif Clause ##

# INITIAL CODE
opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

for app in apps_data[1:]:
    price = float(app[4])
    
    if price == 0:
        app.append("free")
    elif price>0 and price <20:
        app.append("affordable")
    elif price>20 and price <50:
        app.append("expensive")
    elif price>50:
        app.append("very expensive")
apps_data[0].append("price_label")