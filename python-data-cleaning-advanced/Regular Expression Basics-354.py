## 1. Introduction ##

import pandas as pd

hn=pd.read_csv("hacker_news.csv", encoding="UTF-8")

## 2. The Regular Expression Module ##

import re

titles = hn["title"].tolist()

python_mentions=0
pattern=r'[pP]ython'
for a in titles:
    if re.search(pattern,a):
        python_mentions+=1
    else:
        pass

print(python_mentions)

## 3. Counting Matches with pandas Methods ##

import pandas as pd

hn=pd.read_csv("hacker_news.csv", encoding="UTF-8")
titles=hn["title"]
print(titles)
pattern=r'[pP]ython'
python_mentions=titles.str.contains(pattern).sum()

## 4. Using Regular Expressions to Select Data ##

titles = hn['title']

pattern=r'[rR]uby'
ruby_titles=titles[titles.str.contains(pattern)]

## 5. Quantifiers ##

# The `titles` variable is available from
# the previous screens
pattern=r'e[-]*mail'
email_bool=titles.str.contains(pattern)
email_count=email_bool.sum()

email_titles=titles[email_bool]

## 6. Character Classes ##

pattern=r'\[\w+\]'

tag_titles=titles.str.contains(pattern)
tag_count=tag_titles.sum()

## 7. Accessing the Matching Text with Capture Groups ##

pattern = r"\[(\w+)\]"


tag_freq=titles.str.extract(pattern)[0].value_counts()
    

## 8. Negative Character Classes ##

def first_10_matches(pattern):
    """
    Return the first 10 story titles that match
    the provided regular expression
    """
    all_matches = titles[titles.str.contains(pattern)]
    first_10 = all_matches
    return first_10


pattern=r'[Jj]ava[^Ss]'
java_titles=first_10_matches(pattern)

## 9. Word Boundaries ##

def first_10_matches(pattern):
    """
    Return the first 10 story titles that match
    the provided regular expression
    """
    all_matches = titles[titles.str.contains(pattern)]
    first_10 = all_matches
    return first_10


pattern=r'\b[Jj]ava\b'
java_titles=first_10_matches(pattern)

## 10. Matching at the Start and End of Strings ##

pat1=r'^\[(\w+)\]'
beginning_count=titles.str.extract(pat1).iloc[:,0].value_counts().sum()
pat2=r'\[(\w+)\]$'
ending_count=titles.str.extract(pat2).iloc[:,0].value_counts().sum()

## 11. Challenge: Using Flags to Modify Regex Patterns ##

import re

email_tests = pd.Series(['email', 'Email', 'e Mail', 'e mail', 'E-mail',
              'e-mail', 'eMail', 'E-Mail', 'EMAIL', 'emails', 'Emails',
              'E-Mails'])
pat=r'\be[-]?[ ]?mail[s]?\b'
pat1=r'(e[-]?[ ]?mail)'
t=email_tests.str.contains(pat, flags=re.I).sum()

email_mentions=titles.str.contains(pat, flags=re.I).sum()
te=titles.str.extract(pat1, flags=re.I)[0].value_counts()
