import numpy as np

list16 = np.array([1,2,3])
list17 = np.array([4,5,6])
print( list16 + list17 )
print( list16 * list17 )
print( list16 ** 2 )
print( list17 ** 2 )



# list15 = np.array([10,20,30,40,50])
# new_list = list15[list15>20]
# print(new_list)
# print(list15)


# list14 = np.array([[1,2,3,4,5],
#                    [6,7,8,9,10],
#                    [11,12,13,14,15],
#                    [16,17,18,19,20]])
#print(list14[0,:])     row0
#print(list14[0:2,:])   row0 & row1
#print(list14[:,0])     col0
#print(list14[:,0:3])   col0,col1,col2


# list13 = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(list13)
# print(list13[0,:])          # row 1
# print(list13[0:2,:])        # row0 & row1
# print(list13[:,0])          # col0
# print(list13[:,0:2])        # 0col & 1col



# list12 = np.array([[1,2,3],
#                   [4,5,6]])
# print( list12[0,0] ) # 0 row 0 col --> 1
# print( list12[1,2] ) # 1 row 2 col --> 6
# print( list12[:,0] ) # 0 col [1,4]
# print( list12[:,1] ) # 1 col [2,5]
# print( list12[:,2] ) # 2 col [3,6]
# print( list12[0,:] ) # 0 row [1,2,3]
# print( list12[1,:] ) # 1 row [4,5,6]



# list11 = np.array([10,20,30,40,50])
# print(list11[2],list11[-3])
# print(list11[0:3])
# print(list11[1:4])
# print(list11[2:])
# print(list11[:2])
# print(list11[-3:])
# print(list11[-3:-1])


# list10 = np.array([[1,2,3],[4,5,6]],dtype=float)
# print(list10.shape)
# print(list10.ndim)
# print(list10.size)
# print(list10.dtype)



# list9 = np.linspace(0,3,4)
# print(list9)

# list8 = np.full((2,2),7)
# print(list8)

# list7 = np.arange(1,10,2)
# print(list7)

# list6 = np.eye(3)
# print(list6)

# list5 = np.ones((3,3))
# print(list5)

# list4 = np.zeros((3,3))
# print(list4)

# list1 = np.array([10,20,30,40,50])
# print(list1)
# print(list1.shape)

# list2 = np.array([[1,2],[3,4],[5,6]])
# print(list2)
# print(list2.shape)

# list3 = np.array([10,20,30],dtype=float)
# print(list3)