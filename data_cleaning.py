import pandas as pd

#Loads the JSON dataset into a pandas Dataframe.
data= pd.read_json ('C:/Users/joshu/Downloads/delhi_metro_trips.json')

#Displays dataset in table format.
print(data)

#To show all the columns in the dataset
print(data.columns)

#to find data types and missing value in the dataset.
data.info()

#To get the statistical summary of the numerical values in the dataset and round off to 2 digits after decimal
print(data.describe().round(2))

#To get the statistical summary of individual columns
print(data['Distance_km'].describe())

#To find the number of negative values in column(Fare, Cost_per_passenger, Passengers, TripID)
print((data['Distance_km']<0).sum())

#To find missing values in the multiple coulmns
print(data[['TripID', 'Date', 'From_Station', 'To_Station', 'Distance_km', 'Fare',
       'Cost_per_passenger', 'Passengers', 'Ticket_Type', 'Remarks']].isnull().sum())

#To remove extra space after the From_Station and To_Station
data['From_Station'] = data['From_Station'].str.strip()
data['To_Station'] = data['To_Station'].str.strip()

#To find the number of missing values in the coulmns
print(data.isnull().sum())


#To find the null rows in the passengers
missing_rows_Passengers = data[data['Passengers'].isnull()]
print(missing_rows_Passengers)

#To Find the median of the Passengers and fill the median in the null rows
print(f'The median of Passengers: {data['Passengers'].median()}')
data['Passengers'] = data['Passengers'].fillna(data['Passengers'].median())

#To check if the median is filled in the null rows
print(data.iloc[[342,543,9778]])
print(f'The number of missing rows in Passengers column are: {data['Passengers'].isnull().sum()}')


#To find missing values in Ticket_Type
missing_rows_Ticket_Type = data[data['Ticket_Type'].isnull()]
print(missing_rows_Ticket_Type)

#To replace the missing values in the Ticket_Type
data['Ticket_Type']= data['Ticket_Type'].fillna('unknown')

#To check if the unknown is filled in the null rows
print(data.iloc[[94,112,9834]])
print(f'The number of missing rows in Ticket_Type column are: {data['Ticket_Type'].isnull().sum()}')


#To find the missing rows in Remarks
missing_rows_Remarks=data[data['Remarks'].isnull()]
print(missing_rows_Remarks)

#To replace the missing rows in Remarks
data['Remarks']=data['Remarks'].fillna('No Remarks')

#To check if the No Remarks is filled in the null rows
print(data.iloc[[5,33,112]])
print(f'The number of missing rows in Remaks: {data['Remarks'].isnull().sum()}')

#To make the 1st letter captial of the From_Station and check 
data['From_Station'] = data['From_Station'].str.replace(r'\s+', ' ', regex=True).str.title()
print(data['From_Station'].str.contains(r'\s{2,}', regex=True).any())

#To make the 1st letter captial of the To_Station and check 
data['To_Station'] = data['To_Station'].str.strip().str.replace(r'\s+', ' ', regex=True).str.title()
print(data['To_Station'].str.contains(r'\s{2,}', regex=True).any())

#To find the rows where the From_Station name and To_Station name are the same
print((data['From_Station'] == data['To_Station']).sum())

#To remove the rows where the From_Station name and To_Station name are the same and check
data = data[data['From_Station'] != data['To_Station']]
print((data['From_Station'] == data['To_Station']).sum())

#To convert Date column to datetime format
data['Date'] = pd.to_datetime(data['Date'], errors='coerce')
print(data['Date'])
print(data['Date'].isnull().sum())
print(data['Date'].dtype)


#To check the numbers after decimal are round off to 2 digits
invalid_Cost_per_passenger = data[data['Cost_per_passenger'] != data['Cost_per_passenger'].round(2)]
print(f'The number of data that do not have 2 digits after decimal: {len(invalid_Cost_per_passenger)}')

#To round off the numbers to 2 digits after decimal and check
data['Cost_per_passenger'] = data['Cost_per_passenger'].round(2)

invalid_Cost_per_passenger = data[data['Cost_per_passenger'] != data['Cost_per_passenger'].round(2)]

print(f'The number of data that do not have 2 digits after decimal:  {len(invalid_Cost_per_passenger) }')

#To check the numbers after decimal are round off to 2 digits in Distance_km
invalid_Distance_km = data[data['Distance_km'] != data['Distance_km'].round(2)]
print(f'The number of data that do not have 2 digits after decimal: { len(invalid_Distance_km)}')

#To round off the numbers to 2 digits after decimal and check for Distance_km
data['Distance_km'] = data['Distance_km'].round(2)
invalid_Distance_km = data[data['Distance_km'] != data['Distance_km'].round(2)]
print(f'The number of data that do not have 2 digits after decimal:  {len(invalid_Distance_km)}')


print(data.iloc[[112,543,9834]]) 

#To change the json file to csv
data.to_csv('cleaned_data.csv',index=False)

#To find the path of csv file
import os
print(os.getcwd())












