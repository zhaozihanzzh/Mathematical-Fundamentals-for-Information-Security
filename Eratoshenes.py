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
import math
# 爱拉托斯散筛法
# Python 自带了大数支持
def find_prime(n):
    if n == 1: return {}
    if n == 2: return {2}
    primes=[2, 3]
    i = 4
    while i <= n:
        # 在漫长的等待中输出一些进度信息
        if not i % 100000: print("Progress: ", i)
        sqrt_result = int(math.sqrt(i))
        j = 0
        while j < primes.__len__():
            if primes[j] > sqrt_result:
                break
            if i % primes[j] == 0:
                break
            j = j + 1
        if primes[j] > sqrt_result or i % primes[j]:
            primes.append(i)
        i = i + 1
    return primes
# 我将不会把结果输出到文件中，因为要计算出sqrt(10^300)个素数，根据素数定理，约有2.895*10^147个素数，
# 假如每个素数占用1字节，需要2.696*10^138 GB 存储空间。
print(find_prime(100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000))