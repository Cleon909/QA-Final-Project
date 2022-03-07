CREATE TABLE IF NOT EXISTS academics (
    id INTEGER NOT NULL AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    current_institution VARCHAR(30) DEFAULT 'unkown',
    field_of_study VARCHAR(150) DEFAULT 'unkown',
    PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS papers (
    id INTEGER NOT NULL AUTO_INCREMENT,
    title VARCHAR(200) NOT NULL,
    year_published INTEGER,
    field_of_study VARCHAR(150) DEFAULT 'unkown',
    PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS authors (
    id INTEGER NOT NULL AUTO_INCREMENT,
    academic_id INTEGER NOT NULL,
    paper_id INTEGER NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (academic_id) REFERENCES academics(id),
    FOREIGN KEY (paper_id) REFERENCES papers(id) 
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

LOCK TABLES `academics` AS t1 WRITE, `academics` AS t2 READ;
INSERT INTO `academics` SELECT * FROM(
			SELECT 1 a, 'Bob Dole' b, 'University of Bradford' c, 'Metaphysics' d UNION ALL
            SELECT 2, 'Gisela Joseph','Zombie College', 'Magic History' UNION ALL
            SELECT 3, 'Durga Van As', 'Unseen University', 'Foreign Life Gardening' UNION ALL
			SELECT 4, 'Nerva Augustus', 'University of Ithica', 'Hermetic Semiosis' UNION ALL
            SELECT 5, 'Antoninus Pius', 'GURPS Illuminati University', 'Illumanti History'UNION ALL
            SELECT 6, 'Narciso Baumann', 'Unseen University', 'English Literature' UNION ALL
			SELECT 7, 'Trajan Augustus', 'University of Bradford', 'Dutch Ethnic Etymology' UNION ALL
            SELECT 8, 'Captain Ahab','Zombie College', 'Hermetic Semiosis' UNION ALL
            SELECT 9, 'Luke Skywalker','Zombie College','Metaphysics' UNION ALL
            SELECT 10, 'Darth Vader', 'GURPS Illuminati University', 'Dutch Ethnic Etymology' UNION ALL
			SELECT 11, 'Luitenent Starbuck', 'Unseen University', 'Illumanti History' UNION ALL
            SELECT 12, 'Marcus Aurelius', 'University of Bradford', 'Hermetic Semiosis' UNION ALL
            SELECT 13, 'Hadrian Augustus', 'GURPS Illuminati University', 'Dutch Ethnic Etymology' UNION ALL
            SELECT 14, 'Hector Salamancis', 'Unseen University', 'Foreign Life Gardening' UNION ALL
			SELECT 15, 'Noble Johnson', 'Starfleet Academy', 'English Literature' UNION ALL
            SELECT 16, 'Augustus Ceaser', 'University of Ithica', 'Dutch Ethnic Etymology' UNION ALL
            SELECT 17, 'Heracleus Ceaser','Zombie College', 'Illumanti History' UNION ALL
            SELECT 18, 'Count Belisarius', 'Unseen University', 'Magic History' UNION ALL
			SELECT 19, 'Cyrus The Great', 'Starfleet Academy', 'South Carribean Semiotics' UNION ALL
            SELECT 20, 'Scipio Africanus', 'University of Ithica', 'Foreign Life Gardening') data
WHERE NOT EXISTS (SELECT NULL
					FROM academics AS t2);
UNLOCK TABLES;
		


LOCK TABLES `papers` AS t1 WRITE, `papers` AS t2 READ;
INSERT INTO `papers` SELECT * FROM(
SELECT 1 a, 'Nihilism and dialectic appropriation' b, 1985 c, 'Advanced Semiotics' d UNION ALL 
SELECT 2, 'Marxist capitalism in the works of Gaiman', 2020, 'The Occult' UNION ALL
SELECT 3, 'Bob Diamond and Metasemiotics in Finance', 2010, 'Computer Science and Etymology' UNION ALL
SELECT 4, 'Postpatriarchial libertarianism in the works of Glass', 1999, 'Music and the Movement of the Spheres' UNION ALL
SELECT 5, 'Reinventing Constructivism: Modernism in the works of Eco', 2018, 'Semiotics and history of Evolution' UNION ALL
SELECT 6, 'A Biography of Eric "Eazy-E" Wright', 1998, 'Biography as the Expression of Power' UNION ALL
SELECT 7, 'The Principle Knowledge That God Is Omniscience', 2022, 'Mathematics of the Celestial Heavens' UNION ALL
SELECT 8, 'An Introduction to the Analysis of Theological Task', 2020, 'Ancient Astronauts' UNION ALL
SELECT 9, 'Precapitalist constructivist theory and postdeconstructive appropriation', 2006, 'Creationist Cosmologies' UNION ALL
SELECT 10, 'Precapitalist dematerialism and constructivism', 1970, 'The Occult' UNION ALL
SELECT 11, 'Sartreist absurdity in the works of Gaiman', 1696, 'Advanced Semiotics' UNION ALL
SELECT 12, 'Examining the QCD Law in Models of Monopoles: Firewalls', 1066, 'Creationist Cosmologies' UNION ALL
SELECT 13, 'Reflexive tactics for algebra, revisited', 1453, 'Ancient Astronauts' UNION ALL
SELECT 14, 'Evolution of SASyLF 2008-2021', 453, 'Biography as the Expression of Power' UNION ALL
SELECT 15, 'Bunched Fuzz: Sensitivity for Vector Metrics', 2001, 'Biography as the Expression of Power' UNION ALL
SELECT 16, 'Worlds of the Phaedo and the Term', 1875, 'Biography as the Expression of Power' UNION ALL
SELECT 17, 'Dark Spirituality as a Symbol Female', 1930, 'Creationist Cosmologies' UNION ALL
SELECT 18, 'Which can Jump Highe, a Car Flea of a Dog Flea?', 2010, 'Music and the Movement of the Spheres' UNION ALL
SELECT 19, 'Do Woodpeckers get Headaches?', 2006, 'Mathematics of the Celestial Heavens' UNION ALL
SELECT 20, 'The propulsion Paramters of Penguin Poop', 2008, 'Ancient Astronauts') data
WHERE NOT EXISTS (SELECT NULL
					FROM `papers` AS t2);
UNLOCK TABLES;

LOCK TABLES `authors` AS t1 WRITE, `authors` AS t2 READ;
INSERT INTO `authors` SELECT * FROM(
SELECT 1 a, 1 b, 7 c UNION ALL 
SELECT 2, 2, 7 UNION ALL
SELECT 3, 3, 5 UNION ALL
SELECT 4, 4, 3 UNION ALL
SELECT 5, 5, 19 UNION ALL
SELECT 6, 6, 9 UNION ALL
SELECT 7, 7, 8 UNION ALL
SELECT 8, 8, 4 UNION ALL
SELECT 9, 9, 20 UNION ALL
SELECT 10, 10, 19 UNION ALL
SELECT 11, 11, 18 UNION ALL
SELECT 12, 12, 17 UNION ALL
SELECT 13, 13, 16 UNION ALL
SELECT 14, 14, 15 UNION ALL
SELECT 15, 15, 14 UNION ALL
SELECT 16, 16, 13 UNION ALL
SELECT 17, 17, 12 UNION ALL
SELECT 18, 12, 11 UNION ALL
SELECT 19, 19, 10 UNION ALL
SELECT 20, 20, 9 UNION ALL
SELECT 21, 2, 8 UNION ALL
SELECT 22, 18, 7 UNION ALL
SELECT 23, 4, 6 UNION ALL
SELECT 24, 7, 5 UNION ALL
SELECT 25, 12, 4 UNION ALL
SELECT 26, 20, 3 UNION ALL
SELECT 27, 1, 2 UNION ALL
SELECT 28, 4, 1) data
WHERE NOT EXISTS (SELECT NULL 
	FROM authors AS t2 );
UNLOCK TABLES