# ========================================
# Task 4: 상관관계 분석
# ========================================
# 
# 과제 내용:
# 1) 히트맵을 통한 상관관계 분석
#    삼성전자, 카카오, 네이버의 주가 상관관계를 히트맵으로 표현
# 2) 종목 간 상관관계 분석
#    각 종목 간 주가의 상관관계를 히트맵으로 시각화

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os

# 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

def load_data():
    """데이터 로드 함수"""
    print("📂 데이터 로드 중...")
    
    csv_path = os.path.join('data', 'stock_close_prices.csv')
    
    if not os.path.exists(csv_path):
        print(f"❌ 데이터 파일이 없습니다: {csv_path}")
        print("먼저 task1_주식데이터수집.py를 실행해주세요.")
        return None
    
    data = pd.read_csv(csv_path, index_col=0, parse_dates=True)
    print(f"✅ 데이터 로드 완료: {len(data)}개 데이터")
    
    return data

def calculate_correlation(data):
    """상관계수 계산 함수"""
    print("📊 상관계수 계산 중...")
    
    # 종가 데이터만 추출
    close_data = data[['삼성전자', '카카오', '네이버']]
    
    # 상관계수 계산
    correlation_matrix = close_data.corr()
    
    print("\n📋 상관계수 매트릭스:")
    print(correlation_matrix.round(3))
    
    return correlation_matrix

def plot_correlation_heatmap(correlation_matrix):
    """상관관계 히트맵 생성"""
    print("📊 상관관계 히트맵 생성 중...")
    
    plt.figure(figsize=(10, 8))
    
    # 히트맵 생성
    sns.heatmap(correlation_matrix, 
                annot=True, 
                cmap='coolwarm', 
                center=0,
                square=True,
                fmt='.3f',
                cbar_kws={'shrink': 0.8},
                linewidths=0.5)
    
    # 그래프 설정
    plt.title('주식 종목 간 상관관계 히트맵', fontsize=16, fontweight='bold', pad=20)
    plt.xlabel('종목', fontsize=12)
    plt.ylabel('종목', fontsize=12)
    
    # 레이아웃 조정
    plt.tight_layout()
    
    # 그래프 저장
    plot_path = os.path.join('plots', 'correlation_heatmap.png')
    plt.savefig(plot_path, dpi=300, bbox_inches='tight')
    print(f"✅ 그래프 저장 완료: {plot_path}")
    
    # 그래프 표시
    plt.show()
    
    return plot_path

def analyze_correlation(correlation_matrix):
    """상관관계 분석 함수"""
    print("\n📈 상관관계 분석 중...")
    
    stocks = ['삼성전자', '카카오', '네이버']
    
    print("\n📋 종목별 상관관계 분석:")
    
    for i, stock1 in enumerate(stocks):
        for j, stock2 in enumerate(stocks):
            if i < j:  # 중복 제거
                corr_value = correlation_matrix.loc[stock1, stock2]
                
                # 상관관계 해석
                if corr_value > 0.7:
                    interpretation = "강한 양의 상관관계"
                elif corr_value > 0.3:
                    interpretation = "중간 양의 상관관계"
                elif corr_value > -0.3:
                    interpretation = "약한 상관관계"
                elif corr_value > -0.7:
                    interpretation = "중간 음의 상관관계"
                else:
                    interpretation = "강한 음의 상관관계"
                
                print(f"  {stock1} vs {stock2}: {corr_value:.3f} ({interpretation})")
    
    # 전체 상관관계 요약
    print("\n📊 전체 상관관계 요약:")
    avg_correlation = correlation_matrix.values[np.triu_indices_from(correlation_matrix.values, k=1)].mean()
    print(f"  평균 상관계수: {avg_correlation:.3f}")
    
    if avg_correlation > 0.5:
        print("  → 종목들이 서로 강한 상관관계를 보입니다.")
    elif avg_correlation > 0.3:
        print("  → 종목들이 서로 중간 정도의 상관관계를 보입니다.")
    else:
        print("  → 종목들이 서로 약한 상관관계를 보입니다.")
    
    return correlation_matrix

def main():
    """메인 실행 함수"""
    print("=" * 60)
    print("🚀 Task 4: 상관관계 분석")
    print("=" * 60)
    
    # 1. 데이터 로드
    data = load_data()
    
    if data is None:
        return
    
    # 2. 상관계수 계산
    correlation_matrix = calculate_correlation(data)
    
    # 3. 상관관계 히트맵 생성
    plot_path = plot_correlation_heatmap(correlation_matrix)
    
    # 4. 상관관계 분석
    correlation_matrix = analyze_correlation(correlation_matrix)
    
    # 5. 결과 저장
    result_path = os.path.join('data', 'correlation_matrix.csv')
    correlation_matrix.to_csv(result_path)
    print(f"\n💾 결과 저장 완료: {result_path}")
    
    print("\n🎉 Task 4 완료!")
    print(f"📁 결과 파일: {plot_path}")
    
    return correlation_matrix

if __name__ == "__main__":
    result = main()
