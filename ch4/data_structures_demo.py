# ========================================
# 파이썬 기초 3장: 자료구조 심화
# ========================================
# 
# 📚 상세 학습 가이드: 학습가이드/03-자료구조심화.md
# 🔗 관련 챕터: 3장 - 자료구조 심화
# 
# 이 파일은 파이썬의 다양한 자료구조와 collections 모듈을 학습하는 예제입니다.
# 자료구조는 데이터를 효율적으로 저장하고 관리하는 방법을 제공합니다.

# ========================================
# 📌 리스트를 스택으로 활용
# ========================================
# 
# 스택은 LIFO (Last In, First Out) 구조로, 마지막에 들어온 데이터가 먼저 나갑니다.
# 📖 더 자세한 내용: 학습가이드/03-자료구조심화.md#1-리스트를-스택으로-활용

def demonstrate_stack():
    """스택 자료구조를 리스트로 구현하는 예시"""
    print("=== 스택 (Stack) 구현 ===")
    stack = []
    
    # 데이터 추가 (push)
    print("데이터 추가 (push):")
    for i in range(1, 6):
        stack.append(i)
        print(f"  {i} 추가 → 스택: {stack}")
    
    # 데이터 제거 (pop)
    print("\n데이터 제거 (pop):")
    while stack:
        item = stack.pop()
        print(f"  {item} 제거 → 스택: {stack}")

demonstrate_stack()

# ========================================
# 📌 리스트를 큐로 활용
# ========================================
# 
# 큐는 FIFO (First In, First Out) 구조로, 먼저 들어온 데이터가 먼저 나갑니다.
# 📖 더 자세한 내용: 학습가이드/03-자료구조심화.md#2-리스트를-큐로-활용

def demonstrate_queue():
    """큐 자료구조를 리스트로 구현하는 예시"""
    print("\n=== 큐 (Queue) 구현 ===")
    queue = []
    
    # 데이터 추가 (enqueue)
    print("데이터 추가 (enqueue):")
    for i in range(1, 6):
        queue.append(i)
        print(f"  {i} 추가 → 큐: {queue}")
    
    # 데이터 제거 (dequeue)
    print("\n데이터 제거 (dequeue):")
    while queue:
        item = queue.pop(0)  # 첫 번째 요소 제거
        print(f"  {item} 제거 → 큐: {queue}")

demonstrate_queue()

# ========================================
# 📌 튜플 (Tuple)
# ========================================
# 
# 튜플은 변경할 수 없는(immutable) 순서가 있는 데이터 집합입니다.
# 📖 더 자세한 내용: 학습가이드/03-자료구조심화.md#3-튜플-tuple

def demonstrate_tuple():
    """튜플 사용 예시"""
    print("\n=== 튜플 (Tuple) 사용 ===")
    
    # 튜플 생성
    coordinates = (10, 20)
    colors = ("red", "green", "blue")
    mixed = (1, "hello", 3.14, True)
    
    print(f"좌표: {coordinates}")
    print(f"색상: {colors}")
    print(f"혼합: {mixed}")
    
    # 튜플 접근
    print(f"첫 번째 좌표: {coordinates[0]}")
    print(f"마지막 색상: {colors[-1]}")
    
    # 튜플은 수정할 수 없음 (주석 해제하면 오류 발생)
    # coordinates[0] = 5  # TypeError 발생

demonstrate_tuple()

# ========================================
# 📌 세트 (Set)
# ========================================
# 
# 세트는 중복이 없는 유일한 요소들의 집합입니다.
# 📖 더 자세한 내용: 학습가이드/03-자료구조심화.md#4-세트-set

def demonstrate_set():
    """세트 사용 예시"""
    print("\n=== 세트 (Set) 사용 ===")
    
    # 세트 생성
    numbers = {1, 2, 3, 4, 5}
    fruits = {"apple", "banana", "orange"}
    
    print(f"숫자 세트: {numbers}")
    print(f"과일 세트: {fruits}")
    
    # 중복 제거
    duplicates = [1, 2, 2, 3, 3, 3, 4, 5, 5, 1]
    unique_numbers = set(duplicates)
    print(f"중복 제거 전: {duplicates}")
    print(f"중복 제거 후: {unique_numbers}")
    
    # 집합 연산
    set1 = {1, 2, 3, 4}
    set2 = {3, 4, 5, 6}
    
    print(f"\n집합 연산:")
    print(f"  set1: {set1}")
    print(f"  set2: {set2}")
    print(f"  합집합: {set1 | set2}")
    print(f"  교집합: {set1 & set2}")
    print(f"  차집합: {set1 - set2}")
    print(f"  대칭차집합: {set1 ^ set2}")

demonstrate_set()

