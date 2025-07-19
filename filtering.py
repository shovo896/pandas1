data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [24, 27, 22, 32, 29],
    'City': ['Dhaka', 'Chittagong', 'Dhaka', 'Khulna', 'Sylhet']
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# Method 1: Boolean Indexing
filtered_df1 = df[df['Age'] > 25]
print("\nMethod 1 - Boolean Indexing (Age > 25):")
print(filtered_df1)

# Method 2: query()
filtered_df2 = df.query("Age > 25")
print("\nMethod 2 - query() (Age > 25):")
print(filtered_df2)

#  Method 3: loc[] with condition
filtered_df3 = df.loc[df['Age'] > 25]
print("\nMethod 3 - loc[] with condition (Age > 25):")
print(filtered_df3)

#  Method 4: apply() with lambda
filtered_df4 = df[df['Age'].apply(lambda x: x > 25)]
print("\nMethod 4 - apply() with lambda (Age > 25):")
print(filtered_df4)
