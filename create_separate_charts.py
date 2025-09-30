import matplotlib.pyplot as plt
import numpy as np
import os

# Set up the plotting style
plt.style.use('default')
plt.rcParams['font.size'] = 14

# Create images directory if it doesn't exist
os.makedirs('images', exist_ok=True)

# Data for Academic Ranking Distribution
rank_labels = ['Professor', 'Associate Professor', 'Assistant Professor']
rank_sizes = [1, 2, 6]
rank_colors = ['#1f77b4', '#ff7f0e', '#2ca02c']

# Data for Degree Distribution
degree_labels = ['PhD', "Master's Degree"]
degree_sizes = [1, 8]
degree_colors = ['#d62728', '#9467bd']

# Create Academic Ranking pie chart
fig1, ax1 = plt.subplots(figsize=(12, 10))

# Function to create custom labels with both percentage and count
def make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        val = int(round(pct*total/100.0))
        return f'{pct:.1f}%\n({val})'
    return my_autopct

wedges1, texts1, autotexts1 = ax1.pie(rank_sizes, labels=rank_labels,
                                       autopct=make_autopct(rank_sizes),
                                       colors=rank_colors, startangle=90,
                                       textprops={'fontsize': 11},
                                       pctdistance=0.75)

# Style the percentage text
for autotext in autotexts1:
    autotext.set_color('white')
    autotext.set_fontweight('bold')
    autotext.set_fontsize(10)

# Style the labels
for text in texts1:
    text.set_fontsize(12)
    text.set_fontweight('bold')

ax1.set_title('Faculty Academic Ranking Distribution\nMSU-IIT College of Computer Studies\n(Total: 9 Faculty)',
              fontsize=16, fontweight='bold', pad=30)

plt.tight_layout()
plt.savefig('images/faculty_academic_ranking_distribution.png', dpi=300, bbox_inches='tight',
            facecolor='white', edgecolor='none')
plt.close()

# Create Degree Distribution pie chart
fig2, ax2 = plt.subplots(figsize=(12, 10))
wedges2, texts2, autotexts2 = ax2.pie(degree_sizes, labels=degree_labels,
                                       autopct=make_autopct(degree_sizes),
                                       colors=degree_colors, startangle=90,
                                       textprops={'fontsize': 11},
                                       pctdistance=0.75)

# Style the percentage text
for autotext in autotexts2:
    autotext.set_color('white')
    autotext.set_fontweight('bold')
    autotext.set_fontsize(10)

# Style the labels
for text in texts2:
    text.set_fontsize(12)
    text.set_fontweight('bold')

ax2.set_title('Faculty Degree Distribution\nMSU-IIT College of Computer Studies\n(Total: 9 Faculty)',
              fontsize=16, fontweight='bold', pad=30)

plt.tight_layout()
plt.savefig('images/faculty_degree_distribution.png', dpi=300, bbox_inches='tight',
            facecolor='white', edgecolor='none')
plt.close()

print("Separate pie charts created successfully!")
print("\nFiles created:")
print("- images/faculty_academic_ranking_distribution.png")
print("- images/faculty_degree_distribution.png")

print("\nAcademic Ranking Distribution:")
for label, count, pct in zip(rank_labels, rank_sizes, [11.1, 22.2, 66.7]):
    print(f"  {label}: {count} faculty ({pct}%)")

print("\nDegree Distribution:")
for label, count, pct in zip(degree_labels, degree_sizes, [11.1, 88.9]):
    print(f"  {label}: {count} faculty ({pct}%)")