# ========================================
# 📌 딕셔너리 (Dictionary)
# ========================================
# 
# 딕셔너리는 키(key)와 값(value)의 쌍으로 이루어진 데이터 구조입니다.
# 📖 더 자세한 내용: 학습가이드/03-자료구조심화.md#5-딕셔너리-dictionary

def demonstrate_dictionary():
    """딕셔너리 사용 예시"""
    print("\n=== 딕셔너리 (Dictionary) 사용 ===")
    
    # 딕셔너리 생성
    student = {
        "name": "김파이썬",
        "age": 20,
        "grade": "A",
        "subjects": ["수학", "영어", "과학"]
    }
    
    print(f"학생 정보: {student}")
    
    # 접근
    print(f"이름: {student['name']}")
    print(f"나이: {student.get('age')}")  # 안전한 접근
    
    # 수정
    student["age"] = 21
    student["city"] = "서울"  # 새 키-값 추가
    print(f"수정 후: {student}")
    
    # 모든 키, 값, 항목 출력
    print(f"키들: {list(student.keys())}")
    print(f"값들: {list(student.values())}")
    print(f"항목들: {list(student.items())}")

demonstrate_dictionary()

# ========================================
# 📌 Collections 모듈
# ========================================
# 
# collections 모듈은 고급 자료구조를 제공합니다.
# 📖 더 자세한 내용: 학습가이드/03-자료구조심화.md#6-collections-모듈

from collections import deque, Counter, OrderedDict, namedtuple

def demonstrate_collections():
    """collections 모듈 사용 예시"""
    print("\n=== Collections 모듈 사용 ===")
    
    # 1. deque (양방향 큐)
    print("1. deque (양방향 큐):")
    dq = deque([1, 2, 3, 4, 5])
    print(f"  원본: {dq}")
    
    dq.append(6)        # 오른쪽에 추가
    dq.appendleft(0)    # 왼쪽에 추가
    print(f"  추가 후: {dq}")
    
    dq.rotate(2)        # 2칸 회전
    print(f"  회전 후: {dq}")
    
    # 2. Counter (개수 세기)
    print("\n2. Counter (개수 세기):")
    text = ["apple", "banana", "apple", "orange", "banana", "apple"]
    counter = Counter(text)
    print(f"  텍스트: {text}")
    print(f"  개수: {counter}")
    print(f"  가장 많이 나타난 것: {counter.most_common(2)}")
    
    # 3. OrderedDict (순서 보장 딕셔너리)
    print("\n3. OrderedDict (순서 보장):")
    od = OrderedDict()
    od['first'] = 1
    od['second'] = 2
    od['third'] = 3
    print(f"  순서가 보장된 딕셔너리: {od}")
    
    # 4. namedtuple (이름 있는 튜플)
    print("\n4. namedtuple (이름 있는 튜플):")
    Point = namedtuple('Point', ['x', 'y'])
    p = Point(10, 20)
    print(f"  점: {p}")
    print(f"  x좌표: {p.x}, y좌표: {p.y}")

demonstrate_collections()

# ========================================
# 📌 실전 예제: 학생 관리 시스템
# ========================================
# 
# 학습한 자료구조들을 활용한 실전 예제입니다.

def student_management_system():
    """학생 관리 시스템 예제"""
    print("\n=== 학생 관리 시스템 ===")
    
    # 학생 데이터를 딕셔너리 리스트로 저장
    students = [
        {"name": "김철수", "age": 20, "grade": "A", "subjects": ["수학", "영어"]},
        {"name": "이영희", "age": 21, "grade": "B", "subjects": ["과학", "국어"]},
        {"name": "박민수", "age": 19, "grade": "A", "subjects": ["수학", "과학"]}
    ]
    
    # Counter로 성적 분포 확인
    grades = [student["grade"] for student in students]
    grade_counter = Counter(grades)
    print(f"성적 분포: {grade_counter}")
    
    # 세트로 모든 과목 수집
    all_subjects = set()
    for student in students:
        all_subjects.update(student["subjects"])
    print(f"모든 과목: {all_subjects}")
    
    # 나이순으로 정렬 (튜플 사용)
    age_tuples = [(student["age"], student["name"]) for student in students]
    age_tuples.sort()
    print(f"나이순 정렬: {age_tuples}")

student_management_system()

# ========================================
# 💡 학습 정리
# ========================================
# 
# 이 파일에서 학습한 내용:
# 1. 리스트를 스택과 큐로 활용하는 방법
# 2. 튜플의 불변성과 특징
# 3. 세트의 집합 연산과 중복 제거 기능
# 4. 딕셔너리의 키-값 쌍 관리
# 5. collections 모듈의 고급 자료구조
# 6. 실전 프로젝트에서의 자료구조 활용
# 
# 📚 다음 단계: 학습가이드/04-고급파이썬기법.md
