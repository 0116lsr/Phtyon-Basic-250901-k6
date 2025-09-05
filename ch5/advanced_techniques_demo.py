# ========================================
# 파이썬 기초 4장: 고급 파이썬 기법
# ========================================
# 
# 📚 상세 학습 가이드: 학습가이드/04-고급파이썬기법.md
# 🔗 관련 챕터: 4장 - 고급 파이썬 기법
# 
# 이 파일은 파이썬의 고급 기능들을 학습하는 예제입니다.
# 리스트 컴프리헨션, enumerate, zip, 람다 함수 등을 통해 더 효율적인 코드를 작성할 수 있습니다.

# ========================================
# 📌 리스트 컴프리헨션 (List Comprehension)
# ========================================
# 
# 리스트를 간결하고 효율적으로 생성하는 파이썬의 고급 문법입니다.
# 📖 더 자세한 내용: 학습가이드/04-고급파이썬기법.md#1-리스트-컴프리헨션-list-comprehension

def demonstrate_list_comprehension():
    """리스트 컴프리헨션 사용 예시"""
    print("=== 리스트 컴프리헨션 (List Comprehension) ===")
    
    # 기본 사용법
    print("1. 기본 사용법:")
    numbers = [1, 2, 3, 4, 5]
    squares = [x**2 for x in numbers]
    print(f"  원본: {numbers}")
    print(f"  제곱: {squares}")
    
    # 조건문 포함
    print("\n2. 조건문 포함:")
    even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]
    print(f"  짝수의 제곱: {even_squares}")
    
    # 중첩 반복문
    print("\n3. 중첩 반복문:")
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    flattened = [element for row in matrix for element in row]
    print(f"  원본 행렬: {matrix}")
    print(f"  평면화: {flattened}")
    
    # 2차원 리스트 생성
    print("\n4. 2차원 리스트 생성:")
    matrix_2d = [[0 for j in range(3)] for i in range(3)]
    print(f"  3x3 영행렬: {matrix_2d}")

demonstrate_list_comprehension()

# ========================================
# 📌 enumerate() 함수
# ========================================
# 
# 반복 가능한 객체를 순회하면서 인덱스와 값을 동시에 가져오는 함수입니다.
# 📖 더 자세한 내용: 학습가이드/04-고급파이썬기법.md#2-enumerate-함수

def demonstrate_enumerate():
    """enumerate() 함수 사용 예시"""
    print("\n=== enumerate() 함수 ===")
    
    fruits = ["사과", "바나나", "체리", "딸기"]
    
    print("1. 기본 사용법:")
    for index, fruit in enumerate(fruits):
        print(f"  {index}: {fruit}")
    
    print("\n2. 시작값 지정:")
    for index, fruit in enumerate(fruits, 1):
        print(f"  {index}번째: {fruit}")
    
    print("\n3. 딕셔너리 생성:")
    fruit_dict = {index: fruit for index, fruit in enumerate(fruits)}
    print(f"  인덱스-과일 딕셔너리: {fruit_dict}")

demonstrate_enumerate()

# ========================================
# 📌 zip() 함수
# ========================================
# 
# 여러 개의 반복 가능한 객체를 동시에 순회하는 함수입니다.
# 📖 더 자세한 내용: 학습가이드/04-고급파이썬기법.md#3-zip-함수

def demonstrate_zip():
    """zip() 함수 사용 예시"""
    print("\n=== zip() 함수 ===")
    
    names = ["철수", "영희", "민수"]
    ages = [25, 30, 35]
    cities = ["서울", "부산", "대구"]
    
    print("1. 기본 사용법:")
    for name, age, city in zip(names, ages, cities):
        print(f"  {name}은(는) {age}세이고 {city}에 살고 있습니다.")
    
    print("\n2. 딕셔너리 생성:")
    people = {name: {"age": age, "city": city} 
              for name, age, city in zip(names, ages, cities)}
    print(f"  사람들 정보: {people}")
    
    print("\n3. 리스트로 변환:")
    zipped = list(zip(names, ages, cities))
    print(f"  묶인 데이터: {zipped}")
    
    print("\n4. 길이가 다른 리스트:")
    short_list = ["A", "B"]
    long_list = [1, 2, 3, 4, 5]
    zipped_short = list(zip(short_list, long_list))
    print(f"  짧은 리스트 기준: {zipped_short}")

