# ========================================
# 파이썬 기초 5장: 객체지향 프로그래밍
# ========================================
# 
# 📚 상세 학습 가이드: 학습가이드/05-객체지향프로그래밍.md
# 🔗 관련 챕터: 5장 - 객체지향 프로그래밍
# 
# 이 파일은 파이썬의 객체지향 프로그래밍을 학습하는 예제입니다.
# 클래스, 상속, 다형성, 캡슐화 등 객체지향의 핵심 개념을 다룹니다.

# ========================================
# 📌 클래스와 객체 기본
# ========================================
# 
# 클래스는 객체를 만들기 위한 설계도이고, 객체는 클래스로부터 생성된 실제 인스턴스입니다.
# 📖 더 자세한 내용: 학습가이드/05-객체지향프로그래밍.md#1-클래스와-객체

class Person:
    """
    사람을 나타내는 클래스
    
    속성:
        name (str): 이름
        age (int): 나이
    """
    
    def __init__(self, name, age):
        """
        Person 객체를 생성하는 생성자
        
        매개변수:
            name (str): 이름
            age (int): 나이
        """
        self.name = name
        self.age = age
        print(f"{self.name} 객체가 생성되었습니다.")
    
    def introduce(self):
        """자기소개를 하는 메서드"""
        return f"안녕하세요, 저는 {self.name}이고 {self.age}세입니다."
    
    def have_birthday(self):
        """생일을 맞아 나이가 한 살 증가하는 메서드"""
        self.age += 1
        print(f"{self.name}의 생일! 이제 {self.age}세가 되었습니다.")
    
    def __str__(self):
        """객체를 문자열로 표현할 때 사용되는 메서드"""
        return f"Person(name='{self.name}', age={self.age})"

def demonstrate_basic_class():
    """기본 클래스 사용 예시"""
    print("=== 클래스와 객체 기본 ===")
    
    # 객체 생성
    person1 = Person("홍길동", 25)
    person2 = Person("김철수", 30)
    
    # 메서드 호출
    print(person1.introduce())
    print(person2.introduce())
    
    # 속성 접근
    print(f"{person1.name}의 나이: {person1.age}")
    
    # 메서드로 상태 변경
    person1.have_birthday()
    
    # 객체 문자열 표현
    print(f"person1: {person1}")

demonstrate_basic_class()

# ========================================
# 📌 클래스 변수와 인스턴스 변수
# ========================================
# 
# 클래스 변수는 모든 객체가 공유하고, 인스턴스 변수는 각 객체마다 독립적입니다.
# 📖 더 자세한 내용: 학습가이드/05-객체지향프로그래밍.md#3-클래스-변수와-인스턴스-변수

class BankAccount:
    """은행 계좌를 나타내는 클래스"""
    
    # 클래스 변수 (모든 계좌가 공유)
    bank_name = "파이썬 은행"
    total_accounts = 0
    
    def __init__(self, account_number, initial_balance=0):
        """계좌 생성자"""
        # 인스턴스 변수 (각 계좌마다 독립적)
        self.account_number = account_number
        self.balance = initial_balance
        
        # 클래스 변수 수정
        BankAccount.total_accounts += 1
        print(f"새 계좌 생성: {account_number}, 잔액: {initial_balance:,}원")
    
    def deposit(self, amount):
        """입금 메서드"""
        if amount > 0:
            self.balance += amount
            return f"{amount:,}원 입금. 잔액: {self.balance:,}원"
        else:
            return "입금액은 0보다 커야 합니다."
    
    def withdraw(self, amount):
        """출금 메서드"""
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return f"{amount:,}원 출금. 잔액: {self.balance:,}원"
        else:
            return "잔액이 부족하거나 잘못된 금액입니다."
    
    def get_balance(self):
        """잔액 조회 메서드"""
        return f"계좌 {self.account_number} 잔액: {self.balance:,}원"
    
    @classmethod
    def get_total_accounts(cls):
        """총 계좌 수를 반환하는 클래스 메서드"""
        return cls.total_accounts
    
    @classmethod
    def set_bank_name(cls, new_name):
        """은행명을 변경하는 클래스 메서드"""
        cls.bank_name = new_name

