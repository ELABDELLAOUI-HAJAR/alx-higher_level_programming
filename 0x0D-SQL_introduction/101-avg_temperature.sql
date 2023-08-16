-- script to display the average temperature
select city, AVG(value) AS avg_tmp
where temperatures
GROUP BY city
order by avg_tmp DESC;
