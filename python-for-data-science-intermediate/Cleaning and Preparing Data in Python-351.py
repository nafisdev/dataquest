## 1. Introducing Data Cleaning ##

# Read the text on the left, and then scroll to the bottom
# to find the instructions for the coding exercise

num_rows=len(moma)

# Write your answer to the instructions below -- the list of
# lists is stored using the variable name `moma`

## 2. Reading our MoMA Dataset ##

# import the reader function from the csv module
from csv import reader

# use the python built-in function open()
# to open the children.csv file
opened_file = open('artworks.csv')

# use csv.reader() to parse the data from
# the opened file
read_file = reader(opened_file)

# use list() to convert the read file
# into a list of lists format
children = list(read_file)

# remove the first row of the data, which
# contains the column names
children = children[1:]
moma=list(children)

# Write your code here

## 3. Replacing Substrings with the Replace Method ##

age1 = "I am thirty-one years old"
age2=age1.replace('one','two')
age1

## 4. Cleaning the Nationality and Gender Columns ##

# Variables you create in previous screens
# are available to you, so you don't need
# to read the CSV again
moma
children[0]

for val in moma:
    val[2]=val[2].replace('(','')
    val[2]=val[2].replace(')','')
    val[5]=val[5].replace('(','')
    val[5]=val[5].replace(')','')

## 5. String Capitalization ##

for i in moma:
    if i[5].title()=='Male':
        i[5]='Male'
    elif i[5].title()=='Female':
        i[5]='Female'
    else:
        i[5]='Gender Unknown/Other'
    if not i[2]:
        i[2]='Nationality Unknown'
    else:
        i[2]=i[2].title()

## 6. Errors During Data Cleaning ##

def clean_and_convert(date):
    # check that we don't have an empty string
    if date != "":
        # move the rest of the function inside
        # the if statement
        date = date.replace("(", "")
        date = date.replace(")", "")
        date = int(date)
    return date

d=clean_and_convert(moma[31][4])
moma[31]
for i in moma:
    i[3]=clean_and_convert(i[3])
    i[4]=clean_and_convert(i[4])
    

## 7. Parsing Numbers from Complex Strings, Part One ##

test_data = ["1912", "1929", "1913-1923",
             "(1951)", "1994", "1934",
             "c. 1915", "1995", "c. 1912",
             "(1988)", "2002", "1957-1959",
             "c. 1955.", "c. 1970's", 
             "C. 1990-1999"]

bad_chars = ["(",")","c","C",".","s","'", " "]

def strip_characters(s):
    if s and s!='':
        
        for k in bad_chars:
            s=s.replace(k,'')
    return s
        
        

k=strip_characters('(1951)')
stripped_test_data=[]
for i in test_data:
    stripped_test_data.append(strip_characters(i))

## 8. Parsing Numbers from Complex Strings, Part Two ##

test_data = ["1912", "1929", "1913-1923",
             "(1951)", "1994", "1934",
             "c. 1915", "1995", "c. 1912",
             "(1988)", "2002", "1957-1959",
             "c. 1955.", "c. 1970's", 
             "C. 1990-1999"]

bad_chars = ["(",")","c","C",".","s","'", " "]

def strip_characters(string):
    for char in bad_chars:
        string = string.replace(char,"")
    return string

stripped_test_data = ['1912', '1929', '1913-1923',
                      '1951', '1994', '1934',
                      '1915', '1995', '1912',
                      '1988', '2002', '1957-1959',
                      '1955', '1970', '1990-1999']

def process_date(i):
    if '-' in i:
        li=i.split('-')
        avg=(int(li[0])+int(li[1]))/2
        i=round(avg)
    return int(i)

processed_test_data=[]
for i in stripped_test_data:
    i=processed_test_data.append(process_date(i))
    
for i in moma:
    i[6]=process_date(strip_characters(i[6]))