# ============================Dz1=============================
def first(key,y):
  if key in y:
    return True
  if key not in y:
    return False
y = {
    "name" : "Vlad",
    "age" :  16,
    "country" : "IF"
}
key= "name"
print(first(key,y))
# ============================Dz2=============================
ke=[]
def second(list,va):
 ke = []
 for key in list:
    if list[key]==va:
        ke.append(key)
        return ke
list= {
    "Sasha" : "good",
    "Andriy" : "good",
    "Sophia" : "bad",
    "Igor" : "good",
    "Petro" : "very good"
}
va = "good"
print(second(list,va))

# ============================Dz3=============================

My_dict={
    "lastname" : "Yuzevych",
    "age": 16,
}
print(My_dict)
x=input("Enter your name: \t")
y=input("Enter your faculty: \t")
My_dict.update({"name" : x})
My_dict.update({"faculty": y})
print(My_dict)
My_dict.update({"mid_numeber":12})
print(My_dict)
