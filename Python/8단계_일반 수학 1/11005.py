alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
s ='' # 진법 계산한 결과 저장할 문자열

N, B = map(int, input().split()) # 10진법 수 N, B진법

while N: # N이 0이 될 때까지 계산
     s += str(alphabet[N%B]) # N%B해서 나온 결과를 s에 하나씩 저장
     N //= B # 나머지 없애서 다시 저장
    
print(s[::-1]) # 역순으로 출력(낮은 자릿수부터 계산했으니)