import pandas as pd

# Creating a DataFrame from a dictionary
data = {'Name': ['Saim', 'Saboor', 'Hamza','Asif'],
        'Age': [35, 23, 22,38],
        'City': ['London', 'Lucknow', 'Vadodra','Kolkata']}

df = pd.DataFrame(data)

# Displaying the DataFrame
print(df)