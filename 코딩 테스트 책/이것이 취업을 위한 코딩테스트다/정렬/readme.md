정렬이란 특정한 기준에 따라서 순서대로 나열하는 것을 말한다.
프로그램에서 데이터를 가공할 때 오름차순이나 내림차순으로 정렬해서 사용하는 경우가 많기에 정렬 알고리즘은 프로그램을 작성할 때 가장 많이 사용되는 알고리즘이다. 정렬알고리즘으로 데이터를 정렬하면 다음장에서 배울 이진 탐색이 가능해진다. 정렬 알고리즘은 이진 탐색의 전처리 과정이기도 하니 제대로 알고 넘어가자.
정렬 알고리즘에서는 흔히 데이터의 개수를 N이라고 **표현한다**. 다음 예제에서는 n = 10 인경우를 가정한다. 
\


퀵 정렬의 시간 복잡도에대해 알아보자.

퀵정렬의 평균 시간 복잡도는 o(nlogn)이다.

앞서 다루었던 두 정렬 알고리즘에 비해 매우 빠르다.
퀵정렬이 어떻게 평균적으로 onlogn의 시간 복잡도를 가지는 지 궁금할 수 있는데 퀵정렬의 시간 복잡도에대한 증명은 초보자가 다루기에 간단하지 않다. 

퀵 정렬에서 최선의 경우를 생각해보자. 피벗값의 위치가 변경되어 분할이 일어날 때마다 정확히 왼쪽 리스트와 오른쪽 리스트를 절반씩 분할한다면 어떠띾 데이터의 개수가 8개라고 가정하고 다음과 같이 정확히절반씩 분할한다면 어떨까?이때 높이를 확인해보면, 데이터의 개수가 n개일때 높이는  logN이라고 할 수 있다.

컴퓨터과학에서 log의 의미는 밑이 2인로그를 의미한다. 데이터의 개수가 많을 수록 극명하게 이 알고리즘의 효율이 좋다는 것을 알 수 있다.


평균시간 복잡도를 기준으로 각 정렬 알고리즘이 데이터의 개수에 따라 얼마나 많은 연산을 요구하는지를 보여주기 위해 작성했고 엄밀한 연산 비교횟수는 아니다.



일반적으로 컴퓨터 공학 학부에서 퀵 정렬을 공부 할 때는 퀵정렬의 수학적인 검증에 대해서도 공부하지만 코딩테스트를 준비하는 과정에서는 그림을 통해 직관적인 이해를 하는 것만으로 충분하다.




## 계수 정렬

계수 정렬 알고리즘은 특정한 조건이 부합할 때만 사용할 수 있지만 매우 빠른 정렬 알고리즘이다.

모든 데이터가 양의 정수인 상황을 가정해보자 데이터의 개수가 N 데이터중 최댓값이 K일때 계수 정렬은 최악의 경우에도 수행시간 O(N+K)를 보장한다. 계수 정렬은 이처럼 매우 빠르게 동작할 뿐만아니라 원리 또한 매우 간단하다. 예를 들어 데이터의 값이 무한한 범위를 가질수 있는 실후형 데이터가 주어지는 경우 계수 정렬은 사용하기 어렵다. 일반적으로 가장 큰 데이터와 가장 작은 데이터의 차이가 1000000 을 넘지 않을 때 효과적으로 사용할 수 있다.


가장 작은 값과 가장 큰 데이터의 차이가 1,000,000dlaus chd 1,000,001개의 데이터가 들어갈 수 있는 리스트를 초기화해야한다.


계수 정렬은 앞서 다루었던 3가지 정렬 알고리즘처럼 직접 데이터의 값을 비교한 뒤에 위치를 변경하며 정렬하는 방식이아니다.



계수 정렬은 일반적으로 별도의 리스트를 선언하고 그안에 정렬에 대한 정보를 담는다는 특징이 있다. 구체적인 예시를 통해 계수 정렬에 대해서 이해해보자. 단 말했듯이 계수 정렬은 데이터의 크기가 제한되어있을 때 한에서 데이터의 개수가 많더라도 빠르게 동작한다.


