
################################################################
#                                                              #
#            MS984 : DAIP CASE 4 - Group 5                     #
#       Sports Statistician Moderate Mistakes Analysis         #
#                                                              #
################################################################

# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style='whitegrid')

# Load data
file_path = 'C:/Users/Admin/Downloads/GS Eng.Sco. Moderate mistakes 22-24.xlsx'
df = pd.read_excel(file_path, sheet_name='Export')

# Display initial rows
df.head()


# Data preparation and cleaning
df['StartDate'] = pd.to_datetime(df['StartDate'])
df['Year'] = df['StartDate'].dt.year
df.info()

# Mistake Type Visualization (Adjusted to Avoid Scrollbar)
plt.figure(figsize=(10, 4))  # Adjusted height for better fit
formal_palette = ['#4C72B0', '#8172B3']

# Countplot (horizontal bars, thinner)
sns.countplot(
    y='MistakeType',
    data=df,
    palette=formal_palette,
    hue='MistakeType',
    legend=False,
    width=0.4  # Slightly thinner bars for visual clarity
)

# Titles and labels clearly visible
plt.title('Frequency of Mistake Types', fontsize=15, fontweight='bold')
plt.xlabel('Count', fontsize=12)
plt.ylabel('Mistake Type', fontsize=12)

# Annotate each bar with counts clearly
ax = plt.gca()
for container in ax.containers:
    ax.bar_label(container, fontsize=11, padding=4)

# Adjust layout and margins to avoid scrollbars and overlap
plt.tight_layout(pad=2.0)

# Display clearly fitted plot
plt.show()


# Visualize Mistake Categories 
plt.figure(figsize=(8,5))
sns.countplot(y='MistakeTypeCategory', data=df, hue='MistakeTypeCategory', palette='coolwarm', legend=False)
plt.title('Frequency of Mistake Categories')
plt.xlabel('Count')
plt.ylabel('Mistake Category')
plt.show()

# Errors per year with professional light shades
errors_per_year = df['Year'].value_counts().sort_index()

# Define formal, light-shaded color palette
light_formal_colors = ['#9ecae1', '#a1d99b', '#bcbddc']  # soft shades of blue, green, purple

# Create bar plot
ax = errors_per_year.plot(kind='bar', color=light_formal_colors, figsize=(9, 5), width=0.6)

# Title and axis labels clearly defined
plt.title('Yearly Moderate Mistakes', fontsize=16, fontweight='bold')
plt.xlabel('Year', fontsize=14)
plt.ylabel('Number of Errors', fontsize=14)

# Annotate bars with clear labels
for container in ax.containers:
    ax.bar_label(container, fontsize=12, padding=3)

# Clean up layout to ensure clarity
plt.tight_layout()

# Display the plot
plt.show()

import numpy as np

# Data preparation
events_per_year = df.groupby('Year')['Event'].nunique()
errors_per_year = df['Year'].value_counts().sort_index()

# Calculate correlation
correlation = events_per_year.corr(errors_per_year)
print(f'Correlation between total events and errors: {correlation:.2f}')

# Bar positioning
x = np.arange(len(events_per_year))  # positions for each group
width = 0.35  # width of the bars

# Plot bars clearly side-by-side
fig, ax = plt.subplots(figsize=(10, 6))
bars1 = ax.bar(x - width/2, events_per_year, width, label='Events', color='#9ecae1')
bars2 = ax.bar(x + width/2, errors_per_year, width, label='Errors', color='#a1d99b')

# Labels and titles
ax.set_title('Total Events vs Errors per Year', fontsize=16, fontweight='bold')
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Count', fontsize=14)
ax.set_xticks(x)
ax.set_xticklabels(events_per_year.index)

# Bar annotations
ax.bar_label(bars1, padding=3, fontsize=12)
ax.bar_label(bars2, padding=3, fontsize=12)

# Legend positioning
ax.legend()

# Adjust layout clearly
fig.tight_layout()

# Display plot
plt.show()

plt.figure(figsize=(12,7)) # increase figure width for clarity
ax = sns.countplot(data=df, x='MistakeTypeCategory', hue='MistakeType', palette='Set2')

# Rotate x-axis labels for clear visibility
plt.xticks(rotation=45, ha='right')

# Set titles and labels clearly
plt.title('Mistake Category by Mistake Type', fontsize=14, pad=15)
plt.xlabel('Mistake Category', fontsize=12, labelpad=10)
plt.ylabel('Count', fontsize=12, labelpad=10)

# Adjust legend placement
plt.legend(title='Mistake Type', fontsize=10, title_fontsize=11)

# Automatically adjusts subplot parameters for best layout fit
plt.tight_layout()

plt.show()

df['Month'] = df['StartDate'].dt.month

monthly_errors = df.groupby('Month').size()

plt.figure(figsize=(10,5))
monthly_errors.plot(marker='o', linestyle='-', color='purple')
plt.title('Monthly Trends in Moderate Mistakes')
plt.xlabel('Month')
plt.ylabel('Number of Errors')
plt.xticks(range(1,13))
plt.grid(True)
plt.show()

# Top 10 Competitions by Mistake Frequency (Enhanced Visualization)
top_competitions = df['Competition'].value_counts().head(10)

# Formal, soft color palette
colors = sns.color_palette("Blues_r", len(top_competitions))

# Plot horizontal bar chart clearly
plt.figure(figsize=(10, 6))
ax = top_competitions.plot(kind='barh', color=colors)

# Titles and axis labels with professional font sizes
plt.title('Top 10 Competitions by Mistake Frequency', fontsize=16, fontweight='bold')
plt.xlabel('Number of Mistakes', fontsize=14)
plt.ylabel('Competition', fontsize=14)

# Annotate bars clearly
for container in ax.containers:
    ax.bar_label(container, fontsize=12, padding=5)

# Ensure highest mistakes are at the top
plt.gca().invert_yaxis()

# Adjust layout neatly
plt.tight_layout()

# Display plot
plt.show()