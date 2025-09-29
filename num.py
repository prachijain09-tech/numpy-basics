
#chapter 1 
#1 creating array from pyton list
#list-> array mupy has function  which coverts  list to array 
#syntax =np.array([elements of list])

'''import numpy as np
list1=[1,2,3,'prachi',5]
print(np.array(list1))'''


#2  with default  values  ( by default zero  if need it can be replaced by any value  in future )
#syntax =np.zeros(shape)  shape=size of array
'''import numpy as np
default_zero_value=np.zeros(4)
print(default_zero_value)'''


#by default 1
#syntax =np.ones(shape)  shape=size of array
'''import numpy as np   
default_one_value=np.ones([2,3]) # 2 rows and 3 columns
print(default_one_value)'''

#not zero not one any specific value  
#syntax =np.full(shape,value)  shape=size of array value=specific value
'''import numpy as np
specific_value=np.full((2,3),7) #2 rows and 3 columns with value 7
print(specific_value)'''


#3 creating sequeces of numbers in numpy array
'''import numpy as np
sequence=np.arange(1,10,2) #start ,end,step size
print(sequence)
'''

#creating  identity matrix
''''import numpy as np 
identity_matrix= np.eye(3)
print(identity_matrix)
'''

#chapter 2 
#1  shape(no of rows and columns)
'''import numpy as np 
arr_2d=np.array([[1,2,3],[4,5,6]])
print(arr_2d.shape) 
'''
#size (total number of elements in array )
'''import numpy as np
arr_2d=np.array([[1,2,3],[4,5,6]])
print(arr_2d.size)  
'''

#ndim (no of dimensions)
'''import numpy as np
arr_1d=np.array([1,2,3,4,5])
arr_2d=np.array([[1,2,3],[4,5,6]])
arr_3d=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(arr_1d.ndim)
print(arr_2d.ndim)
print(arr_3d.ndim)'''

#dtype (data type of elements in array)
'''import numpy as np
arr_1d=np.array([1,2,3.5,4,5.6])        
print(arr_1d.dtype)  
'''

#change  data type of array ,  and know type of array
'''import numpy as np
arr_1d=np.array([1,2,3,4,5])
print(arr_1d.dtype)
arr_1d=arr_1d.astype(float)
print(arr_1d.dtype,arr_1d)
'''

#operations on array ( operators +,-,*,**exponention,// floor division ,%) 
'''import numpy as np
arr=np.array([1,2,3,4])
print(arr)
print(arr+2)  
print(arr-2)
print(arr*2)
print(arr**2)
'''

#18 september 2025

#aggregate functions (sum,min,max,mean,median,std, variance ) 
'''import numpy as np 
arr=np.array([1,2,3,4])
print(np.sum(arr)) 
print(np.min(arr))
print(np.max(arr)) 
print(np.mean(arr))
print(np.median(arr))
print(np.std(arr))
print(np.var(arr))
'''

#indexing( a single index ) and slicing(a porition of array)
# numpy  follows zero based indexing(right to left ) and also has negative indexing (left to right )

'''import numpy as np
#syntax 1d  name[index]
arr_1d=np.array([10,20,30,40,50])
print(arr_1d[2])  #30
print(arr_1d[-1])  #50
 #synatx 2d name[row_index,column_index]
arr_2d=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr_2d[1,1])  #6
print(arr_2d[2,0])  #1
'''

#slicing
'''import numpy as np
#syntax 1d  name[start:end(excluded):step]
arr_1d=np.array([10,20,30,40,50])   
print(arr_1d[1:4:2])  #20,40
print(arr_1d[:3])    #10,20,30 (default start index is 0, default step size is 1, jaha rukna he )
print(arr_1d[::-1])  #50,40,30,20,10 (reverse array)

#syntax 2d name[row_start:row_end(excluded):row_step,column_start:column_end(excluded):column_step]
arr_2d=np.array([[1,2,3,16],[4,5,6,17],[7,8,9,18],[10,11,12,19], [13,14,15,20]])
print(arr_2d[0:4:2,1:3:2]) 
print(arr_2d[::-1,::1])'''


#fancy indexing (using list of indices to access multiple elements)
#pass indices as a list 
'''import numpy as np
#syntax 1d  name[[index1,index2,index3,...]]
arr=np.array([10,20,30,40,50])
print(arr[[0,1,2]]) 

#syntax 2d name[[row_index1,row_index2,...],[column_index1,column_index2,...]]
arr_2d=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr_2d[[0,1],[1,2]])  #2,6
'''

#boolean masking (using conditions to filter elements)
'''import numpy as np
#syntax 1d  name[condition]
arr=np.array([10,20,30,40,50])
print(arr[arr>25])

#syntax 2d name[condition]
arr_2d=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr_2d[arr_2d%2==0])  
'''

#reshaping (changing the shape of an array without changing its data)
# only possible when dimension match unless it will show error 
#reshaping does not  create copy it returns view(affects original array )
'''import numpy as np 
#syntax name.reshape(new_shape)
arr=np.array([1,2,3,4,5,6])
print(arr.reshape(2,3)) #2 rows and 3 columns 
print(arr.reshape(2,4)) # error not possible 
'''

#flatten - creates copy no change in original array
#ravel - creates view change in original array
'''import numpy as np
arr=np.array([[1,2,3],[4,5,6]])
print(arr.flatten())
print(arr.ravel())
'''

