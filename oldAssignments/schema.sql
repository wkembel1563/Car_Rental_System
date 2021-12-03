CREATE TABLE CUSTOMER
(
  CustID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  Name 		VARCHAR(20) 	NOT NULL,
  Phone 	CHAR(14) 	NOT NULL
);

CREATE TABLE RENTAL
(
  CustID	INTEGER 	NOT NULL,
  VehicleID 	VARCHAR(20) 	NOT NULL,
  StartDate 	DATE,
  OrderDate 	DATE,
  RentalType 	INTEGER 	, 
  Qty 		INTEGER,
  ReturnDate 	DATE,
  TotalAmount 	INTEGER, 
-- (constraint here to check total is derived correctly)
  PaymentDate 	DATE,

  FOREIGN KEY(CustID) 		REFERENCES CUSTOMER(CustID),
  FOREIGN KEY(VehicleID) 	REFERENCES VEHICLE(VehicleID)
);

CREATE TABLE VEHICLE
(
  VehicleID 	VARCHAR(20) 	NOT NULL,
  Description 	VARCHAR(50),
  Year 		INTEGER,
  Type 		INTEGER,
  Category 	INTEGER,

  PRIMARY KEY(VehicleID)
);

CREATE TABLE RATE
(
  Type 		INTEGER 	NOT NULL,
  Category 	INTEGER		NOT NULL, 
  Weekly	INTEGER		NOT NULL,
  Daily 	INTEGER		NOT NULL, 

  PRIMARY KEY(Type, Category)
);

