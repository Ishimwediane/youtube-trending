# YouTube Trends Dashboard

A small dashboard project to visualize daily YouTube trending videos. Built with Pandas and Plotly Dash.

## Running locally

1. Put your CSV file inside the `data/` folder. It should be named `daily_trending_videos.csv`.
2. Install the stuff in `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the app:
   ```bash
   python app.py
   ```
4. Open the link in your browser (usually `http://127.0.0.1:8050/`).

## Deploying to Render
I included a `render.yaml` so you can just push this repo to GitHub and connect it to a free Render web service.
If the dataset is too big for the free tier, run `python create_sample.py` to make a smaller 5% version of the dataset first, and just upload that one.
