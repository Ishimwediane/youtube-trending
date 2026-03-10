import pandas as pd
import os

def create_sample_dataset(input_file: str, output_file: str, sample_fraction: float = 0.05):
    """
    Reads a large CSV and saves a smaller randomized sample of it.
    This is extremely useful for deploying to free cloud tiers (like Render or Heroku)
    where RAM is limited to 512MB.
    
    Args:
        input_file (str): Path to the original large dataset.
        output_file (str): Path to save the smaller sampled dataset.
        sample_fraction (float): Percentage of data to keep (0.05 = 5%).
    """
    print(f"Loading '{input_file}' to create a smaller sample...")
    
    if not os.path.exists(input_file):
        print(f"Error: {input_file} not found.")
        return
        
    try:
        # Load the massive dataset
        df = pd.read_csv(input_file)
        original_rows = len(df)
        
        # Take a random sample
        sample_df = df.sample(frac=sample_fraction, random_state=42)
        
        # Save it
        sample_df.to_csv(output_file, index=False)
        
        sampled_rows = len(sample_df)
        print(f"Success! Sampled {original_rows} rows down to {sampled_rows} rows ({sample_fraction*100}%).")
        print(f"Saved smaller dataset to: {output_file}")
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # We will read the original and save it as a new file in the data folder
    INPUT_CSV = "data/daily_trending_videos.csv"
    OUTPUT_CSV = "data/daily_trending_videos_sample.csv"
    
    # 5% of 100MB is ~5MB, which will easily run on Render's 512MB free tier
    create_sample_dataset(INPUT_CSV, OUTPUT_CSV, sample_fraction=0.05)
