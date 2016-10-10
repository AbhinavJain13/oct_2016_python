-- #1 
-- select countries.name, languages.language, languages.percentage
-- FROM countries
-- JOIN languages
-- ON countries.id = languages.country_id
-- WHERE language = "slovene"
-- ORDER by percentage desc;
--

-- #2
-- SELECT countries.name, count(distinct cities.id)
-- FROM world.countries
-- JOIN world.cities
-- ON countries.id = cities.country_id
-- GROUP BY countries.name
-- ORDER BY count(distinct cities.id) desc;
-- 

-- #3
-- SELECT cities.name, cities.population, countries.name
-- FROM world.cities
-- JOIN world.countries
-- ON countries.id = cities.country_id
-- WHERE countries.name = "mexico" AND cities.population > 500000
-- ORDER BY population desc;
--

-- #4
-- SELECT countries.name, languages.language, languages.percentage
-- FROM world.languages
-- JOIN world.countries
-- ON countries.id = languages.country_id
-- WHERE languages.percentage > 89
-- ORDER BY percentage desc;
-- 

-- -- #5
-- SELECT countries.name, countries.surface_area, countries.population
-- FROM world.countries
-- WHERE countries.surface_area < 501 AND countries.population > 100000;
-- 

--  #6
-- SELECT countries.name, countries.government_form, countries.capital, countries.life_expectancy
-- FROM world.countries
-- WHERE countries.government_form = "Constitutional Monarchy" AND countries.capital > 200 AND countries.life_expectancy > 75;
-- 

-- #7
-- SELECT countries.name, cities.name, cities.district, cities.population
-- FROM world.cities
-- JOIN world.countries
-- ON countries.id = cities.country_id
-- WHERE countries.name = "Argentina" AND cities.district = "Buenos Aires" AND cities.population > 500000;
--

-- #8
-- SELECT countries.region, count(distinct countries.id)
-- FROM world.countries
-- GROUP BY countries.region
-- ORDER BY count(distinct countries.id) desc;