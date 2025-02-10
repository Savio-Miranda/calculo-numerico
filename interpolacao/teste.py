X = [1, 2, 3, 4, 5, 6]

for i in range(len(X)):
    for j in range(len(X)):
        if j != i:
            print(X[j])
    print(5*"-")