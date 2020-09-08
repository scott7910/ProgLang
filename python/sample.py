import io
import sys

# 標準入力
_INPUT = """\
1
2
3
6.5
5
"""
sys.stdin = io.StringIO(_INPUT)

# if,for
list = [float(input()) for i in range(5)]
for i in list:
    pass
    if i % 2 == 0:
        print(str(i) + ":even")
    elif i % 2 == 1:
        print(str(i) + ":odd")
    else:
        print(str(i) + ":other")


# for

#
