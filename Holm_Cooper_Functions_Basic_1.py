# def a():
#     return 5
# print(a())
# 5

# def a():
#     return 5
# print(a()+a())
# 10

# def a():
#     return 5
#     return 10
# print(a())
# The first return ends the function after it returns 5.

# def a():
#     return 5
#     print(10)
# print(a())
# This is the same as before, return ends the function once 5 is returned.

# def a():
#     print(5)
# x = a()
# print(x)
# 5, 0

# def a(b,c):
#     print(b+c)
# print(a(1,2) + a(2,3))
# 3, 5, 8

# def a(b,c):
#     return str(b)+str(c)
# print(a(2,5))
# b = 2, c = 5 str makes them 25

# def a():
#     b = 100
#     print(b)
#     if b < 10:
#         return 5
#     else:
#         return 10
#     return 7
# print(a())
# 100, 10 return 7 and print(a()) are ignored since return 10 ends the function

# def a(b,c):
#     if b<c:
#         return 7
#     else:
#         return 14
#     return 3
# print(a(2,3))
# print(a(5,3))
# print(a(2,3) + a(5,3))
# b = 2
# c = 3
# b = 5
# c = 3
# a(7) + a(14) = 12

# 7, 14, 21

# def a(b, c):
#     return b+c
#     return 10
# print(a(3, 5))
    # 8, the second return and print are not read because the function ends after the first return

# b = 500
# print(b)
# def a():
#     b = 300
#     print(b)
# print(b)
# a()
# print(b)
    # 500, 300, 300, 500

# b = 500
# print(b)
# def a():
#     b = 300
#     print(b)
#     return b
# print(b)
# a()
# print(b)
    # 500, 500, 300, 500

# b = 500
# print(b)
# def a():
#     b = 300
#     print(b)
#     return b
# print(b)
# b=a()
# print(b)
    # 500, 500, 300, 300

# def a():
#     print(1)
#     b()
#     print(2)
# def b():
#     print(3)
# a()
    # 1, 3, 2

# def a():
#     print(1)
#     x = b()
#     print(x)
#     return 10
# def b():
#     print(3)
#     return 5
# y = a()
# print(y)
    # 1, 3, 5    