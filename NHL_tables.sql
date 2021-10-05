/* ATTRIBUTE - DATE TYPE - CONSTRAINT*/ 

CREATE TABLE Player
(
	id 		INTEGER 	NOT NULL,
	team_id 	INTEGER 	NOT NULL, 
	name text 	VARCHAR(20) 	NOT NULL, 
	position 	VARCHAR(20), 
	skill_level 	INTEGER, 
	salary 		INTEGER, 

	/* Constraints */ 	
	PRIMARY KEY(id), 
	UNIQUE(name), 
	FOREIGN KEY(team_id) REFERENCES Team (id)
); 

CREATE TABLE Team
(
	id, 
	name, 
	city, 
	coach, 
	/* uses name player name as foreign key*/ 
	captain, 

	/* Constraints */  
	PRIMARY KEY(id), 
	FOREIGN KEY(captain) REFERENCES Player (name)

); 

CREATE TABLE Game
(
	game_id, 
	host_id, 
	guest_id, 
	host_score, 
	guest_score, 
      /* need to convert excel date (dd-mm-yyyy) to sql date (yyyy-mm-dd)
	game_date, 

	/* Constraints */ 
	PRIMARY KEY(game_id), 
	FOREIGN KEY(host_id) REFERENCES Team (team_id), 
	FOREIGN KEY(guest_id) REFERENCES Team (team_id) 
); 

CREATE TABLE Injury
(
	injury_id, 
	player_id, 
	incident_description, 
	injury_description, 

	/* Constraints */ 
	PRIMARY KEY(id), 
	FOREIGN KEY(player_id) REFERENCES Team(team_id)
); 
