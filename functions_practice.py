# hello function 
def hello():
  print("Hello, user!")
  
# pack function
def pack(a,b,c):
  return [a,b,c]

# eat lunch function
def eat_lunch(my_lst):
  if len(my_lst) == 0:
    print("My lunchbox is empty...")
  else:
    for i in range(len(my_lst)):
      if i == 0:
        print(f"I'll eat {my_lst[0]} first")
      else:
        print(f"I'll eat {my_lst[i]} next")

hello()
print(pack("a","b","c"))
print(pack(1,2,3))
eat_lunch([])
eat_lunch(["sandwich"])
eat_lunch(["apple","chips","sandwich","cookie"])