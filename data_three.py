from statistic_output import csv_to_df, statistics

df = csv_to_df('dataThree.csv')

statistics(list(df['x']), list(df['x']))
