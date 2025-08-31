import pandas as pd
df0 = pd.read_csv('daily_sales_data_0.csv')
df1 = pd.read_csv('daily_sales_data_1.csv')
df2 = pd.read_csv('daily_sales_data_2.csv')
df = pd.concat([df0, df1, df2])


df['price'] = df['price'].str.replace('$', '', regex=False).astype(float)

# Compute sales
df['sales'] = df['price'] * df['quantity']

# Conditionally set ModProduct
df = df[df['product'] == 'pink morsel']

data = {
'product': df['product'],
    'sales': df['sales'],

    'date': df['date'],
    'region': df['region'],

}
df = pd.DataFrame(data)
output_df = df[['sales', 'date', 'region']]
output_df.to_csv('formatted_sales.csv', index=False)

print(df)


