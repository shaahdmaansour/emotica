
CREATE TABLE IF NOT EXISTS Person(
PersonID SERIAL PRIMARY KEY,
FName VARCHAR(20),
LName VARCHAR(20),
Email VARCHAR(20),
TPassword VARCHAR(64),
PhoneNumber VARCHAR(11),
DateOfBirth DATE,
Gender BOOLEAN,
 CHECK (
        Email ~* '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
    )
);


CREATE TABLE IF NOT EXISTS TUser(
UserID SERIAL PRIMARY KEY,
AssignedTID INT, 
LowestMoodStreak INT,
CHECK(LowestMoodStreak>0)
);

CREATE TABLE IF NOT EXISTS Therapist(
TherapistID SERIAL PRIMARY KEY,
Specialization VARCHAR(64),
LiscenceNumber VARCHAR(32)
);

CREATE TABLE IF NOT EXISTS  Motivator(
MotivatorID SERIAL PRIMARY KEY,
HighestStreak INT DEFAULT 0,
CurrentStreak INT DEFAULT 0,
DailyLog BOOLEAN, --we can change it if you want
Notfication TEXT
);
CREATE TABLE IF NOT EXISTS  Advice(
AdviceID SERIAL PRIMARY KEY,
AdviceType VARCHAR(20),
AdviceContent TEXT

);

CREATE TABLE IF NOT EXISTS  Music(
MusicID SERIAL PRIMARY KEY,
MusicType VARCHAR(20),
musicContent BYTEA

);
CREATE TABLE IF NOT EXISTS MoodEntry(
EntryID SERIAL PRIMARY KEY,
moodDate DATE,
moodScore INT,
moodColor INT, --each number for a color, EX:  0-> black
AdviceID INT,--reference for new entity called advices(id,type,TEXT)
MusicID INT,--reference for new entity called music (id,type,BYTEA)
mcqGeneratedForm JSON,
UserID INT,
MotivatorID INT,
FOREIGN KEY(UserID) REFERENCES TUser(UserID),
FOREIGN KEY(MotivatorID) REFERENCES Motivator(MotivatorID),
FOREIGN KEY (MusicID) REFERENCES Music(MusicID),
FOREIGN KEY (AdviceID) REFERENCES Advice(AdviceID)
);

CREATE TABLE IF NOT EXISTS MCQResponse(
ResponseID SERIAL PRIMARY KEY,
SelectedOption TEXT,
Score INT,
EntryID INT,

FOREIGN KEY (EntryID) REFERENCES MoodEntry(EntryID)
);

CREATE TABLE IF NOT EXISTS  MCQQuestions(

QuestionID SERIAL PRIMARY KEY,
QuestionText TEXT,
ResponseID INT,
FOREIGN KEY(ResponseID) REFERENCES MCQResponse(ResponseID)


);

CREATE TABLE IF NOT EXISTS  Appointment(
AppointmentID SERIAL PRIMARY KEY,
Status VARCHAR(20),
AppointmentDate DATE,
StartTime TIME,--It's just an initial format until we agree on it
EndTime TIME,--It's just an initial format until we agree on it
AType VARCHAR(20),
UserID INT,
TherapistID INT,
FOREIGN KEY (TherapistID) REFERENCES Therabist(TherapistID),
FOREIGN KEY (UserID) REFERENCES TUser(UserID)


);
CREATE TABLE IF NOT EXISTS  SupportGroup(
GroupID SERIAL PRIMARY KEY,
GroupName VARCHAR(30),
SAdmin VARCHAR(30),
Description VARCHAR(30),
CreateDate DATE,
TherapistID INT,
FOREIGN KEY (TherapistID) REFERENCES Therabist(TherapistID)
);



CREATE TABLE IF NOT EXISTS  Alert(
AlertID SERIAL PRIMARY KEY,
AlertType VARCHAR(20),
TriggeredDate DATE,
ALocation TEXT, --the link of google maps
MessageSent TEXT,
UserID INT,
FOREIGN KEY (UserID) REFERENCES TUser(UserID)


);

CREATE TABLE IF NOT EXISTS  Notes(
NoteID SERIAL PRIMARY KEY,
CreatedBy VARCHAR(50),
DateModified DATE,
EntryDate DATE,
NContent TEXT,
PersonID INT,
FOREIGN KEY (PersonID) REFERENCES Person(PersonID)

);



CREATE TABLE IF NOT EXISTS  CreateGp(

CreatedGroup VARCHAR(50),
TherapistID INT,
PRIMARY KEY (CreatedGroup, TherapistID),
FOREIGN KEY (TherapistID) REFERENCES Therabist(TherapistID)


);

CREATE TABLE IF NOT EXISTS  JoinedGp(
JoinedGroup VARCHAR(50),
UserID INT,
PRIMARY KEY (JoinedGroup, UserID),
FOREIGN KEY (UserID) REFERENCES TUser(UserID)


);

CREATE TABLE IF NOT EXISTS  emergencyContact(
EmergencyContact VARCHAR(11),
PersonID INT ,

 PRIMARY KEY (EmergencyContact, PersonID),
    FOREIGN KEY (PersonID) REFERENCES Person(PersonID)
);

CREATE TABLE IF NOT EXISTS  Msg(
Msg TEXT,
GroupID INT,
PRIMARY KEY (Msg, GroupID),
FOREIGN KEY (GroupID) REFERENCES SupportGroup(GroupID)

);

CREATE TABLE IF NOT EXISTS  GroupMembers(
GroupMembers VARCHAR(50),
UserID INT,
PRIMARY KEY (GroupMembers, UserID),
FOREIGN KEY (UserID) REFERENCES TUser(UserID)

);

CREATE TABLE IF NOT EXISTS  GroupMembership(

UserID INT,
GroupID INT,
JoinedDate DATE,
PRIMARY KEY (GroupID, UserID),
FOREIGN KEY (UserID) REFERENCES TUser(UserID),
FOREIGN KEY (GroupID) REFERENCES SupportGroup(GroupID)

);
