import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv("medical_examination.csv")

# Add 'overweight' column
bmi = df["weight"]/((df["height"]/100)**2)
df['overweight'] = [ 1 if i>25 else 0 for i in bmi]

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df["cholesterol"] = [1 if i > 1 else 0 for i in df["cholesterol"]]
df["gluc"] = [1 if i > 1 else 0 for i in df["gluc"]]

categorical_cols = ['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight']
obj_col = "cardio"

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df, id_vars=[obj_col],value_vars=sorted(categorical_cols))

    # Draw the catplot with 'sns.catplot()'
    fig = sns.catplot(data=df_cat, kind='count', x='variable', hue='value',col=obj_col)
    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df[(df['ap_lo']<=df['ap_hi']) &
                (df['height'] >= df['height'].quantile(0.025)) &
                (df['height']<=df['height'].quantile(0.975)) &
                (df['weight']>=df['weight'].quantile(0.025)) &
                (df['weight']<=df['weight'].quantile(0.975))]
    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(corr)

    # Set up the matplotlib figure
    fig = plt.figure(figsize=(8, 8))
    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr, annot=True, fmt='.1f', mask=mask, cbar_kws={'shrink':0.5}, vmax=.8, center=0.09)

    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
