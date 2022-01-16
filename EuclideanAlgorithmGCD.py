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
# 广义欧几里得除法求最大公因数
def gcd(x, y):
    while (y != 0):
        temp = x % y
        x = y
        y = temp
    return x
def euclideanAlgorithm(input1, input2):
    if (input1 < 0): input1 = -input1
    if (input2 < 0): input2 = -input2
    if (input1 == 0 and input2 == 0):
        # 没有最大公因数
        print("两数不能全为 0 ")
        return
    if (input1 < input2):
        swap = input2
        input2 = input1
        input1 = swap
    print("最大公因数", gcd(input1, input2))
print("请输入第一个参数，输完后按 Enter")
x = input()
print("请输入第二个参数，输完后按 Enter")
y = input()
euclideanAlgorithm(int(x), int(y))

""" 以下是 C++ STL（g++ (GCC) 11.1.0 linux）中 __gcd 的实现：
  template<typename _EuclideanRingElement>
    _GLIBCXX20_CONSTEXPR
    _EuclideanRingElement
    __gcd(_EuclideanRingElement __m, _EuclideanRingElement __n)
    {
      while (__n != 0)
	{
	  _EuclideanRingElement __t = __m % __n;
	  __m = __n;
	  __n = __t;
	}
      return __m;
    }
"""