--****PLEASE ENTER YOUR DETAILS BELOW****
--Q2-tds-queries.sql


/* Comments for your marker:




*/


/*
2(i) Query 1
*/
--PLEASE PLACE REQUIRED SQL STATEMENT FOR THIS PART HERE

select dem_points as "Demerit Points", dem_description as "Demerit Description"
from demerit
where dem_description like '%heavy%' or dem_description like '%Heavy%' or dem_description like 'Exceed%'
order by dem_points, dem_description;



/*
2(ii) Query 2
*/
--PLEASE PLACE REQUIRED SQL STATEMENT FOR THIS PART HERE

select veh_maincolor as "Main Colour", veh_vin as "VIN", to_char(veh_yrmanuf, 'yyyy') as "Year Manufactured"
from vehicle
where (veh_modname = 'Range Rover' or  veh_modname = 'Range Rover Sport') 
        and 
            (to_char(veh_yrmanuf, 'yyyy') = '2012' or to_char(veh_yrmanuf, 'yyyy') = '2013' or to_char(veh_yrmanuf, 'yyyy') = '2014')
order by to_char(veh_yrmanuf, 'yyyy') desc, veh_maincolor asc;


/*
2(iii) Query 3
*/
--PLEASE PLACE REQUIRED SQL STATEMENT FOR THIS PART HERE

select d.lic_no as "Licence No.", lic_fname || '' || lic_lname as "Driver Fullname", lic_dob as "DOB",
        lic_street || '' || lic_town || '' || lic_postcode as "Driver Address", 
        sus_date as "Suspended on", sus_enddate as "Suspended Till"
from driver d join suspension s on d.lic_no = s.lic_no
where add_months(sus_date, 30) > sysdate
order by d.lic_no ASC, sus_date DESC;


/*
2(iv) Query 4
*/
--PLEASE PLACE REQUIRED SQL STATEMENT FOR THIS PART HERE


select d.dem_code as "Demerit Code", dem_description as "Demerit Description", count(*) as "Total Offences (All Months)",
       sum (case extract(month from off_datetime) when 1 then 1 else 0 end)as Jan,
       sum (case extract(month from off_datetime) when 2 then 1 else 0 end)as Feb,
       sum (case extract(month from off_datetime) when 3 then 1 else 0 end)as Mar,
       sum (case extract(month from off_datetime) when 4 then 1 else 0 end)as Apr,
       sum (case extract(month from off_datetime) when 5 then 1 else 0 end)as May,
       sum (case extract(month from off_datetime) when 6 then 1 else 0 end)as Jun,
       sum (case extract(month from off_datetime) when 7 then 1 else 0 end)as Jul,
       sum (case extract(month from off_datetime) when 8 then 1 else 0 end)as Aug,
       sum (case extract(month from off_datetime) when 9 then 1 else 0 end)as Sep,
       sum (case extract(month from off_datetime) when 10 then 1 else 0 end)as Oct,
       sum (case extract(month from off_datetime) when 11 then 1 else 0 end)as Nov,
       sum (case extract(month from off_datetime) when 12 then 1 else 0 end)as Dec
from demerit d join offence o on d.dem_code = o.dem_code
group by d.dem_code, dem_description
order by count(off_no) DESC, d.dem_code asc;

/*
2(v) Query 5
*/
--PLEASE PLACE REQUIRED SQL STATEMENT FOR THIS PART HERE

select veh_manufname as "Manufacturer Name", count(off_no) as "Total No. of Offences"
from vehicle v join offence o on v.veh_vin = o.veh_vin
group by veh_manufname
having count(off_no) = (select max(count(off_no))
                        from vehicle v join offence o on v.veh_vin = o.veh_vin
                        group by v.veh_manufname);





/*
2(vi) Query 6
*/
--PLEASE PLACE REQUIRED SQL STATEMENT FOR THIS PART HERE

select d.lic_no as "Licence No.", d.lic_fname || ' ' || d.lic_lname as "Driver Name", o.officer_id as "Officer ID", o.officer_fname || ' ' || officer_lname as "Officer Name"
from offence f join driver d on f.lic_no = d.lic_no
                join officer o on f.officer_id = o.officer_id
