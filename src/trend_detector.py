from .statistics import add_zscore

def moving_avgs(df, col='views'):
    # compute 7d and 14d averages
    df[f'{col}_7d'] = df[col].rolling(7, min_periods=1).mean()
    df[f'{col}_14d'] = df[col].rolling(14, min_periods=1).mean()
    return df

def find_spikes(df, col='views', limit=2.0):
    z_col = f'{col}_z'
    if z_col not in df.columns:
        df = add_zscore(df, col)
        
    df['is_spike'] = df[z_col] > limit
    return df
