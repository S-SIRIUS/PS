# 럭키 스트레이트
n = int(input())
list_n = list(map(int, list(str(n))))
standard = len(list_n)//2
print(list_n)
if sum(list_n[0:standard]) == sum(list_n[standard:]):
    print("LUCKY")
else:
    print("READY")
