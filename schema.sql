CREATE DATABASE delhi_metro_travel;
USE delhi_metro_travel;
CREATE TABLE cleaned_data (
    TripID INT,
    Date DATE,
    From_Station VARCHAR(100),
    To_Station VARCHAR(100),
    Distance_km FLOAT,
    Fare FLOAT,
    Cost_per_passenger FLOAT,
    Passengers INT,
    Ticket_Type VARCHAR(50),
    Remarks VARCHAR(255)
);