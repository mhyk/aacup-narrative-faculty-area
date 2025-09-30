import matplotlib.pyplot as plt
import numpy as np

# Set up the plotting style
plt.style.use('default')
plt.rcParams['figure.figsize'] = (12, 6)
plt.rcParams['font.size'] = 12

# Create figure with two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 7))

# Data for Academic Ranking Distribution
rank_labels = ['Professor', 'Associate Professor', 'Assistant Professor']
rank_sizes = [1, 2, 6]
rank_percentages = [11.1, 22.2, 66.7]
rank_colors = ['#1f77b4', '#ff7f0e', '#2ca02c']

# Data for Degree Distribution
degree_labels = ['PhD', "Master's Degree"]
degree_sizes = [1, 8]
degree_percentages = [11.1, 88.9]
degree_colors = ['#d62728', '#9467bd']

# Create Academic Ranking pie chart
wedges1, texts1, autotexts1 = ax1.pie(rank_sizes, labels=rank_labels, autopct='%1.1f%%',
                                       colors=rank_colors, startangle=90, textprops={'fontsize': 10})
ax1.set_title('Faculty Academic Ranking Distribution\n(Total: 9 Faculty)', fontsize=14, fontweight='bold', pad=20)

# Create Degree Distribution pie chart
wedges2, texts2, autotexts2 = ax2.pie(degree_sizes, labels=degree_labels, autopct='%1.1f%%',
                                       colors=degree_colors, startangle=90, textprops={'fontsize': 10})
ax2.set_title('Faculty Degree Distribution\n(Total: 9 Faculty)', fontsize=14, fontweight='bold', pad=20)

# Add count labels to the charts
for i, (wedge, count) in enumerate(zip(wedges1, rank_sizes)):
    angle = (wedge.theta2 + wedge.theta1) / 2
    x = wedge.center[0] + 0.7 * wedge.r * np.cos(np.radians(angle))
    y = wedge.center[1] + 0.7 * wedge.r * np.sin(np.radians(angle))
    ax1.annotate(f'({count})', xy=(x, y), ha='center', va='center',
                fontweight='bold', fontsize=9, color='white')

for i, (wedge, count) in enumerate(zip(wedges2, degree_sizes)):
    angle = (wedge.theta2 + wedge.theta1) / 2
    x = wedge.center[0] + 0.7 * wedge.r * np.cos(np.radians(angle))
    y = wedge.center[1] + 0.7 * wedge.r * np.sin(np.radians(angle))
    ax2.annotate(f'({count})', xy=(x, y), ha='center', va='center',
                fontweight='bold', fontsize=9, color='white')

# Improve layout
plt.tight_layout()

# Add main title
fig.suptitle('MSU-IIT College of Computer Studies Faculty Profile',
             fontsize=16, fontweight='bold', y=0.95)

# Save the figure
plt.savefig('faculty_distribution_charts.png', dpi=300, bbox_inches='tight',
            facecolor='white', edgecolor='none')

plt.show()

print("Pie charts created successfully!")
print("\nSummary:")
print("Academic Ranking Distribution:")
for label, count, pct in zip(rank_labels, rank_sizes, rank_percentages):
    print(f"  {label}: {count} faculty ({pct}%)")

print("\nDegree Distribution:")
for label, count, pct in zip(degree_labels, degree_sizes, degree_percentages):
    print(f"  {label}: {count} faculty ({pct}%)")