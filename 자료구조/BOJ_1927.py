# 최소힙(실버2)
import sys
import heapq
heap=[]
n=int(sys.stdin.readline().strip())
for i in range(0, n):
    data = int(sys.stdin.readline().strip())
    if(data==0):
        if(len(heap)==0):
            print(0)
        else:
            print(heap[0])
            heapq.heappop(heap)
    else:
        heapq.heappush(heap, data)


