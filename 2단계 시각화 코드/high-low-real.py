import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.family'] = 'AppleGothic'
plt.rcParams['axes.unicode_minus'] = False

file_path = '2단계.xlsx'

df = pd.read_excel(
file_path,
sheet_name='소득집단별 주중 주말 실제 여가 Top 5'
)

low = df[df['소득집단'] == '저소득']
high = df[df['소득집단'] == '비저소득']

categories = list(
set(low['여가활동']).union(set(high['여가활동']))
)

low_values = []
high_values = []

for category in categories:

    low_row = low[low['여가활동'] == category]
    high_row = high[high['여가활동'] == category]

    if len(low_row) > 0:
        low_values.append(low_row['합산 비율'].values[0])
    else:
        low_values.append(0)

    if len(high_row) > 0:
        high_values.append(high_row['합산 비율'].values[0])
    else:
        high_values.append(0)

x = np.arange(len(categories))
width = 0.35

fig, ax = plt.subplots(figsize=(12, 6))

ax.bar(
x - width/2,
low_values,
width,
label='저소득'
)

ax.bar(
x + width/2,
high_values,
width,
label='비저소득'
)

ax.set_xticks(x)

ax.set_xticklabels(
categories,
rotation=20
)

ax.set_ylabel('비율')

ax.set_title('소득집단별 실제 여가 유형 비교')

ax.legend()

plt.tight_layout()

plt.savefig(
'그룹막대그래프.png',
dpi=300,
bbox_inches='tight'
)

plt.show()