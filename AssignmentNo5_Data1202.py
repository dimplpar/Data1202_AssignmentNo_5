#PART 1
# Import pandas
import pandas as pd

# Set file path to a variable
input_file_path = r"C:\Users\Durham\Desktop\Duraham\Courses\data1202\vgsales.csv"

# Read Data into a DataFrame
input_raw_data = pd.read_csv(input_file_path)

# Filter DataFrame for proper years
between_00_05 = input_raw_data[(input_raw_data["Year"] >= 2000) & (input_raw_data["Year"] <= 2005)]

print(between_00_05)

#PART 2
# How to create an engine and connect to a database

# import required libraries
import pandas as pd
from sqlalchemy import create_engine
import pymysql

# create engine
engine = create_engine('mysql+pymysql://database:username@localhost/data1202')

# connection string
conn = engine.connect()

# read a simple query into DataFrame
df = pd.read_sql("SELECT * FROM data1202.vgsales_new", conn)

# print DataFrame
print(df.head())

# read a complex query into DataFrame
complex_df = pd.read_sql('''SELECT
    Round(SUM(NA_Sales)) as 'NA_Sales',
    ROUND(SUM(EU_Sales)) as 'EU_Sales',
    ROUND(SUM(JP_Sales)) as 'JP_Sales',
    ROUND(SUM(Global_Sales)) AS 'Global_Sales',
    ROUND((SUM(NA_Sales)/SUM(Global_Sales)) * 100) as 'NA_GlobalShare'

FROM
    data1202.vgsales_new
WHERE
    Genre = 'Action'
        AND Year>= 2005''', conn)

print(complex_df)
