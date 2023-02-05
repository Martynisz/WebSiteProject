DROP TABLE allmachines;
CREATE TABLE "allmachines" (
"id" INTEGER PRIMARY KEY,
"name" char(30) NOT NULL,
"excercise" char(50) NOT NULL
);
insert into allmachines(name,excercise) VALUES('lawka prosta','wyciskaqnie sztangi');
insert into allmachines(name,excercise) VALUES('lawka prosta','wyciskanie hantli lezac');
insert into allmachines(name,excercise) VALUES('lawka prosta','triceps sztangielkami');
insert into allmachines(name,excercise) VALUES('lawka prosta','rozpietki');
insert into allmachines(name,excercise) VALUES('lawka prosta','wioslowanie w opadzie');
insert into allmachines(name,excercise) VALUES('lawka prosta','odwrocone rozpietki lezac');
insert into allmachines(name,excercise) VALUES('lawka skosna','wyciskanie sztangi');
insert into allmachines(name,excercise) VALUES('lawka skosna','wyciskanie hantelek');
insert into allmachines(name,excercise) VALUES('llawka skosna','rozpietki');
insert into allmachines(name,excercise) VALUES('llawka skosna','wioslowanie lezac');
insert into allmachines(name,excercise) VALUES('llawka skosna','odwrotne rozpietki lezac');
insert into allmachines(name,excercise) VALUES('hantel','biceps z rotacja');
insert into allmachines(name,excercise) VALUES('hantel','triceps zza glowy');
insert into allmachines(name,excercise) VALUES('hantel','biceps hwytem mlotkowym');
insert into allmachines(name,excercise) VALUES('hantel','wyciskanie sztangielek zza glowy');
insert into allmachines(name,excercise) VALUES('hantel','rotatory');
insert into allmachines(name,excercise) VALUES('hantel','przysiady z hantelkami');
insert into allmachines(name,excercise) VALUES('hantel','spacer farmera');

UPDATE allmachines
set name="hantelka"
WHERE name="hantel";

SELECT * from allmachines;
