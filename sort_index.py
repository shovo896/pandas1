import pandas as pd

# Corrected data (fixed 'Bob' string and used numbers for Age and Score)
data = {
    'Name': ['Alice', 'Bob'],
    'Age': [28, 29],
    'Score': [85, 55]
}

# DataFrame with custom index
df = pd.DataFrame(data, index=[1, 0])

# Print the original DataFrame
print(df)

# Print the DataFrame as string with index
print(df.to_string(index=True))
print("\n")

# Sort the DataFrame by index and print
sorted_df = df.sort_index()
print(sorted_df.to_string(index=True))
