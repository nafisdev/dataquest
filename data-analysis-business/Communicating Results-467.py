## 2. The Scenario ##

import pandas as pd

playstore = pd.read_csv("googleplaystore.csv")
print(playstore.shape)
answer='no'




playstore.iloc[10472,:]["Last Updated"]=playstore.iloc[10472,:]["Genres"]

playstore.iloc[10472,:]["Genres"]="Lifestyle"

playstore.iloc[10472,:]["Category"]="Lifestyle"



print(playstore.iloc[10472,:])

playstore=playstore.drop([10472])

## 3. Cleaning the Data ##

def clean_size(size):
    """Convert file size string to float and megabytes"""
    size = size.replace("M","")
    if size.endswith("k"):
        size = float(size[:-1])/1000
    elif size == "Varies with device":
        size = pd.np.NaN
    else:
        size = float(size)
    return size

# playstore["Price"] = playstore["Price"].str.replace("$", "").astype("float")

# paid = playstore[playstore["Price"] != 0].copy()

paid.drop(["Type"], axis=1, inplace=True)
paid["Reviews"]=paid["Reviews"].astype("int")
paid["Size"] = paid["Size"].apply(clean_size).astype("float")


paid.info()

## 4. Removing Duplicates ##

paid.sort_values(by="Reviews", ascending=False, inplace=True)

paid.drop_duplicates(inplace=True,keep="first",subset=["App"])

print(paid.duplicated("App").sum())

paid.reset_index(drop=True, inplace=True)

## 5. Exploring the Price ##

affordable_apps = paid[paid["Price"]<50].copy()

cheap=affordable_apps["Price"]<5

reasonable=affordable_apps["Price"]>=5
affordable_apps[cheap].hist(column="Price", grid=False, figsize=(12,6))
affordable_apps[reasonable].hist(column="Price", grid=False, figsize=(12,6))
affordable_apps["affordability"]=None
affordable_apps["affordability"]=affordable_apps["affordability"].mask(cheap,"cheap")
affordable_apps["affordability"]=affordable_apps["affordability"].mask(reasonable,"reasonable")

## 6. Price vs. Rating ##

cheap = affordable_apps["Price"] < 5
reasonable = affordable_apps["Price"] >= 5

cheap_mean=affordable_apps[cheap]["Price"].mean()
affordable_apps["price_criterion"]=0
cheapmask=(affordable_apps["Price"]<cheap_mean) * cheap
affordable_apps["price_criterion"]=affordable_apps["price_criterion"].mask(cheapmask,1).astype("float")

affordable_apps[reasonable].plot(kind="scatter", x="Price", y="Rating")

reasonable_mean=affordable_apps[reasonable]["Price"].mean()
reasonablemask=(affordable_apps["Price"]<reasonable_mean) * reasonable
affordable_apps["price_criterion"]=affordable_apps["price_criterion"].mask(reasonablemask,1).astype("float")

## 7. Price vs Category and Genres ##

affordable_apps["genre_count"] = affordable_apps["Genres"].str.count(";")+1

genres_mean = affordable_apps.groupby(
    ["affordability", "genre_count"]
).mean()[["Price"]]


def label_genres(row):
    """For each segment in `genres_mean`,
    labels the apps that cost less than its segment's mean with `1`
    and the others with `0`."""

    aff = row["affordability"]
    gc = row["genre_count"]
    price = row["Price"]

    if price < genres_mean.loc[(aff, gc)][0]:
        return 1
    else:
        return 0

def label_categories(row):
    """For each segment in `genres_mean`,
    labels the apps that cost less than its segment's mean with `1`
    and the others with `0`."""

    aff = row["affordability"]
    gc = row["Category"]
    price = row["Price"]

    if price < categories_mean.loc[(aff, gc)][0]:
        return 1
    else:
        return 0
    
affordable_apps["genre_criterion"] = affordable_apps.apply(
    label_genres, axis="columns"
)

categories_mean=affordable_apps.groupby(["affordability", "Category"]).mean()[["Price"]]

affordable_apps["category_criterion"] = affordable_apps.apply(
    label_categories, axis="columns"
)

