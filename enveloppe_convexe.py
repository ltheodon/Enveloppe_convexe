def orientation(P,Q,R):
	a=Q[0]-P[0]
	b=Q[1]-P[1]
	c=R[0]-P[0]
	d=R[1]-P[1]
	det=a*d-b*c
	if det > 0:
		return 1
	elif det==0:
		return 0
	else:
		return -1


def jarvis(L):
	n=len(L)
	EnvConvexe=[]
	for i in range(n):
		for j in range(n):
			Listeorientation=[]
			if i!=j:
				for k in range(n):
					if k!=i and k!=j:
						Listeorientation.append(orientation(L[i],L[j],L[k]))
				a=Listeorientation[0]
				sommet=True
				for v in Listeorientation:
					if (v!=a):
						sommet=False
				if sommet and (i not in EnvConvexe):
					EnvConvexe.append(i)
				if sommet and (j not in EnvConvexe):
					EnvConvexe.append(j)
	return EnvConvexe


from random import gauss
n = 50
x = [gauss(-5,5) for i in range(n)]
y = [gauss(-5,5) for i in range(n)]
L = [[x[i],y[i]] for i in range(n)]

#print(L)

def prochain_sommet(L,i):
	imin=0
	if (i==0):imin=1
	for j in range(len(L)):
		if orientation(L[i],L[j],L[imin])>0:
			imin=j
	return imin


Enveloppe = jarvis (L)


P = L[prochain_sommet(L,Enveloppe[0])]

# On a les sommets de l'enveloppe convexe, mais ces derniers ne sont pas encore triés dans le bon ordre (cf plot ci-dessous)
'''
import matplotlib.pyplot as plt
plt.plot([L[i][0] for i in range(n)],[L[i][1] for i in range(n)], 'ko')
plt.plot(L[Enveloppe[0]][0],L[Enveloppe[0]][1], 'bo')
plt.plot(P[0],P[1], 'ro')
#plt.plot([L[i][0] for i in Enveloppe],[L[i][1] for i in Enveloppe ], 'r-')
plt.show()
'''

def point_abs_min(L):
    indice=0
    i = 1
    xmin = L[0][0]
    ymin = L[0][1]
    n = len(L)
    for i in range(n):
        if L[i][0]<xmin:
            xmin = L[i][0]
            ymin = L[i][1]
            indice = i
        elif L[i][0] == xmin and L[i][1]<ymin:
            ymin = L[i][1]
            indice = i
    return indice



def jarvis2(L):
	i=point_abs_min(L)
	suivant=prochain_sommet(L,i)
	Enveloppe=[i,suivant]
	while (suivant!=i):
		suivant=prochain_sommet(L,suivant)
		Enveloppe.append(suivant)
	return Enveloppe


# Affichage de l'enveloppe convexe
Enveloppe = jarvis2(L)
import matplotlib.pyplot as plt
plt.plot([L[i][0] for i in range(n)],[L[i][1] for i in range(n)], 'ko')
plt.plot([L[i][0] for i in Enveloppe],[L[i][1] for i in Enveloppe ], 'r-')
plt.show()

def graham_andrew(L):
	#L= tri_nuage(L)
	EnvSup =[]
	EnvInf =[]
	for i in range(len(L)):
		while len(EnvSup ) >=2 and orientation(L[i],L[ EnvSup [ -1]] ,L[ EnvSup[ -2]]) <=0:	
			print(orientation(L[i],L[ EnvSup [ -1]] ,L[ EnvSup[ -2]]))
			EnvSup.pop()
		EnvSup.append (i)
		while len( EnvInf ) >=2 and orientation(L[ EnvInf [ -2]] ,L[ EnvInf[ -1]] ,L[i]) <=0:
			EnvInf.pop()
		EnvInf.append (i)
		print(i)
		print(EnvSup)
	return EnvInf [: -1]+ EnvSup [:: -1]

P0 = [0.1,3.2]
P1 = [1.5,2.3]
P2 = [2.8,0.3]
P3 = [4.9,3.3]
P4 = [2.3,3.8]
P5 = [4.3,1.7]
P6 = [3.7,4.4]
P7 = [0.5,0.7]
P8 = [5.8,0.9]

L = [P0,P1,P2,P3,P4,P5,P6,P7,P8]

L = [P0,P7,P1,P4,P2,P6,P5,P7,P8]

GA = graham_andrew(L)








