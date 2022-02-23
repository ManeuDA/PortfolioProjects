/*

Queries Used for Tableau Project

*/

--1.

-- Looking at Total Cases vs Total Deaths: Average Death Percentage 
-- Metric: SUM(new_deaths)/SUM(Nullif(new_cases,0))*100
SELECT SUM(new_cases) as Total_Cases, SUM(new_deaths) as Total_Deaths, SUM(new_deaths)/SUM(Nullif(new_cases,0))*100 as Death_Percentage 
FROM PortfolioProject..[Covid Death]
--WHERE location in ('Canada', 'Germany', 'South Korea', 'United States')
ORDER BY 1,2 



-- Looking at Total Cases vs Total Deaths (Daily Covid Mortarlity Percentage) 
-- Showing Daily Covid Mortality Percentage in Multiple Countries (in this case: Canada, Germany, South Korea, United States)
-- Metric: (total_death/total_cases)*100 
--SELECT location, date, total_cases, total_deaths, (total_deaths/Nullif(total_cases,0))*100 as MortailityPercentage
--FROM PortfolioProject..[Covid Death]
--WHERE location in ('Canada', 'Germany', 'South Korea', 'United States')
--ORDER BY 1,2 

--2. 

-- Showing Countries with Total Death Count per Population 
SELECT continent, SUM(new_deaths) as TotalDeathCount
FROM PortfolioProject..[Covid Death]
--WHERE location in ('Canada', 'Germany', 'South Korea', 'United States')
GROUP BY continent
ORDER BY TotalDeathCount desc 


--3. 

-- Looking at Countries with Total Infection Rate compared to Population 
-- Metric for Total Infection Rate: SUM(new_Cases)
-- Metric for Percentage of Infected Population: MAX(total_cases/population)*100 
-- Note: NULLIF(population,0) used to avoid ERROR message
-- CREATE VIEW TotalInfectionRate as
SELECT continent, location, population, SUM(new_cases) as TotalInfectionCount, MAX(total_cases/NULLIF(population,0))*100 as PercentageCovidPopulation
FROM PortfolioProject..[Covid Death]
--WHERE location in ('Canada', 'Germany', 'South Korea', 'United States')
GROUP BY continent, location, population
ORDER BY PercentageCovidPopulation desc

--4. 

-- Looking at TotalVaccinated per Country
-- Metric: Average Percent Fully Vaccinated per Country (Total_Fully_Vaccinated/nullif(population,0))*100 

--CREATE VIEW TotalVaccinated as
SELECT dea.continent, dea.location, dea.date, dea.population, vac.people_fully_vaccinated
, MAX(vac.people_fully_vaccinated) OVER (Partition by dea.location ORDER BY dea.location, dea. date, dea.population) as Total_Fully_Vaccinated
FROM PortfolioProject..[Covid Death] dea 
Join PortfolioProject..[Covid Vaccination] vac
	ON dea.location = vac.location
	and dea.date = vac.date 
	and dea.population = vac.population 
-- ORDER BY 1,2,3

SELECT Continent, location, date, Population,people_fully_vaccinated, Total_Fully_Vaccinated, (Total_Fully_Vaccinated/nullif(population,0))*100 as Average_Fully_Vaccinated
FROM TotalVaccinated



