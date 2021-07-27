def remove2(X):
    n=len(X)-2
    i=0
    while i<n:
        m=len(X)
        if i+2<=m-1:
            if X[i]==X[i+2]:
                X.pop(i+2)
            else:
                i+=1
        else:
            i+=1
    print(len(X),',nums=',X)