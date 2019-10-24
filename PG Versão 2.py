
import numpy as np

n=4
m = np.random.randint(2,size=(n,n))

#alt = [[m[0:i+1,0:j+1],m[i+1:,j+1:]] for j in range(m.shape[1]-1) for i in range(m.shape[0]-1)]
#indexes = [[(0,1+i,0,j+1),(i+1,max_size,j+1,max_size)] for j in range(m.shape[1]-1) for i in range(m.shape[0]-1)]
np.random.seed(100)
   
def break_into_indexes(array,b=[0,0,0,0]):
    row1,col1 = b[1],b[3]
    return [[[row1,1+i,col1,j+1],[i+1,array.shape[0]+row1,j+1,array.shape[1]+col1]] 
             for j in range(col1,col1+array.shape[1]-1) 
             for i in range(row1,row1+array.shape[0]-1)]
def index_to_array(matrix,index):
    return matrix[index[0]:index[1],index[2]:index[3]]
def list_to_alt(matrix,list_index):
    output = []
    [output.append(index_to_array(matrix,ind)) for ind in list_index]
    return output
def print_arrays(m,list_indexes):
    for index in list_indexes:
        print(list_to_alt(m,index))
        print('\n')
        
indexes = break_into_indexes(m)



result_list = list()
for k in range(len(indexes)):
    init_game = [0,0,0,0]
    for o in range(len(indexes[k])):
        yo = indexes[k][o]
        if ((yo[1]-yo[0])>2 and (yo[3]-yo[2])>2):
            tempy = indexes[k].copy()
            del tempy[o]
            tempy_indexes =  break_into_indexes(index_to_array(m,yo),
                                                b=init_game,
                                                )
            
            for indexy in tempy_indexes:
                tempy2 = tempy.copy()
                for indexy2 in indexy:
                    tempy2.append(indexy2)
                result_list.append(tempy2)

        init_game = yo

    
