/*

Queries Used for Tableau Project

*/

--1.

-- Looking at Total Cases vs Total Deaths (Daily Covid Mortarlity Percentage) 
-- Showing Daily Covid Mortality Percentage in Multiple Countries (in this case: Canada, Germany, South Korea, United States)
-- Metric: (total_death/total_cases)*100 
SELECT location, date, total_cases, total_deaths, (total_deaths/Nullif(total_cases,0))*100 as MortailityPercentage
FROM PortfolioProject..[Covid Death]
--WHERE location in ('Canada', 'Germany', 'South Korea', 'United States')
ORDER BY 1,2 

--2. 

-- Showing Countries with Total Death Count per Population 
SELECT location, SUM(new_cases) as TotalDeathCount
FROM PortfolioProject..[Covid Death]
--WHERE location in ('Canada', 'Germany', 'South Korea', 'United States')
GROUP BY location
ORDER BY TotalDeathCount desc 


--3. 

-- Looking at Countries with Highest Infection Rate compared to Population 
-- Metric for Highest Infection Rate: MAX(total_Cases)
-- Metric for Percentage of Infected Population: MAX(total_cases/population)*100 
-- Note: NULLIF(population,0) used to avoid ERROR message
--CREATE VIEW HighestInfectionRate as
SELECT continent, location, population, MAX(total_cases) as TotalInfectionCount, MAX(total_cases/NULLIF(population,0))*100 as PercentageCovidPopulation
FROM PortfolioProject..[Covid Death]
--WHERE location in ('Canada', 'Germany', 'South Korea', 'United States')
GROUP BY continent, location, population
ORDER BY PercentageCovidPopulation desc

--4. 

-- Looking at Population Infected by Countries 
-- Metric: MAX (total_cases/population)*100
SELECT location, date, population, MAX(total_cases) as HighestInfectCount, MAX(total_cases/population)*100 as PercentPopulationInfected
FROM PortfolioProject..[Covid Death]
--WHERE location in ('Canada', 'Germany', 'South Korea', 'United States')
GROUP BY location, population
ORDER BY PercentPopulationInfected desc 




--5. 
--CREATE VIEW PercentageRollingTotalVaccination as
WITH PopvsVac (Continent, Location, Date, Population, New_Vaccinations, RollingTotalVaccinations)
AS
(
SELECT dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations
, SUM(vac.new_vaccinations) OVER (Partition by dea.location ORDER BY dea.location, dea.date) as RollingTotalVaccinations
--, (RollingTotalVaccinations/population)*100 --> Gives you an ERROR because you can't use a column you just created.  USE CTE ór 
-- If I only partition by dea.location, the new_vaccinations column will start sum as well. IMPORTANT to use ORDER BY dea.location and dea.date so that counting only for TotalVaccinations Column 
FROM PortfolioProject..[Covid Death] dea
Join PortfolioProject..[Covid Vaccination] vac
	ON dea.location = vac.location
	and dea.date = vac.date 
---ORDER BY 1,2,3
)
SELECT*, (RollingTotalVaccinations/Nullif(Population,0))*100 as PercentageRollingTotalVaccinations
FROM PopvsVac

--6. 

--CREATE VIEW DailyCovidCasePercentage as 
SELECT continent, location, date, population, total_cases, (total_cases/population)*100 as CasePercentage
FROM PortfolioProject..[Covid Death]
WHERE location in ('Canada', 'Germany', 'South Korea', 'United States')
ORDER BY 1,2

--7.

-- CREATE VIEW TotalCasesTotalDeathTotalVaccinated as
SELECT dea.continent, dea.location, dea.date, dea.population, dea.new_cases, dea.new_deaths, vac.people_fully_vaccinated
, SUM(dea.new_cases) OVER(Partition by dea.location ORDER BY dea.location, dea. date, dea.population ) as Total_Cases 
, SUM(dea.new_deaths) OVER (Partition by dea.location ORDER BY dea.location, dea. date, dea.population) as Total_Deaths
, SUM(vac.people_fully_vaccinated) OVER (Partition by dea.location ORDER BY dea.location, dea. date, dea.population) as Total_Fully_Vaccinated 
FROM PortfolioProject..[Covid Death] dea 
Join PortfolioProject..[Covid Vaccination] vac
	ON dea.location = vac.location
	and dea.date = vac.date 
	and dea.population = vac.population 
ORDER BY 1,2,3





