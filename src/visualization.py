import plotly.express as px
import plotly.graph_objects as go

def plot_views(df):
    return px.line(df, x='date', y='views', title='Daily Views')

def plot_ma(df):
    f = go.Figure()
    f.add_trace(go.Scatter(x=df['date'], y=df['views'], opacity=0.4, name='Views'))
    
    if 'views_7d' in df.columns:
        f.add_trace(go.Scatter(x=df['date'], y=df['views_7d'], name='7d MA'))
    if 'views_14d' in df.columns:
        f.add_trace(go.Scatter(x=df['date'], y=df['views_14d'], name='14d MA'))
        
    f.update_layout(title='Views & Moving Averages', hovermode='x unified')
    return f

def plot_spikes(df):
    f = go.Figure()
    f.add_trace(go.Scatter(x=df['date'], y=df['views'], name='Views'))
    
    if 'is_spike' in df.columns:
        s = df[df['is_spike']]
        f.add_trace(go.Scatter(
            x=s['date'], y=s['views'], mode='markers', name='Spikes (Z>2)',
            marker=dict(color='red', size=8)
        ))
    
    f.update_layout(title='Detected Trend Spikes', hovermode='closest')
    return f

def plot_topics(df):
    if len(df) == 0: return go.Figure()
    f = px.bar(df, x='score', y='word', orientation='h', title='Top Topics in Titles')
    f.update_layout(yaxis={'categoryorder':'total ascending'})
    return f

def plot_topic_lines(df):
    if len(df) == 0: return go.Figure()
    return px.line(df, x='date', y='views', color='word', title='Topic Views Over Time')
