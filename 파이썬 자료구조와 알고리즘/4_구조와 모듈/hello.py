# 파이썬에서 모듈은 def 를 사용하여 정의한다.
# def 가 실행되면, 함수의 객체와 참조가 같이 생성된다.
# 반환값을 정의하지 않으면 파이썬은 자동으로 None을 반환한다.
# C와 마찬가지로 아무런 값을 반환하지 않는 함수는 프로시저라고 부른다.

# 함수를 호출할 때마다 활성화 레코드가 생성된다
# 활성화 레코드에는 함수의 정보가 기록되며 이를 스택에 저장한다.
# 활성화 레코드가 처리 되는 순서
# 1. 함수의 실제 매개변수를 스택에 저장
# 2. 반환주소를 스택에 저장
# 3. 스택의 최상위 인덱스를 함수의 지역변수에 필요한 총량만큼 늘린다.
# 4. 함수로 건너뛴다.
# 활성화 레코드를 풀어내는 절차
# 1. 스택의 최상위 인덱스는 함수에 소비된 총 메모리양(지역 변수) 만큼 감소한다.
# 2. 반환주소를 스택에서 빼낸다.
# 3. 스택의 최상위 인덱스는 함수의 실제 매개변수만큼 감소한다.
#
#

def append(number ,number_list =None):
    if number_list is None:
        number_list = []
    number_list.append(number)
    return number_list

# 패키지는 모듈과 __init__.py 파일이 있는 디렉터리다.
# 파이썬은 인잇 파일이 있는 디렉터리를 패키지로 취급
# 모듈 검색 경로 중 string 과 같이 흔한 이름의 디렉터리에 유효한 모듈이 들어있는 경우 이러한 모듈이 검색되지않는 문제 방지


hello = "hello"
def world():
    return "world"
if __name__ =="__main__":
    print("{0} 직접 실행 됬다 ㅋ".format(__name__))
else:
    print("{0} 임포트 됨 ㅋ".format(__name__))

# 자기 파일에선 main
# 남의 파일에선 자기 이름으로 불린다.