where d.lic_lname = o.officer_lname
group by f.dem_code, d.lic_no, d.lic_fname || ' ' || d.lic_lname, o.officer_id, o.officer_fname || ' ' || o.officer_lname
having count(dem_code) > 1
order by d.lic_no asc;



/*
2(vii) Query 7
*/
--PLEASE PLACE REQUIRED SQL STATEMENT FOR THIS PART HERE

select m.dem_code as "Demerit Code", m.dem_description as "Demerit Description", d.lic_no as "Licence No.", 
                d.lic_fname||' '||d.lic_lname as "Driver Fullname" , count(*) as "Total Times Booked"
from offence o join driver d on o.lic_no = d.lic_no
                        join demerit m on o.dem_code = m.dem_code
group by m.dem_code, m.dem_description, d.lic_no, d.lic_fname||' '||d.lic_lname                
having (m.dem_code, count(*)) in (              
                                    select Demerit_Code, max(Total)
                                    from (
                                            select m.dem_code as Demerit_Code,  d.lic_no as Licence_No,  count(*) as Total
                                            from offence o join driver d on o.lic_no = d.lic_no
                                                                    join demerit m on o.dem_code = m.dem_code
                                            group by m.dem_code,  d.lic_no)
                                    group by  Demerit_Code)
order by m.dem_code asc, d.lic_no asc;




/*
2(viii) Query 8
*/
--PLEASE PLACE REQUIRED SQL STATEMENT FOR THIS PART HERE
with t1 as(

select case
when ASCII(SUBSTR(veh_vin, 1, 1)) >= 65 and ASCII(SUBSTR(veh_vin, 1, 1)) <= 67 then 'Africa'
when ASCII(SUBSTR(veh_vin, 1, 1)) >= 74 and ASCII(SUBSTR(veh_vin, 1, 1)) <= 82 then 'Asia'
when ASCII(SUBSTR(veh_vin, 1, 1)) >= 83 and ASCII(SUBSTR(veh_vin, 1, 1)) <= 90 then 'Europe'
when ASCII(SUBSTR(veh_vin, 1, 1)) >= 49 and ASCII(SUBSTR(veh_vin, 1, 1)) <= 53 then 'North America'
when ASCII(SUBSTR(veh_vin, 1, 1)) >= 54 and ASCII(SUBSTR(veh_vin, 1, 1)) <= 55 then 'Oceania'
when ASCII(SUBSTR(veh_vin, 1, 1)) >= 56 and ASCII(SUBSTR(veh_vin, 1, 1)) <= 57 then 'South America'
else 'Unknown' 
end as Region, count(*) as mycount

from vehicle

group by case
when ASCII(SUBSTR(veh_vin, 1, 1)) >= 65 and ASCII(SUBSTR(veh_vin, 1, 1)) <= 67 then 'Africa'
when ASCII(SUBSTR(veh_vin, 1, 1)) >= 74 and ASCII(SUBSTR(veh_vin, 1, 1)) <= 82 then 'Asia'
when ASCII(SUBSTR(veh_vin, 1, 1)) >= 83 and ASCII(SUBSTR(veh_vin, 1, 1)) <= 90 then 'Europe'
when ASCII(SUBSTR(veh_vin, 1, 1)) >= 49 and ASCII(SUBSTR(veh_vin, 1, 1)) <= 53 then 'North America'
when ASCII(SUBSTR(veh_vin, 1, 1)) >= 54 and ASCII(SUBSTR(veh_vin, 1, 1)) <= 55 then 'Oceania'
when ASCII(SUBSTR(veh_vin, 1, 1)) >= 56 and ASCII(SUBSTR(veh_vin, 1, 1)) <= 57 then 'South America'
else 'Unknown' 
end

)

select Region as "Region", mycount as "Total Vehicles Manufatured", 
            to_char(round(mycount*100 / (select count(*) from vehicle), 2), '9999999999999999999990.99')||'%' as "Percentage of Vehicles Manufactured"
from t1

union all

select '        TOTAL' as Region, sum(mycount), to_char(sum(round(mycount*100 / (select count(*) from vehicle), 2)), '9999999999999999999990.99')||'%' as mycount
from t1

order by "Total Vehicles Manufatured" asc,  "Region" asc