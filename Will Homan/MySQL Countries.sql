SELECT name, language, percentage
FROM countries
JOIN languages
ON countries.id = languages.country_id
WHERE languages.language = 'Slovene'
ORDER BY languages.percentage DESC;

SELECT countries.name, COUNT(cities.id)
FROM countries
LEFT JOIN cities
ON countries.id = cities.country_id
GROUP BY countries.name;

SELECT cities.name
FROM countries
LEFT JOIN cities
ON countries.id = cities.country_id
WHERE countries.name = "Mexico" and cities.population > 500000
ORDER BY cities.population DESC;

SELECT name, language, percentage
FROM countries
JOIN languages
ON countries.id = languages.country_id
WHERE languages.percentage > 89
ORDER BY languages.percentage DESC;

SELECT name, surface_area, countries.population
FROM countries
WHERE surface_area < 501 AND countries.population > 100000;

SELECT name, government_form, life_expectancy, capital
FROM countries
WHERE government_form = "Constitutional Monarchy" AND capital > 200 AND life_expectancy > 75;

SELECT countries.name, cities.name, cities.district, cities.population
FROM countries
LEFT JOIN cities
ON countries.id = cities.country_id
WHERE countries.name = "Argentina" AND cities.district = "Buenos Aires" AND cities.population > 500000;

SELECT region, COUNT(countries.id)
FROM countries
GROUP BY region
ORDER BY COUNT(countries.id) DESC