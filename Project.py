def test(n):
    """ """
    div_sum = [1]*n
    for i in range(2, int(n/2) + 1):
        for j in range(i, n, i):
            if j != i:
                div_sum[j] += i
    print(div_sum)
    total = 0
    for i in range(1, n):
        s = div_sum[i]
        if s < n:
           s1 = div_sum[s]
           if  s1 == i and s != i:
              total += s1
    print(total)
test(int(input()))
