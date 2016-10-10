-- select countries.name, languages.language,languages.percentage  
-- from languages
-- join countries on countries.id = languages.country_id
-- where languages.language="Slovene"

-- select countries.name, count(cities.name)
-- from cities
-- join countries on countries.id= cities.country_id
-- group by (countries.name)
-- order by count(cities.name) DESC

-- select  cities.name, cities.population
-- from cities
-- join countries on countries.id =cities.country_id
-- where countries.name="Mexico" and cities.population > 500000
-- order by cities.population DESC

-- select countries.name, languages.percentage
-- from languages
-- join countries on countries.id =languages.country_id
-- where languages.percentage > 89
-- order by languages.percentage DESC

-- select name,surface_area,population
-- from countries
-- where surface_area<501 and population>100000

-- select countries.name, countries.capital, countries.life_expectancy, countries.government_form
-- from countries
-- where capital>200 and life_expectancy >75 and government_form="Constitutional Monarchy"

-- select countries.name, cities.name, cities.district, cities.population
-- from cities
-- join countries on countries.id= cities.country_id
-- where cities.district="Buenos Aires" and cities.population>500000

-- select region, count(name)
-- from countries
-- group by (region) 
-- order by count(name) DESC