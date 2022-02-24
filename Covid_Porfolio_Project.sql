UPDATE PortfolioProject..[Covid Death]
SET[continent] = REPLACE([continent],0,'Null')
-- Replace 0 to 'Null' in Column continunt in data type varchar(50)

DELETE
FROM PortfolioProject..[Covid Death]
WHERE continent = 'Null'
-- Delete 'Null' in column continent (irrelevant data)

SELECT*	
FROM PortfolioProject..[Covid Death]
ORDER BY 3,4


SELECT*
FROM PortfolioProject..[Covid Vaccination]
ORDER BY 3,4

-- Select Data to be used 
SELECT location, date, population, total_cases, new_cases, total_deaths 
FROM PortfolioProject..[Covid Death]
Order by 1,2

-- Looking at Total Cases vs Total Deaths 
-- Showing Covid Mortality Rate in specific country 
SELECT location, date, total_cases, total_deaths, (total_deaths/total_cases)*100 as MortalityPercentage
FROM PortfolioProject..[Covid Death]
WHERE location like '%ermany%'  -- only part of keyword is known 
ORDER BY 1,2 

-- Looking at Total Cases vs Total Deaths (Daily Covid Mortarlity Percentage) 
-- Showing Daily Covid Mortality Percentage in Multiple Countries (in this case: Canada, Germany, South Korea, United States)
-- Metric: (total_death/total_cases)*100 
SELECT location, date, total_cases, total_deaths, (total_deaths/total_cases)*100 as MortailityPercentage
FROM PortfolioProject..[Covid Death]
WHERE location in ('Canada', 'Germany', 'South Korea', 'United States')
ORDER BY 1,2 

-- Looking at Total Cases vs Population (Daily Covid Case Percentage)
-- Showing Daily Covid Case Percentage in Multiple Countries
-- Metric: (total_cases/population)*100
SELECT continent, location, date, population, total_cases, (total_cases/population)*100 as CasePercentage
FROM PortfolioProject..[Covid Death]
WHERE location in ('Canada', 'Germany', 'South Korea', 'United States')
ORDER BY 1,2


-- Looking at Countries with Highest Infection Rate compared to Population 
-- Metric for Total Infection Count: MAX(total_Cases)
-- Metric for Percentage of Infected Population: MAX(total_cases/population)*100 
-- Note: NULLIF(population,0) used to avoid ERROR message
SELECT continent, location, population, SUM(new_cases) as TotalInfectionCount, MAX(total_cases/NULLIF(population,0))*100 as PercentageCovidPopulation
FROM PortfolioProject..[Covid Death]
--WHERE location in ('Canada', 'Germany', 'South Korea', 'United States')
GROUP BY continent, location, population
ORDER BY PercentageCovidPopulation desc

-- Showing Countries with Total Deaths Count per Population 
SELECT continent, location, MAX(total_deaths) as TotalDeathCount
FROM PortfolioProject..[Covid Death]
--WHERE location in ('Canada', 'Germany', 'South Korea', 'United States')
GROUP BY continent, location
ORDER BY TotalDeathCount desc 

-- Looking Covid Total Deaths Count by Continent 
SELECT continent, SUM(new_cases) as TotalDeathCount
FROM PortfolioProject..[Covid Death]
--WHERE location in ('Canada', 'Germany', 'South Korea', 'United States')
GROUP BY continent
ORDER BY TotalDeathCount desc

-- GLOBAL Daily Numbers 
-- Metric: SUM(new_deaths)/SUM(Nullif(new_cases,0))*100
SELECT location, date, SUM(new_cases) as DailyTotalGlobalCases, SUM(new_deaths) as DailyTotalGlobalDeaths
, SUM(new_deaths)/SUM(Nullif(new_cases,0))*100 as DailyTotalDeathPercentage
FROM PortfolioProject..[Covid Death]
--WHERE location in ('Canada', 'Germany', 'South Korea', 'United States')
GROUP BY location, date
ORDER BY 1,2 

