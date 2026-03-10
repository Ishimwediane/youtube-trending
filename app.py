import dash
from dash import dcc, html
import pandas as pd
import os

from src.load_data import load_data
from src.preprocess import clean_and_prep
from src.statistics import daily_agg
from src.trend_detector import moving_avgs, find_spikes
from src.topic_analysis import get_topics, topic_trends
import src.visualization as viz

# check for sample first, otherwise use main file
file_to_load = 'data/daily_trending_videos_sample.csv'
if not os.path.exists(file_to_load):
    file_to_load = 'data/daily_trending_videos.csv'

print(f"reading from {file_to_load}...")
raw = load_data(file_to_load)

# start processing if we got data
if raw is not None and not raw.empty:
    df = clean_and_prep(raw)
    daily = daily_agg(df)
    
    daily = moving_avgs(daily)
    daily = find_spikes(daily)
    
    tops = get_topics(df)
    top_words = tops['word'].tolist() if not tops.empty else []
    
    t_trends = topic_trends(df, top_words) if top_words else pd.DataFrame()
    
    # build plots
    p1 = viz.plot_views(daily)
    p2 = viz.plot_ma(daily)
    p3 = viz.plot_spikes(daily)
    p4 = viz.plot_topics(tops)
    p5 = viz.plot_topic_lines(t_trends)
    
else:
    print("no data found or empty dataframe")
    import plotly.graph_objects as go
    empty = go.Figure().update_layout(title="No Data")
    p1 = p2 = p3 = p4 = p5 = empty

# set up dash app
app = dash.Dash(__name__)
server = app.server

app.layout = html.Div([
    html.H2("YouTube Trends Dashboard", style={'textAlign': 'center'}),
    html.Hr(),
    
    html.Div([
        html.Div([dcc.Graph(figure=p1)], style={'width': '49%', 'display': 'inline-block'}),
        html.Div([dcc.Graph(figure=p2)], style={'width': '49%', 'display': 'inline-block'})
    ]),
    
    html.Div([dcc.Graph(figure=p3)]),
    html.Hr(),
    
    html.Div([
        html.Div([dcc.Graph(figure=p4)], style={'width': '40%', 'display': 'inline-block', 'verticalAlign': 'top'}),
        html.Div([dcc.Graph(figure=p5)], style={'width': '59%', 'display': 'inline-block', 'verticalAlign': 'top'})
    ])
], style={'padding': '20px'})

if __name__ == '__main__':
    app.run(debug=True, port=8050)
