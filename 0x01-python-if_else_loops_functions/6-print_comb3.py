 in range(0, 9):
    for b in range(a + 1, 10):
        if a == 8:
            print('{}{}'.format(a, b))
        else:
            print('{}{}'.format(a, b), end=", ")
