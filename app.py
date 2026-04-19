import streamlit as st
import pandas as pd
import mysql.connector

# Title for the app
st.title("Delhi Metro Trip Analysis")

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Bellajoshua@04",   # replace this
    database="delhi_metro_travel"
)

# To load the cleaned csv file
data = pd.read_csv("cleaned_data.csv")  
st.write("Data preview:", data)

section = st.sidebar.selectbox(
    "Choose Section",
    ["Route Analysis", "Station Analysis", "Revenue Analysis", "Passenger Analysis", "Travel Pattern Analysis"]
)

if section == "Route Analysis":
    option = st.selectbox(
        "Choose a query for Route Analysis",
        ["Route with highest passenger traffic", 
         "Routes generating highest total revenue",
          "Average fare for each route",
           "Routes having longest travel distances" ]
    )
elif section == "Station Analysis":
    option = st.selectbox(
        "Choose a query for Station Analysis",
        ["Highest number of trip departures", 
         "Highest number of passengers",
         "Top 10 most frequently used metro stations",
         "Station pairs are most frequently used for travel"
         ]
    )
elif section == "Revenue Analysis":
    option = st.selectbox(
        "Choose a query for Revenue Analysis",
        ["Total revenue generated from all trips", 
         "Average fare per trip",
         "Routes generating the highest revenue per kilometer",
         "Ticket type that generates the highest revenue"
         ]
    )
elif section == "Passenger Analysis":
    option = st.selectbox(
        "Choose a query for Passenger Analysis",
        ["Average number of passengers per trip", 
         "Trips recorded the highest passenger counts",
         "Passenger distribution by ticket type",
         "Total passenger count for each station"
         ]
    )
elif section == "Travel Pattern Analysis":
    option = st.selectbox(
        "Choose a query for Travel Pattern Analysis",
        ["Trips occured during peak, off-peak, festival, and weekend conditions", 
         "Travel condition generating the highest revenue",
         "The monthly passenger trend across the dataset",
         "Travel condition that has the highest average passenger count per trip"
         ]
    )
# --------------Route Analyis-------------

if option == "Route with highest passenger traffic":
    query = """
    SELECT From_Station, To_Station,
    SUM(Passengers) AS Total_Passengers
    FROM cleaned_data
    GROUP BY From_Station, To_Station
    ORDER BY Total_Passengers DESC;
    """

elif option == "Routes generating highest total revenue":
    query = """
   SELECT  To_Station, SUM(Passengers) AS Total_Passengers
    FROM cleaned_data
    GROUP BY To_Station
    ORDER BY Total_Passengers DESC;
    """

elif option == "Average fare for each route":
    query = """
    SELECT From_Station, To_Station, ROUND(AVG(Fare),2) AS Avg_Fare
    FROM cleaned_data
    GROUP BY From_Station, To_Station;
    """

elif option == "Routes having longest travel distances":
    query = """
    SELECT From_Station, To_Station, MAX(Distance_km) AS Max_Distance
    FROM cleaned_data
    GROUP BY From_Station, To_Station
    ORDER BY Max_Distance DESC;
    """

# -------- STATION ANALYSIS --------
if option == "Highest number of trip departures":
    query = """
   SELECT From_Station, count(*) AS Trip_Departures
    FROM cleaned_data
    GROUP BY From_Station
    ORDER BY Trip_Departures DESC; 
    """

elif option == "Passengers Received by Station":
    query = """
    SELECT To_Station, SUM(Passengers) AS Total_Passengers
    FROM cleaned_data
    GROUP BY To_Station
    ORDER BY Total_Passengers DESC;
    """

elif option == "Top 10 most frequently used metro stations":
    query = """
    SELECT Station, SUM(Total) AS Total_Passengers
    FROM (
        SELECT From_Station AS Station, SUM(Passengers) AS Total
        FROM cleaned_data GROUP BY From_Station
        UNION ALL
        SELECT To_Station AS Station, SUM(Passengers) AS Total
        FROM cleaned_data GROUP BY To_Station
    ) AS combined
    GROUP BY Station
    ORDER BY Total_Passengers DESC
    LIMIT 10;
    """

elif option == "Station pairs are most frequently used for travel":
    query = """
    SELECT LEAST(From_Station, To_Station) AS Station_A,
           GREATEST(From_Station, To_Station) AS Station_B,
           SUM(Passengers) AS Total_Passengers
    FROM cleaned_data
    GROUP BY Station_A, Station_B
    ORDER BY Total_Passengers DESC;
    """

# -------- REVENUE ANALYSIS --------
elif option == "Total revenue generated from all trips":
    query = """
    SELECT ROUND(SUM(Fare),2) AS Total_Fare  
    FROM cleaned_data;"""

