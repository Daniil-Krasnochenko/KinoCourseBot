-- Создаём базу данных
DROP DATABASE IF EXISTS kinocourse;
CREATE DATABASE kinocourse;
USE kinocourse;

-- таблица звёзд (актёров, режиссёров и т. д.)
DROP TABLE IF EXISTS persons;
CREATE TABLE persons (
	id SERIAL PRIMARY KEY,
	firstname varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL,
	lastname varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL
); 

-- таблица профиля звёзд
DROP TABLE IF EXISTS person_profiles;
CREATE TABLE person_profiles (
	actor_id BIGINT UNSIGNED NOT NULL UNIQUE,
	FOREIGN KEY (actor_id) REFERENCES persons(id),
	career varchar(100) NOT NULL,
	height DOUBLE UNSIGNED NOT NULL,
	birthday DATE NOT NULL,
	zodiak VARCHAR(10) NOT NULL,
	birthplace varchar(50) NOT NULL,
	genres varchar(50) NOT NULL,
	filmscount SMALLINT UNSIGNED NULL,
	photo_id BIGINT UNSIGNED NULL,
	gender char(1) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL
); 

-- таблица фильмов
DROP TABLE IF EXISTS films;
CREATE TABLE films (
	id SERIAL PRIMARY KEY,
	name varchar(50) NULL
);

-- таблица профиля фильма
DROP TABLE IF EXISTS film_profiles;
CREATE TABLE film_profiles (
	film_id BIGINT UNSIGNED NOT NULL UNIQUE,
	FOREIGN KEY (film_id) REFERENCES films(id),
	original_title varchar(50) NULL,
	photo_id bigint unsigned NULL,
	rate DOUBLE UNSIGNED NULL,
	`release` YEAR NULL,
	country varchar(50) NULL,
	slogan varchar(100) NULL,
	runtime TIME NULL,
	certificate TINYINT UNSIGNED NULL COMMENT 'возрастные ограничения'
);

-- таблица подробной информации фильма
DROP TABLE IF EXISTS film_details;
CREATE TABLE film_details (
	film_id BIGINT UNSIGNED NOT NULL UNIQUE,
	FOREIGN KEY (film_id) REFERENCES films(id),
	writers varchar(100) NULL,
	produced_by varchar(100) NULL,
	operator varchar(100) NULL,
	composer varchar(100) NULL,
	designer varchar(100) NULL,
	editor varchar(100) NULL,
	budget BIGINT UNSIGNED NULL,
	gross_US BIGINT UNSIGNED NULL,
	gross_worldwide BIGINT UNSIGNED NULL
);

-- таблица профилей сериалов
DROP TABLE IF EXISTS serials_profiles;
CREATE TABLE serials_profiles (
	film_id BIGINT UNSIGNED NOT NULL UNIQUE,
	FOREIGN KEY (film_id) REFERENCES films(id),
	original_title varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL,
	photo_id bigint unsigned NULL,
	rate double unsigned NULL,
	seasons_count TINYINT NULL,
	`release` year NULL,
	country varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL,
	slogan varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL,
	runtime time NULL
);

-- таблица пользователей сайта
DROP TABLE IF EXISTS users;
CREATE TABLE users (
	id SERIAL PRIMARY KEY,
	firstname varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL,
	lastname varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL,
	email varchar(120) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL,
	phone BIGINT UNSIGNED NULL
);

-- таблица профиля пользователей сайта
DROP TABLE IF EXISTS user_profiles;
CREATE TABLE user_profiles (
	user_id BIGINT UNSIGNED NOT NULL UNIQUE,
	FOREIGN KEY (user_id) REFERENCES users(id),
	gender char(1) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL,
	birthday date NULL,
	photo_id bigint unsigned NULL,
	created_at datetime DEFAULT CURRENT_TIMESTAMP NULL,
	hometown varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL,
	interesting varchar(100) NULL,
	about varchar(100) NULL,
	website varchar(50) NULL
);

