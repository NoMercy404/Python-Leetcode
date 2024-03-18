def numberOfSteps(n):
    counter = 0
    while (n > 0):
        counter += 1
        if (n % 2 == 0):
            n = n / 2
        else:
            n = n - 1
    return (counter)
