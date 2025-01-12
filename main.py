import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib
matplotlib.use('Agg')  # Use Agg backend for non-interactive plotting
import matplotlib.pyplot as plt
import yfinance as yf
import datetime
import os

# Define the number of columns for the subplot grid
num_columns = 4

# Create a list of tickers for indices and ETFs
indices = ["^GSPC", "^DJI", "^IXIC", "BTC-USD", "ETH-USD"]
etfs = ["XLY", "XLP", "XLE", "XLF", "XLV", "XLI", "XLB", "XLRE", "XLK",
        "XTL", "XLU", "TLT", "SOXX", "IGV", "SKYY", "KWEB",
        "ITA", "PBW", "TAN", "USO", "URNM"]

# Create a figure with subplots
total_plots = len(indices) + len(etfs)
num_rows = (total_plots + num_columns - 1) // num_columns  # Calculate number of rows needed

# Increase figsize for larger plots (width, height)
fig, axs = plt.subplots(num_rows, num_columns, figsize=(60,15 * num_rows))
axs = axs.flatten()  # Flatten to easily iterate over

# Load and display index plots
for i, ticker in enumerate(indices):
    img_path = f"{ticker}.png"  # Assuming images are saved as ticker names
    if os.path.exists(img_path):
        img = plt.imread(img_path)
        axs[i].imshow(img)
        axs[i].set_title(ticker, fontsize=16)  # Increase title font size
        axs[i].axis('off')  # Hide axes

# Load and display ETF plots
for j, ticker in enumerate(etfs):
    img_path = f"{ticker}.png"  # Assuming images are saved as ticker names
    if os.path.exists(img_path):
        img_index = len(indices) + j
        img = plt.imread(img_path)
        axs[img_index].imshow(img)
        axs[img_index].set_title(ticker, fontsize=16)  # Increase title font size
        axs[img_index].axis('off')  # Hide axes

# Read news headlines from CSV file
news_df = pd.read_csv(f"news_titles_{datetime.datetime.now().strftime('%Y-%m-%d')}.csv")

# Display news headlines in the remaining subplots
for k in range(len(news_df)):
    if k < (num_rows * num_columns) - total_plots:
        axs[total_plots + k].text(0.5, 0.5, news_df.iloc[k]['Title'], ha='center', va='center', fontsize=14)
        axs[total_plots + k].axis('off')  # Hide axes

# Adjust layout to prevent overlap and improve spacing
plt.tight_layout()
plt.show()

# Save the combined figure as an image (optional)
plt.savefig("DailyCheck_results.png")