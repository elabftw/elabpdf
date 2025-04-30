import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe

df = pd.read_csv('mozilla-observatory-scans.csv')

grades = ['a+', 'a', 'a-', 'b+', 'b', 'b-', 'c+', 'c', 'c-', 'd+', 'd', 'd-']
palette = sns.color_palette("RdYlGn", len(grades))
grade_to_color = dict(zip(grades, palette[::-1]))
df['bar_color'] = df['note'].map(grade_to_color)

plt.figure(figsize=(12, 6))
ax = sns.barplot(
    data=df,
    x='name',
    y='score',
    hue='name',
    palette=df['bar_color'].tolist(),
    dodge=False,
    legend=False
)
for bar, name in zip(ax.patches, df['name']):
    bar.set_path_effects([pe.withSimplePatchShadow(offset=(4, -4), shadow_rgbFace='gray', alpha=0.6)])
    if name == 'elabftw':
        bar.set_edgecolor('#00FB00')
        bar.set_linewidth(2)

for label in ax.get_xticklabels():
    if label.get_text() == 'elabftw':
        label.set_fontweight('bold')
ax.set_xlabel('')
plt.ylabel('Score')
plt.title('Mozilla Security Observatory Scoring', fontsize=20)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
# to show it directly
#plt.show()
plt.savefig('mozilla-plot.png', dpi=111, bbox_inches='tight')
