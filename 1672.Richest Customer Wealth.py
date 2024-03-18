def maximumWealth(accounts):
    tab = []
    for i in accounts:
        sum = 0
        for a in i:
            sum += a
        tab.append(sum)
    return max(tab)