import pandas as pd
# Read data from the Excel spreadsheet
df = pd.read_excel('data.xlsx', sheet_name='Sheet1')
# Calculate the average of column A
average = df['A'].mean()
print('Average of column A:', average)
# Find the maximum value in column B
maximum = df['B'].max()
print('Maximum value in column B:', maximum)
# Create a new Excel file and write the results
output_df = pd.DataFrame({'Average': [average], 'Maximum': [maximum]})
output_df.to_excel('output.xlsx', sheet_name='Sheet1', index=False)
print('Results written to output.xlsx')