import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

def get_topics(df, col='title', n=15):
    txt = df[col].dropna()
    if len(txt) == 0:
        return pd.DataFrame()
        
    # get top words ignoring standard english filler
    vec = TfidfVectorizer(stop_words='english', max_features=1000)
    matrix = vec.fit_transform(txt)
    
    scores = matrix.sum(axis=0).A1
    words = vec.get_feature_names_out()
    
    res = pd.DataFrame({'word': words, 'score': scores})
    return res.sort_values('score', ascending=False).head(n).reset_index(drop=True)

def topic_trends(df, words):
    res = []
    tmp = df.copy()
    tmp['dt'] = tmp['trending_date'].dt.date
    
    for w in words:
        # crude regex text search for words in title
        match = tmp[tmp['title'].str.contains(rf'\b{w}\b', case=False, na=False)]
        if len(match) > 0:
            agg = match.groupby('dt')['views'].sum().reset_index()
            agg['word'] = w
            res.append(agg)
            
    if not res:
        return pd.DataFrame()
        
    return pd.concat(res, ignore_index=True).rename(columns={'dt': 'date'})
