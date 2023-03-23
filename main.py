import pandas as pd

# Define the file paths for the before and after CSV files
before_file = 'before.csv'
after_file = 'after.csv'

# Read the CSV files and store them as dataframes
before_df = pd.read_csv(before_file)
after_df = pd.read_csv(after_file)

# Merge the dataframes using the index
merged_df = pd.merge(before_df, after_df, left_index=True, right_index=True)

# Create a new column to indicate whether each row is an addition or deletion
merged_df['change'] = 'unchanged'
merged_df.loc[merged_df['after_column'].isnull(), 'change'] = 'deleted'
merged_df.loc[merged_df['before_column'].isnull(), 'change'] = 'added'

# Display the additions and deletions as separate dataframes
added_df = merged_df.loc[merged_df['change'] == 'added']
deleted_df = merged_df.loc[merged_df['change'] == 'deleted']

print('Added rows:')
print(added_df)
print('Deleted rows:')
print(deleted_df)