import numpy as np
import pandas as pd

def make_frame(price, customers, purchased):
    df = pd.DataFrame({'price': price,
                       'num_customers': customers,
                       'num_sales': purchased
    })

    df['sales_per_customer'] = df['num_sales'] / df['num_customers']
    df['amt_made'] = df['num_sales'] * price
    df['profit'] = df['amt_made'] - 0.4*df['num_sales']
    df['profit_per_customer'] = df['profit']/df['num_customers']

    return df

def make_summary(df):
    summary_df = df.sum(axis=0)
    summary_df['price'] = df['price'].mean()
    summary_df['sales_per_customer'] = summary_df['num_sales']/summary_df['num_customers']
    summary_df['profit_per_customer'] = summary_df['profit']/summary_df['num_customers']

    return summary_df

def format_frame(df):
    if type(df) == pd.Series:
        df = pd.DataFrame(df).T

    columns = ['price', 'num_customers', 'num_sales', 'sales_per_customer', 'amt_made', 'profit', 'profit_per_customer']
    msg = ''

    for index, row in df[columns].iterrows():
        price, num_customers, num_sales, sales_per_customer, amount, profit, profit_per_customer = row
        msg += f'| {index+1} | ${price:4.2f} | {num_customers:.0f} | {num_sales:.0f} | {sales_per_customer:8.6f} | ${amount:.2f} | ${profit:.2f} | ${profit_per_customer:8.6f} |\n'
    return msg

control = make_frame(1.50, [6300, 8100, 4500], [390, 0, 180])
variation = make_frame(1.00, [700, 1200, 500], [80, 0, 50])
print(format_frame(control))
print(format_frame(make_summary(control)))

print("\n\n\n")

print(format_frame(variation))
print(format_frame(make_summary(variation)))
