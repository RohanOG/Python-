# # class Test:
# #     def main():
    
# #         a="test1"
# #         b="test2"
# #         c="test3"
# #         d="test4"
# #         final_str="{3},{2},{1},{0}"
# #         print(final_str.format(a,b,c,d))
# # Test.main()
# class Test:
#     def main():
#         a=input("Enetr valur")
#         b=input("Enetr value")
#         c=input("Enetr value")
#         d=input("Enetr value")
#         final_str="{0},{1},{2},{3}"
#         print(final_str.format(d,c,b,a))
# Test.main()
# NUMPY-----------------------------------------------------------------------------
# import numpy as np
# arr =np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# newarr = arr.reshape(2,3,2)
# print(newarr)
# print(newarr.ndim)


# FLATTENING OF ARRAY_______________________________________________
# import numpy as np
# arr =np.array([[1,2,3],[4,5,6]])
# newarr = arr.reshape(-1)
# print("\n\nOriginal array")
# print(arr)
# print("array dimension->",arr.ndim)
# print("array shape->",arr.shape)

# print("\n\nFlattened Array")
# print(newarr)
# print("array dimension->",newarr.ndim)
# print("array shape->",newarr.shape)




# import numpy as np

# arr = np.array([[[1, 2, 3], [4, 5, 6]],[[7,8,9],[7,6,5]]])

# for x in arr:
#     for y in x:
#         for z in y:
#             print(z,end=" ")



# import numpy as np

# arr = np.array([1, 2, 3, 4, 5, 4, 4])

# x = np.where(arr == 4)

# print(x)


# -------------------------------------------------------------------------------------

# import numpy as np
# class ArraySearch:
#     def ArrSearch():
#         arr=[]
#         n=int(input("Enetr the no. of array elements->"))
#         for x in range (n):
#             arr.append(int(input()))
#         arr=np.array(arr)
#         print("original array ->",arr)
#         print("\n")
#         z=int(input("Enter a number to search in array ->"))
#         x=np.where(arr==z)
#         print("INdexes found->",x)
# ArraySearch.ArrSearch()
# ------------------------------------------------------------------------------------------\

# import pandas as pd

# mydataset = {
#   'cars': ["BMW", "Volvo", "Ford"],
#   'passings': [3, 7, 2]
# }

# myvar = pd.DataFrame(mydataset)

# print(myvar)
# -----------------------------------------------------------------------------------------------
# import pandas as pd

# df = pd.read_csv('data.csv')

# print(df) 
# =======================================================================================================
# =======================================================================================================
import matplot.pyplot as plt
import pandas as pd
class Test:
    def main():
        hui=pd.read_csv('index processed.csv')
        hui.plot.show
Test.main( )