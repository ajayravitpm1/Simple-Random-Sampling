#Problem:Hospital_Staffs

#importing pandas library to use the function read_csv() to open and store the file in an object
import pandas as pd
#data=pd.read_csv("File_location\Hospital_staffs.csv")
data=pd.read_csv("File_location\Hospital_staffs.csv")
#store the names in a list
#list(data[column_name])
l=list(data["Name List"])
print(l)

#importing random library to generate a random sample
#random.sample(sequential data,required sample size)
import random
r=random.sample(l,500)
print(r)
#converting list of sample to dataframe inorder to create csv file of names of random staffs
r=pd.DataFrame(r)
#using to_csv() function to create csv file
r.to_csv("File_location\File_name.csv")
