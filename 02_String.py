## 파이썬의 기본 자료형은 String, Boolean, list, set, tuple, dictionary, int, float  등이 있다.

## String
# 문자열을 나타낸다. 큰 따옴표(" ") 혹은 작은 따옴표(' ')로 나타낸다. 여러줄에 걸쳐 문자열을 표현할 때는 따옴표를 세번씩 사용하여 감싼다. 이는 주석처리에도 이용할수있다.
""" 여러줄에 걸친
주석 처리 혹은
"""
s = '''
변수 선언
가능
'''

print(s)

s1 = "Missu"
s2 = 'missu'
print(s1, type(s1))
print(s2, type(s2))

# 인덱싱
# 문자열 변수에 대괄호를 통해 인덱싱을 할 수 있다.
print(s1[0:3])  # Mis
print(s1[0:-1]) # Miss
print(s1[::-1]) # (전체 reverse), ussiM
print(s1[4:1:-1])   # uss

# 문자열 끼리 덧셈이 가능하다.
a = 'I'
b = 'Love'
c = 'You'
print(a+b+c)     #ILoveYou
print(a,b,c)     #I Love You   띄어쓰기 위해서는 print 함수에서 콤마로 구분한다.

# 문자열 곱셈도 가능하다.
print('*'*5)   # *****

# 문자열 포맷팅
name = 'Jaeyoon'
print("방법1: 제 이름은 {0}입니다.".format(name))    #포맷 함수를 사용,
print(f"방법2: 제 이름은 {name}입니다.") # f 스트링을 사용, 넣고자하는 위치에 변수명 기입
print("방법3: 제 이름은 %s입니다."%(name))   # % 포맷팅 사용

print("방법1-1: 제 이름은 {0:^10}입니다.".format(name))    #글자 자리수와 정렬을 할 수 있다.
print("방법1-2: 제 이름은 {0:<10}입니다.".format(name))
print("방법1-3: 제 이름은 {0:>10}입니다.".format(name))
print("방법1-4: 제 이름은 {0:!>10}입니다.".format(name))     # 공백채우기 가능
print(f"방법2-1: 제 이름은 {name:^10}입니다.") # f 스트링 역시 정렬이 가능하다.
print(f"방법2-2: 제 이름은 {name:10}입니다.")
print("방법3-1: 제 이름은 %10s입니다."%(name))
print("방법3-1: 제 이름은 %-10s입니다."%(name))

#여러 변수 사용
age = 25
print("방법1: 제 이름은 {0}이고, 나이는 {1}살입니다.".format(name,age))
print(f"방법2: 제 이름은 {name}이고, 나이는 {age}살입니다.")
print("방법3: 제 이름은 %s이고, 나이는 %d살입니다."%(name, age))       #### % 포맷팅을 사용할 때 문자열에 %를 표현하고싶으면 %%으로 작성해야한다.

# 탈출문자 (?)
# \n, \t, \\, \', \"
# 문자열 속에 따옴표를 넣고 싶을 때
print("저는 '코딩' 연습중입니다.")   # 큰 따옴표, 작은 따옴표를 구분해서 쓴다.
print("저는 \"코딩\" 연습중입니다.") # 같은 문자를 쓸때 백슬래시를 이용한다.
print("저는\n코딩\n연습중입니다.")    # \n 은 한 줄 띄어서 출력해준다.
print("저는\t코딩\t연습중입니다.")    # \t 는 한 탭 띄어서 출력해준다.

## print함수는 마지막 기본값이 \n으로 되어 있다. end 파라미터를 바꿔줌으로써 출력의 변화를 줄 수 있다.
print("저는", end = " ")
print("코딩", end = " ")
print("연습")
print("중입니다.")

# 파일 경로를 불러올 때
path1 = "C:\\Users\\hjy9891\\PycharmProjects\\Practice\\02_String.py"
path2 = "C:/Users/hjy9891/PycharmProjects/Practice/02_String.py"
# 백슬래시를 두번씩 써 주거나 슬래시를 통해 경로를 입력해야한다.


# 문자열의 길이
print(s)
print(len(s))

# 글자 변환
s = 'abcde'
print(s)
s = s.replace('c', 'z')
print(s)

# count
c = s.count('a')
print(c)
s += "aaa"
c = s.count('a')
print(c)

# find는 없는 값을 찾을때 -1도 반환
idx_a = s.find("a")
print(idx_a)

# index는 없는 값 찾을 때 에러
idx_b = s.index("b")
print(idx_b)

# 문자열 중간에 :을 삽입한다.
s = ":".join(s)
print(s)

# 대문자 변환
print(s.upper())

# 소문자 변환
print(s.lower())

s = s.split(":")    # : 기준으로 문자열 나누기
print(s)

## 공백 지우기
test = "\n저는 코딩을\t공부중입니다.    "
print(test, end="")
print("ddd")

test = test.rstrip()
print(test, end="")
print("ddd")

test = test.lstrip()
print(test, end="")
print("ddd")

## strip은 양쪽 공백 지우기가 가능하다.