-- таблица наград фильмов
DROP TABLE IF EXISTS awards;
CREATE TABLE awards (
	film_id BIGINT UNSIGNED NOT NULL,
	FOREIGN KEY (film_id) REFERENCES films(id),
	oscar BIT DEFAULT 0 NOT NULL COMMENT 'Оскар',
	gg BIT DEFAULT 0 NOT NULL COMMENT 'Золотой глобус',
	ba BIT DEFAULT 0 NOT NULL COMMENT 'Британская академия',
	ca BIT DEFAULT 0 NOT NULL COMMENT 'Сезар',
	sag BIT DEFAULT 0 NOT NULL COMMENT 'Премия Гильдии актеров',
	nika BIT DEFAULT 0 NOT NULL COMMENT 'Национальная кинематографическая премия «Ника»',
	ge BIT DEFAULT 0 NOT NULL COMMENT 'Национальная кинематографическая премия «Золотой орел»',
	saturn BIT DEFAULT 0 NOT NULL COMMENT 'Academy of Science Fiction, Fantasy & Horror Films',
	ga BIT DEFAULT 0 NOT NULL COMMENT 'Гойя',
	emmy BIT DEFAULT 0 NOT NULL COMMENT 'Эмми',
	afa BIT DEFAULT 0 NOT NULL COMMENT 'Азиатская киноакадемия',
	efa BIT DEFAULT 0 NOT NULL COMMENT 'Европейская киноакадемия',
	mtv BIT DEFAULT 0 NOT NULL COMMENT 'Премия канала «MTV»',
	mtvrwa BIT DEFAULT 0 NOT NULL COMMENT 'Кинонаграды «MTV-Россия»',
	razzie BIT DEFAULT 0 NOT NULL COMMENT 'Золотая малина',
	georges BIT DEFAULT 0 NOT NULL COMMENT 'Жорж'
);

-- таблица кинофестивалей
DROP TABLE IF EXISTS festivals;
CREATE TABLE festivals (
	film_id BIGINT UNSIGNED NOT NULL UNIQUE,
	FOREIGN KEY (film_id) REFERENCES films(id),
	CFF BIT DEFAULT 0 NOT NULL COMMENT 'Каннский кинофестиваль',
	BIFF BIT DEFAULT 0 NOT NULL COMMENT 'Берлинский кинофестиваль',
	VFF BIT DEFAULT 0 NOT NULL COMMENT 'Венецианский кинофестиваль',
	MIFF BIT DEFAULT 0 NOT NULL COMMENT 'Московский Международный Кинофестиваль',
	KVIFF BIT DEFAULT 0 NOT NULL COMMENT 'Karlovy Vary International Film Festival',
	Kinotavr BIT DEFAULT 0 NOT NULL COMMENT 'Кинотавр: Открытый российский кинофестиваль Кинотавр',
	SS BIT DEFAULT 0 NOT NULL COMMENT 'San Sebastián International Film Festival',
	Sundance BIT DEFAULT 0 NOT NULL COMMENT 'Sundance Film Festival'
);

-- таблица с жанрами
DROP TABLE IF EXISTS genres;
CREATE TABLE genres (
	film_id BIGINT UNSIGNED NOT NULL UNIQUE,
	FOREIGN KEY (film_id) REFERENCES films(id),
	anime BIT DEFAULT 0 NULL COMMENT 'Аниме',
	biography BIT DEFAULT 0 NULL COMMENT 'Биография',
	`actions` BIT DEFAULT 0 NULL COMMENT 'Боевик',
	western BIT DEFAULT 0 NULL COMMENT 'Вестерн',
	military BIT DEFAULT 0 NULL COMMENT 'Военный жанр',
	detective BIT DEFAULT 0 NULL COMMENT 'Детектив',
	child BIT DEFAULT 0 NULL COMMENT 'Детский',
	documentary BIT DEFAULT 0 NULL COMMENT 'Документальный',
	drama BIT DEFAULT 0 NULL COMMENT 'Драма',
	games BIT DEFAULT 0 NULL COMMENT 'Игры',
	historical BIT DEFAULT 0 NULL COMMENT 'Исторический',
	comedy BIT DEFAULT 0 NULL COMMENT 'Комедии',
	concerts BIT DEFAULT 0 NULL COMMENT 'Концерты',
	short BIT DEFAULT 0 NULL COMMENT 'Короткометражка',
	crime BIT DEFAULT 0 NULL COMMENT 'Криминал',
	melodrama BIT DEFAULT 0 NULL COMMENT 'Мелодрама',
	music BIT DEFAULT 0 NULL COMMENT 'Музыкальный',
	cartoon BIT DEFAULT 0 NULL COMMENT 'Мультфильм',
	musical BIT DEFAULT 0 NULL COMMENT 'Мюзикл',
	news BIT DEFAULT 0 NULL COMMENT 'Новости',
	adventures BIT DEFAULT 0 NULL COMMENT 'Приключения',
	`real` BIT DEFAULT 0 NULL COMMENT 'Реальное ТВ',
	family BIT DEFAULT 0 NULL COMMENT 'Семейные',
	sports BIT DEFAULT 0 NULL COMMENT 'Спортивные',
	`show` BIT DEFAULT 0 NULL COMMENT 'Ток-шоу',
	thriller BIT DEFAULT 0 NULL COMMENT 'Триллер',
	horror BIT DEFAULT 0 NULL COMMENT 'Ужасы',
	fantastic BIT DEFAULT 0 NULL COMMENT 'Фантастика',
	noir BIT DEFAULT 0 NULL COMMENT 'Фильм-нуар',
	fantasy BIT DEFAULT 0 NULL COMMENT 'Фэнтези',
	ceremnia BIT DEFAULT 0 NULL COMMENT 'Церемния'
);

