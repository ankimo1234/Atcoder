S = input()
l = len(S)
if l > 1:
    if S[0].isupper() and S[1:].islower():
        print("Yes")
    else:
        print("No")
else:
    if S[0].isupper():
        print("Yes")
    else:
        print("No")