def demonstrate_class_variables():
    """클래스 변수와 인스턴스 변수 예시"""
    print("\n=== 클래스 변수와 인스턴스 변수 ===")
    
    # 계좌 생성
    account1 = BankAccount("123-456-789", 10000)
    account2 = BankAccount("987-654-321", 50000)
    
    print(f"은행명: {BankAccount.bank_name}")
    print(f"총 계좌 수: {BankAccount.get_total_accounts()}")
    
    # 계좌별 잔액 조회
    print(account1.get_balance())
    print(account2.get_balance())
    
    # 입출금
    print(account1.deposit(5000))
    print(account2.withdraw(10000))
    
    # 은행명 변경
    BankAccount.set_bank_name("새로운 파이썬 은행")
    print(f"변경된 은행명: {BankAccount.bank_name}")

demonstrate_class_variables()

# ========================================
# 📌 상속 (Inheritance)
# ========================================
# 
# 기존 클래스의 속성과 메서드를 새로운 클래스가 물려받는 것입니다.
# 📖 더 자세한 내용: 학습가이드/05-객체지향프로그래밍.md#4-상속-inheritance

class Animal:
    """동물을 나타내는 부모 클래스"""
    
    def __init__(self, name, species):
        self.name = name
        self.species = species
        print(f"{self.name} ({self.species})이(가) 생성되었습니다.")
    
    def make_sound(self):
        """소리를 내는 메서드 (자식 클래스에서 오버라이딩 예정)"""
        return "Some generic sound"
    
    def move(self):
        """움직이는 메서드"""
        return f"{self.name} is moving"
    
    def eat(self, food):
        """먹는 메서드"""
        return f"{self.name} is eating {food}"

class Dog(Animal):
    """개를 나타내는 자식 클래스"""
    
    def __init__(self, name, breed):
        # 부모 클래스의 생성자 호출
        super().__init__(name, "Dog")
        self.breed = breed
        print(f"품종: {self.breed}")
    
    def make_sound(self):  # 메서드 오버라이딩
        """개만의 소리"""
        return "Woof! Woof!"
    
    def fetch(self):  # 자식 클래스만의 메서드
        """공을 가져오는 메서드"""
        return f"{self.name} is fetching the ball"
    
    def wag_tail(self):  # 자식 클래스만의 메서드
        """꼬리를 흔드는 메서드"""
        return f"{self.name} is wagging its tail"

class Cat(Animal):
    """고양이를 나타내는 자식 클래스"""
    
    def __init__(self, name, color):
        super().__init__(name, "Cat")
        self.color = color
        print(f"색깔: {self.color}")
    
    def make_sound(self):  # 메서드 오버라이딩
        """고양이만의 소리"""
        return "Meow~ Meow~"
    
    def climb(self):  # 자식 클래스만의 메서드
        """나무를 타는 메서드"""
        return f"{self.name} is climbing the tree"

def demonstrate_inheritance():
    """상속 예시"""
    print("\n=== 상속 (Inheritance) ===")
    
    # 동물 객체들 생성
    dog = Dog("멍멍이", "골든리트리버")
    cat = Cat("야옹이", "검은색")
    
    # 부모 클래스의 메서드 사용
    print(f"\n{dog.move()}")
    print(f"{cat.move()}")
    print(f"{dog.eat('사료')}")
    print(f"{cat.eat('생선')}")
    
    # 오버라이딩된 메서드 사용
    print(f"\n{dog.make_sound()}")
    print(f"{cat.make_sound()}")
    
    # 자식 클래스만의 메서드 사용
    print(f"\n{dog.fetch()}")
    print(f"{dog.wag_tail()}")
    print(f"{cat.climb()}")

demonstrate_inheritance()

# ========================================
# 📌 다형성 (Polymorphism)
# ========================================
# 
# 같은 인터페이스를 가진 객체들이 서로 다른 방식으로 동작하는 것입니다.
# 📖 더 자세한 내용: 학습가이드/05-객체지향프로그래밍.md#5-다형성-polymorphism

