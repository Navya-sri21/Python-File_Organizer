CREATE DATABASE file_organizer_db;

USE file_organizer_db;

drop  table files;
drop  table categories;
drop table organization_logs;

-- CATEGORIES TABLE --
create table categories(category_id int  primary key auto_increment,
						category_name varchar(50) not null);
                        
-- FILES TABLE--
create table files( file_id int primary key auto_increment,
					file_name varchar(100),
                    extension varchar(20),
                    file_size int,
                    category_id int, foreign key (category_id) references categories(category_id),
                    file_path varchar(500)
                    );
                    
-- ORGANIZATION_LOGS TABLE --
create table organization_logs(log_id int primary key auto_increment,
								file_id int, foreign key(file_id) references files(file_id),
                                action varchar(50),
                                action_data datetime default current_timestamp);


-- insert the values in categories table---
insert into categories(category_name) values ('Documents'),('Images'),('Videos'),('Audio'),('Archives'),('Others');
desc categories;
select * from categories;


-- insert the values into the files table --

insert into files (file_name, extension,file_size, category_id,file_path)
			values('resume.pdf','.pdf',25000,1,'c:/Files/resume.pdf'),
				  ('photo.jpd','.jpg',1500000,2,'c:/Files/photo.jpg'),
                  ('movie.mp4','.mp4',5000000,3,'c:/Files/movie.mp4'),
                  ('song.mp3','.mp3',400000,4,'c:/Files/song.mp3');
INSERT INTO files
(file_name, extension, file_size, category_id, file_path)
VALUES
-- Audio files
('song1.mp3', '.mp3', 4000000, 4, 'C:/Files/song1.mp3'),
('podcast.wav', '.wav', 8000000, 4, 'C:/Files/podcast.wav'),
('music.flac', '.flac', 12000000, 4, 'C:/Files/music.flac'),

-- Video files
('movie.mp4', '.mp4', 50000000, 3, 'C:/Files/movie.mp4'),
('video1.avi', '.avi', 30000000, 3, 'C:/Files/video1.avi'),
('tutorial.mkv', '.mkv', 45000000, 3, 'C:/Files/tutorial.mkv'),

-- Archive files
('backup.zip', '.zip', 15000000, 5, 'C:/Files/backup.zip'),
('project.rar', '.rar', 20000000, 5, 'C:/Files/project.rar'),
('data.7z', '.7z', 10000000, 5, 'C:/Files/data.7z'),

-- Other files
('data.db', '.db', 500000, 6, 'C:/Files/data.db'),
('notes.log', '.log', 200000, 6, 'C:/Files/notes.log'),
('config.json', '.json', 100000, 6, 'C:/Files/config.json');

desc files;

select* from files;
-- INSERTING VALUES IN ORGANIZATION TABLE --

INSERT INTO organization_logs (file_id, action)
VALUES
(1, 'File Uploaded'),
(2, 'File Organized'),
(3, 'File Moved'),
(4, 'File Renamed'),
(5, 'File Categorized'),
(6, 'File Updated'),
(7, 'File Deleted'),
(8, 'File Scanned'),
(9, 'File Downloaded'),
(10, 'Duplicate File Detected'),
(11, 'File Restored'),
(12, 'File Organization Failed');





