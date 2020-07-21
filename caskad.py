class perm :
	def __init__(self,a=0,b=0,c=0,d=0):
		self.a=a
		self.b=b
		self.c=c
		self.d=d

		self.mat=[]
		self.mat.append([1,2,3,4])
		self.mat.append([self.a,self.b,self.c,self.d])

    ## texadrutyan  print

	def pr(self):
		for i in range (2):
			for j in range (4):
				print (self.mat[i][j],end = " ")
			print() 

     
	## texadrutyunneri bazmapatkum
def mult (a,b):   		
	ex = perm(1,2,3,4)
						   
	for i in range(4):
		for j in range(3): 
			if a.mat[0][j]>a.mat[0][j+1]:

				a.mat[0][j],a.mat[0][j+1]=a.mat[0][j+1],a.mat[0][j]
				a.mat[1][j],a.mat[1][j+1]=a.mat[1][j+1],a.mat[1][j]

	for i in range(4):
		for j in range(3): 
			if b.mat[0][j]>b.mat[0][j+1]:

				b.mat[0][j],b.mat[0][j+1]=b.mat[0][j+1],b.mat[0][j]
				b.mat[1][j],b.mat[1][j+1]=b.mat[1][j+1],b.mat[1][j]
     			


	for k in range(4):					
		i = a.mat[1][k] 
		c = b.mat[1][i-1]
		ex.mat[1][k]=c

	return ex

 
 ## matrici sarqum
def mec_m():
	mad = [ ]
	for i in range(4):
		mad.append([])
		for j in range(4):
			mad[i].append(0)
	## miavorneri lcnum
	for i in range(4):
		for j in range(4):
			if i == j :
				gen = perm (1,2,3,4)
				mad[i][j]=gen
			 
	return mad

## print big matric
def pbm(m):
	for i in range(4):
		print("########")
		for j in range(4):
			if (type(m[i][j]) == perm):

				m[i][j].pr()

				print()
			else:
				print (0)
				#print()

##input a anum texadrutyun@ matricum
def inp(x,y):

	
	for i in range(4):
		if y.mat[0][i]== y.mat[1][i]: 
			continue				   	
		i1= y.mat[0][i]
		j1= y.mat[1][i]
		
		if j1 > i1 :
			if x[i1-1][j1-1] == 0:
				x[i1-1][j1-1]=y
				
				break

				
			break
	return x

	## matric@ fulla te che 
def isfull(m):
	sum = 0
	for i in range(4):
		for j in range(4):
			if i < j:
				if type (m[i][j])==perm:
					sum = sum +1 
	if sum == 6:
		return 1
	else:
		return 0

##stugeuma a input arvela te che 
def isinp(a,b):
	
	x1=0
	y1=0
	for i in range(4):
		for j in range(4):
			if i < j:
				if type( a[i][j] )==perm:
					x1=x1+1
	for i in range(4):
		for j in range(4):
			if i < j:
				if type(b[i][j])==perm:
					y1=y1+1		
						

	if x1==y1:
		return 0
	else:
		return 1
# copy a anum matric@ m 
def cop_mat(a):
	b = mec_m()
	for i in range(4):
		for j in range(4):
			b[i][j]=a[i][j]
	return b		
 
# tanum bazmapatkuma , heta tali lcrac zangvac@ 
def check (mat , hert):
	
	while 1 > 0:
		ltex1 = []
		for i in range(4):
			for j in range(4):
				if i < j:
					if mat[i][j] == hert:
						for i1 in range(4):
							for j1 in range(4):
								if i1<j1:
									if mat[i1][j1] != 0 :
										sev = perm ()
										if i1 < i:
											sev = mult(mat[i1][j1],hert)
											ltex1.append(sev)
										elif i1 > i:
											sev = mult( hert, mat[i1][j1]  )
											ltex1.append(sev)
										else:
											sev = mult(hert,mat[i1][j1])
											ltex1.append(sev)
											sev = mult(mat[i1][j1],hert)
											ltex1.append(sev)
		return ltex1						
                                      

def copy_list(a):
	cop=[]
	for i in range (len(a)):
		cop.append(a[i])
	return cop


def is_point(a):
	k = 0
	for i in range (4):
		if a.mat[0][i]==a.mat[1][i]:
			if i == 3:
				return 1
			continue	
			
	return -1			


# a matric 
def is_buzy(a,b):

	for i in range (4):
		if b.mat[0][i]==b.mat[1][i]:
			if i == 3:
				return b 
			continue
		else:
			x = b.mat[0][i]
			y = b.mat[1][i]
			break		
	return a[x-1][y-1]		
							
def opp1(tex):
	
	vaz = perm()
	a = []
	b = []

	a.append(tex.mat[0])
	b.append(tex.mat[1])
	vaz.mat[0][0]= tex.mat[1][0]
	vaz.mat[0][1]= tex.mat[1][1]
	vaz.mat[0][2]= tex.mat[1][2]
	vaz.mat[0][3]= tex.mat[1][3]

	vaz.mat[1][0]= 1
	vaz.mat[1][1]= 2
	vaz.mat[1][2]= 3
	vaz.mat[1][3]= 4


	return vaz


###################################################################################
##################################################################################         

kar = mec_m() 
       #(1,2,3,4)
a = perm(2,3,4,1)

       #(1,2,3,4)
b = perm(2,1,3,4)
ltex= []
inp(kar,a)

kar1 = cop_mat(kar)
ltex= check(kar,a)

inp(kar,b)


if isinp(kar,kar1) == 0:
	temp =perm()
	temp = is_buzy(kar,b)
	temp = opp1(temp)
	temp = mult(b,temp)
	kar = inp(kar , temp)
	ltex = ltex + check(kar,temp)
else:
	ltex = ltex + check(kar,b)


leng = len(ltex)
copy = []
copy = copy_list(ltex)
payman = 0





while  leng != 0:

	kar1 = mec_m()
	kar1 =cop_mat (kar)
	kar = inp (kar,ltex[0])
	if isfull(kar)==1:
		print ("matric@ fula ")
		break

	if isinp(kar1,kar) == True :
		ltex = ltex + check(kar,ltex[0])
		copy = copy_list(ltex)
		del ltex[0]
		leng = len(ltex)
		leng = leng - 1

	else:
		del ltex[0]
		leng = leng - 1
	if leng == 0 :
		payman = 1

	
			
if payman == 1:

	l = len(copy)
	shoch = 0
	while l != 0:
		temp =perm()
		temp = is_buzy(kar,copy[shoch])
		temp = opp1(temp)
		temp = mult(copy[shoch],temp)
		kar1 = mec_m()
		kar1 =cop_mat (kar)
		kar = inp(kar , temp)
		if isinp(kar1,kar)==1:
			
			break
		else:
			del copy[shoch]
			l = l - 1
		

pbm(kar)