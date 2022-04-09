import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", index_col = "date")

# Clean data
df = df.drop(df[(df['value']<df['value'].quantile(0.025))].index)
df = df.drop(df[(df['value']>df['value'].quantile(0.975))].index)

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December']
def draw_line_plot():
    # Draw line plot
    fig = plt.figure(figsize = (20, 10))
    plt.plot(df['value'])
    plt.xlabel("Date")
    plt.ylabel("Page Views")
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar["month"] = pd.DatetimeIndex(df_bar.index).month
    df_bar["year"] = pd.DatetimeIndex(df_bar.index).year
    df_bar = df_bar.groupby(["year", "month"])['value'].mean()
    df_bar = df_bar.unstack()
  
    # Draw bar plot
    fig = df_bar.plot(kind= 'bar').figure
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(title= 'Months', labels = months)

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = pd.DatetimeIndex(df_box["date"]).year
    df_box['month'] = pd.DatetimeIndex(df_box["date"]).month
    
  # Draw box plots (using Seaborn)
    fig, axes = plt.subplots(1, 2, figsize=(20,5))
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')
    sns.boxplot(ax=axes[0], x = "year", y = "value", data = df_box)

    axes[1].set_title('Month-wise Box Plot (Trend)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')
    sns.boxplot(ax=axes[1], x = "month", y = "value", data = df_box) 
    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