-- GLOBAL NUMBERS
-- Metric:SUM(new_deaths)/sum(nullif(new_cases,0))*100
SELECT SUM(new_cases) as TotalGlobalCases, SUM(new_deaths) as TotalGlobalDeaths
, SUM(new_deaths)/sum(nullif(new_cases,0))*100 as TotalDeathPercentage
FROM PortfolioProject..[Covid Death]
--WHERE location in ('Canada', 'Germany', 'South Korea', 'United States')
--GROUP BY date
ORDER BY 1,2 

-- Looking at Total Population vs Global Rolling Vaccination Counts
-- JOIN TWO TABLES 
SELECT dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations, dea.date 
, SUM(vac.new_vaccinations) OVER (Partition by dea.location ORDER BY dea.location, dea, date) as RollingTotalVaccinations
--, (RollingTotalVaccinations/population)*100 --> Gives you an ERROR because you can't use a column you just created.  
-- If I only partition by dea.location, the new_vaccinations column will start sum as well. 
-- IMPORTANT to use ORDER BY dea.location and dea.date so that counting only for RollingTotalVaccinations Column 
FROM PortfolioProject..[Covid Death] dea
Join PortfolioProject..[Covid Vaccination] vac
	ON dea.location = vac.location
	and dea.date = vac.date 
ORDER BY 1,2,3

-- USE CTE (COMMON TABLE EXPRESSIONS)
WITH PopvsVac (Continent, Location, Date, Population, New_Vaccinations, RollingTotalVaccinations)
AS
(
SELECT dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations
, SUM(vac.new_vaccinations) OVER (Partition by dea.location ORDER BY dea.location, dea.date) as RollingTotalVaccinations
--, (RollingTotalVaccinations/population)*100 --> Gives you an ERROR because you can't use a column you just created.   
-- If I only partition by dea.location, the new_vaccinations column will start sum as well. 
-- IMPORTANT to use ORDER BY dea.location and dea.date so that counting only for RollingTotalVaccinations Column 
FROM PortfolioProject..[Covid Death] dea
Join PortfolioProject..[Covid Vaccination] vac
	ON dea.location = vac.location
	and dea.date = vac.date 
--ORDER BY 2,3
)
SELECT*, (RollingTotalVaccinations/Nullif(Population,0))*100 as PercentageRollingTotalVaccinations
FROM PopvsVac

-- VISUALIZATION 
CREATE VIEW PercentageRollingTotalVaccination as
WITH PopvsVac (Continent, Location, Date, Population, New_Vaccinations, RollingTotalVaccinations)
AS
(
SELECT dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations
, SUM(vac.new_vaccinations) OVER (Partition by dea.location ORDER BY dea.location, dea.date) as RollingTotalVaccinations
--, (RollingTotalVaccinations/population)*100 --> Gives you an ERROR because you can't use a column you just created.  USE CTE ór 
-- If I only partition by dea.location, the new_vaccinations column will start sum as well. IMPORTANT to use ORDER BY dea.location and dea.date so that counting only for TotalVaccinations Column 
FROM PortfolioProject..[Covid Death] dea
JOIN PortfolioProject..[Covid Vaccination] vac
	ON dea.location = vac.location
	and dea.date = vac.date 
--ORDER BY 2,3
)
SELECT*, (RollingTotalVaccinations/Nullif(Population,0))*100 as PercentageRollingTotalVaccinations
FROM PopvsVac



-- TEMP TABLE (TEMPORARY TABLE) 
-- JOIN TWO TABLES 
DROP TABLE IF exists #RollingPercentPopulationVaccinated -- If any change is made in the table below, it won't affect the outcome 
CREATE TABLE #RollingPercentPopulationVaccinated 
(
Continent nvarchar(50),
Location nvarchar(50),
Date datetime,
Population numeric,
New_Vaccinations numeric,
RollingTotalVaccinations numeric
)

INSERT INTO #RollingPercentPopulationVaccinated
SELECT dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations
, SUM(vac.new_vaccinations) OVER (Partition by dea.location ORDER BY dea.location, dea.date) as RollingTotalVaccinations
JOIN PortfolioProject..[Covid Vaccination] vac
	ON dea.location = vac.location
	and dea.date = vac.date 
--ORDER BY 2,3

SELECT*, (RollingTotalVaccinations/Nullif(Population,0))*100 as PercentageRollingTotalVaccinations
FROM #RollingPercentPopulationVaccinated

