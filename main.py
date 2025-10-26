def PrimeList(N):
    if N <= 2:
        return ""
    
    # 创建一个布尔数组，初始值都为True
    is_prime = [True] * N
    is_prime[0] = False  # 0不是质数
    is_prime[1] = False  # 1不是质数
    
    # 埃拉托斯特尼筛法
    for i in range(2, int(N**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, N, i):
                is_prime[j] = False
    
    # 收集所有质数
    primes = [str(i) for i in range(2, N) if is_prime[i]]
    
    # 以空格连接并返回
    return " ".join(primes)
