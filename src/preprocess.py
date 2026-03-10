import pandas as pd

def clean_and_prep(data):
    # map columns to what the app expects
    renames = {'published_at': 'publish_time', 'fetch_date': 'trending_date', 'comments': 'comment_count'}
    data = data.rename(columns=renames)
    
    # drop nas
    data = data.dropna()
    
    # fix the date fields
    if 'trending_date' in data.columns:
        data['trending_date'] = pd.to_datetime(data['trending_date'], format='mixed', errors='coerce')
    if 'publish_time' in data.columns:
        data['publish_time'] = pd.to_datetime(data['publish_time'], format='mixed', errors='coerce')
        
    date_cols = [c for c in ['trending_date', 'publish_time'] if c in data.columns]
    if date_cols:
        data = data.dropna(subset=date_cols)
        
    return data
