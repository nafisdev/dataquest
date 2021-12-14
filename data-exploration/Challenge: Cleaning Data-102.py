## 4. Filtering Out Bad Data ##

import matplotlib.pyplot as plt
true_avengers = pd.DataFrame()

avengers['Year'].hist()
print(avengers.columns)
true_avengers=avengers[avengers['Year']>=1960]

## 5. Consolidating Deaths ##

import numpy as np
def cou(ele):
    a_string=str(ele)
    matches = re.finditer('YES', a_string)
    matches_positions = [match.start() for match in matches]
    return len(matches_positions)
print(true_avengers[['Death1','Death2','Death3','Death4','Death5']])
# true_avengers[['Death1','Death2','Death3','Death4','Death5']].fillna('NO', inplace=True)
deaths=true_avengers[['Death1','Death2','Death3','Death4','Death5']].astype(str).agg('-'.join, axis=1)

true_avengers['Deaths']=deaths.apply(cou)

## 6. Verifying Years Since Joining ##

joined_accuracy_count  = int()
true_avengers.head()




joined_accuracy_count=true_avengers[true_avengers['Year'].astype(int)+true_avengers['Years since joining'].astype(int) == 2015].shape[0]