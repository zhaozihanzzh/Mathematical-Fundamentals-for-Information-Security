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
# 《信息安全数学基础》，第二版，陈恭亮，P49 T15
# 决定一个整数是否被一个给定整数整除的算法
def isDividedWithoutRemainder(divisor, dividend):
    if not divisor:
        print("除数不能为 0 ")
        return
    # 先转成正数
    if divisor < 0:
        divisor = -divisor
    if dividend < 0:
        dividend = -dividend
    # 被除数位数减去除数位数是商的最小位数
    divisor_bit = 1
    divisor_test = 10
    while divisor_test <= divisor:
        divisor_bit = divisor_bit + 1
        divisor_test = divisor_test * 10
    dividend_bit = 1
    dividend_test = 10
    while dividend_test <= dividend:
        dividend_bit = dividend_bit + 1
        dividend_test = dividend_test * 10
    # 不完全商的最小值：
    min_q = dividend_test // divisor_test // 10 #int(math.pow(10, (dividend_bit - divisor_bit - 1)))
    # 不完全商的最大值(取不到max_q)：
    max_q = dividend_test // divisor_test * 10
    
    q = (min_q + max_q) // 2
    # 二分查找，找到不完全商
    while not (q * divisor <= dividend and (q + 1) * divisor > dividend):
        if (q + 1) * divisor <= dividend:
            min_q = q + 1
            q = (min_q + max_q) // 2
        else:
            max_q = q
            q = (min_q + max_q) // 2
    if q * divisor == dividend:
        return True
    else:
        return False

# 测试
print("能否被整除：")
print(isDividedWithoutRemainder(11, 100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000))