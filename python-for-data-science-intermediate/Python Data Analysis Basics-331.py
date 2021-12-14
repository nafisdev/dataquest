## 1. Reading the MoMA Dataset ##

from csv import reader

# Read the `artworks_clean.csv` file
opened_file = open('artworks_clean.csv')
read_file = reader(opened_file)
moma = list(read_file)
moma = moma[1:]

# Convert the birthdate values
for row in moma:
    birth_date = row[3]
    if birth_date != "":
        birth_date = int(birth_date)
    row[3] = birth_date
    
# Convert the death date values
for row in moma:
    death_date = row[4]
    if death_date != "":
        death_date = int(death_date)
    row[4] = death_date

# Write your code below
for row in moma:
    date = row[6]
    if date != "":
        date = int(date)
    row[6] = date

## 2. Calculating Artist Ages ##

ages=[]
for a in moma:
    date=int(a[6]) if a[6] and a[6]!='' else 0
    birth=int(a[3]) if a[3] and a[3]!='' else 0
    age=0 if date==0 or birth ==0 else date-birth
    ages.append(int(age))
    
final_ages=[]
for a in ages:
    if a>20:
        final_ages.append(a)
    else:
        final_ages.append("Unknown")
    

## 3. Converting Ages to Decades ##

# The final_ages variable is available
# from the previous screen

decades=[]
for i in final_ages:
    i=str(i)
    i=i[:-1]+'0s'if i!='Unknown' else i
    decades.append(i)

## 4. Summarizing the Decade Data ##

# The decades variable is available
# from the previous screen

decade_frequency={}
for i in decades:
    if i in decade_frequency.keys():
        decade_frequency[i]+=1
    else:
        decade_frequency[i]=1
    

## 5. Inserting Variables into Strings ##

artist = "Pablo Picasso"
birth_year = 1881
t="{artist}'s birth year is {birth_year}"
v=t.format(artist=artist,birth_year=birth_year)
print(v)

## 6. Creating an Artist Frequency Table ##

artist_freq={}
for a in moma:
    i=a[1]
    if i in artist_freq.keys():
        artist_freq[i]+=1
    
    else:
        artist_freq[i]=1        
    

## 7. Creating an Artist Summary Function ##

def artist_summary(name):
    print(name)
    print(artist_freq[name],)
    t="There are {0} artworks by {1} in the data set"
    t=t.format(artist_freq[name],name)
    print(t)
    
    
    
artist_summary("Henri Matisse")

## 8. Formatting Numbers Inside Strings ##

pop_millions = [
    ["China", 1379.302771],
    ["India", 1281.935991],
    ["USA",  326.625791],
    ["Indonesia",  260.580739],
    ["Brazil",  207.353391],
]

for i in pop_millions:
    c=i[0]
    p=i[1]
    t="The population of {0} is {1:,.2f} million"
    print(t.format(c,p))

## 9. Challenge: Summarizing Artwork Gender Data ##

g_freq={}
for i in moma:
    g=i[5]
    if g in g_freq:
        g_freq[g]+=1
    else:
        g_freq[g]=1
        
for i in g_freq:
    t="There are {0:,d} artworks by {1} artists"
    print(t.format(g_freq[i],i))