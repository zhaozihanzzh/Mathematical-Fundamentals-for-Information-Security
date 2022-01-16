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
# Diffie-Hellman 算法
import random
# 最大公因数
def gcd(x, y):
    while (y != 0):
        temp = x % y
        x = y
        y = temp
    return x
# 模重复平方计算法，其中 b 是底数，n 是幂，m 是模
def fastModularExponentiation(b: int, n: int, m: int) -> int:
    a = 1
    b = b % m
    while (True):
        if n % 2 : 
            a = (a * b) % m 
        b = (b * b) % m
        n = n >> 1
        if (n == 0):
            break
    return a
def diffie_hellman(p :int, g :int):
    # g = 2
    # p 是大素数
    print("为 Alice 选取 x，x >= 1, x <= p - 1")
    print("如果您想让程序随机生成一个 x 的话，输入 0 按回车")
    x = int(input())
    if x == 0:
        x = random.randint(1, p - 1)
        print("随机选择的 x =", x)
    r1 = fastModularExponentiation(g, x, p)
    print("Alice 发送 R1", r1)

    print("为 Bob 选取 y，y >= 1, y <= p - 1")
    print("如果您想让程序随机生成一个 y 的话，输入 0 按回车")
    y = int(input())
    if y == 0:
        y = random.randint(1, p - 1)
        print("随机选择的 y =", y)
    r2 = fastModularExponentiation(g, y, p)
    print("Bob 发送 R2")
    
    alice_k = fastModularExponentiation(r2, x, p)
    print("Alice 计算出的 k 是", alice_k)

    bob_k = fastModularExponentiation(r1, y, p)
    print("Bob 计算出的 k 是", bob_k)

print("Diffie-Hellman 算法")
print("请输入素数 p ：")
p = int(input())
# g = 2
print("输入 g ，g >= 1 且 g <= p，且 g 与 p 互素：")
g = int(input())
if g < 1 or g > p or gcd(g, p) != 1:
    print("g 不符合要求。")
    exit()
diffie_hellman(p, g)

# 以下是一个 386 位的大素数
# 10407932194664399081925240327364085538615262247266704805319112350403608059673360298012239441732324184842421613954281007791383566248323464908139906605677320762924129509389220345773183349661583550472959420547689811211693677147548478866962501384438260291732348885311160828538416585028255604666224831890918801847068222203140521026698435488732958028878050869736186900714720710555703168729087