class Shape:
    """도형을 나타내는 부모 클래스"""
    
    def __init__(self, name):
        self.name = name
    
    def area(self):
        """면적을 계산하는 메서드 (자식 클래스에서 구현)"""
        raise NotImplementedError("서브클래스에서 구현해야 합니다.")
    
    def perimeter(self):
        """둘레를 계산하는 메서드 (자식 클래스에서 구현)"""
        raise NotImplementedError("서브클래스에서 구현해야 합니다.")

class Rectangle(Shape):
    """사각형을 나타내는 클래스"""
    
    def __init__(self, width, height):
        super().__init__("사각형")
        self.width = width
        self.height = height
    
    def area(self):
        """사각형의 면적 계산"""
        return self.width * self.height
    
    def perimeter(self):
        """사각형의 둘레 계산"""
        return 2 * (self.width + self.height)

class Circle(Shape):
    """원을 나타내는 클래스"""
    
    def __init__(self, radius):
        super().__init__("원")
        self.radius = radius
    
    def area(self):
        """원의 면적 계산"""
        return 3.14159 * self.radius ** 2
    
    def perimeter(self):
        """원의 둘레 계산"""
        return 2 * 3.14159 * self.radius

def demonstrate_polymorphism():
    """다형성 예시"""
    print("\n=== 다형성 (Polymorphism) ===")
    
    # 다양한 도형 객체들 생성
    shapes = [
        Rectangle(5, 3),
        Circle(4),
        Rectangle(2, 6),
        Circle(3)
    ]
    
    # 다형성 활용: 같은 메서드 호출이지만 각각 다른 방식으로 동작
    for shape in shapes:
        area = shape.area()
        perimeter = shape.perimeter()
        print(f"{shape.name}: 면적={area:.2f}, 둘레={perimeter:.2f}")

demonstrate_polymorphism()

# ========================================
# 📌 접근 제어와 @property
# ========================================
# 
# 데이터를 보호하고 안전하게 관리하는 방법입니다.
# 📖 더 자세한 내용: 학습가이드/05-객체지향프로그래밍.md#6-접근-제어

class Temperature:
    """온도를 나타내는 클래스 (접근 제어 예시)"""
    
    def __init__(self, celsius=0):
        self._celsius = celsius  # Protected 변수 (내부 사용)
        self.__secret = "비밀 정보"  # Private 변수 (클래스 내부에서만 사용)
    
    @property
    def celsius(self):
        """섭씨 온도 조회 (getter)"""
        print(">> getter가 호출되었습니다.")
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        """섭씨 온도 설정 (setter)"""
        print(">> setter가 호출되었습니다.")
        if value < -273.15:
            raise ValueError("절대 영도(-273.15°C)보다 낮을 수 없습니다.")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        """화씨 온도 조회 (getter)"""
        return self._celsius * 9/5 + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        """화씨 온도 설정 (setter)"""
        self.celsius = (value - 32) * 5/9
    
    def get_secret(self):
        """비밀 정보 조회 메서드"""
        return self.__secret

def demonstrate_access_control():
    """접근 제어 예시"""
    print("\n=== 접근 제어와 @property ===")
    
    # 온도 객체 생성
    temp = Temperature(25)
    print(f"초기 섭씨 온도: {temp.celsius}°C")
    print(f"초기 화씨 온도: {temp.fahrenheit}°F")
    
    # 온도 변경 (setter 호출)
    print("\n온도 변경:")
    temp.celsius = 30
    print(f"변경된 섭씨 온도: {temp.celsius}°C")
    print(f"변경된 화씨 온도: {temp.fahrenheit}°F")
    
    # 화씨로 온도 설정
    print("\n화씨로 온도 설정:")
    temp.fahrenheit = 86
    print(f"설정된 섭씨 온도: {temp.celsius}°C")
    print(f"설정된 화씨 온도: {temp.fahrenheit}°F")
    
    # 잘못된 값 설정 시도
    print("\n잘못된 값 설정 시도:")
    try:
        temp.celsius = -300
    except ValueError as e:
        print(f"오류: {e}")
    
    # 비밀 정보 접근
    print(f"\n비밀 정보: {temp.get_secret()}")
    
    # Private 변수 직접 접근 시도 (오류 발생)
    try:
        print(temp.__secret)
    except AttributeError as e:
        print(f"Private 변수 접근 오류: {e}")

