import os
from pathlib import Path

# # global/local variables
# x = 5
# print(f"Before the class: x={x}")
#
#
# class Test:
#     x = 6
#     print(f"In the class: x={x}")
#
#     def test(self):
#         x = 7
#         print(f"In func in the class: x={x}")
#
#     x = 8
#     print(f"After func in the class: x={x}")
#
#
# x = 10
# print(f"After the class and changing: x={x}")
# class_object = Test()
# class_object.test()

# # test about id
# a = 1
# b = 2
# print(f"a = {a}, id(a) = {id(a)}; ------- b = {b}, id(b) = {id(b)}.")
# a, b = b, a
# print(f"a = {a}, id(a) = {id(a)}; ------- b = {b}, id(b) = {id(b)}.")

path_folder = os.getcwd()
path_2 = Path.cwd()
path_3 = Path.home()
print(path_folder, f'\n{path_2}', f'\n{path_3}', end='')
