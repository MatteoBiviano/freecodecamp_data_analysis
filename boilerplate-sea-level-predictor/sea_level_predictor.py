import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    x = np.arange(df['Year'].min(), 2050, 1)
    reg = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    
    y = x*reg.slope + reg.intercept

    plt.plot(x,y)


    # Create second line of best fit
    new_df = df[df['Year'] >= 2000]

    reg = linregress(new_df['Year'], new_df['CSIRO Adjusted Sea Level'])
    x = np.arange(2000,2050,1)
    print(x)
    y = x*reg.slope + reg.intercept
    print(y)
    plt.plot(x,y)

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()