## 1. Introduction ##

import pandas as pd
import re

hn = pd.read_csv("hacker_news.csv")
titles = hn['title']

pattern=r'[Ss][Qq][Ll]'
sql_counts=titles.str.contains(pattern).sum()

## 2. Capture Groups ##

hn_sql = hn[hn['title'].str.contains(r"\w+SQL", flags=re.I)].copy()

hn_sql["flavor"]=hn_sql['title'].str.extract(r"(\w+SQL)", flags=re.I)
hn_sql["flavor"]=hn_sql["flavor"].str.lower()

sql_pivot=hn_sql.pivot_table(index="flavor",values=['num_comments'])

## 3. Using Capture Groups to Extract Data ##

vc=titles.str.extract(r'[Pp]ython[ ]([\d.]+)')[0].value_counts()
print(list(vc))
print(list(vc.index))

py_versions_freq=dict(zip(list(vc.index),list(vc)))

## 4. Counting Mentions of the 'C' Language ##

def first_10_matches(pattern):
    """
    Return the first 10 story titles that match
    the provided regular expression
    """
    all_matches = titles[titles.str.contains(pattern)]
    first_10 = all_matches.head(10)
    return first_10

pattern = r"\b[Cc]\b[^.][^+]"
first_ten=first_10_matches(pattern)

## 5. Using Lookarounds to Control Matches Based on Surrounding Text ##

pattern = r"\b(?<!Series )[Cc](?![+]|[.])\b" 
print(titles[titles.str.contains(pattern)])
c_mentions=titles.str.contains(pattern).sum()

## 6. BackReferences: Using Capture Groups in a RegEx Pattern ##

pattern=r'\b(\w+)[ ]\1\b'
repeated_words=titles[titles.str.contains(pattern)]

## 7. Substituting Regular Expression Matches ##

email_variations = pd.Series(['email', 'Email', 'e Mail',
                        'e mail', 'E-mail', 'e-mail',
                        'eMail', 'E-Mail', 'EMAIL'])

# pat=r'\be[-]?[ ]?mail[s]?\b'
# pattern=r'\be[ ]?[-]?mail[s]?\b'
# p=r'(\be[ ]?[-]?mail[s]?\b)'
# email_uniform=email_variations.str.replace(pattern,"email",flags=re.I)
# # d=titles.str.extract(p,flags=re.I)[0].value_counts()
# # print(d)
# # titles_clean=titles.str.replace(pattern,"email",flags=re.I)
# titles_clean=titles_clean.str.replace(pattern,"email",flags=re.I).astype(str)
# titles_clean=titles_clean.str.replace("Email:","email:").astype(str)
# a=titles_clean[titles_clean.str.contains(r'email')]
# print(a)
# d1=titles[titles_clean.str.contains('email')]
# vc=titles_clean.str.extract(r'(email)',flags=re.I)[0].value_counts()
# print(d1)
pattern = r"\be[-\s]?mail"
email_uniform = email_variations.str.replace(pattern, "email", flags=re.I)
titles_clean = titles.str.replace(pattern, "email", flags=re.I)

## 8. Extracting Domains from URLs ##

test_urls = pd.Series([
 'https://www.amazon.com/Technology-Ventures-Enterprise-Thomas-Byers/dp/0073523429',
 'http://www.interactivedynamicvideo.com/',
 'http://www.nytimes.com/2007/11/07/movies/07stein.html?_r=0',
 'http://evonomics.com/advertising-cannot-maintain-internet-heres-solution/',
 'HTTPS://github.com/keppel/pinn',
 'Http://phys.org/news/2015-09-scale-solar-youve.html',
 'https://iot.seeed.cc',
 'http://www.bfilipek.com/2016/04/custom-deleters-for-c-smart-pointers.html',
 'http://beta.crowdfireapp.com/?beta=agnipath',
 'https://www.valid.ly?param',
 'http://css-cursor.techstream.org'
])
pattern=r"https?://([\w\.\-]+)/?.*"
# as=r'\bhttp[s]?://([\w-]*(\w*\.)*\w*)'
# pattern=r'\bhttp[s]?://((?:www\.|ww2\.)?(?:[\w-]+\.){1,}\w+)\b'
# pattern=r'\b(http[s]?://)?((www\.|ww2\.)?([\w-]+\.)+\w+^/)/(\w+/?-?\.?)+'
domains=hn['url'].str.extract(pattern,flags=re.I)[0]
domains.name='url'
test_urls_clean=test_urls.str.extract(pattern,flags=re.I)[0]
top_domains=domains.value_counts().head(5)

## 9. Extracting URL Parts Using Multiple Capture Groups ##

# `test_urls` is available from the previous screen
pattern = r"(https?)://([\w\.\-]+)/?(.*)"
# as=r'\b(http[s]?)://([\w-]*[\w*\.]*\w*)/?'
# ([\w-]*[\w/]*[\w?]*[\w=]*[\w\.]*\*[\w]*)
# pattern=r'\b(http[s]?://)(www\.|ww2\.[\w-]+\.)+\w+/(\w+/?-?\.?)+'
domains=hn['url']
domains.name='url'
test_url_parts=test_urls.str.extract(pattern,flags=re.I)
url_parts=domains.str.extract(pattern,flags=re.I)
top_domains=domains.value_counts().head(5)

## 10. Using Named Capture Groups to Extract Data ##

pattern = r"(?P<protocol>https?)://(?P<domain>[\w\.\-]+)/?(?P<path>.*)"
domains=hn['url']
url_parts=domains.str.extract(pattern,flags=re.I)