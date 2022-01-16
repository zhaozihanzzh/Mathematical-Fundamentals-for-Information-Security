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
# 求s, t 使得 sa + tb = (a, b)
# 《信息安全数学基础》，第二版，陈恭亮，P28 定理 1.3.7：
# 设 a, b 是任意两个正整数，则 s_{n}a+t_{n}b=(a, b)；
# 对 j = 0, 1, 2, ..., n-1, n，这里 s_{j}，t_{j} 归纳地定义为
# s_{-2} = 1, s_{-1} = 0, s_{j} = (-q_{j})s_{j-1}+s_{j-2},
# t_{-2} = 0, t_{-1} = 1, t_{j} = (-q_{j})t_{j-1}+t_{j-2}
# 其中 q_{j}=[r_{j-2}/r_{j-1}] 是广义欧几里得除法中取最小非负余数时的不完全商。
def findST(a, b):
    if (a == 0 and b == 0):
        print("a 和 b 不能全为 0，这样不存在最大公因数")
        return
    if (b == 0):
        # 此时 b = 0
        s = 1
        t = 0
    else:
        s_jminus2 = 1
        s_jminus1 = 0
        t_jminus2 = 0
        t_jminus1 = 1
        q = a // b
        r_minus2 = b
        r_minus1 = a % b
        if (r_minus1 == 0):
            # 此时 a = 0，b 是 a 的因数，最大公因数为 b 的绝对值
            s = 0
            t = 1
        while (r_minus1 != 0):
            last_q = q
            q = r_minus2 // r_minus1
            r = (-q) * r_minus1 + r_minus2
            s = (-last_q) * s_jminus1 + s_jminus2
            t = (-last_q) * t_jminus1 + t_jminus2
            r_minus2 = r_minus1
            r_minus1 = r
            s_jminus2 = s_jminus1
            s_jminus1 = s
            t_jminus2 = t_jminus1
            t_jminus1 = t
    if (s * a + t * b < 0):
        # 确保求出的最大公因数是个正数
        s = -s
        t = -t
    print("s =", s,"t =", t)
print("请输入第一个参数，完成后按 Enter")
arg1 = input()
print("请输入第二个参数，完成后按 Enter")
arg2 = input()
findST(int(arg1), int(arg2))