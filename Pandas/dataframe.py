import pandas as pd
# create DataFrame From dictionary
cars = {
       'Brand' : ['Honda' , 'Toyoto' , 'Ford' , 'Audi'],
       'Price' : [22000 ,25000 , 27000 , 35000]
    }

df = pd.DataFrame(cars)
print(df);

# creating dataframe from list

names = list(map(str , input().split()))
age = list(map(int , input().split()))

de = pd.DataFrame(list(zip(names , age)) , columns = ['Name' , 'Age'])
print(de)

#create a blank dataframe

blank = pd.DataFrame
print(blank)