demonstrate_zip()

# ========================================
# 📌 람다 함수 (Lambda Function)
# ========================================
# 
# 이름 없이 정의되는 간단한 함수입니다.
# 📖 더 자세한 내용: 학습가이드/04-고급파이썬기법.md#4-람다-함수-lambda-function

def demonstrate_lambda():
    """람다 함수 사용 예시"""
    print("\n=== 람다 함수 (Lambda Function) ===")
    
    # 기본 사용법
    print("1. 기본 사용법:")
    add = lambda x, y: x + y
    print(f"  add(3, 5) = {add(3, 5)}")
    
    # map()과 함께 사용
    print("\n2. map()과 함께 사용:")
    numbers = [1, 2, 3, 4, 5]
    squares = list(map(lambda x: x**2, numbers))
    print(f"  원본: {numbers}")
    print(f"  제곱: {squares}")
    
    # filter()와 함께 사용
    print("\n3. filter()와 함께 사용:")
    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
    print(f"  짝수만: {even_numbers}")
    
    # sorted()와 함께 사용
    print("\n4. sorted()와 함께 사용:")
    students = [("철수", 85), ("영희", 92), ("민수", 78)]
    sorted_students = sorted(students, key=lambda student: student[1], reverse=True)
    print(f"  점수순 정렬: {sorted_students}")

demonstrate_lambda()

# ========================================
# 📌 성능 비교와 최적화
# ========================================
# 
# 다양한 방법의 성능을 비교하고 최적화 방법을 학습합니다.
# 📖 더 자세한 내용: 학습가이드/04-고급파이썬기법.md#5-성능-비교와-최적화

import time

def performance_comparison():
    """성능 비교 예시"""
    print("\n=== 성능 비교 ===")
    
    n = 100000  # 테스트할 데이터 크기
    
    # for문 방식
    start_time = time.time()
    result_for = []
    for i in range(n):
        result_for.append(i**2)
    for_time = time.time() - start_time
    
    # 리스트 컴프리헨션 방식
    start_time = time.time()
    result_comp = [i**2 for i in range(n)]
    comp_time = time.time() - start_time
    
    print(f"For문 시간: {for_time:.4f}초")
    print(f"컴프리헨션 시간: {comp_time:.4f}초")
    print(f"성능 향상: {for_time/comp_time:.2f}배")
    
    # 제너레이터 표현식 (메모리 효율적)
    print("\n메모리 효율성:")
    squares_gen = (x**2 for x in range(1000000))  # 제너레이터
    squares_list = [x**2 for x in range(1000000)]  # 리스트
    
    print(f"제너레이터 메모리: {squares_gen.__sizeof__()} bytes")
    print(f"리스트 메모리: {squares_list.__sizeof__()} bytes")

performance_comparison()

# ========================================
# 📌 실전 예제: 데이터 처리 시스템
# ========================================
# 
# 학습한 고급 기법들을 활용한 실전 예제입니다.

