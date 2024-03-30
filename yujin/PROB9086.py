#문자열
T = int(input())
for _ in range(T):
    S = input()
    print(S[0]+S[len(S)-1])
#S[-1]로 써도 되는듯