-- таблица фильмов в избранных у пользователей
DROP TABLE IF EXISTS favorite;
CREATE TABLE favorite (
	user_id BIGINT UNSIGNED NOT NULL,
	FOREIGN KEY (user_id) REFERENCES users(id),
	film_id BIGINT UNSIGNED NOT NULL,
	FOREIGN KEY (film_id) REFERENCES films(id),
	rating TINYINT NULL
);

-- таблица актёров в фильмах
DROP TABLE IF EXISTS `cast`;
CREATE TABLE `cast` (
	film_id BIGINT UNSIGNED NOT NULL,
	FOREIGN KEY (film_id) REFERENCES films(id),
	actor_id BIGINT UNSIGNED NOT NULL,
	FOREIGN KEY (actor_id) REFERENCES persons(id)
);

-- ===========================================================================================================================================
-- заполняем таблицы
INSERT INTO persons (id,firstname,lastname) VALUES 
	(1,'Киану','Ривз'),
	(2,'Леонардо','ДиКаприо'),
	(3,'Мадс','Миккельсен'),
	(4,'Кристиан','Бэйл'),
	(5,'Сирша','Ронан'),
	(6,'Мэттью','МакКонахи'),
	(7,'Хью','Джекман'),
	(8,'Райан','Рейнольдс'),
	(9,'Марго','Робби'),
	(10,'Том','Холланд');

INSERT INTO person_profiles (actor_id,career,height,birthday,zodiak,birthplace,genres,filmscount,photo_id,gender) VALUES 
	(1,'Актер, Продюсер, Режиссер',1.86,'1964-09-02','Дева','Бейрут, Ливан','Драма, комедия, боевик',241,1,'м'),
	(2,'Актер, Продюсер, Сценарист',1.83,'1974-11-11','Скорпион','Голливуд, Лос-Анджелес, Калифорния, США','Драма, документальный, триллер',225,2,'м'),
	(3,'Актер, Сценарист, Продюсер',1.83,'1965-11-22','Скорпион','Копенгаген, Дания','Драма, боевик, комедия',87,3,'м'),
	(4,'Актер, Продюсер',1.83,'1974-01-30','Водолей','Хаверфордвест, Пембрукшир, Уэльс, Великобритания','Драма, боевик, триллер',124,4,'м'),
	(5,'Актриса',1.68,'1994-04-12','Овен','Бронкс, Нью-Йорк, США','Драма, мелодрама, комедия',92,5,'ж'),
	(6,'Актер, Продюсер, Режиссер, Сценарист',1.82,'1969-11-04','Скорпион','Увалд, Техас, США','Комедия, драма, криминал',223,6,'м'),
	(7,'Актер, Продюсер',1.88,'1968-10-12','Весы','Сидней, Новый Южный Уэльс, Австралия','Драма, короткометражка, комедия',262,7,'м'),
	(8,'Актер, Продюсер, Сценарист',1.88,'1976-10-23','Весы','Ванкувер, Британская Колумбия, Канада','Комедия, короткометражка, драма',197,8,'м'),
	(9,'Актриса, Продюсер',1.68,'1990-07-02','Рак','Голд-Кост, Квинсленд, Австралия','Драма, комедия, фэнтези',94,9,'ж'),
	(10,'Актер, Режиссер',1.73,'1996-06-01','Близнецы','Кингстон-апон-Темс, Большой Лондон, Великобритания','Боевик, приключения, драма',62,10,'м');
	
