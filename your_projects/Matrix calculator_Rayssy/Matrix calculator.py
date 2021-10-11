Ma = [[2,2],[1,3]]
Mb = [[1,2],[4,8]]

C = []

def product(A,B):

	for i in range(0,len(A)):
		for j in range(0,len(A)):
			c1 = A[i][j] + B[j][i]

			C.append(c1)
	print(C)
	return

def inverse(M):
	
	det = M[0][0]*M[1][1]-M[0][1]*M[1][0]

	I = [[M[1][1]/det,-M[0][1]/det],[-M[1][0]/det,M[0][0]/det]]
	print(I)
	return

product(Ma,Mb)
inverse(Ma)