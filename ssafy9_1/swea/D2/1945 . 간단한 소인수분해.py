T = int(input()) #입력받은 수

for ts in range(1,T+1):
    n = int(input())
    d = {2:0,3:0,5:0,7:0,11:0}
    
    for i in [2,3,5,7,11]: #소인수분해
        while True:
            if n%i == 0:
                d[i] += 1
                n /= i
            else:
                break
        
    print(f'#{ts}', *d.values())