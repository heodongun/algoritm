#DFS
# a=[[0,1,1,0],[1,0,0,1],[1,0,0,0],[0,1,0,0]]
# visited=[0,0,0,0]
#
# def al(cul,n):
#     visited[cul]=1
#     print(cul+1)
#     for i in range(n):
#         if a[cul][i]==1 and visited[i]==0:
#             al(i,n)
#
# al(0,4)
from re import split

from pycparser.ply.yacc import resultlimit
from pygments.lexers import graph


# def dfs(student, target, visited): #dfs라는 함수를 만들어준다.
#     if student == target: #target노드까지 갔다면 True를 반환해준다.
#         return True
#     visited.add(student) #방문을 하면 visited안에 추가해준다.
#     for friend in graph[student]: #반학생수만큼 돈다.
#         if friend not in visited: #만약 한번도 이 노드를 들르지않았다면
#             if dfs(friend, target, visited): #방문하지않았다면 노드를 따라 쭉 간다.
#                 return True #이게 없다면 노드를 찾았는데도 반복문이 끝날때까지 True가 나오지않아서 False가 뜬다.
#     return False #반복문이 돌때까지 True가 나오지않으면 False를 리턴해준다.
#
#
# N, M = map(int, input().split())  #학생수와 입력받을 갯수를 입력받는다.
# graph = {i: [] for i in range(1, N + 1)} #사전 자료형으로 학생수만큼 만들어준다 keys는 1부터 학생수만큼이고 value는 빈 배열이다.
#
# for i in range(M): #반복문을 돌린다
#     a, b = map(int, input().split()) #입력을 받고 int로 바꾸어준다.
#     graph[a].append(b) #graph의 a라는 키값에 b를 추가해준다.
#     graph[b].append(a) #graph의 a라는 키값에 b를 추가해준다.
#
#
# x, y = map(int, input().split()) #친구인지 확인해보고 싶은 친구 번호를 적는다.
#
#
# visited = set() #빈 집합을 생성한다.
# if dfs(x, y, visited): #True면 YES로 출력하고 아니면 NO로 출력한다.
#     print("YES")
# else:
#     print("NO")

#BFS
# from collections import deque
#
# def bfs(graph, start,visited):
#     queue = deque()
#     visited[start] = True
#     while queue:
#         v=queue.popleft()
#         print(v,end=" ")
#         for u in graph[v]:
#             if u not in visited:
#                 queue.append(u)
#                 visited[u] = True
# graph=[
#     [],
#     [2,3,8],
#     [1,7],
#     [1,4,5],
#     [3,5],
#     [3,4],
#     [7],
#     [2,6,8],
#     [1,7]
# ]
#
# visited = [False]*9
# bfs(graph,1,visited)
#
# def dfs(x,y):
#     if x<=-1 or x>=n or y<=-1 or y>=m:
#         return False
#     if bayel[x][y]==0:
#         bayel[x][y]=1
#         dfs(x-1,y)
#         dfs(x+1,y)
#         dfs(x,y+1)
#         dfs(x,y-1)
#         return True
#     return False
#
#
# n,m=map(int,input().split())
# bayel=[]
# for i in range(m):
#     bayel.append(list(map(int,input())))
#
# sum=0
# for i in range(m):
#     for j in range(n):
#         if dfs(i,j)==True:
#             sum+=1
# print(sum)

def dfs(y, x, color):
    if x < 0 or y < 0 or x >= 7 or y >= 7:
        return 0
    if babel[y][x] != color:
        return 0

    babel[y][x] = 0
    result = 1
    result += dfs(y + 1, x, color)
    result += dfs(y - 1, x, color)
    result += dfs(y, x + 1, color)
    result += dfs(y, x - 1, color)

    return result



babel = []
for i in range(7):
    babel.append(list(map(int, input().split())))

sum = 0


for i in range(7):
    for j in range(7):
        color = babel[i][j]
        if color != 0:
            result = dfs(i, j, color)
            if result >= 3:
                sum += 1

print(sum)