## 8. Results and Impact ##

import pandas as pd
playstore = pd.read_csv("googleplaystore.csv")
playstore.drop(labels=10472, inplace=True)

def clean_size(size):
    """Convert file size string to float and megabytes"""
    size = size.replace("M","")
    if size.endswith("k"):
        size = float(size[:-1])/1000
    elif size == "Varies with device":
        size = pd.np.NaN
    else:
        size = float(size)
    return size

playstore["Price"] = playstore["Price"].str.replace("$", "").astype(float)

paid = playstore[playstore["Price"] != 0].copy()

paid.drop("Type", axis="columns", inplace=True)
paid["Reviews"] = paid["Reviews"].astype(int)
paid["Size"] = paid["Size"].apply(clean_size).astype(float)

paid.drop_duplicates(inplace=True)
paid.drop([2151, 4301], inplace=True)

paid.sort_values("Reviews", ascending=False, inplace=True)
paid.drop_duplicates("App", inplace=True)
paid.reset_index(inplace=True, drop=True)

affordable_apps = paid[paid["Price"]<50].copy()

cheap = affordable_apps["Price"] < 5
reasonable = affordable_apps["Price"] >= 5
affordable_apps["affordability"] = affordable_apps.apply(
    lambda row: "cheap" if row["Price"] < 5 else "reasonable",
    axis=1
)

cheap_mean = affordable_apps.loc[cheap, "Price"].mean()

affordable_apps.loc[cheap, "price_criterion"] = affordable_apps["Price"].apply(
    lambda price: 1 if price < cheap_mean else 0
)

reasonable_mean = affordable_apps.loc[reasonable, "Price"].mean()

affordable_apps.loc[reasonable,"price_criterion"] = affordable_apps["Price"].apply(
    lambda price: 1 if price < reasonable_mean else 0
)

affordable_apps["genre_count"] = affordable_apps["Genres"].str.count(";")+1



genres_mean = affordable_apps.groupby(
    ["affordability", "genre_count"]
).mean()[["Price"]]

categories_mean = affordable_apps.groupby(
    ["affordability", "Category"]
).mean()[["Price"]]


def label_genres(row):
    """For each segment in `genres_mean`,
    labels the apps that cost less than its segment's mean with `1`
    and the others with `0`."""

    aff = row["affordability"]
    gc = row["genre_count"]
    price = row["Price"]

    if price < genres_mean.loc[(aff, gc)][0]:
        return 1
    else:
        return 0

affordable_apps["genre_criterion"] = affordable_apps.apply(
    label_genres, axis="columns"
)

def label_categories(row):
    """For each segment in `categories_mean`,
    labels the apps that cost less than its segment's mean with `1`
    and the others with `0`."""

    aff = row["affordability"]
    cat = row["Category"]
    price = row["Price"]

    if price < categories_mean.loc[(aff, cat)][0]:
        return 1
    else:
        return 0

affordable_apps["category_criterion"] = affordable_apps.apply(
    label_categories, axis="columns"
)
criteria = ["price_criterion", "genre_criterion", "category_criterion"]
affordable_apps["Result"] = affordable_apps[criteria].mode(axis='columns')

cheapmask=(affordable_apps["Price"]<cheap_mean)*(affordable_apps["affordability"]=="cheap")
reasonablemask=(affordable_apps["Price"]<reasonable_mean)*(affordable_apps["affordability"]=="reasonable")
affordable_apps["New Price"]=affordable_apps["Price"].mask(cheapmask,cheap_mean).round(2)
affordable_apps["New Price"]=affordable_apps["New Price"].mask(reasonablemask,reasonable_mean).round(2)



def clean(elem):
    if elem:
        elem=elem.replace('+','').replace(',','')
    return elem
affordable_apps["Installs"]=affordable_apps["Installs"].apply(clean).astype(int)

affordable_apps["Impact"]=(affordable_apps["New Price"]-affordable_apps["Price"])*affordable_apps["Installs"]


total_impact=affordable_apps["Impact"].sum()
print(total_impact)