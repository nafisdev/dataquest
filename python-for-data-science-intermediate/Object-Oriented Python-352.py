## 3. Defining a Class ##

class MyClass:
    pass

## 4. Instantiating a Class ##

class MyClass:
    pass
        

        
my_instance=MyClass()
print(type(my_instance))
        

## 5. Creating Methods ##

class MyClass:
    def first_method():
        return "This is my first_method"
    
my_instance=MyClass()

## 6. Understanding "self'" ##

class MyClass:
    
    def first_method(self):
        return "This is my first method"
    
    def print_self(self):
        print(self)
    
my_instance = MyClass()
# my_instance.first_method()
print(my_instance.print_self())
print(my_instance)
result=my_instance.first_method()

## 7. Creating a Method that Accepts an Argument ##

class MyClass:
    
    def first_method(self):
        return "This is my first method"
   
    def return_list(self,input_list):
        return input_list
    
    # Add method here
    
my_instance=MyClass()
result=my_instance.return_list([1,2,3])

## 8. Attributes and the Init Method ##

class MyList:
    def __init__(self,initial_data):
        self.data=initial_data
        
my_list=MyList([1,2,3,4,5])

print(my_list.data)

## 9. Creating an Append Method ##

class MyList:

    def __init__(self, initial_data):
        self.data = initial_data
        
    # Add method here
    def append(self,new_item):
        self.data.append(new_item)
        
        
my_list=MyList([1,2,3,4,5])
print(my_list.data)
my_list.append(6)
print(my_list.data)
    

## 10. Creating and Updating an Attribute ##

class MyList:

    def __init__(self, initial_data):
        self.data = initial_data
        # Calculate the initial length
        self.length = 0
        for item in self.data:
            self.length += 1

    def append(self, new_item):
        self.data = self.data + [new_item]
        self.length+=1
        # Update the length here
        
my_list=MyList([1,1,2,3,5])
print(my_list.length)
my_list.append(8)
print(my_list.length)