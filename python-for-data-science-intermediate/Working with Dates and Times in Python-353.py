## 1. Introduction ##

from csv import reader
rea=open("potus_visitors_2015.csv")
da=reader(rea)
potus=list(da)[1:]

## 3. The Datetime Module ##

import datetime as dt

## 4. The Datetime Class ##

import datetime as dt


ibm_founded=dt.datetime(1911,6,16,0)
man_on_moon=dt.datetime(1969,7,20,20,17)

## 5. Using Strptime to Parse Strings as Dates ##

# The `potus` list of lists is available from
# the earlier screen where we created it
date_2_str = "12-24-1984"
date_2_dt = dt.datetime.strptime(date_2_str, "%m-%d-%Y")
print(date_2_dt)

date_format='%m/%d/%y %H:%M'
for i in potus:
    k=0
    i[2]=dt.datetime.strptime(i[2],date_format)

## 6. Using Strftime to Format Dates ##

visitors_per_month={}

for i in potus:
    va=i[2]
    s=dt.datetime.strftime(va,'%B, %Y')
    if s in visitors_per_month.keys():
        visitors_per_month[s]+=1
    else:
        visitors_per_month[s]=1

## 7. The Time Class ##

appt_times=[]

for i in potus:
    v=i[2]
    t=v.time()
    appt_times.append(t)

## 8. Comparing Time Objects ##

min_time=min(appt_times)
max_time=max(appt_times)

## 9. Calculations with Dates and Times ##

dt_1 = dt.datetime(1981, 1, 31)
dt_2 = dt.datetime(1984, 6, 28)
dt_3 = dt.datetime(2016, 5, 24)
dt_4 = dt.datetime(2001, 1, 1, 8, 24, 13)
answer_1=dt_2-dt_1
answer_2=dt_3+dt.timedelta(days=56)
answer_3=dt_4-dt.timedelta(seconds=3600)

## 10. Summarizing Appointment Lengths ##

for row in potus:
    end_date = row[3]
    end_date = dt.datetime.strptime(end_date, "%m/%d/%y %H:%M")
    row[3] = end_date
    
appt_lengths={}
for row in potus:
    v1=row[2]
    v2=row[3]
    l=v2-v1
    if l in appt_lengths.keys():
        appt_lengths[l]+=1
    else:
        appt_lengths[l]=1
        
max_length=max(appt_lengths)
min_length=min(appt_lengths)