#최대힙(실버2)
import sys
import heapq
heap = []
a = int(sys.stdin.readline())
for i in range(a):
    data = int(sys.stdin.readline())
    if data == 0:
        if (len(heap)==0):
            print(0)
        else:
            print(-heap[0]) # 부호를 바꾸어서 최대 힙을 구현한다.
            heapq.heappop(heap)
    else:
        heapq.heappush(heap, -data)
