SELECT countries.name, languages.language, languages.percentage 
FROM languages JOIN countries 
on languages.country_id = countries.id
WHERE languages.language = "Slovene"
ORDER BY languages.percentage DESC;

SELECT countries.name, COUNT(cities.name)
FROM countries JOIN cities
ON cities.country_id = countries.id
GROUP BY countries.id
ORDER BY COUNT(cities.name) DESC;

SELECT cities.name, cities.population, countries.name
FROM cities JOIN countries
on cities.country_id = countries.id
WHERE cities.population > 500000 AND countries.name = "Mexico"
ORDER BY cities.population DESC;

SELECT countries.name, languages.language, languages.percentage
FROM languages JOIN countries 
on languages.country_id = countries.id
WHERE languages.percentage > 89
ORDER BY languages.percentage DESC;

SELECT countries.name, countries.surface_area, SUM(cities.population) AS "country_population"
FROM countries JOIN cities
on cities.country_id = countries.id
WHERE cities.population > 100000 and countries.surface_area < 501
GROUP BY countries.id;

SELECT countries.name, countries.government_form, countries.life_expectancy, countries.capital
FROM countries
WHERE countries.government_form = "Constitutional Monarchy" and countries.life_expectancy > 75 and countries.capital > 200;

SELECT countries.name, cities.name, cities.district, cities.population
FROM cities JOIN countries
on cities.country_id = countries.id
WHERE cities.district = "Buenos Aires" and cities.population > 500000;

SELECT countries.region, COUNT(countries.name)
FROM countries
GROUP BY countries.region
ORDER BY COUNT(countries.name) DESC;