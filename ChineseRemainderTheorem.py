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
# 中国剩余定理
# 求最大公因数
def gcd(x: int, y: int) -> int:
    while (y != 0):
        temp = x % y
        x = y
        y = temp
    return x
# 求逆元
def MultiplicativeInverseOfModulo(a: int, m: int) -> int:
    if (a == 0 and m == 0):
        print("a 和 b 不能全为 0，这样不存在最大公因数")
        return
    # 求 s，t 使得 sa+tm=1，此时 s mod m 就是要求的逆元
    if (m == 0):
        # 此时 m = 0
        s = 1
        t = 0
    else:
        s_jminus2 = 1
        s_jminus1 = 0
        t_jminus2 = 0
        t_jminus1 = 1
        q = a // m
        r_minus2 = m
        r_minus1 = a % m
        if (r_minus1 == 0):
            # 此时 a = 0，m 是 a 的因数，最大公因数为 m 的绝对值
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
    if (s * a + t * m < 0):
        # 确保求出的最大公因数是个正数
        s = -s
        t = -t
    return s % m
# 主程序
def ChineseRemainderTheorem(b_list: list[int], m_list: list[int]) -> list[int]:
    # 求 m
    m = 1
    for m_elem in m_list:
        m = m * m_elem
    # 求 x
    x = 0
    i = 0
    while i < b_list.__len__():
        M_elem = m // m_list[i]
        x = (x + b_list[i] * MultiplicativeInverseOfModulo(M_elem, m_list[i]) * M_elem) % m
        i = i + 1
    return [x, m]

print("请输入方程组中方程的数量，完成后按 Enter 确认")
list_len = int(input())
if list_len <= 0:
    print("方程数量必须是正整数。")
    exit(0)
i = 0
b_list = []
m_list = []
while i < list_len:
    print("请输入第 {} 个方程中的 b，完成后按 Enter：".format(i + 1))
    b_list.insert(i, int(input()))
    print("请输入第 {} 个方程中的 m，完成后按 Enter：".format(i + 1))
    m_list.insert(i, int(input()))
    if m_list[i] <= 0:
        print("m 必须是正整数")
        exit(0)
    i = i + 1
# 检查这 m 个数是否两两互素
i = 0
while i < list_len:
    j = i + 1
    while j < list_len:
        if gcd(m_list[i], m_list[j]) != 1:
            print(m_list[i], "和", m_list[j], "不互素，无法使用中国剩余定理")
            exit(0)
        j = j + 1
    i = i + 1
# 求解
result = ChineseRemainderTheorem(b_list, m_list)
print("解得 x ≡ ", result[0], " (mod ", result[1], ")", sep="")