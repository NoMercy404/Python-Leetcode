def fizzBuzz(n):
    tab = []
    for i in range(1, n + 1):
        if (i % 3 != 0 and i % 5 != 0):
            tab.append(str(i))
        elif (i % 3 == 0 and i % 5 != 0):
            tab.append("Fizz")
        elif (i % 3 != 0 and i % 5 == 0):
            tab.append("Buzz")
        elif (i % 3 == 0 and i % 5 == 0):
            tab.append("FizzBuzz")
    return (tab)
