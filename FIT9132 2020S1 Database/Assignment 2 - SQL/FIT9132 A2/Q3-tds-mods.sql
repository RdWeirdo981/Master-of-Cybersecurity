--****PLEASE ENTER YOUR DETAILS BELOW****
--Q3-tds-mods.sql


/* Comments for your marker:




*/


/*
3(i) Changes to live database 1
*/
--PLEASE PLACE REQUIRED SQL STATEMENTS FOR THIS PART HERE

alter table officer
add book_times number(10);

update officer t1
set book_times = (select book_times, count(*) as mycount 
        from offence f join officer o on f.officer_id = o.officer_id
        group by o.officer_id) 






/*
3(ii) Changes to live database 2
*/
--PLEASE PLACE REQUIRED SQL STATEMENTS FOR THIS PART HERE










/*
3(iii) Changes to live database 3
*/
--PLEASE PLACE REQUIRED SQL STATEMENTS FOR THIS PART HERE


































