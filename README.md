# Introduction
•This python code imports csv file.

•It also runs few queries over the data imported from the file

# Steps
PART 1:
1. We have imported the required library to get started with pandas. "pandas" is the library which we have imported which imports all the inbuilt functionality associated with python.

2. Then, we have specified the path for the csv file. The csv file named "vgsales.csv" contains few records of the sales.

3. Additonally, we are fetching data from the csv file and are printing it using the inbuilt 'read_csv()' function. We have also created a variable 'input_raw_data' to store the output of the function.

4. Lastly, we have created a variable named 'between_00_05' which only retreives records from the year 2000 to 2005. 

5. We have used an inbuilt function print() to print the content of the variable 'between_00_05'.

PART 2:
1. Using 'pip install pymysql' we have installed the 'mysql' with python

2. We have imported the required library to get started with pandas. "pandas" is the library which we have imported which imports all the inbuilt functionality associated with python.

3. We have then imported 'create_engine' libraby which is the library used for establishing connection with the database.

4. Then we have imported 'pymysql' which contains all the inbuilt function to work with sql query.

5. Finally, using the inbuilt 'create_engine()' we have created a connection with the database and using connect(), we have connected to it.

6. Using the inbuilt 'read_sql()', we are reading the contents of 'vgsales_new' table of database 'data1202' and are storing it to variable 'df',

7. Using the inbuilt 'head()', we are displaying the contents of the variable 'df'.

8. Finally, we have created a complex query inorder to retrieve the global sales of movies which are released in and after 2005 of Genre 'Action'. For that, we have counted the sum of the columns 'NA_Sales','EU_Sales','JP_Sales','Global_Sales' and have rounded them up. Then, we have calculated the output of 'NA_GlobalShare' by dividing (NA_Sales/Global_SAles)*100. From this, we have chosen the movies of the Genre 'Action' and which are released in and after 2005.

9. This data we have stored in the variable 'complex_df'. Finally, using the inbuilt 'print()', we are printing the contents of the variable 'complex_df'.

# Libraries included in this file
1.pandas - Pandas is the most commonly used open source Python package for data science / data analysis and machine learning tasks.
2.sqlalchemy - SQLAlchemy is a Python SQL toolkit and Object Relational Mapper that provides complete SQL capability and flexibility to application developers.
3.pymysql - It is a Python interface for connecting to a MySQL database server.
