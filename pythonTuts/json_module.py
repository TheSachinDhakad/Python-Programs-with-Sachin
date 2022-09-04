import json
# data= '{"var1" : "sachin" , "var2" : "9098224586"}'
# # print(data)
# # print(data['var1'])    ----->throw the error
# parsed = json.loads(data)
# print((parsed['var1']))

data2 = {
    "channel" : "cwh",
    "cars" : ["bmw" , "audi"],
    "fridge":("roti","cold drink"),
    "isbad" : False
}
jcomp = json.dumps(data2)
print(jcomp)


#what is sort_keys parameter in dumps