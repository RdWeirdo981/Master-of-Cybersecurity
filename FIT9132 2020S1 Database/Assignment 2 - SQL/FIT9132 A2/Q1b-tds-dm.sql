--****PLEASE ENTER YOUR DETAILS BELOW****
--Q1b-tds-dm.sql


SET SERVEROUTPUT ON;


/* Comments for your marker:




*/


/*
1b(i) Create a sequence 
*/
--PLEASE PLACE REQUIRED SQL STATEMENT(S) FOR THIS PART HERE

create sequence offence_seq 
start with 100 
increment by 1;

select * from cat;




/*
1b(ii) Take the necessary steps in the database to record data.
*/
--PLEASE PLACE REQUIRED SQL STATEMENT(S) FOR THIS PART HERE

insert into offence values (offence_seq.nextval, TO_DATE('10-Aug-2019', 'DD-MON-YYYY'), ' 72 Aberg Avenue Richmond South 3121', 100, 10000011, '100389', 'JYA3HHE05RA070562');
insert into offence values (offence_seq.nextval, TO_DATE('16-Oct-2019', 'DD-MON-YYYY'), ' 72 Aberg Avenue Richmond South 3121', 101, 10000015, '100389', 'JYA3HHE05RA070562');
insert into offence values (offence_seq.nextval, TO_DATE('7-Jan-2020', 'DD-MON-YYYY'), ' 72 Aberg Avenue Richmond South 3121', 99, 10000015, '100389', 'JYA3HHE05RA070562');

select * from offence;



/*
1b(iii) Take the necessary steps in the database to record changes. 
*/
--PLEASE PLACE REQUIRED SQL STATEMENT(S) FOR THIS PART HERE


delete from offence
where lic_no = '100389' and dem_code = 99;

select * 
from offence;






