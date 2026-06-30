import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'AppleGothic'
plt.rcParams['axes.unicode_minus'] = False

groups = ['저소득', '비저소득']

gap = [0.414, 0.380]

fig, ax = plt.subplots(figsize=(6, 5))

bars = ax.bar(
groups,
gap
)

ax.set_ylabel('여가격차지수')

ax.set_title('소득집단별 여가격차지수 평균')

ax.text(
0.5,
0.42,
'p = 0.0319',
ha='center',
fontsize=11
)

plt.tight_layout()

plt.savefig(
'여가격차지수.png',
dpi=300,
bbox_inches='tight'
)

plt.show()