demonstrate_access_control()

# ========================================
# 📌 실전 예제: 쇼핑몰 상품 관리 시스템
# ========================================
# 
# 학습한 객체지향 개념들을 활용한 실전 예제입니다.

class Product:
    """상품을 나타내는 기본 클래스"""
    
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
        self._discount = 0
        self._stock = 0
    
    @property
    def discount(self):
        return self._discount
    
    @discount.setter
    def discount(self, value):
        if 0 <= value <= 100:
            self._discount = value
        else:
            raise ValueError("할인율은 0-100 사이여야 합니다.")
    
    @property
    def final_price(self):
        return self.price * (1 - self._discount / 100)
    
    @property
    def stock(self):
        return self._stock
    
    def add_stock(self, quantity):
        if quantity > 0:
            self._stock += quantity
        else:
            raise ValueError("수량은 0보다 커야 합니다.")
    
    def sell(self, quantity):
        if quantity <= self._stock:
            self._stock -= quantity
            return True
        return False
    
    def get_info(self):
        return f"{self.name} - {self.final_price:,.0f}원 (재고: {self.stock}개)"

class Electronics(Product):
    """전자제품을 나타내는 클래스"""
    
    def __init__(self, name, price, brand, warranty_years):
        super().__init__(name, price, "전자제품")
        self.brand = brand
        self.warranty_years = warranty_years
    
    def get_info(self):
        return f"{self.brand} {self.name} - {self.final_price:,.0f}원 (재고: {self.stock}개, 보증: {self.warranty_years}년)"

class Clothing(Product):
    """의류를 나타내는 클래스"""
    
    def __init__(self, name, price, size, color):
        super().__init__(name, price, "의류")
        self.size = size
        self.color = color
    
    def get_info(self):
        return f"{self.name} ({self.color}, {self.size}) - {self.final_price:,.0f}원 (재고: {self.stock}개)"

def shopping_mall_system():
    """쇼핑몰 상품 관리 시스템"""
    print("\n=== 쇼핑몰 상품 관리 시스템 ===")
    
    # 상품들 생성
    laptop = Electronics("노트북", 1000000, "삼성", 2)
    phone = Electronics("스마트폰", 800000, "애플", 1)
    shirt = Clothing("셔츠", 50000, "L", "파란색")
    pants = Clothing("바지", 70000, "M", "검은색")
    
    # 재고 추가
    laptop.add_stock(10)
    phone.add_stock(5)
    shirt.add_stock(20)
    pants.add_stock(15)
    
    # 할인 적용
    laptop.discount = 15  # 15% 할인
    shirt.discount = 20   # 20% 할인
    
    # 상품 정보 출력
    products = [laptop, phone, shirt, pants]
    for product in products:
        print(product.get_info())
    
    # 판매 시뮬레이션
    print(f"\n=== 판매 시뮬레이션 ===")
    if laptop.sell(2):
        print("노트북 2대 판매 완료")
        print(f"남은 재고: {laptop.stock}개")
    
    if shirt.sell(5):
        print("셔츠 5개 판매 완료")
        print(f"남은 재고: {shirt.stock}개")
    
    # 다형성 활용: 모든 상품의 총 재고 계산
    total_stock = sum(product.stock for product in products)
    print(f"\n전체 재고 수량: {total_stock}개")

shopping_mall_system()

# ========================================
# 💡 학습 정리
# ========================================
# 
# 이 파일에서 학습한 내용:
# 1. 클래스와 객체의 개념과 사용법
# 2. 생성자와 메서드 정의
# 3. 클래스 변수와 인스턴스 변수 구분
# 4. 상속을 활용한 클래스 설계
# 5. 메서드 오버라이딩으로 다형성 구현
# 6. 접근 제어로 데이터 보호
# 7. @property로 안전한 속성 관리
# 8. 실전 프로젝트에서의 객체지향 활용
# 
# 📚 다음 단계: 학습가이드/06-데이터분석라이브러리.md
