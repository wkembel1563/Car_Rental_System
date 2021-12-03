/* ATTRIBUTE - DATE TYPE - CONSTRAINT*/ 

CREATE TABLE Player
(
	id 		INTEGER 	NOT NULL,
	team_id 	INTEGER 	NOT NULL, 
	name 		VARCHAR(30) 	NOT NULL, 
	position 	VARCHAR(30), 
	skill_level 	INTEGER, 
	salary 		INTEGER, 

	/* Constraints */ 	
	PRIMARY KEY(id), 
	UNIQUE(name), 
	FOREIGN KEY(team_id) REFERENCES Team (id)
); 

CREATE TABLE Team
(
	id INTEGER NOT NULL,
	name VARCHAR(30) NOT NULL,
	city VARCHAR(30) NOT NULL,
	coach VARCHAR(30) NOT NULL,
	/* uses name player name as foreign key*/
	captain,

	/* Constraints */
	PRIMARY KEY(id),
	FOREIGN KEY(captain) REFERENCES Player (name)

);

CREATE TABLE Game
(
	game_id		INTEGER		NOT NULL, 
	host_id		INTEGER		NOT NULL, 
	guest_id	INTEGER		NOT NULL, 
	host_score	INTEGER, 
	guest_score	INTEGER, 
	/* Date will autoconvert to correct format from csv file */ 
	game_date	date, 

	/* Constraints */ 
	PRIMARY KEY(game_id), 
	FOREIGN KEY(host_id) REFERENCES Team (team_id), 
	FOREIGN KEY(guest_id) REFERENCES Team (team_id) 
); 

CREATE TABLE Injury
(
	injury_id INTEGER NOT NULL,
	player_id INTEGER NOT NULL,
	incident_description VARCHAR(255),
	injury_description VARCHAR (255),

	/* Constraints */
	PRIMARY KEY(id),
	FOREIGN KEY(player_id) REFERENCES Team(team_id)
);
