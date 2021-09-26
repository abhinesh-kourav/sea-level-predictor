import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(20,5)) 
    plt.scatter(x,y)

    # Create first line of best fit
    res = linregress(x,y)
    pred_x = pd.Series([i for i in range(1880,2051)])
    pred_y = res.slope*pred_x+res.intercept
    plt.plot(pred_x, pred_y,'red')

    # Create second line of best fit
    new_df = df.loc[df['Year']>=2000]
    new_x = new_df['Year']
    new_y = new_df['CSIRO Adjusted Sea Level']
    res2 = linregress(new_x,new_y)
    pred_x2 = pd.Series([i for i in range(2000,2051)])
    pred_y2 = pred_x2*res2.slope + res2.intercept
    plt.plot(pred_x2, pred_y2,'black')

    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level') 
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()