import streamlit as st
import pandas as pd

# Title for the app
st.title("Delhi Metro Trip Analysis")

# To load the cleaned csv file
data = pd.read_csv("cleaned_data.csv")  
st.write("Data preview:", data.head())

# User can select the Station names
From_Station = st.selectbox("Select a station", data['From_Station'].unique())
To_Station= st.selectbox("Select a station", data['To_Station'].unique())
filtered_data = data[(data['From_Station'] == From_Station) & (data['To_Station'] == To_Station)]
st.write(f"Trips from {From_Station} to {To_Station}:", filtered_data)


# Total passengers per day
passengers_per_day = filtered_data.groupby('Date')['Passengers'].sum()
st.line_chart(passengers_per_day)


# Dropdown to select a remark
selected_remark = st.selectbox("Select a Remark", data['Remarks'].dropna().unique())

# Filter data by selected remark
filtered_by_Remark = data[data['Remarks'] == selected_remark]
st.write(f"Trips with remark '{selected_remark}':", filtered_by_Remark)

# Dropdown to select Ticket_type
selected_ticket_type=st.selectbox("Select a Ticket type",data['Ticket_Type'].dropna().unique())

# Filter data by select ticket type
filtered_by_ticket_type = data[data['Ticket_Type']== selected_ticket_type]
st.write(f"Trips with Ticket type '{selected_ticket_type}':",filtered_by_ticket_type)

# Convert 'Date' column to datetime
data['Date'] = pd.to_datetime(data['Date'], errors='coerce')

# Date input for the user
search_date = st.date_input("Search trips by Date")

# Filter by date
if search_date:
    filtered_by_date = data[data['Date'] == pd.to_datetime(search_date)]
    st.write(f"Trips on {search_date}:", filtered_by_date)

# Number input for TripID
search_tripid = st.number_input("Search trips by TripID")

# Filter by TripID
if search_tripid:
    filtered_by_tripid = data[data['TripID'] == search_tripid]
    st.write(f"Trip with TripID '{search_tripid}':", filtered_by_tripid)