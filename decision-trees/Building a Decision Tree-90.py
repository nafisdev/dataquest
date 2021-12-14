## 4. Determining the Column to Split On ##

def find_best_column(data, target_name, columns):
    # Fill in the logic here to automatically find the column in columns to split on
    # data is a dataframe
    # target_name is the name of the target variable
    # columns is a list of potential columns to split on
    information_gains=[]
    for a in columns:
        information_gains.append(calc_information_gain(income,a,target_name))
    highest_gain=columns[information_gains.index(max(information_gains))]
    return highest_gain

# A list of columns to potentially split income with
columns = ["age", "workclass", "education_num", "marital_status", "occupation", "relationship", "race", "sex", "hours_per_week", "native_country"]

income_split=find_best_column(income, "high_income", columns)




## 5. Creating a Simple Recursive Algorithm ##

# We'll use lists to store our labels for nodes (when we find them)
# Lists can be accessed inside our recursive function, whereas integers can't.  
# Look at the python missions on scoping for more information on this topic
label_1s = []
label_0s = []

def id3(data, target, columns):
    # The pandas.unique method will return a list of all the unique values in a series
    unique_targets = pandas.unique(data[target])
    
    if len(unique_targets) == 1:
        # Insert code here to append 1 to label_1s or 0 to label_0s, based on what we should label the node
        if 0 in unique_targets:
            label_1s.append(1)
        elif 1 in unique_targets:
            label_0s.append(0)
        return
        # See lines 2 and 3 in the algorithm
        
        # Returning here is critical -- if we don't, the recursive tree will never finish, and run forever
        best_column =find_best_column(data,target,columns)
        column_median=data[best_column].median()
        
        left_split = data[data[best_column] <= column_median]
        right_split = data[data[best_column] > column_median]

        for split in [left_split, right_split]:
            id3(split, target, columns)
        # See our example above for when we returned
        return
    
    # Find the best column to split on in our data
    best_column = find_best_column(data, target, columns)
    # Find the median of the column
    column_median = data[best_column].median()
    
    # Create the two splits
    left_split = data[data[best_column] <= column_median]
    right_split = data[data[best_column] > column_median]
    
    # Loop through the splits and call id3 recursively
    for split in [left_split, right_split]:
        # Call id3 recursively to process each branch
        id3(split, target, columns)
    
# Create the data set that we used in the example on the last screen
data = pandas.DataFrame([
    [0,20,0],
    [0,60,2],
    [0,40,1],
    [1,25,1],
    [1,35,2],
    [1,55,1]
    ])
# Assign column names to the data
data.columns = ["high_income", "age", "marital_status"]

# Call the function on our data to set the counters properly
id3(data, "high_income", ["age", "marital_status"])

## 7. Storing the Tree ##

# Create a dictionary to hold the tree  
# It has to be outside of the function so we can access it later
tree = {}

# This list will let us number the nodes  
# It has to be a list so we can access it inside the function
nodes = []
c=0
def id3(data, target, columns, tree):
    unique_targets = pandas.unique(data[target])
    # Assign the number key to the nodes list
    nodes.append(len(nodes) + 1)
    tree["number"] = nodes[-1]

    if len(unique_targets) == 1:
        # Insert code here that assigns the "label" field to the nodes list
        if 0 in unique_targets:
            tree['label']=0
        elif 1 in unique_targets:
            tree['label']=1
        return
    
    best_column = find_best_column(data, target, columns)
    column_median = data[best_column].median()
    tree['column']=best_column
    tree['median']=column_median
    # c+=1
    # tree['number']=c
    # Insert code here that assigns the "column" and "median" fields to the nodes list
    
    left_split = data[data[best_column] <= column_median]
    right_split = data[data[best_column] > column_median]
    split_dict = [["left", left_split], ["right", right_split]]
    
    for name, split in split_dict:
        tree[name] = {}
        id3(split, target, columns, tree[name])

# Call the function on our data to set the counters properly
id3(data, "high_income", ["age", "marital_status"], tree)

## 8. Printing Labels for a More Attractive Tree ##

def print_with_depth(string, depth):
    # Add space before a string
    prefix = "    " * depth
    # Print a string, and indent it appropriately
    print("{0}{1}".format(prefix, string))
    
    
def print_node(tree, depth):
    # Check for the presence of "label" in the tree
    if "label" in tree:
        # If found, then this is a leaf, so print it and return
        print_with_depth("Leaf: Label {0}".format(tree["label"]), depth)
        # This is critical -- without it, you'll get infinite recursion
        return
    # Print information about what the node is splitting on
    print_with_depth("{0} > {1}".format(tree["column"], tree["median"]), depth)
    
    # Create a list of tree branches
    branches = [tree["left"], tree["right"]]
        
    # Insert code here to recursively call print_node on each branch
    # Don't forget to increment depth when you pass it in
    depth+=1
    for tree in branches:
        print_node(tree,depth)

print_node(tree, 0)

## 10. Making Predictions Automatically ##

def predict(tree, row):
    if "label" in tree:
        return tree["label"]
    
    column = tree["column"]
    median = tree["median"]
    
    if (row[column]<=median):
        return predict(tree['left'],row)
    
    elif (row[column]>median):
        return predict(tree['right'],row)
    
    
    # Insert code here to check whether row[column] is less than or equal to median
    # If it's less than or equal, return the result of predicting on the left branch of the tree
    # If it's greater, return the result of predicting on the right branch of the tree
    # Remember to use the return statement to return the result!

# Print the prediction for the first row in our data
print(predict(tree, data.iloc[0]))

## 11. Making Multiple Predictions ##

new_data = pandas.DataFrame([
    [40,0],
    [20,2],
    [80,1],
    [15,1],
    [27,2],
    [38,1]
    ])
# Assign column names to the data
new_data.columns = ["age", "marital_status"]

def batch_predict(tree, df):
    # Insert your code here
    l=[]
    print(df)
    for a in range(len(df)):
        # df1=pandas.DataFrame(a)
        print(df.iloc[a,:])
        l.append(predict(tree,df.iloc[a,:]))
        
    return pandas.Series(l)

predictions = batch_predict(tree, new_data)