앞서 언급했듯이 모든 데이터가 양의 정수인 상황에서 데이터의 개수를 N, 데이터 중 최대 값의 크기를 K라고 할 때, 계수 정렬의 시간 복잡도는 O(N+K)이다. 계수 정렬은 앞에서부터 데이터를 하나씩 확인하면서 리스트에서 적절한 인덱스의 값을 1씩 증가시킬 뿐만 아니라 추후에 리스트의 각 인덱스에 해당하는 값들을 확인할 때 데이터중 최댓값의 크기만큼 반복을 수행해야하기 때문이다.

따라서 데이터의 범위만 한정되어있다면 효과적으로 사용할 수 있으며 항상 빠르게 동작한다. 사실상 현존하는 정렬 알고리즘중에서 기수정렬과 더불어 가장 빠르다고 볼 수 있다. 
보통 기수 정렬은 계수 정렬에 비해서 동작은 느리지만 처리하는 정수의 크기는 더크다. 다만 알고리즘원리나 소스코드는 더욱 복잡하다 다행히 반드시 기수 정렬을 이용해야만 해결할수 있는 문제는 코테에서 거의 출제되지 않는다.


계수 정렬은 때에 따라서 심각한 비효율성을 초례할 수 있다.
예를 들어서 데이터가 0 과 999,999단 2개만 존재한다고 가정해보자. 이럴 때에도 리스트의 크기가 100만개가 되도록 선언해야한다. 따라서 항상 사용할 수 있는 정렬알고리즘은 아니며 동일한 값을 가지는 데이터가 여러개 등장할 때 적합하다. 예를 들어 성적의 경우 100점을 맞은 학생이 여러명일 수 있기 때문에 계수 정렬이 효과적이다.

반면에 앞에서 설명한 퀵정렬은 일반적인 경우에서 평균적으로 빠르게 동작하기 때문에 데이터의 특정을 파악하기 어렵다면 퀵정렬을 이용하는 것이좋다.

일반적인 코테 환경상에서는 메모리 공간상의 제약과 입출력 시간 문제로 인하여 입력되는 데이터의 개수를 1000만개 이상으로 설정할 수 없는 경우가 많기 때문에 정렬문제에서 데이터의 개수는 1000만개 미만으로 출제될 것이다.

파이썬은 기본 정렬라이브러리인 sorted()함수를 제공한다. sorted()는 퀵정렬과 동작 방식이 비슷한 병합정렬을 기반으로 만들어졌는데, 병합정렬은 일반적으로 퀵정렬보다 느리지만 최악의 경우에도 시간 복잡도 o(nlogn)을 보장한다는 특징이 있다. 이러한 sorted 함수는 리스트 , 딕셔너리 자료형등을 입력받아서 정렬된 결과를 출력한다.


sorted 나 sort 를 이용할 때에는 key 매개변수를 입력으로 받을 수 있다. key값으로는 하나의 함수가 들어가야하며 이는 정렬 기준이되낟. 예를 들어 리스트의 데이터가 튜플로 구성되어있을 때 각 데이터의 두 번째 원소를 기준으로 설정하는 경우 다음과같은 소스코드 형태로 작성가능하다.

```py
array = [ ('밥나나ㅏ', 2), ('사과', 5), ('당근', 3)]

def setting(data):
    return data[1]

result = sorted(array, key=setting)

print(result)
```



코테 정렬 3가지 유형

1. 정렬 라이브러리로 풀 수 있는 문제: 단순히 정렬 기법을 알고 있는지 물어보는 문제로 기본 정렬 라이브러리의 사용방법을 숙지하고 있으며 어렵지 않게 풀 수 있다.
2. 정렬 알고리즘의 원리에 대해서 물어보는 문제
3. 더빠른 정렬이 필요한 문제

