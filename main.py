def primo(n):
    div=0
    if(n>=2):
        for i in range(1,n+1):
            if(n%i==0):
                div+=1
    if(div==2):
        return "es primo"
    else:
        return "no es primo"

print(primo(8))
print(primo(1))
print(primo(5))
