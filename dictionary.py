# create dictionary with ()

person = dict(
    name = "Zakaria", 
    age = 34.9,
    work = "data engineer"
)

print(person["name"])
print(person["work"])





#iterate over a dictionary 
words = {
    "data structure": "means of storing data",
    "regression": "a fuction to best fit data",
    "method": "a function bound to an object"
}

#iterate over both keys and values

for key, value in words.items():
    print(f"key: {key}")
    print(f"value: {value}")


    #iterate over keys 
    for key, in words.keys():
        print(key)
  
   
