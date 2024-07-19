def one(x,y):
  try:
    if y in x:
        x.index(y)
        return x
    else:
        raise ValueError(f"Error, {y} is not in list")
  except ValueError as e:
      print(e)
x=["apple","banana","orange","watermelon","grape","pineapple"]
y="car"
print(one(x,y))


def two(x,y):
    try:
        if y in x:
            x.remove(y)
            return (x)
        else:
            raise ValueError ("Word is not find")
    except ValueError as e:
        print(e)

x = ["boy", "toy", "doll", "game", "ball", "pen"]
y = "toy"
print(two(x,y))



def three(x):
    try:
      if x%2==0:
        return x
      else:
        raise ValueError("x%2!=0")
    except ValueError as e:
      print("Error",e)
x=int(input("Enter number\t"))
print(three(x))

