### List, Tuple, Set, Dictionary

# 리스트는 배열의 형태로 다양한 자료형을 저장할 수 있다.
# 대괄호를 통해 표현할 수 있다.
lst = [1,2,3]
print(lst)
print(type(lst))

# String Type과 마찬가지로, 인덱싱이 가능하다.
print(lst[0])
print(lst[2])
print(lst[-1])

# 리스트의 원소로는 문자열, 숫자, 딕셔너리, 리스트 등 다양한 원소를 저장한다.
lst = [1,'test', {3:'Three'}, [3,4,5]]
print(lst)
print(lst[-1][2])   # 인덱싱 두번으로 원소를 찾아올 수 있다.

## 리스트 Method
# append 함수는 원소를 하나 추가한다.
lst.append('추가')
print(lst)

# extend 함수는 다른 리스트를 이어 붙인다.
add_lst = ['새로운 리스트', '추가합니다.']
lst.extend(add_lst)
print(lst)

# 더하기 연산으로도 extend와 같은 결과를 출력할 수 있다.
lst = lst + add_lst
print(lst)

# insert(i, x) i위치에 x 원소를 추가한다.
lst.insert(1,'인덱스가 1인 자리에 추가')
print(lst)

# remove  특정값을 제거한다. 제거할 원소가 없을 시 ValueError
lst.remove('인덱스가 1인 자리에 추가')
print(lst)
# lst.remove('22')     ValueError: list.remove(x): x not in list

# pop, 특정 인덱스 위치의 값을 제거 후 반환한다.
pop_value = lst.pop(2)
print(lst,'\n', pop_value)

# clear 모든 원소 삭제
lst.clear()
print(lst)

# index 찾는 원소의 첫번째 인덱스값을 반환, 찾기시작하는 위치와 끝 위치 지정가능
lst = [1,3,5,7,8,9,3,3]
print(lst.index(3))
print(lst.index(3,2))

# count, 원소의 개수를 반환
print(lst.count(3))

# sort, 기본으로 오름차순 정렬
lst.sort()
print(lst)

## 다양한 자료가 있을때?
lst = [1,{1:'one'}, [3,2,4], 'sdf']
print(lst)
# 에러가 난다.
# lst.sort()
# print(lst)

# reverse는 거꾸로 뒤집어준다.

### append와 pop Method를 통해 Stack을 구현할 수 있다.
stack = [1,2,3]
stack.append(7)
print(stack)
print(stack.pop())
print(stack.pop())
print(stack)

## append와 pop(0) 을 통해 Queue를 구현할 수 있다. 하지만 이 방법의 경우, 맨 앞의 원소를 빼낸 후 모든 데이터를
## 왼쪽으로 한차례 움직여야하기 때문에 실행속도가 느리다는 단점이 있다.
## collections.deque 를 import 하여 큐와 관련된 연산을 수행할 수 있다.
from collections import deque
dq = deque([1,4,2,3])
print(dq)
print(dq.popleft())
print(dq)


## List comprehension
# 한줄로 리스트를 만들 수 있다
comp_lst = [x for x in range(0,10,2)]   # 0부터 10이전까지 짝수 출력
print(comp_lst)
comp_lst.clear()    #초기화
comp_lst = [x for x in range(10) if x%2==0] # if문을 사용
print(comp_lst)

# 이중으로 for문을 사용할 수도 있음
comp_lst = [(x,y) for x in range(1,4) for y in range(4,7)]
print(comp_lst)

lst = [[1,2,3],[4,5,6],[7,8,9]]
comp_lst = [x for element in lst for x in element]
print(comp_lst)


## List comprehension을 이중으로 사용할 수 있음
matrix = [
    [1,3,5,6,7],
    [2,4,3,5,2],
    [1,5,7,8,5]
]
# 위와 같은 3*5 matrix를 Transpose 가능
# 5 열에 해당하는 matrix[0]의 길이만큼, 각 row의 해당 열의 원소를 리스트로 만드는 역할
Trans_matrix = [[row[i] for row in matrix]for i in range(len(matrix[0]))]
print(Trans_matrix)

## 내장함수로도 Transpose를 구현가능
##### 내장함수에 대한 정리도 추후에
new_matrix = list(zip(*matrix))
print(new_matrix)



# Tuple
# 원소의 변경이 가능한 리스트와 다르게
lst = [1,3,5]
print(lst)
lst[1] = 4
print(lst)

# 소괄호로 묶어준 Tuple은 원소의 변경이 불가능할 때 사용한다.
tp = tuple()
tp = (1,3,5)
print(tp)
print(type(tp))

## set
# 중복값의 사용이 가능한 리스트와 다르게
# 각 원소의 중복을 허용하지 않으며, 집합 연산이 가능하다.
# 또한, 순서의 의미가 없다.
A = {1,3,5,7,10,10,10}
B = {2,4,6,8,10,10}
print(A, type(A),B,type(B))

C = A&B
print(C)
C = A|B
print(C)
C = A-B
print(C)
C = A^B
print(C)

# 집합도 comprehension이 가능하다.
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)


## 딕셔너리
# Key: Value 쌍으로 이루어져있다. Key를 통해 Value를 찾을 수 있다.
d = dict()
d['key1'] = 1
d['key2'] = 12
print(d)

# Key는 변하지 않는 값으로 설정해야한다. 따라서, 리스트를 Key로 사용할 수 없다.

# get method
# 키 값에 해당하는 value를 반환한다.
print(d.get('key1'))
# 키값에 해당하는 value가 없을 때는 None을 반환한다.
print(d.get('key4'))
print(d)
# 키값에 해당하는 value가 없을 때 초기값을 주어 딕셔너리에 추가할 수 있다.
d['key4'] = d.get('key4', '기본값')
print(d['key4'])
print(d)

# key, value, (key,value) 의 리스트를 만들 수 있다.
d_key = d.keys()
d_value = d.values()
d_item = d.items()

# for문을 통해 k, v를 모두 확인할 수 있다.
for k,v in d.items():
    print('키 : {:10}\t밸류 : {:>10}'.format(k,v))