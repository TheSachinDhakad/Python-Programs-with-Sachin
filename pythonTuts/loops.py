# list1 = [["sachin",91],["nitesh",71],["aniket",14],["shrutii",100]]
# dict1 = dict(list1)
# print(dict1)
# # for name , roll_no in list1:
# # for name , roll_no in dict1.items():
# #     print(name ,"its roll numbr ", roll_no)
# for item in dict1:
#     print(item)
#
#
#
#

items = [int , float , "sachin" ,45,34,65,34,6,3,5,45,23,54,6,7]
for item in items:
    if str(item).isnumeric() and item>6:
        print(item)