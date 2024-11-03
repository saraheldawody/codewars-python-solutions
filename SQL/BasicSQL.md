# Practice SQL

## Challenge 1 (Revising The Select Query)

### Description
Query all columns for all American cities in the CITY table with populations larger than 100000. The CountryCode for America is USA.

The CITY table is described as follows:

![Challenge 1](https://s3.amazonaws.com/hr-challenge-images/8137/1449729804-f21d187d0f-CITY.jpg "a title")

### Solution

```sql
SELECT *
FROM CITY
WHERE COUNTRYCODE = 'USA'
AND POPULATION > 100000;
```

## Challenge 2 (Revising The Select Query 2)

### Description
Query the NAME field for all American cities in the CITY table with populations larger than 120000. The CountryCode for America is USA.

The CITY table is described as follows:

![Challenge 2](https://s3.amazonaws.com/hr-challenge-images/8137/1449729804-f21d187d0f-CITY.jpg "a title")

### Solution

```sql
SELECT NAME
FROM CITY
WHERE COUNTRYCODE ='USA'
AND POPULATION > 120000;
```