INSERT INTO films (id,name) VALUES 
	(1,'Зеленая миля'),
	(2,'Побег из Шоушенка'),
	(3,'Властелин колец: Возвращение короля'),
	(4,'Властелин колец: Две крепости'),
	(5,'Властелин колец: Братство Кольца'),
	(6,'Форрест Гамп'),
	(7,'Король Лев'),
	(8,'Карты, деньги, два ствола'),
	(9,'Список Шиндлера'),
	(10,'Начало');

INSERT INTO film_profiles (film_id,original_title,photo_id,rate,`release`,country,slogan,runtime,certificate) VALUES 
	(1,'The Green Mile',11,9.1,'1999','США','Пол Эджкомб не верил в чудеса. Пока не столкнулся с одним из них','03:09',16),
	(2,'The Shawshank Redemption',12,9.1,'1994','США','Страх - это кандалы. Надежда - это свобода','02:22',16),
	(3,'The Lord of the Rings: The Return of the King',13,8.6,'2003','США','There can be no triumph without loss. No victory without suffering. No freedom without sacrifice','03:21',12),
	(4,'The Lord of the Rings: The Two Towers',14,8.6,'2002','Новая Зеландия, США','Приключение продолжается','02:59',12),
	(5,'The Lord of the Rings: The Fellowship of the Ring',15,8.6,'2001','Новая Зеландия, США','Power can be held in the smallest of things...','02:58',12),
	(6,'Forrest Gump',16,8.9,'1994','США','Мир уже никогда не будет прежним, после того как вы увидите его глазами Форреста Гампа','02:22',12),
	(7,'The Lion King',17,8.8,'1994','США','The Circle of Life','01:28',0),
	(8,'Lock, Stock and Two Smoking Barrels',18,8.6,'1998','Великобритания','They lost half a million at cards but they''ve still got a few tricks up their sleeve','01:47',18),
	(9,'Schindler''s List',19,8.8,'1993','США','Этот список - жизнь','03:15',16),
	(10,'Inception',20,8.7,'2010','США, Великобритания','Твой разум - место преступления','02:28',12);

