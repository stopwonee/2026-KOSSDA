import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'AppleGothic'
plt.rcParams['axes.unicode_minus'] = False

groups = ['저소득', '비저소득']

passive = [23.0, 19.8]
active = [77.0, 80.2]

fig, ax = plt.subplots(figsize=(7, 5))

ax.bar(
groups,
passive,
label='소극적 여가'
)

ax.bar(
groups,
active,
bottom=passive,
label='적극적 여가'
)

ax.set_ylabel('비율 (%)')

ax.set_title('소득집단별 희망 여가 유형')

ax.legend()

plt.tight_layout()

plt.savefig(
'적극소극_비율그래프.png',
dpi=300,
bbox_inches='tight'
)

plt.show()