def daily_agg(df):
    res = df.copy()
    res['date'] = res['trending_date'].dt.date
    
    cols_to_sum = [c for c in ['views', 'likes', 'dislikes', 'comment_count'] if c in res.columns]
    
    # group by the date and sum everything
    return res.groupby('date')[cols_to_sum].sum().reset_index().sort_values('date')

def get_stats(df, col='views'):
    return {
        'mean': df[col].mean(),
        'var': df[col].var(),
        'std': df[col].std()
    }

def add_zscore(df, col='views'):
    st = get_stats(df, col)
    # check to avoid dividing zero
    if st['std'] == 0:
        df[f'{col}_z'] = 0
    else:
        df[f'{col}_z'] = (df[col] - st['mean']) / st['std']
    return df
