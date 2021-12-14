## 2. Point Guards ##

# Enter code here.


point_guards=nba[nba['pos']=='PG']

## 3. Points Per Game ##

point_guards['ppg'] = point_guards['pts'] / point_guards['g']

# Make sure ppg = pts/g
point_guards[['pts', 'g', 'ppg']].head(5)

## 4. Assist Turnover Ratio ##

point_guards = point_guards[point_guards['tov'] != 0]

point_guards['atr']=point_guards['ast']/point_guards['tov']

## 5. Visualizing the Point Guards ##

plt.scatter(point_guards['ppg'], point_guards['atr'], c='y')
plt.title("Point Guards")
plt.xlabel('Points Per Game', fontsize=13)
plt.ylabel('Assist Turnover Ratio', fontsize=13)
plt.show()

## 9. Setup (continued) ##

def centroids_to_dict(centroids):
    dictionary = dict()
    # iterating counter we use to generate a cluster_id
    counter = 0

    # iterate a pandas data frame row-wise using .iterrows()
    for index, row in centroids.iterrows():
        coordinates = [row['ppg'], row['atr']]
        dictionary[counter] = coordinates
        counter += 1

    return dictionary

centroids_dict = centroids_to_dict(centroids)

## 10. Step 1 (Euclidean Distance) ##

import math

def calculate_distance(centroid, player_values):
    root_distance = 0
    
    for x in range(0, len(centroid)):
        difference = centroid[x] - player_values[x]
        squared_difference = difference**2
        root_distance += squared_difference

    euclid_distance = math.sqrt(root_distance)
    return euclid_distance

q = [5, 2]
p = [3,1]

# Sqrt(5) = ~2.24
print(calculate_distance(q, p))

## 11. Step 1 (Continued) ##

# Add the function, `assign_to_cluster`
# This creates the column, `cluster`, by applying assign_to_cluster row-by-row
# Uncomment when ready

def assign_to_cluster(row):
    lowest_distance=-1
    closest_cluster=-1
    # euclidean_distance
    
    
    for cluster_id,centroid in centroids_dict.items():
        df_row = [row['ppg'], row['atr']]
        euclidean_distance = calculate_distance(centroid, df_row)
        
        if lowest_distance == -1:
            lowest_distance = euclidean_distance
            closest_cluster = cluster_id
        # (centroid,df_row)
        elif euclidean_distance < lowest_distance:
            lowest_distance = euclidean_distance
            closest_cluster = cluster_id
    return closest_cluster


point_guards['cluster'] = point_guards.apply(lambda row: assign_to_cluster(row), axis=1)

## 13. Step 2 ##

def recalculate_centroids(df):
    new_centroids_dict = dict()
    # 0..1...2...3...4
    for cluster_id in range(0, num_clusters):
        # Finish the logic
        values_in_cluster=df[df['cluster']==cluster_id] 
        # new_centroids_dict[cluster]=new_centroids_dict[cluster_id].mean()
        new_centroid = [np.average(values_in_cluster['ppg']),np.average(values_in_cluster['atr'])]
        new_centroids_dict[cluster_id] = new_centroid
    return new_centroids_dict

centroids_dict = recalculate_centroids(point_guards)
# new_centroids_dict=centroids_dict

## 14. Repeat Step 1 ##

point_guards['cluster'] = point_guards.apply(lambda row: assign_to_cluster(row), axis=1)
visualize_clusters(point_guards, num_clusters)