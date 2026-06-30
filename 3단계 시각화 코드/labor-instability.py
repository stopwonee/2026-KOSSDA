# ============================================================
# KOSSDA 공모전용 시각화
# 분석2 : 노동 구조 불안정성 패널
# (고용형태 / 근무형태 / 임금형태)
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# ------------------------------------------------------------
# 한글 폰트 설정 (Mac)
# ------------------------------------------------------------

plt.rcParams['font.family'] = 'AppleGothic'
plt.rcParams['axes.unicode_minus'] = False

# ------------------------------------------------------------
# 엑셀 파일 불러오기
# ------------------------------------------------------------

employment_file = '분석2_1_고용안정성_카이제곱결과(1).xlsx'
worktype_file = '분석2_2_근무형태_카이제곱결과(1).xlsx'
wage_file = '분석2_3_임금형태안정성_카이제곱결과(1).xlsx'

# ------------------------------------------------------------
# 데이터 입력
# (네 분석 결과 기준)
# ------------------------------------------------------------

# 고용형태
employment_stable = [56.5, 90.1]
employment_unstable = [43.5, 9.9]

# 근무형태
work_stable = [61.2, 96.6]
work_unstable = [38.8, 3.4]

# 임금형태
wage_stable = [71.6, 98.9]
wage_unstable = [28.4, 1.1]

groups = ['저소득', '비저소득']

# ------------------------------------------------------------
# Figure 생성
# ------------------------------------------------------------

fig, axes = plt.subplots(1, 3, figsize=(13, 5))

# ------------------------------------------------------------
# 색상
# ------------------------------------------------------------

stable_color = '#9ecae1'
unstable_color = '#d62728'

# ------------------------------------------------------------
# 패널 데이터 묶기
# ------------------------------------------------------------

titles = [
    '고용형태',
    '근무형태',
    '임금형태'
]

stable_data = [
    employment_stable,
    work_stable,
    wage_stable
]

unstable_data = [
    employment_unstable,
    work_unstable,
    wage_unstable
]

stable_labels = [
    '정규직',
    '전일제',
    '안정 임금'
]

unstable_labels = [
    '비정규직',
    '시간제',
    '불안정 임금'
]

# ------------------------------------------------------------
# 그래프 반복 생성
# ------------------------------------------------------------

for i, ax in enumerate(axes):

    stable = stable_data[i]
    unstable = unstable_data[i]

    # 안정 구조
    ax.bar(
        groups,
        stable,
        color=stable_color,
        label=stable_labels[i]
    )

    # 불안정 구조
    ax.bar(
        groups,
        unstable,
        bottom=stable,
        color=unstable_color,
        label=unstable_labels[i]
    )

    # % 텍스트 표시
    for j in range(len(groups)):

        # 안정 비율
        ax.text(
            j,
            stable[j] / 2,
            f'{stable[j]:.1f}%',
            ha='center',
            va='center',
            fontsize=10
        )

        # 불안정 비율
        ax.text(
            j,
            stable[j] + unstable[j] / 2,
            f'{unstable[j]:.1f}%',
            ha='center',
            va='center',
            fontsize=10,
            color='white'
        )

    # 패널 제목
    ax.set_title(
        titles[i],
        fontsize=14,
        pad=10
    )

    # y축
    ax.set_ylim(0, 100)

    # grid 최소화
    ax.grid(
        axis='y',
        linestyle='--',
        alpha=0.12
    )

    # 테두리 제거
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

# ------------------------------------------------------------
# 메인 제목
# ------------------------------------------------------------

fig.suptitle(
    '저소득 청년의 노동 구조 불안정성',
    fontsize=18,
    fontweight='bold',
    y=1.03
)

# ------------------------------------------------------------
# 범례
# ------------------------------------------------------------

handles = [
    plt.Rectangle((0,0),1,1,color=stable_color),
    plt.Rectangle((0,0),1,1,color=unstable_color)
]

labels = ['안정 구조', '불안정 구조']

fig.legend(
    handles,
    labels,
    loc='lower center',
    ncol=2,
    frameon=False,
    fontsize=11
)

# ------------------------------------------------------------
# 배경색
# ------------------------------------------------------------

fig.patch.set_facecolor('white')

# ------------------------------------------------------------
# 레이아웃 정리
# ------------------------------------------------------------

plt.tight_layout(rect=[0, 0.08, 1, 1])

# ------------------------------------------------------------
# 저장
# ------------------------------------------------------------

plt.savefig(
    'analysis2_labor_instability_panel.png',
    dpi=300,
    bbox_inches='tight'
)

# ------------------------------------------------------------
# 출력
# ------------------------------------------------------------

plt.show()