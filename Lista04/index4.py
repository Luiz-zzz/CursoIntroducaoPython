N = int(input())
X = list(map(int, input().split()))

min_value = X[0]
min_position = 0

for i in range(1, N):
  if X[i] < min_value:
   min_value = X[i]
   min_position = i
    
print(f'Menor valor: {min_value}')
print(f'Posicao: {min_position}')
