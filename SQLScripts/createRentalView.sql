CREATE VIEW vRentalInfo 
(OrderDate,	StartDate,	ReturnDate,	TotalDays, 
  VIN,		Vehicle,	Type,		Category, 
  CustomerID, 	CustomerName, OrderAmount, RentalBalance)
 
AS

Select OrderDate, StartDate, ReturnDate, 
	CASE	WHEN RentalType = 1 THEN Qty 
		 	WHEN RentalType = 7 THEN Qty * 7 
	END 	AS 'TotalDays',

	VehicleID, Description, 

	CASE 	WHEN Type = 1 THEN "Compact"
			WHEN Type = 2 THEN "Medium"
			WHEN Type = 3 THEN "Large"
			WHEN Type = 4 THEN "SUV"
			WHEN Type = 5 THEN "Truck"
			WHEN Type = 6 THEN "VAN"
	END 	AS 'Type', 

	CASE 	WHEN Category = 0 THEN "Basic"
			WHEN Category = 1 THEN "Luxury"
	END 	AS 'Category', 

	CustID, Name, TotalAmount, 

	CASE 	WHEN Returned = 0 THEN TotalAmount ELSE 0 
	END 	AS 'RentalBalance'
FROM ((CUSTOMER NATURAL JOIN RENTAL) NATURAL JOIN VEHICLE)
ORDER BY startdate asc;
