
 def printname(name):
     print(name)
 
print_name("Aleena")

printname("Aleena")
 def decorator(fn):
     def wrapperfn(name):
         print("my name is")
         fn(name)
         print("execution ended")
              return wrapperfn

 s1 = decorator(printname)
s1("aleena")
