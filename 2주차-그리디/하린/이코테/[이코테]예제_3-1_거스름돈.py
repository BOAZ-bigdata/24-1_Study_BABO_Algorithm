"""
그리디 알고리즘
이코테 예제 3-1

문제
당신은 음식점의 계산을 도와주는 점원이다.
카운터에는 거스름돈으로 사용할 500원, 100원, 50원, 10원짜리 동전이 무한히 존재한다고 가정한다.
손님에게 거슬러 줘야 할 돈이 N원일 때 거슬러 줘야 할 동전의 최소 개수를 구하라.
단, 거슬러 줘야 할 돈 N은 항상 10의 배수이다.
"""

"""
생각
거슬러 줘야 할 동전의 "최소 개수"라는 말을 보고 greedy 알고리즘을 이용하는 것을 알 수 있음.
N원을 거슬러 줘야 할 때, 가장 큰 단위인 500원부터 최대로 거슬러줌 -> 나눈 몫으로 생각
"""

# 내 코드 

N = int(input())

# 총 거슬러 줘야 할 동전의 개수
count=0

# 500원, 100원, 50원, 10원 차례로 계산
money = [500, 100, 50, 10]

for coin in money:
    # 가장 큰 단위부터, 나눈 몫을 count에 더함
    count += N // coin
    # 아직 거슬러주지 못한 돈은 나머지로 계산
    N %= coin


"""

그리디 문제는 가장 큰 단위 혹은 가장 작은 단위 순서대로 푸는 문제가 많음 -> list로 작성하거나 input을 받아서 정렬 후 문제풀면 좋을듯하다

"""