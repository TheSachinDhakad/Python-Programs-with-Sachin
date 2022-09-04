# def print_name(a, b, c, d):
#     print(a,b,c,d)
def funargs(normal , *args,**krghs):
    print(normal)
    # print(type(args))
    # print(args[0])
    for item in args:
        print(item)
    print("\n")

    for key ,value in krghs.items():
        print(f"{key} is a {value}")


a = ["sachin ","dhakad","nitesh" , "nagar" , "friend"]
normal = "this is a normal"
kw = {"sachin":"student","nitesh":"roommate" , "nri":"college","bhopal":"city"}

funargs(normal,*a,**kw)