elif option == "Average fare per trip":
    query ="""SELECT From_Station, To_Station, ROUND(AVG(Fare),2) AS Avg_Fare
    FROM cleaned_data
    GROUP BY From_Station, To_Station
    ORDER BY Avg_Fare;"""

elif option == "Routes generating the highest revenue per kilometer":
    query = """
    SELECT From_Station, To_Station,
    ROUND(SUM(Fare)/SUM(Distance_km),2) AS Revenue_per_km
    FROM cleaned_data
    GROUP BY From_Station, To_Station
    ORDER BY Revenue_per_km DESC;
    """

elif option == "Ticket type that generates the highest revenue":
    query = """
   SELECT
    Ticket_Type, COUNT(*) AS Total_Ticket_Type,
    ROUND(SUM(Fare),2) AS Total_Fare
    FROM cleaned_data
    GROUP BY Ticket_Type
    ORDER BY Total_Fare DESC;
    """

# -------- PASSENGER ANALYSIS --------
elif option == "Average number of passengers per trip":
    query = """
    SELECT ROUND(AVG(Passengers), 2) AS Avg_Passengers_Per_Trip
    FROM cleaned_data;"""

elif option == "Trips recorded the highest passenger counts":
    query = """
    SELECT TripID, SUM(Passengers) AS Total_Passengers
    FROM cleaned_data
    GROUP BY TripID
    ORDER BY Total_Passengers DESC;
    """

elif option == "Passenger distribution by ticket type":
    query = """
    SELECT Ticket_Type, SUM(Passengers) AS Passenger_distribution
    FROM cleaned_data
    GROUP BY Ticket_Type
    ORDER BY Passenger_distribution DESC;
    """

elif option == "Total passenger count for each station":
    query = """
    SELECT Station, SUM(Total) AS Total_Passengers
    FROM (
        SELECT From_Station AS Station, SUM(Passengers) AS Total
        FROM cleaned_data GROUP BY From_Station
        UNION ALL
        SELECT To_Station AS Station, SUM(Passengers) AS Total
        FROM cleaned_data GROUP BY To_Station
    ) AS combined
    GROUP BY Station
    ORDER BY Total_Passengers DESC;
    """

# -------- Travel Pattern Analysis  --------
elif option == "Trips occured during peak, off-peak, festival, and weekend conditions":
    query = """
    SELECT  Remarks, COUNT(DISTINCT TripID) AS Number_of_Trips
    FROM cleaned_data
    WHERE Remarks IN ('Peak', 'Off-Peak', 'Festival', 'Weekend')
    GROUP BY Remarks
    ORDER BY Number_of_Trips;
    """

elif option == "Travel condition generating the highest revenue":
    query = """
    SELECT Remarks, ROUND(SUM(Fare),2) AS Total_Fare
    FROM cleaned_data
    GROUP BY Remarks
    ORDER BY Total_Fare DESC;
    """

elif option == "The monthly passenger trend across the dataset":
    query = """
    SELECT DATE_FORMAT(Date, '%M %Y') AS Month,
        SUM(Passengers) AS Total_Passengers
    FROM cleaned_data
    GROUP BY Month
    ORDER BY MIN(Date);
        """

elif option == "Travel condition that has the highest average passenger count per trip":
    query = """
    SELECT  Remarks, 
    COUNT(*) AS Number_of_Trips,
    ROUND(AVG(Passengers),2) AS Avg_Passengers
    FROM cleaned_data
    GROUP BY Remarks
    ORDER BY Avg_Passengers DESC;
    """

df = pd.read_sql(query, conn)
st.write(df)

st.title("Ticket type analysis")
query = """
SELECT
    Ticket_Type, COUNT(*) AS Total_Ticket_Type,
    ROUND(SUM(Fare),2) AS Total_Fare
FROM cleaned_data
GROUP BY Ticket_Type
ORDER BY Total_Fare DESC;
"""
df = pd.read_sql(query, conn)
st.write(df)
st.bar_chart(df.set_index('Ticket_Type'))

st.title("Passenger trend in months and years")
query = """
    SELECT DATE_FORMAT(Date, '%y / %m') AS Month,
        SUM(Passengers) AS Total_Passengers
    FROM cleaned_data
    GROUP BY Month
    ORDER BY MIN(Date);"""
df = pd.read_sql(query, conn)
st.write(df)
st.line_chart(df.set_index('Month'))

# User can select the Station names
From_Station = st.selectbox("Select a station", data['From_Station'].unique())
To_Station= st.selectbox("Select a station", data['To_Station'].unique())
filtered_data = data[(data['From_Station'] == From_Station) & (data['To_Station'] == To_Station)]
st.write(f"Trips from {From_Station} to {To_Station}:", filtered_data)


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