INSERT INTO genres (film_id,anime,biography,actions,western,military,detective,child,documentary,drama,games,historical,comedy,concerts,short,crime,melodrama,music,cartoon,musical,news,adventures,`real`,family,sports,`show`,thriller,horror,fantastic,noir,fantasy,ceremnia) VALUES 
	(1,0,0,1,0,0,0,0,0,1,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0),
	(2,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
	(3,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0),
	(4,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0),
	(5,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0),
	(6,0,0,0,0,0,0,0,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
	(7,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0),
	(8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
	(9,0,1,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
	(10,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0);

	
INSERT INTO awards (film_id,Oscar,GG,BA,CA,SAG,Nika,GE,Saturn,GA,Emmy,AFA,EFA,MTV,MTVRWA,Razzie,Georges) VALUES 
	(1,1,0,0,0,0,1,0,0,1,0,0,1,0,0,1,0),
	(2,0,1,0,1,0,0,0,0,0,0,0,1,0,1,0,0),
	(3,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0),
	(4,1,0,0,1,0,0,0,0,0,0,1,0,0,1,0,1),
	(5,0,0,0,0,1,0,0,1,0,1,0,0,0,0,1,0),
	(6,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0),
	(7,0,0,1,0,0,0,1,0,0,0,0,0,1,0,0,0),
	(8,1,0,1,0,0,1,0,1,0,0,0,1,0,0,1,0),
	(9,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0),
	(10,0,0,1,0,0,1,0,0,0,1,0,1,0,1,0,0);

INSERT INTO festivals (film_id,CFF,BIFF,VFF,MIFF,KVIFF,Kinotavr,SS,Sundance) VALUES 
	(1,0,1,0,1,1,0,0,0),
	(2,0,0,0,0,0,0,0,0),
	(3,1,0,1,0,0,0,0,1),
	(4,0,0,0,0,0,0,1,0),
	(5,0,1,0,1,0,1,0,0),
	(6,0,0,1,0,1,0,0,0),
	(7,0,1,0,1,0,0,0,0),
	(8,0,0,1,0,0,0,0,1),
	(9,0,1,0,0,1,0,1,0),
	(10,1,0,0,1,0,1,0,1);

-- эти таблицы заполнял через рандомный генератор
INSERT INTO `film_details` VALUES 
	(1,'Prudence Parker','Bo Flatley IV','Dr. Golda Greenholt','Kayley Boyle I','Mr. Ulices Klein','Angie Powlowski',692919403754,82518102148,277429646426),
	(2,'Brigitte Toy','Ms. Ara Harber','Frank Wiegand Jr.','Dr. Harvey Herzog','April Renner PhD','Mrs. Hillary Schulist',825159637046,845476262356,622061064076),
	(3,'Gregg Hahn','Ms. Lorna McLaughlin Sr.','Nathaniel Barton','Prof. Karen O\'Conner Jr.','Zander Casper','Dr. Remington Grimes III',624222503834,844084085190,882592561753),
	(4,'Elnora Larson','Dr. Alexander Terry III','Dr. Cyril Gorczany','Dena Tremblay','Linwood Donnelly','Prof. Brett Pouros I',826306156954,851620876167,953135428980),
	(5,'Lea Bayer','Ryley Bashirian','Miss Amie Daugherty MD','Verlie Kutch','Madyson Kreiger','Dr. Sigmund Thompson Jr.',773141353725,104600949811,502777846892),
	(6,'Gladys Cremin','Prof. Flossie Steuber','Miss Ardella Casper','Efren Toy','Yolanda Langworth PhD','Kimberly Beer',840039672493,180462950372,191671302349),
	(7,'Oran Mueller Jr.','Dr. Brando Ondricka','Hettie Reichert V','Maybell Douglas','Ms. Adelia Marquardt','Miss Alana Walker',744157824172,451120920884,791206769104),
	(8,'Chanelle Tromp','Zora Marquardt','Quincy Hammes','Walton Heller','Miss Mertie Friesen DDS','Prof. Keith Legros',56765643208,376980288323,759468873335),
	(9,'Carlee Sanford','Dr. Winnifred Becker','Lilly Effertz','Sunny Fahey','Mrs. Aleen Metz I','Alexa McGlynn',690751689677,611397320149,766046361644),
	(10,'Terence Casper','Christina Brakus','Dr. Javon Robel I','Miss Pascale Kunde','Brad Wunsch','Gaetano Green',283232031820,852494029177,86002160925);

INSERT INTO `serials_profiles` VALUES 
	(1,'Aut asperiores',4,6.1,4,1970,'Russian Federation','Odio qui aliquid beatae aperiam et officia quia.','01:23'),
	(2,'Iusto itaque',5,5.6,7,1973,'Romania','Incidunt maxime voluptatem dolor suscipit quia ess','23:14:00'),
	(3,'Id voluptas est',7,4.6,3,2001,'Bulgaria','Minus quas mollitia et sit iusto quas doloribus.','01:26'),
	(4,'Porro aut',1,7.9,8,2015,'Guatemala','Et quos ut non omnis omnis rerum.','06:39:00'),
	(5,'Similique',4,6.4,6,2013,'Trinidad and Tobago','Consectetur maxime voluptates architecto similique','02:09'),
	(6,'Quia accusantium',6,8.6,7,1999,'Singapore','Nesciunt autem aliquid maxime doloribus.','1:57'),
	(7,'Eligendi eos',2,8.3,4,2006,'Peru','Ut sunt quia accusamus qui vel corporis.','01:56'),
	(8,'Rerum.',4,7.6,5,1970,'Dominica','Quia beatae rerum dolor expedita nam.','2:58'),
	(9,'Voluptas quidem',6,8.4,5,2020,'Sao Tome and Principe','Qui sed culpa et sed.','03:16'),
	(10,'Sunt repellendus',8,7.3,6,1976,'Lesotho','Veniam quia autem enim nisi error accusantium minu','2:03');

INSERT INTO `users` VALUES 
	(1,'Wava','Volkman','ella.goyette@example.org',89357142368),
	(2,'Hellen','Cormier','veum.llewellyn@example.net',89995850361),
	(3,'Devante','Friesen','viviane.casper@example.com',89361078809),
	(4,'Remington','Thompson','bheathcote@example.net',89265516220),
	(5,'Charlotte','Gulgowski','osinski.moises@example.org',89411174623),
	(6,'Lisette','Ullrich','schumm.bart@example.org',89690760878),
	(7,'Nyasia','Kessler','savion29@example.org',89641389493),
	(8,'Jessica','Hilll','pwolff@example.org',89478856249),
	(9,'Hermina','Mosciski','otis.block@example.com',89247707823),
	(10,'Alford','Heathcote','allie.dach@example.net',89702781378);

INSERT INTO `user_profiles` VALUES 
	(1,'ж','1970-05-04',5,'1978-05-25 19:19:40','Бейрут, Ливан','Ducimus omnis est porro nihil earum quaerat non. Natus neque quasi quod quia repellendus. Ut itaque ','Quia tenetur vero illum architecto nihil corporis voluptas. Explicabo at enim et quos. Qui facilis r','http://www.jacobslittel.com/'),
	(2,'ж','2012-03-01',1,'2019-06-11 07:43:02','Голливуд, Лос-Анджелес, Калифорния, США','Enim culpa iusto sequi assumenda minus et aut qui. Praesentium numquam animi consequatur non. Vel id','Quia nesciunt adipisci quibusdam occaecati. Et labore veritatis culpa voluptatem minima. Sapiente am','http://www.cremin.com/'),
	(3,'ж','2008-02-21',3,'2008-06-12 12:08:15','Бронкс, Нью-Йорк, США','Excepturi rerum mollitia provident nostrum nihil maxime officia. Asperiores est dolor a dicta aspern','Incidunt eveniet accusamus illo. Voluptatum deleniti occaecati velit nulla neque aliquam. Odio neque','http://nitzschemraz.net/'),
	(4,'м','1985-03-25',2,'1979-12-25 16:30:34','Копенгаген, Дания','Perferendis id illum beatae blanditiis. Id ad voluptatem nulla est molestiae et quam.','Id aut eligendi asperiores. Dolorem vitae quisquam quia quisquam molestias. Odio doloremque alias de','http://kuhicbrown.info/'),
	(5,'м','2015-08-30',6,'1992-04-05 08:56:30','Бейрут, Ливан','Eos et eligendi ut rerum velit veritatis quos. Dicta est ipsam beatae quidem molestias error atque. ','Dolorem aliquid et assumenda quis aliquid. Accusantium id dicta quisquam nostrum qui. Tenetur maxime','http://www.gorczany.com/'),
	(6,'м','1980-05-26',7,'2014-12-03 17:32:51','Бронкс, Нью-Йорк, США','Veritatis ut rerum illum error culpa. Libero praesentium velit mollitia unde provident vel. Perferen','Et vero hic illum. Quo ex odit quia quia. Delectus reprehenderit sint quasi amet assumenda accusamus','http://millshyatt.net/'),
	(7,'м','1974-03-22',2,'1979-12-20 06:15:25','Голливуд, Лос-Анджелес, Калифорния, США','Eum soluta quis ducimus molestiae sint porro dolor incidunt. Aliquam et temporibus qui non. Fugiat a','Neque corporis aut vel esse asperiores est unde. Optio maxime ut debitis excepturi. Facilis sed nisi','http://daniel.com/'),
	(8,'ж','1979-10-06',9,'1990-06-27 12:18:03','Бейрут, Ливан','Adipisci est sit placeat numquam nihil. Repellat dolores aut qui voluptate praesentium. Minima moles','Quisquam eum iure rerum animi rerum quia minus. Aliquid excepturi provident dolore dolores ut et quo','http://gusikowski.com/'),
	(9,'м','1994-11-14',10,'2009-10-19 16:34:14','Сидней, Новый Южный Уэльс, Австралия','Est assumenda illum est qui explicabo fugiat. Facere est quaerat voluptate suscipit quis ipsa ipsa. ','Vel fuga qui odit quam. Harum accusantium saepe modi voluptas.','http://jaskolskiskiles.com/'),
	(10,'ж','1994-04-16',7,'2016-10-30 19:18:46','Копенгаген, Дания','Illum quis qui nobis voluptas velit. Aperiam aut iste ratione iste dolores sit vel. Sed incidunt num','Sit voluptas veniam nostrum sint. Recusandae est dolore nihil facilis et. Ut ut minus aut quod magni','http://beier.com/');
	

INSERT INTO `cast` VALUES 
(1,7),(8,8),(3,2),(4,3),(4,3),(5,9),(4,7),(9,9),(2,5),(7,2),(8,2),(5,8),(2,9),(8,9),(3,9),(5,3),(4,7),(7,8),(6,5),(2,6),(4,9),(3,5),(9,7),(7,7),(4,1),(2,3),(5,6),(5,2),(7,8),(9,1),(7,7),(1,2),(6,5),(9,2),(4,4),(8,2),(5,7),(3,3),(2,2),(2,7);

INSERT INTO `favorite` VALUES 
(9,2,8),(9,8,1),(4,10,4),(3,5,1),(6,7,2),(1,6,10),(7,6,7),(2,3,9),(7,5,7),(5,1,8);



-- ==================================================================================================================================================
-- представления и запросы

	-- топ 5 фильмов
DROP VIEW IF EXISTS top_5;
CREATE VIEW top_5 AS 
	SELECT * 
	FROM film_profiles fp
	ORDER BY rate DESC 
	LIMIT 5

SELECT original_title, rate FROM top_5

	-- выборка информации о фильме
DROP VIEW IF EXISTS film_info;
CREATE VIEW film_info AS
	SELECT f.name, fp.`release`, fp.country, fp.rate 
	FROM film_profiles fp 
	JOIN films f 
	WHERE fp.film_id = f.id
	
SELECT * FROM film_info

	-- фильмы с оскарами
DROP VIEW IF EXISTS oscar;
CREATE VIEW oscar AS
	SELECT name 
	FROM films f 
	JOIN awards a 
	WHERE a.film_id = f.id AND oscar = 1

SELECT * FROM oscar 

-- ==============================================================================================================================================
-- список фильмов в которых сыграл актёр
DROP PROCEDURE IF EXISTS kinopoisk.actor_films;

DELIMITER $$
$$
CREATE PROCEDURE kinopoisk.actor_films(actor_id BIGINT UNSIGNED)
BEGIN
	SELECT f.name
	FROM persons p
	JOIN `cast` c 
	JOIN films f
	WHERE f.id = c.film_id AND p.id = c.actor_id AND p.id = actor_id;
END$$
DELIMITER ;

CALL actor_films(1);

-- аналогично список актёров в фильме
DROP PROCEDURE IF EXISTS film_cast;

DELIMITER $$
$$
CREATE PROCEDURE film_cast(film_id BIGINT UNSIGNED)
BEGIN
	SELECT p.firstname, p.lastname 
	FROM films f 
	JOIN `cast` c 
	JOIN persons p 
	WHERE f.id = c.film_id AND p.id = c.actor_id AND f.id = film_id;
END$$
DELIMITER ;

CALL film_cast(1);

-- список любимых фильмов пользователя
DROP PROCEDURE IF EXISTS kinopoisk.user_favorite_films;

DELIMITER $$
$$
CREATE PROCEDURE kinopoisk.user_favorite_films(user_id BIGINT UNSIGNED)
BEGIN
	SELECT f.name 
	FROM favorite fav
	JOIN films f
	WHERE fav.film_id = f.id AND fav.user_id = user_id; 
END$$
DELIMITER ;

CALL user_favorite_films(9);

-- найти общие города пользователя и звезды
DROP PROCEDURE IF EXISTS kinopoisk.find_stars_birthplace;

DELIMITER $$
$$
CREATE PROCEDURE kinopoisk.find_stars_birthplace(user_id_ BIGINT UNSIGNED)
BEGIN
	SELECT p.firstname, p.lastname, pp.birthplace 
	FROM person_profiles pp 
	JOIN user_profiles up 
	JOIN persons p 
	WHERE p.id = pp.actor_id AND up.hometown = pp.birthplace AND user_id = user_id_;
END$$
DELIMITER ;

CALL find_stars_birthplace(7)

-- триггер на валиность даты рождения пользователя
DROP TRIGGER IF EXISTS kinopoisk.valid_age;
USE kinopoisk;

DELIMITER $$
$$
CREATE DEFINER=`optikrus`@`localhost` TRIGGER `valid_age` BEFORE UPDATE ON `user_profiles` FOR EACH ROW BEGIN
	IF NEW.birthday >= CURRENT_DATE() THEN 
		SIGNAL SQLSTATE '45000'
		SET MESSAGE_TEXT = 'Дата не обновлена. Некорректные данные';
	END IF;
END$$
DELIMITER ;
