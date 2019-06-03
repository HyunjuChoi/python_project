import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mlp
import seaborn as sns
from matplotlib import font_manager, rc

font_name = font_manager.FontProperties(fname="C:/Windows/Fonts/NanumGothic.ttf").get_name()
rc('font', family=font_name)


data = pd.read_excel('./고속도로교통사고통계.xls',skipinitialspace=True)

#데이터 보기
data.columns = ['시도', '시군구','발생건수', '사망자수', '부상자수',' 중상자수','경상자수', '부상신고자수']
print('********************2016 고속도로 부문별 교통사고 원본 데이터********************\n')
print(data.head(7))
print('\n')

#데이터 전처리
#처음 4행 제거
data = data.iloc[4:, :]

#시군구 합계값 필요 없으므로 제거. 
#필요 시 sum() 이용하여 간단히 계산 가능
data = data[data["시군구"] != "합계"]
print('***************2016 고속도로 부문별 교통사고 전처리 데이터***************\n')
print(data.head())

#data 분석
#1. 발생건수 가장 많은 데이터 10개 내림차순
data_ac = data.sort_values(by=["발생건수"], ascending=False)
data_ac_top10 = data_ac.head(10)
plt.figure(figsize=(10,6))
plt.title("발생건수 top10")
sns.barplot(x="시군구", y="발생건수", data=data_ac_top10)
plt.show()

#2. 발생건수 별 사망자수 top10
plt.figure(figsize=(10,6))
plt.title("발생건수 별 사망자 수")
sns.barplot(x="발생건수", y="사망자수", data=data_ac_top10)
plt.show()

#3. 발생건수 별 부상자 수 top10
plt.figure(figsize=(10,6))
plt.title("발생건수 별 부상자 수")
sns.regplot(x=data_ac_top10["발생건수"].astype(float), y=data_ac_top10["부상자수"].astype(float))
plt.show()

#4. 경기,강원, 충남, 경남의 사망자 수 파이그래프로 표현
plt.figure(figsize=(10,6))
plt.title("시도별 사망자 수")
size = [63, 11, 28, 30]
sido = ['경기', '강원', '충남', '경남']

plt.pie(size, explode =(0.1, 0,0,0), labels=sido, autopct='%1.1f%%', shadow=True, startangle=90)
plt.axis('equal')
plt.show()
