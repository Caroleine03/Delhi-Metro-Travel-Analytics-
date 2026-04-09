SELECT * FROM delhi_metro_travel.cleaned_data;

# Route Analysis

# Which metro routes have the highest passenger traffic?
SELECT From_Station, To_Station,
SUM(Passengers) AS Total_Passengers
FROM cleaned_data
GROUP BY From_Station, To_Station
ORDER BY Total_Passengers DESC;

# Which routes generate the highest total revenue?
SELECT From_Station, To_Station, ROUND(SUM(Fare),2) AS Total_Fare
FROM cleaned_data
GROUP BY From_Station, To_Station
ORDER BY Total_Fare DESC;

# What is the average fare for each route?
SELECT From_Station, To_Station, ROUND(AVG(Fare),2) AS Avg_Fare
FROM cleaned_data
GROUP BY From_Station, To_Station;

# Which routes have the longest travel distances?
SELECT From_Station, To_Station, MAX(Distance_km) AS Max_Distance
FROM cleaned_data
GROUP BY From_Station, To_Station
ORDER BY Max_Distance DESC;

# Station Analysis

# Which stations have the highest number of trip departures?
SELECT From_Station, count(*) AS Trip_Departures
FROM cleaned_data
GROUP BY From_Station
ORDER BY Trip_Departures DESC; 

# Which stations receive the highest number of passengers?
SELECT  To_Station, SUM(Passengers) AS Total_Passengers
FROM cleaned_data
GROUP BY To_Station
ORDER BY Total_Passengers DESC;

# What are the top 10 most frequently used metro stations?
SELECT Station, SUM(Total) AS Total_Usage
FROM (
    SELECT From_Station AS Station, SUM(Passengers) AS Total
    FROM cleaned_data
    GROUP BY From_Station
    
    UNION ALL
    
    SELECT To_Station AS Station, SUM(Passengers) AS Total
    FROM cleaned_data
    GROUP BY To_Station
) AS combined
GROUP BY Station
ORDER BY Total_Usage DESC
LIMIT 10;

# Which station pairs are most frequently used for travel?
SELECT 
    LEAST(From_Station, To_Station) AS Station_A,
    GREATEST(From_Station, To_Station) AS Station_B,
    SUM(Passengers) AS Total_Passengers
FROM cleaned_data
GROUP BY Station_A, Station_B
ORDER BY Total_Passengers DESC;

# Revenue Analysis

# What is the total revenue generated from all trips?
SELECT ROUND(SUM(Fare),2) AS Total_Fare
FROM cleaned_data;

#  What is the average fare per trip?
SELECT From_Station, To_Station, ROUND(AVG(Fare),2) AS Avg_Fare
FROM cleaned_data
GROUP BY From_Station, To_Station
ORDER BY Avg_Fare;

# Which routes generate the highest revenue per kilometer?
SELECT From_Station, To_Station, ROUND(SUM(Fare)/SUM(Distance_km),2) AS Revenue_per_km
FROM cleaned_data
GROUP BY From_Station, To_Station
ORDER BY Revenue_per_km DESC;

# Which ticket type generates the highest revenue?
SELECT
 Ticket_Type, COUNT(*) AS Total_Ticket_Type,
 ROUND(SUM(Fare),2) AS Total_Fare
 FROM cleaned_data
 GROUP BY Ticket_Type
 ORDER BY Total_Fare DESC;
 
 # Passenger Analysis
 
 # What is the average number of passengers per trip?
 SELECT ROUND(AVG(Passengers), 2) AS Avg_Passengers_Per_Trip
 FROM cleaned_data;

#Which trips recorded the highest passenger counts?
SELECT TripID, 
 SUM(Passengers) AS Total_Passengers
 FROM cleaned_data
 GROUP BY TripID
 ORDER BY Total_Passengers DESC;
 
 # What is the passenger distribution by ticket type? 
 SELECT Ticket_Type, SUM(Passengers) AS Passenger_distribution
 FROM cleaned_data
 GROUP BY Ticket_Type
 ORDER BY Passenger_distribution DESC;

# What is the total passenger count for each station?
SELECT Station, SUM(Total) AS Total_Passengers
FROM (
    SELECT From_Station AS Station, SUM(Passengers) AS Total
    FROM cleaned_data
    GROUP BY From_Station
    
    UNION ALL
    
    SELECT To_Station AS Station, SUM(Passengers) AS Total
    FROM cleaned_data
    GROUP BY To_Station
) AS combined
GROUP BY Station
ORDER BY Total_Passengers DESC;

# How many trips occur during peak, off-peak, festival, and weekend conditions?
SELECT  Remarks, COUNT(DISTINCT TripID) AS Number_of_Trips
FROM cleaned_data
WHERE Remarks IN ('Peak', 'Off-Peak', 'Festival', 'Weekend')
GROUP BY Remarks
ORDER BY Number_of_Trips;

# Which travel condition generates the highest revenue?
SELECT Remarks, ROUND(SUM(Fare),2) AS Total_Fare
FROM cleaned_data
GROUP BY Remarks
ORDER BY Total_Fare DESC;

# What is the monthly passenger trend across the dataset?
SELECT DATE_FORMAT(Date, '%M %Y') AS Month,
       SUM(Passengers) AS Total_Passengers
FROM cleaned_data
GROUP BY Month
ORDER BY MIN(Date);

# Which travel condition has the highest average passenger count per trip?
SELECT  Remarks, 
COUNT(*) AS Number_of_Trips,
ROUND(AVG(Passengers),2) AS Avg_Passengers
FROM cleaned_data
GROUP BY Remarks
ORDER BY Avg_Passengers DESC;