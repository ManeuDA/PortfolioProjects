
/*

DATA CLEANING 
Queries using INSERT(), UPDATE(), CASE Statement, LEN(), SUBSTRING(), TRIM(), DISTINCT(), MIN(), MAX(), CAST(), CONCAT(), COALESCE()

*/

/*

1. Queries using INSERT(), UPDATE(), CASE Statement, LEN(), SUBSTRING(), TRIM()

*/

-- Select Database Customer Table 
SELECT*
FROM [Google Projects]..[Customer-Table---Sheet1]

-- Insert additional Info into existing Table 
INSERT INTO [Google Projects]..[Customer-Table---Sheet1]
	(customer_id, address, city, state, zipcode, country)
VALUES
	(2645, '333 SQL Road', 'Jackson', 'MI', 49202, 'US')

-- Update the existing Table 
UPDATE [Google Projects]..[Customer-Table---Sheet1]
SET name = 'Alexander Bloom', address = '234 Flower Street'
WHERE customer_id = 2645

SELECT*
FROM [Google Projects]..[Customer-Table---Sheet1]
WHERE customer_id = 2645

-- Find Duplicate: when there is duplicate, more than customer_id will show.
SELECT customer_id, name 
FROM [Google Projects]..[Customer-Table---Sheet1]

-- REMOVE DUPLICATE: Add DISTINCT will elminate duplicate data 
SELECT 
	DISTINCT customer_id
FROM [Google Projects]..[Customer-Table---Sheet1]

-- CASE Statement: it goes thru one or more conditions and returns a value as soon as a condition is met 
SELECT 
	customer_id,
	CASE
		WHEN name = 'Korey Savaga' THEN 'Korey Savage'
		WHEN name = 'Magnolia Crraig' THEN 'Magnolia Craig' 
		ELSE name 
		END AS cleaned_name 
FROM [Google Projects]..[Customer-Table---Sheet1]

	

-- Cleaning String Texts: Query below shows length of country, which is 2 letters. If the data shows more than 2, then it is needed to be identified 
SELECT
	LEN(country) AS Letters_in_country
FROM [Google Projects]..[Customer-Table---Sheet1]

-- Find the wrong data 
SELECT
	country
FROM [Google Projects]..[Customer-Table---Sheet1]
WHERE 
	LEN(country) > 2  -- USA came up instead of US 

-- SUBSTRING(): Since the data is not our own, it need to be accounted under the SUBSTRING()
-- Query below will show the data includes all substring with two letters 'US', meaning data includes both string 'US' and 'USA' 
SELECT
	DISTINCT customer_id --Distinct removed the duplicate 
FROM
	[Google Projects]..[Customer-Table---Sheet1]
WHERE
	SUBSTRING(country,1,2) = 'US' --SUBSTRING(column, number that letter is positioned, how many number that needs to be shown) = 'US' (letter)

-- TRIM(): Removes all whitespaces 
SELECT state
FROM
	[Google Projects]..[Customer-Table---Sheet1]
WHERE 
	LEN(state) > 2 

SELECT 
	DISTINCT customer_id
FROM
	[Google Projects]..[Customer-Table---Sheet1]
WHERE 
	TRIM(state) = 'OH'

/*

2. Queries using DISTINCT(), MIN(), MAX(), UPDATE, TRIM() 

*/



-- NEW QUERY from automobile_data

SELECT DISTINCT*
FROM [Google Projects]..automobile_data 

--Remove Duplicate
SELECT DISTINCT fuel_type
FROM [Google Projects]..automobile_data 

--New Columns
SELECT MIN(length) AS min_length, MAX(length) AS max_length 
FROM [Google Projects]..automobile_data 

-- FIND 'blank' data 
SELECT*
FROM [Google Projects]..automobile_data 
WHERE num_of_doors = ''

-- Update 'blank' data 
UPDATE
	[Google Projects]..automobile_data
SET
	num_of_doors = 'four' --update '' as 'four' 
WHERE
	make = 'mazda' -- 'dodge' 
	AND fuel_type = 'diesel' --'gas' 
	AND body_style = 'sedan';

-- Find Error - Misspelling 
SELECT DISTINCT num_of_cylinders
FROM [Google Projects]..automobile_data 

-- Update the Error 
UPDATE
	[Google Projects]..automobile_data
SET
	num_of_cylinders = 'two' 
WHERE
	num_of_cylinders = 'tow'

-- Error : compression values should range from 7 - 23
SELECT 
	MIN(compression_ratio) AS min_compression_ratio, 
	MAX(compression_ratio) AS max_compression_ratio
FROM [Google Projects]..automobile_data -- Result show range 7-70
 
-- Query without row 70 
SELECT 
	MIN(compression_ratio) AS min_compression_ratio, 
	MAX(compression_ratio) AS max_compression_ratio
FROM [Google Projects]..automobile_data 
WHERE
	compression_ratio <> 70  -- query without the row with 70

-- Check how many row with value 70
SELECT 
	MIN(compression_ratio) AS min_compression_ratio, 
	MAX(compression_ratio) AS max_compression_ratio
FROM [Google Projects]..automobile_data 
WHERE
	compression_ratio = 70 

-- Delete
DELETE [Google Projects]..automobile_data 
WHERE compression_ratio = 70 

-- Extra whitespace 
SELECT 
	DISTINCT drive_wheels
FROM [Google Projects]..automobile_data 

-- Find whitespace 
SELECT 
	DISTINCT drive_wheels, 
	LEN(drive_wheels) AS string_length --  whitespace will show as extra length 
FROM [Google Projects]..automobile_data 

-- TRIM()
UPDATE [Google Projects]..automobile_data 
SET drive_wheels = TRIM(drive_wheels)
WHERE 1=1 -- read as where true 

SELECT 
	MIN(price) AS min_price, 
	MAX(price) AS max_price 
FROM [Google Projects]..automobile_data 

/*

3. Queries using CAST(), CONCAT(), COALESCE(), WHERE date BETWEEN '' AND ''

*/

--CAST(): Can be used to convert anythong from one data type to another
-- Here purchase_price was saved as string which is a wrong data type

SELECT
	purchase_price
FROM 
	[Google Projects]..[Lauren-s-Furniture-Store-Transaction-Table]
ORDER BY
	purchase_price DESC -- To see the price from highest to lowest -- Here the first letter 8 was showing as highest
-- to Change the data type

SELECT
	CAST(purchase_price AS float) 
FROM 
	[Google Projects]..[Lauren-s-Furniture-Store-Transaction-Table]
ORDER BY
	CAST(purchase_price AS float) DESC -- In Bigquery use FLOAT64 

SELECT
	CAST(date AS date) AS date_only,
	purchase_price
FROM
	[Google Projects]..[Lauren-s-Furniture-Store-Transaction-Table]
WHERE 
	date BETWEEN '2020-12-01' AND '2020-12-31'

-- CONCAT(): Adds strings together to create new text strings that can be used as unique keys 
SELECT
	CONCAT(product_code, product_color) AS new_product_code
FROM
	[Google Projects]..[Lauren-s-Furniture-Store-Transaction-Table]
WHERE 
	product = 'couch'

-- COALESCE(): Can be used to return non-null values in a list 

SELECT*
FROM 
	[Google Projects]..[Lauren-s-Furniture-Store-Transaction-Table]

SELECT
	COALESCE(product, product_code) AS product_info
FROM 
	[Google Projects]..[Lauren-s-Furniture-Store-Transaction-Table]