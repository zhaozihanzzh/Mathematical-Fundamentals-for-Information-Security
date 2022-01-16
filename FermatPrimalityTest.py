'''
Copyright (c) 2022 zhaozihanzzh
Mathematical-Fundamentals-for-Information-Security is licensed under Mulan PubL v2.
You can use this software according to the terms and conditions of the Mulan PubL v2.
You may obtain a copy of Mulan PubL v2 at:
         http://license.coscl.org.cn/MulanPubL-2.0
THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND,
EITHER EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT,
MERCHANTABILITY OR FIT FOR A PARTICULAR PURPOSE.
See the Mulan PubL v2 for more details.
'''
# Fermat 素性检验算法
# 最大公因数
import random
def gcd(x, y):
    while (y != 0):
        temp = x % y
        x = y
        y = temp
    return x
# 模重复平方算法(底数，幂，模)
def fastModularExponentiation(b: int, n: int, m: int) -> int:
    a = 1
    b = b % m
    while (True):
        if n % 2:
            a = a * b % m
        b = b * b % m
        n = n >> 1
        if n == 0:
            break
    return a

def FermatPrimalityTest(n : int, threshold : float) -> bool:
    if n < 0:
        # 负数转正数
        n = -n
    if n == 0 or n == 1:
        # 0 或 1 不是素数
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        # 排除除了 2 外所有偶数
        return False
    t = 0
    while True:
        b = random.randint(1, n - 1)
        d = gcd(b, n)
        if d > 1:
            print("发现因数", d)
            return False
        if 1 != fastModularExponentiation(b, n - 1, n):
            return False
        t = t + 1
        if 1 - 0.5 ** t > threshold:
            return True
    
print("请输入要用 Fermat 素性检验算法检验的数字 n，输入完后按 Enter：")
n = int(input())
print("请输入要求检验 n 为素数的概率，输入完后按 Enter：")
p = float(input())
if p >= 1 or p <= 0:
    print("概率应在 (0, 1) 内。")
    exit(0)
if FermatPrimalityTest(n, p) == True:
    print(n, "通过 Fermat 素性检验")
else:
    print(n, "不是素数")