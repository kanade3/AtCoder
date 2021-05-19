s = input()
s += '111111111'
cur = 0 
ok = True

while cur <= len(s)-1:
    word = s[cur:cur+5]
    if word=="11111":
        break
    print(word)
    cur+=5
    if word == "dream":
        if s[cur:cur+2] == "er":
            if s[cur:cur+5]!="erase":
                cur+=2
    
    elif word == "erase":
        if s[cur:cur+1] == "r":
            cur+=1
    else:
        ok=False
        break
print("YES" if ok else "NO")