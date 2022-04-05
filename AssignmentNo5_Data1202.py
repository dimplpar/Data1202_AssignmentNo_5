# Import pandas
import pandas as pd

# Set file path to a variable
input_file_path = r"C:\Users\Durham\Desktop\Duraham\Courses\data1202\vgsales.csv"

# Read Data into a DataFrame
input_raw_data = pd.read_csv(input_file_path)

# Filter DataFrame for proper years
between_00_05 = input_raw_data[(input_raw_data["Year"] >= 2000) & (input_raw_data["Year"] <= 2005)]

print(between_00_05)
