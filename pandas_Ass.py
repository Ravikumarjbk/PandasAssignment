import pandas as pd
# course_name = ['Data Science', 'Machine Learning', 'Big Data', 'Data Engineer']
# duration = [2,3,6,4]
# df = pd.DataFrame({'course_name': course_name, 'duration': duration})

#1
# df = df.iloc[2, [0,1]]
# print(df)

#2
''''loc: The loc function is label-based and is used to select rows and columns by label or condition
iloc: The iloc function is integer-based and is used to select rows and columns by integer location or condition.
 It allows you to access data based on the integer position of the rows and columns rather than their labels'''

#3
# new_df = df.reindex([3,0,1,2])
# print(new_df)
# # new_df = new_df.loc[2]
# new_df = new_df.iloc[2] #yes it gives one index previous
# print(new_df)

#Q4

# import pandas as pd
# import numpy as np
# columns = ['column_1', 'column_2', 'column_3', 'column_4', 'column_5', 'column_6']
# indices = [1,2,3,4,5,6]
#
# df1 = pd.DataFrame(np.random.rand(6,6), columns = columns, index = indices)
# df1 = df1[['column_1', 'column_2', 'column_3', 'column_4', 'column_5', 'column_6']].mean()
# print(df1)
# df1 = df1['column_2'].std()
# print(df1)

#Q5
# df1.loc[2, 'column_2'] = 'patna'
# df1['column_2'] = pd.to_numeric(df1['column_2'], errors='coerce')
# df1_mean = df1['column_2'].mean()
# print(df1_mean)

#Q6

""""The pandas.DataFrame and pandas.Series objects provide several window functions that you can use. Here are some commonly used window functions in Pandas:

Rolling: The rolling function creates a rolling window object, 
which can be used to perform calculations on a fixed-size sliding window of data. 
It provides methods like mean(), sum(), std(), and more to compute rolling statistics.

Expanding: The expanding function creates an expanding window object, 
which expands the window size with each data point. 
It allows you to calculate cumulative statistics like cumulative sum, cumulative mean, or cumulative maximum.

EWM (Exponentially Weighted Moving): 
The ewm function calculates exponentially weighted moving averages or other statistics. It assigns weights to data points based on"""

#Q7
# import datetime
# date = datetime.datetime.now()
# current_year = date.strftime("%Y")
# current_month = date.strftime('%B')
# print(f"current year {current_year}, currect_month {current_month}")

#Q8
# date1 = input("Enter the first date (YYYY-MM-DD): ")
# date2 = input("Enter the second date (YYYY-MM-DD): ")
# date1 = pd.to_datetime(date1)
# date2 = pd.to_datetime(date2)
# date_diffrence = date2 - date1
# days = date_diffrence.days
# hours = date_diffrence.seconds // 3600
# minutes = (date_diffrence.seconds % 3600) // 60
#
# # Display the result
# print(f"Time difference: {days} days, {hours} hours, {minutes} minutes.")

#Q9

# file_path = "C:\\Users\\emanrva\\OneDrive - Ericsson\\Desktop\\pro_s_circledash\\A\\titanic passenger list.csv"
#
# user_path = input("Enter the file path of the CSV file: ")
#
# # Read the CSV file
# df = pd.read_csv(user_path)
# print(df)
# # # Prompt the user to enter the column name
# column_name = input("Enter the column name to convert to categorical: ")
# #
# # # Prompt the user to enter the category order
# category_order = input("Enter the category order (comma-separated values): ").split(',')
# #
# # # Convert the specified column to categorical
# df[column_name] = pd.Categorical(df[column_name], categories=category_order, ordered=True)
# #
# # # Sort the data based on the categorical column
# sorted_data = df.sort_values(column_name)
# #
# # # Display the sorted data
# print(sorted_data)

#11
# file_path = "C:\\Users\\emanrva\\OneDrive - Ericsson\\Desktop\\pro_s_circledash\\A\\student_data.csv"
# user_file = input("Enter file path: ")
# df = pd.read_csv(user_file)
# df_mean = df['test_score'].mean()
# df_mode = df['test_score'].mode()
# df_median = df['test_score'].median()
# print(f"test_score, mean: {df_mean}, mode: {df_mode}, median: {df_median}")


