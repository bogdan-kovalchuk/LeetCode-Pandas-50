import pandas as pd

def find_customers(visits: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    merged = visits.merge(transactions, how='left', on='visit_id')
    no_trans = merged[merged['transaction_id'].isna()]
    return no_trans.groupby('customer_id').size().reset_index(name='count_no_trans')