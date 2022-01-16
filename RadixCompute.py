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
# 编程实现两个二（八、十六）进制数的加法、减法和乘法运算，要求对十进制 300 位以内的整数都实现。
# 十六进制直接当十进制运算，最后输出 hex 后的结果
# 加法
def plus(x: int, y: int, radix: int):
    if (radix == 16):
        radix = 10
    if (x == 0):
        return y
    if (y == 0):
        return x
    is_negative = False
    if (x < 0 and y < 0):
        is_negative = True
        x = -x
        y = -y
    else:
        if (x < 0):
            return minus(y, -x, radix)
        if (y < 0):
            return minus(x, -y, radix)
    carry = 0
    ans = 0
    bit_location = 0
    while (x != 0 or y != 0):

        bit_location += 1
        digit_ans = x % 10 + y % 10
        if (carry == 1):
            digit_ans = digit_ans + 1
        if (digit_ans >= radix):
            carry = 1
            digit_ans = digit_ans % radix
        else:
            carry = 0
        i = 0
        while (i < bit_location - 1):
            i += 1
            digit_ans *= 10
        ans = ans + digit_ans
        x = x // 10
        y = y // 10
    if (carry == 1):
        i = 0
        while (i < bit_location):
            carry *= 10
            i += 1
        ans += carry
    if (is_negative):
        ans = -ans
    return ans

# 减法
def minus(x: int, y: int, radix: int):
    if (radix == 16):
        radix = 10
    if (y == 0):
        return x
    if ((x <= 0 and y > 0) or (x >= 0 and y < 0)):
        return plus(x, -y, radix)
    is_negative = False
    if (x >= 0 and y > 0 and x < y):
        temp = x
        x = y
        y = temp
        is_negative = True
    else:
        if (x <= 0 and y < 0):
            if (x >= y):
                temp = x
                x = -y
                y = -temp
            else:
                is_negative = True
                x = -x
                y = -y
    # 至此，我们保证是大正数减小正数的情况
    carry = 0
    ans = 0
    bitLocation = 0
    while (x > 0 or y > 0):
        bitLocation += 1
        digitAnswer = x % 10 - y % 10
        if (carry == 1):
            digitAnswer -= 1
        if (digitAnswer < 0):
            digitAnswer += radix
            carry = 1
        else:
            carry = 0
        i = 0
        while (i < bitLocation - 1):
            i += 1
            digitAnswer *= 10
        ans += digitAnswer
        x //= 10
        y //= 10
    if (is_negative):
        ans = -ans    
    return ans

# 乘法
def multiply(x: int, y: int, radix: int):
    if (radix == 16):
        radix = 10
    if (x == 0 or y == 0):
        return 0
    isNegative = False
    if (x < 0 and y > 0):
        isNegative = True
        x = -x
    elif (x > 0 and y < 0):
        isNegative = True
        y = -y
    elif x < 0 and y < 0:
        x = -x
        y = -y
    ans = 0
    bitLocation = 0
    while (y != 0):
        bitLocation += 1
        times = 0
        and_res = 0
        while (times < y % 10):
            and_res = plus(and_res, x, radix)
            times += 1
        leftmove = 0
        while (leftmove < bitLocation - 1):
            and_res *= 10
            leftmove += 1
        ans = plus(ans, and_res, radix)
        y = y // 10
    if (isNegative):
        ans = -ans
    return ans

# 测试：
# test = input()   输入 0x7f (str)
# test = int(test) 默认是 base10 (崩溃)
# test = int(test, 16) 把 str(0x7f) 变成 int(127)
print("请输入进制（2，8，16）并回车：")
radix = input()
print("请输入第一个运算数并回车：")
num1 = input()
print("请输入欲执行的运算（+ - *）并回车")
operator = input()
print("请输入第二个运算数并回车：")
num2 = input()
radix = int(radix)
if (radix != 16):
    num1 = int(num1)
    num2 = int(num2)
else:
    # 利用 Python 内建的支持，直接把 16 进制转为十进制，下面运算时当十进制运算，输出时转回来即可
    num1 = int(num1, 16)
    num2 = int(num2, 16)
if (operator == '+'):
    answer = plus(num1, num2, radix)
elif (operator == '-'):
    answer = minus(num1, num2, radix)
elif (operator == '*'):
    answer = multiply(num1, num2, radix)
else:
    print("请输入正确的运算符。")
    exit()
if (radix == 16):
    answer = hex(answer)
print("答案", answer)