def data_processing_system():
    """데이터 처리 시스템 예제"""
    print("\n=== 데이터 처리 시스템 ===")
    
    # 샘플 데이터
    sales_data = [
        ("2024-01-15", "제품A", 1000, 10),
        ("2024-01-16", "제품B", 1500, 5),
        ("2024-01-17", "제품A", 1000, 8),
        ("2024-01-18", "제품C", 2000, 3),
        ("2024-01-19", "제품B", 1500, 12)
    ]
    
    print("원본 데이터:")
    for i, (date, product, price, quantity) in enumerate(sales_data, 1):
        print(f"  {i}. {date} - {product}: {price}원 × {quantity}개")
    
    # 1. 제품별 총 매출 계산 (리스트 컴프리헨션 + 딕셔너리)
    print("\n1. 제품별 총 매출:")
    product_sales = {}
    for date, product, price, quantity in sales_data:
        total = price * quantity
        if product in product_sales:
            product_sales[product] += total
        else:
            product_sales[product] = total
    
    for product, total in product_sales.items():
        print(f"  {product}: {total:,}원")
    
    # 2. 고매출 제품 찾기 (람다 함수 + sorted)
    print("\n2. 매출 순위:")
    sorted_products = sorted(product_sales.items(), key=lambda x: x[1], reverse=True)
    for i, (product, total) in enumerate(sorted_products, 1):
        print(f"  {i}위: {product} - {total:,}원")
    
    # 3. 일별 매출 계산 (enumerate + zip)
    print("\n3. 일별 매출:")
    dates = [item[0] for item in sales_data]
    daily_totals = [item[2] * item[3] for item in sales_data]
    
    for date, total in zip(dates, daily_totals):
        print(f"  {date}: {total:,}원")
    
    # 4. 평균 매출 계산
    avg_sales = sum(daily_totals) / len(daily_totals)
    print(f"\n평균 일일 매출: {avg_sales:,.0f}원")
    
    # 5. 평균 이상인 날 찾기 (리스트 컴프리헨션)
    above_avg_days = [(date, total) for date, total in zip(dates, daily_totals) 
                      if total > avg_sales]
    print(f"\n평균 이상인 날: {len(above_avg_days)}일")
    for date, total in above_avg_days:
        print(f"  {date}: {total:,}원")

data_processing_system()

# ========================================
# 📌 고급 활용 예제: 텍스트 분석
# ========================================
# 
# 람다 함수와 리스트 컴프리헨션을 활용한 텍스트 분석 예제입니다.

def text_analysis():
    """텍스트 분석 예제"""
    print("\n=== 텍스트 분석 ===")
    
    # 샘플 텍스트
    text = "Python is a great programming language. Python is easy to learn. Python is powerful."
    
    # 단어 분리 및 정리
    words = text.lower().replace('.', '').split()
    print(f"원본 텍스트: {text}")
    print(f"단어 리스트: {words}")
    
    # 단어 길이별 분류 (리스트 컴프리헨션)
    short_words = [word for word in words if len(word) < 5]
    long_words = [word for word in words if len(word) >= 5]
    
    print(f"\n짧은 단어 (< 5글자): {short_words}")
    print(f"긴 단어 (≥ 5글자): {long_words}")
    
    # 단어 빈도 계산 (람다 함수 + sorted)
    from collections import Counter
    word_count = Counter(words)
    most_common = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    
    print(f"\n단어 빈도:")
    for word, count in most_common:
        print(f"  {word}: {count}번")
    
    # 특정 조건의 단어 찾기 (람다 함수 + filter)
    python_words = list(filter(lambda word: 'python' in word.lower(), words))
    print(f"\n'python'이 포함된 단어: {python_words}")

text_analysis()

# ========================================
# 💡 학습 정리
# ========================================
# 
# 이 파일에서 학습한 내용:
# 1. 리스트 컴프리헨션으로 간결한 코드 작성
# 2. enumerate()로 인덱스와 값을 동시에 처리
# 3. zip()으로 여러 리스트를 동시에 순회
# 4. 람다 함수로 간단한 연산 정의
# 5. map(), filter(), sorted()와 람다 함수 조합
# 6. 성능 비교를 통한 최적화 방법
# 7. 실전 프로젝트에서의 고급 기법 활용
# 
# 📚 다음 단계: 학습가이드/05-객체지향프로그래밍.md