-- CREATING VIEW TO STORE DATA FOR VISUALIZATION 
CREATE VIEW RollingPercentPopulationVaccinated as 
SELECT dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations
, SUM(vac.new_vaccinations) OVER (Partition by dea.location ORDER BY dea.location, dea.date) as RollingTotalVaccinations
--, (RollingTotalVaccinations/population)*100 --> Gives you an ERROR because you can't use a column you just created.  USE CTE ór 
-- If I only partition by dea.location, the new_vaccinations column will start sum as well. IMPORTANT to use ORDER BY dea.location and dea.date so that counting only for TotalVaccinations Column 
FROM PortfolioProject..[Covid Death] dea
JOIN PortfolioProject..[Covid Vaccination] vac
	ON dea.location = vac.location
	and dea.date = vac.date 
--ORDER BY 2,3

SELECT*
FROM RollingPercentPopulationVaccinated

CREATE VIEW DeathCountbyContinent as
SELECT continent, MAX(total_deaths) as TotalDeathCount
FROM PortfolioProject..[Covid Death]
--WHERE location in ('Canada', 'Germany', 'South Korea', 'United States')
GROUP BY continent
--ORDER BY TotalDeathCount desc

SELECT*
FROM DeathCountbyContinent

CREATE VIEW DailyCovidCasePercentage as 
SELECT continent, location, date, population, total_cases, (total_cases/population)*100 as CasePercentage
FROM PortfolioProject..[Covid Death]
WHERE location in ('Canada', 'Germany', 'South Korea', 'United States')
--ORDER BY 1,2

-- TOTAL CASES, TOTAL DEATHS, FULLY VACCINATED BY COUNTRIES 
DROP TABLE if exists #TotalCasesTotalDeathTotalVaccinated -- If any change is made in the table below, it won't affect the outcome 
CREATE TABLE #TotalCasesTotalDeathTotalVaccinated
(
Continent nvarchar(50),
Location nvarchar(50),
Date datetime,
Population numeric,
New_Cases numeric,
New_Deaths numeric,
People_Fully_Vaccinated numeric,
Total_Cases numeric,
Total_Death numeric,
Total_Fully_Vaccinated numeric, 
)
INSERT INTO #TotalCasesTotalDeathTotalVaccinated
SELECT dea.continent, dea.location, dea.date, dea.population, dea.new_cases, dea.new_deaths, vac.people_fully_vaccinated
, SUM(dea.new_cases) OVER(Partition by dea.location ORDER BY dea.location, dea. date, dea.population ) as Total_Cases 
, SUM(dea.new_deaths) OVER (Partition by dea.location ORDER BY dea.location, dea. date, dea.population) as Total_Deaths
, SUM(vac.people_fully_vaccinated) OVER (Partition by dea.location ORDER BY dea.location, dea. date, dea.population) as Total_Fully_Vaccinated 
FROM PortfolioProject..[Covid Death] dea 
Join PortfolioProject..[Covid Vaccination] vac
	ON dea.location = vac.location
	and dea.date = vac.date 
	and dea.population = vac.population 
--ORDER BY 1,2,3

SELECT Continent, location, date, Population, total_cases, total_death, total_fully_vaccinated 
FROM #TotalCasesTotalDeathTotalVaccinated

-- VISUALIZATION 
CREATE VIEW TotalCasesTotalDeathTotalVaccinated as
SELECT dea.continent, dea.location, dea.date, dea.population, dea.new_cases, dea.new_deaths, vac.people_fully_vaccinated
, SUM(dea.new_cases) OVER(Partition by dea.location ORDER BY dea.location, dea. date, dea.population ) as Total_Cases 
, SUM(dea.new_deaths) OVER (Partition by dea.location ORDER BY dea.location, dea. date, dea.population) as Total_Deaths
, SUM(vac.people_fully_vaccinated) OVER (Partition by dea.location ORDER BY dea.location, dea. date, dea.population) as Total_Fully_Vaccinated 
FROM PortfolioProject..[Covid Death] dea 
Join PortfolioProject..[Covid Vaccination] vac
	ON dea.location = vac.location
	and dea.date = vac.date 
	and dea.population = vac.population 
--ORDER BY 1,2,3
