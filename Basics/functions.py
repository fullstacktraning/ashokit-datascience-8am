# Arbitrary Arguments
# "*"
# def test_func(*nums):
#     print(sum(nums))
#     print(len(nums))
#     print(max(nums))
#     print(min(nums))

# test_func(10,20,30,40,50)


# keyword arguments
# def test_func(name,age):
#     print(name, age)

# test_func(age=40,name="Shiva")
# test_func("Hello",20)





# Default Parameters
# def test_func(param1="Hello",param2="Welcome"):
#     print(param1, param2)

# test_func()             #Hello Welcome
# test_func(100,200)      #100 200
# test_func(None,1000)    #None 1000




# no para - no return type
# no para - with return type
# with para - no return type
# with para - with return type



# def db_func(username,password):
#     if(username == "scott" and password == "tiger"):
#         return "Login Success"
#     else:
#         return "Login Fail"

# res = db_func("scott","tiger")
# print(res)

# def db_func(username,password):
#     if(username=="scott" and password=="tiger"):
#         print("Login Success")
#     else:
#         print("Login Fail")

# db_func("scott","tiger")






# def db_func():
#     username = "AshokIT"
#     password = "AshokIT@123"
    
#     if(username=="AshokIT" and password=="AshokIT@123"):
#         return "Login Success"
#     else:
#         return "Login Fail"

# res = db_func()
# print(res)




# def db_func():
#     username = "admin"
#     password = "admin@123"

#     if(username == "admin" and password == "admin@123"):
#         print("Login Success")
#     else:
#         print("Login Fail")

# db_func()


# def test_func():
#     print("welcome to functions !!!")

# test_func()