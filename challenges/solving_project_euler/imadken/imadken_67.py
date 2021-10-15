

def Maximum_Path_Sum(triangle):

    for i in range( len(triangle)-2 , -1 , -1 ):
    
      for j in range(len(triangle[i])):
    
          triangle[i][j] = int( triangle[i][j] ) + int( max( triangle[i+1][j] , triangle[i+1][j+1] ) )
    

    return triangle[0]

with open("p067_triangle.txt","r") as triangle:

  triangle=[line.replace('\n','').split() for line in triangle.readlines()]


print(Maximum_Path_Sum(triangle))    
    