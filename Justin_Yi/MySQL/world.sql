SELECT countries.name, languages.language, languages.percentage
FROM countries
JOIN languages ON countries.id = languages.country_id
WHERE languages.language = 'Slovene'
ORDER by percentage DESC;

select countries.name, count(cities.country_id) as cities
from countries
Join cities on countries.id = cities.country_id
group by countries.name
ORDER BY cities DESC;

SELECT cities.name, cities.population from countries
JOIN cities ON countries.id = cities.country_id
WHERE countries.name = 'Mexico' and cities.population > 500000

SELECT countries.name, languages.language, languages.percentage from countries
JOIN languages ON countries.id = languages.country_id
WHERE languages.percentage > 89
ORDER by languages.percentage DESC;

SELECT countries.name, countries.surface_area, countries.population FROM countries
WHERE countries.surface_area <501 and countries.population >100000;

SELECT countries.name, countries.government_form, countries.capital, countries.life_expectancy FROM countries
WHERE capital > 200 and life_expectancy >75 and government_form = 'Constitutional Monarchy'

SELECT countries.name, cities.name, cities.district, cities.population from countries
JOIN cities ON countries.id = cities.country_id
WHERE cities.population > 500000 and countries.name = 'Argentina' and cities.district = 'Buenos Aires'

select countries.region, count(countries.id) as country_num
from countries 
group by countries.region
ORDER BY country_num DESC;
