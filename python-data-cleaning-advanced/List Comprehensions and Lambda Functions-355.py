## 1. The JSON Format ##

world_cup_str = """
[
    {
        "team_1": "France",
        "team_2": "Croatia",
        "game_type": "Final",
        "score" : [4, 2]
    },
    {
        "team_1": "Belgium",
        "team_2": "England",
        "game_type": "3rd/4th Playoff",
        "score" : [2, 0]
    }
]
"""

import json
world_cup_obj=json.loads(world_cup_str)

## 2. Reading a JSON file ##

import json


file=open("hn_2014.json")
hn=json.load(file)

print(type(hn))

## 3. Deleting Dictionary Keys ##

def del_key(dict_, key):
    # create a copy so we don't
    # modify the original dict
    modified_dict = dict_.copy()
    del modified_dict[key]
    return modified_dict
import json
file=open('hn_2014.json')
hn=json.load(file)
hn_clean=[]
for a in hn:
    hn_clean.append(del_key(a,'createdAtI'))

## 4. Writing List Comprehensions ##

# LOOP VERSION
#
hn_clean = []
#
# for d in hn:
#     new_d = del_key(d, 'createdAtI')
#     hn_clean.append(new_d)

hn_clean=[del_key(i, 'createdAtI') for i in hn]

## 5. Using List Comprehensions to Transform and Create Lists ##

urls=[i["url"] for i in hn]

## 6. Using List Comprehensions to Reduce a List ##

thousand_points=[i for i in hn_clean if i["points"] > 1000]

num_thousand_points=len(thousand_points)

## 7. Passing Functions as Arguments ##

def get_num_comments(d):
    return d["numComments"]


most_comments=max(hn_clean,key=get_num_comments)
    

## 8. Lambda Functions ##

# def multiply(a, b):
#    return a * b


multiply=lambda x,y: x*y

## 9. Using Lambda Functions to Analyze JSON data ##

hn_sorted_points=sorted(hn_clean, key = lambda x : x["points"],reverse=True)

top_5_titles=[i["title"] for i in hn_sorted_points[0:5]]

## 10. Reading JSON files into pandas ##

import pandas
print(type(hn_clean))
hn_df=pd.DataFrame(hn_clean)

## 11. Exploring Tags Using the Apply Function ##

tags = hn_df['tags']



boola= tags.apply(lambda x:len(x)==4)
four_tags=tags[boola]


tags_types = four_tags.apply(len)
type_lengths = tags_types.value_counts(dropna=False)
print(type_lengths)

## 12. Extracting Tags Using Apply with a Lambda Function ##

def extract_tag(l):
    return l[-1] if len(l) == 4 else None


boola= tags.apply(lambda x:len(x)==4)
cleaned_tags=tags.apply(lambda x:extract_tag(x))
print(cleaned_tags[boola])
hn_df["tags"]=cleaned_tags