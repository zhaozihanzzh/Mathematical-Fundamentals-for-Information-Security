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
# 模重复平方算法
def mod(x, m):
    return x - x // m * m
def fastModularExponentiation(b: int, n: int, m: int) -> int:
    a = 1
    b = mod(b, m)
    while (True):
        if (n - n // 2 * 2):
            a = mod(a * b, m)
        b = mod(b * b, m)
        n = n >> 1
        if (n == 0):
            break
    return a
print("请依次输入底数 b，幂 n 和模 m，每输入一个数均需要按 Enter")
base = int(input())
exp = int(input())
modulo = int(input())
if modulo == 0:
    print("不能模 0 ！")
    exit(0)
print("答案", fastModularExponentiation(base, exp, modulo))