#22th september 25
#advance   numpy  concepts
# insert  1d syntax =np.insert(array,index,value,axis) 
'''import numpy as np 
arr_1d=np.array([1,2,3,4,5])
new_arr_1d=np.insert(arr_1d,2,10) #insert 10 at index 2(1d axix=none)
print(arr_1d)
print(new_arr_1d)

#syntx 2d =np.insert(array,row_index/column_index,value,axis)  axix 0 row , 1 column

arr_2d=np.array([[1,2],[4,5])
new_arr_2d_row=np.insert(arr_2d,0,[10,11],axis=0) #insert row at index 1
new_arr_2d_col=np.insert(arr_2d,1,[10,11],axis=1) #insert column at index 2
print(arr_2d)
print(new_arr_2d_row) 
print(new_arr_2d_col)
'''

#append 
#syntax 1d =np.append(array,value,axis)  axis none
'''import numpy as np
arr_1d=np.array([1,2,3,4,5])
print(np.append(arr_1d,10)) #append 10 at

arr_2d=np.array([[1,2],[4,5]])
print(np.append(arr_2d,[[10,11]],axis=0)) #append row at last
'''

#concatenate
#syntax =np.concatenate((array1,array2,...),axis) axis 0 row 1 column none 1d
'''import numpy as np
arr_1d_1=np.array([1,2,3])
arr_1d_2=np.array([4,5,6])  
print(np.concatenate((arr_1d_1,arr_1d_2)))

arr_2d_1=np.array([[1,2],[3,4]])
arr_2d_2=np.array([[5,6],[7,8]]) 
print(np.concatenate((arr_2d_1,arr_2d_2),axis=0)) #row wise
print(np.concatenate((arr_2d_1,arr_2d_2),axis=1)) #column wise
'''

#delete
#syntax 1d =np.delete(array,index,axis) axis none
'''import numpy as np
arr_1d=np.array([1,2,3,4,5])
print(np.delete(arr_1d,2)) #delete element at index 2
arr_2d=np.array([[1,2,3],[4,5,6]])
print(np.delete(arr_2d,1,axis=0)) #delete row at index 1
print(np.delete(arr_2d,2,axis=1)) #delete column at index
'''

#stacking  vstack ,hstack,dstack
'''import numpy as np
arr_1d_1=np.array([1,2,3])
arr_1d_2=np.array([4,5,6]) 
print(np.vstack((arr_1d_1,arr_1d_2)))   #vertical stacking
print(np.hstack((arr_1d_1,arr_1d_2)))   #horizontal stacking    
print(np.dstack((arr_1d_1,arr_1d_2)))   #depth stacking   
'''

#split hslpit, vsplit (splits in equal paerts only)
'''import numpy as np
arr_1d=np.array([1,2,3,4,5,6])
print(np.split(arr_1d,2))  #split into 3 parts
arr_2d=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(np.vsplit(arr_2d,3))  #vertical split into 3 parts
print(np.hsplit(arr_2d,4))  #horizontal split into 2 parts
'''

#2) broadcasting (without using loops  as loops are slower for large data )
'''import numpy as np
prices=np.array([100,200,300])
discount=10 #scaler single value
final_prices=prices- ( prices *discount/100)
print(final_prices)
''' 
#how numpy handles operations with different shapes
# 1) matching dimensions = normally performs operation 
#2)  expanding dimensions = smaller array is expanded to match larger array
# [1,2,3] + [10]=[11,12,13]
#3) incompatible dimensions = error
# [1,2,3] + [10,20]=error       

'''import numpy as np 
arr_1=np.array([1,2,3])
arr_2=np.array([[10,20,30]])
print(arr_1+arr_2)  #expanding dimensions
arr_sep=([[50]]) 
print(arr_sep+arr_1)   #expanding dimensions 
arr_3=np.array([[1,2]])
arr_4=np.array([[10,20,30]])
print(arr_3+arr_4)  #incompatible dimensions error
'''

#vectorization (performing operations on entire arrays without explicit loops)

#handling missing data and values (for succcessful  ml modals it is important  for eg if in calculator 1/0 it will show error similarly in ml model it will show error if any missing value is there so we have to handle it)
# total three functions are there 1) np.isnan() (detect missing values )
                                # 2) np.nan_to_num() (nan - not a number ) (replace missing values with specified number )
                                # 3) np.isinf() ( ued to detect infinite values )
 
 #1) np.isnan() (boolean function )( no we cannot compare nan with anything it will always return false so we use this function to detect nan values )
'''import numpy as np
arr=np.array([1,2,np.nan,4,np.nan,6])
print(np.isnan(arr))  #True for nan values(true means  at the place of number nan is present(number is missing )  , false means )
'''

#2) np.nan_to_num() (replace nan with specified number )
'''import numpy as np 
arr=np.array([1,2,np.nan,4,np.nan,6])  #by default  0
print(np.nan_to_num(arr, nan=-1))  #replace nan with -1
print(np.nan_to_num(arr))  #replace nan with 0
'''

#3) np.isinf() (detect infinite values )
'''import numpy as np
arr_inf=np.array([1,2,np.inf,4,-np.inf,6])
print(np.isinf(arr_inf))  #True for inf values

cleaned_arr= np.nan_to_num(arr_inf, posinf=100, neginf=-100) #replace inf with 100 and -inf with -100 
print(cleaned_arr)
'''