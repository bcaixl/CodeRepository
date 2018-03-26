# -*-coding:utf-8 -*-
"""
subject:
Given an array of words, return an array of the number of letters that
occupy their positions in the alphabet for each word.
For example, solve(["abode","ABc","xyzD"]) = [4,3,1].
"""


def solve(arr):
    """
    the answer from me
    :param arr:
    :return:
    """
    result_list = []
    k = 0
    for word in arr:
        word_lower = word.lower()  # 将字符创统一大小写
        i = 0
        for letter in word_lower:
            if ord(letter)-97 == i:  # 函数的关键是ord函数可以将字母转化为ASCII表中的数字，与之对应的是chr函数
                k = k+1
            i += 1
        result_list.append(k)
        k = 0
    return(result_list)


def solve2(arr):
    """
    the best Practices from net friend
    :param arr:
    :return:
    """
    return [sum(c == chr(97+i) for i, c in enumerate(w[:26].lower())) for w in arr]

if __name__ == '__main__':
    print(solve(["abode", "ABc", "xyzD"]))
