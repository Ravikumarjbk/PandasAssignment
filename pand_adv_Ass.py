import pandas as pd
#Q1
# s1 = {'name':['ravi', 'mohit', 'sreya', 'rohit'],
#      'colllege': ['nhce', 'ims', 'DU', 'JNU'],
#      'sex':['male','male','female', 'male'],
#      'marks':[80,89,77,90]}
# df = pd.DataFrame(s1)
# g = df.groupby(['marks']).mean()
# df.set_index('name', inplace=True)
# df.drop('marks', axis=1)
# df.rename(columns={'sex':'Gender'})
# df = df.iloc[:1, [2]]
# df.reindex(['rohit', 'sreya', 'ravi'])

#Q2
# def reindex_dataframe(df):
#     new_index = pd.RangeIndex(start=1, stop=len(df)*2, step=2)
#     df = df.reset_index(drop=True)
#     df.index = new_index
#     return df
#
# # Example usage:
# # Assuming you have a DataFrame called df with columns 'A', 'B', and 'C'
# df = pd.DataFrame({'A','B', 'c'})
# new_df = reindex_dataframe(df)

#Q3
# s3 = {'values':[1,2,3,4,5]}
# df3 = pd.DataFrame(s3)
# def sum_of_first_three_val(data):
#     result = sum(df3['values'].head(3))
#     return result
# store = sum_of_first_three_val(df3)
# print(store) # 6

#Q4

# l = ['patna', 'delhi','banglore', 'mumbai']
# df = pd.DataFrame(l, columns=['Text'])
#
# def add_word_count_column(df):
#     df['Word_Count'] = df['Text'].apply(lambda x: len(str(x).split()))
#     return df
#
# # Example usage:
# # Assuming you have a DataFrame called df with a column 'Text'
#
# new_df = add_word_count_column(df)
# print(new_df)

#Q5

# df = {'A': [1,2,3], 'B': [4,5,6]}
# df = pd.DataFrame(df)
# print(df.size)#it giving total no of element in dataframe
# print(df.shape)#it gives dimension of dataframe in the form of row and column

#Q6

# for read excel file we used to  pd.read_excel(path)

#7
# email = ['rainarn@gmail.com', 'sukeshsk@gamil.com', 'raginirg@gamil.com']
# df = pd.DataFrame(email, columns=['Email'])
# def username_add_in_other_column(data):
#     df['username'] = df['Email'].str.split('@').str[0]
#     return df
# result = username_add_in_other_column(df)
# print(result)

#Q8

# s2 = {'A': [6,4,1,2,7,8],
#       'B': [1,9,4,2,7,6],
#       'c': [1,5,8,3,5,8]}
# df = pd.DataFrame(s2)
# df1 = df[df['A'] > 5]
# df2 = df[df['B'] < 10]
# new_df = df[(df['A'] > 5) & (df['B'] < 10)]
# print(new_df)

#Q9

# value = [45,78,90,12,4,23,34]
# df = pd.DataFrame(value, columns=['Values'])
# df = df['Values'].mean()
# df = df['Values'].median()
# df = df['Values'].mode()
# print(df)

#Q10

# def calculate_moving_object(df, sales_column = 'Sales', date_column='Date'):
#     df = df.sort_values(by=date_column)
#     df['MovingAverage'] = df[sales_column].rollimg(window=7, meanperiods=1).mean()
#     return df
# res = calculate_moving_object(df)

#Q11

# df = pd.date_range(start='2023-7-01', end='2023-07-07')
# df = pd.DataFrame(df, columns=['Date'])
# df['weekday_name'] = df['Date'].dt.strftime('%A')
# print(df)

#Q12

# def select_date(df):
#     df['Date'] = pd.to_datetime(df['Date'])
#     start_date = pd.to_datetime('2023-06-10')
#     end_date = pd.to_datetime('2023-07-10')
#     df = df.loc[(df['Date'] >= start_date) & (df['Date'] <= end_date)]
#     return df
# d = {'Date': ['2023-06-14', '2023-06-15', '2023-06-14', '2023-06-14', '2023-06-14']}
# df = pd.DataFrame(d)
# res = select_date(df)
# print(res)

#Q13

# import pandas as pd


