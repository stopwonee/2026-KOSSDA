import subprocess
import sys

packages = ['pandas', 'matplotlib', 'openpyxl']

for package in packages:
    try:
        __import__(package)

    except ImportError:
        print(f'{package} 설치 중...')

        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", package]
        )

import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'AppleGothic'
plt.rcParams['axes.unicode_minus'] = False

file_path = '2단계.xlsx'

try:

    actual_df = pd.read_excel(
        file_path,
        sheet_name='소득집단별 주중 주말 실제 여가 Top 5'
    )

    wish_df = pd.read_excel(
        file_path,
        sheet_name='소득집단별 희망 여가 Top 5'
    )

    print('엑셀 파일 불러오기 성공')

except Exception as e:

    print('엑셀 파일 불러오기 실패')
    print(e)

    sys.exit()

def draw_dumbbell_chart(group_name):

    actual = actual_df[
        actual_df['소득집단'] == group_name
    ][['여가활동', '합산 비율']]

    actual.columns = ['여가활동', '실제']

    wish = wish_df[
        wish_df['소득집단'] == group_name
    ][['여가활동', '비율']]

    wish['비율'] = wish['비율'] / 100

    wish.columns = ['여가활동', '희망']

    merged = pd.merge(
        actual,
        wish,
        on='여가활동',
        how='outer'
    ).fillna(0)

    merged['격차'] = abs(
        merged['희망'] - merged['실제']
    )

    merged = merged.sort_values(
        by='격차',
        ascending=True
    )

    fig, ax = plt.subplots(figsize=(11, 6))

    for i in range(len(merged)):

        ax.plot(
            [
                merged['실제'].iloc[i],
                merged['희망'].iloc[i]
            ],
            [i, i],
            color='gray',
            linewidth=2
        )

    ax.scatter(
        merged['실제'],
        range(len(merged)),
        s=180,
        label='실제 여가'
    )

    ax.scatter(
        merged['희망'],
        range(len(merged)),
        s=180,
        label='희망 여가'
    )

    ax.set_yticks(range(len(merged)))

    ax.set_yticklabels(
        merged['여가활동'],
        fontsize=11
    )

    ax.set_xlabel('비율')

    ax.set_title(
        f'{group_name} 청년의 실제 여가와 희망 여가 간 격차'
    )

    ax.legend()

    ax.grid(
        axis='x',
        linestyle='--',
        alpha=0.4
    )

    plt.tight_layout()

    save_name = f'{group_name}_덤벨차트.png'

    plt.savefig(
        save_name,
        dpi=300,
        bbox_inches='tight'
    )

    plt.show()

draw_dumbbell_chart('저소득')

draw_dumbbell_chart('비저소득')

print('모든 그래프 생성 완료')
