import pandas as pd
import numpy as np

#EX1:
data=pd.read_csv('Automobile_data.csv')
x=data.iloc[:5]
print(x)
x=data.iloc[-5:]
print(x)

#EX2:
data.replace('?', 0)
data.replace('n.a', 0)
data.replace(np.NAN, 0)
print(data)

#EX3:
print(data[data.price == data.price.max()])

#EX4:
T = file.loc[file['company'] == "toyota" ]
T

#EX5
stats = df.groupby(['company']).size().sort_values(ascending = False)
stats

#EX6
price = file[['company','price']].groupby(['company']).max
price

#EX7
avg = df[['company','average-mileage']].groupby(['company']).mean()
avg

#EX8
up = file.sort_values('price' , ascending = True)
up = up.haid()

#EX9
s1 = pd.DataFrame({'Company': ['Ford', 'Mercedes', 'BMV', 'Audi'], 'Price': [23845, 171995, 135925 , 71400]})
s2= pd.DataFrame({'Company': ['Toyota', 'Honda', 'Nissan', 'Mitsubishi '], 'Price': [29995, 23600, 61500 , 58900]})

s = [s1 ,s2]
result = pd.concat(s)
print(result)

#EX10
Car_Price = pd.DataFrame({'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'Price': [23845, 17995, 135925 , 71400]})
car_Horsepower = pd.DataFrame({'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'horsepower': [141, 80, 182 , 160]})

result = pd.merge(Car_Price, car_Horsepower)
