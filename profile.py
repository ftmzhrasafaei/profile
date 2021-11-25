import math


def GetSequences(N):
    sequence = []
    for i in range(N):
        seq = input()
        sequence.append(seq)
    return sequence

#---------------------

def TableSize(sequence):
    chars = []
    lens = len(sequence[0])
    for i in range(len(sequence)):
        for j in range(lens):
            if not(sequence[i][j] in chars):
                chars.append(sequence[i][j])
    return chars , lens

def Score(frequency , N , B , pseudo):
    return((frequency+pseudo)/(N+(B*pseudo)))
def Frequency(sequence, res , col):
    f = 0
    for s in sequence:
        if s[col] == res:
            f = f+ 1
    return f

#-----------------------

def CreateTable(sequence , N , B , pseudo):
    c , l = TableSize(sequence)
    overall = [0 for i in range(len(c))]
    table = [[0 for j in range(l)] for i in range(len(c))]
    o = 0
    for i in range(len(c)):
        for j in range(l):
            #print(c[i] , j,Frequency(sequence , c[i] , j))
            o = Frequency(sequence , c[i] , j) + o
            table[i][j] = Score(Frequency(sequence , c[i] , j) , N , B , pseudo)
        overall[i] = o/B
        o = 0
    for i in range(len(c)):
        for j in range(l):
            table[i][j] = math.log2(table[i][j]/overall[i])
    return table

#----------------------

def FindSubSequence(lseq , mat ,chars , B):
    N = len(mat[0])
    longl = len(lseq)
    best = lseq[0:N]
    bests = FindScore(best , mat , chars , B)
    lsubseq = longl - N + 1
    for i in range(1,lsubseq):
        sub = lseq[i:N+i]
        #print(sub)
        #best = sub
        subs = FindScore(sub , mat , chars , B)
        if bests < subs :
            bests = subs
            best = sub
    return best

#------------------------

def FindScore(seq , mat , chars , B):
    s = 0
    N = len(mat[0])
    for i in range(len(seq)):
        if seq[i] in chars:
            x = chars.index(seq[i])
            sl = mat[x][i]
        else:
             sl =NotInclided(N , B)
        s = s + sl
    return s


#--------------------
def NotInclided(N , B):
    return math.log2(B/(N+B))
#---------------------

# ----- MAIN---------
print('Please Enter the size of MSA')
N = int(input())
print('Please Enter the MSA')
seq = GetSequences(N)
print('Please Enter the sequence for matching')
longseq = input()



pseudocount = 1
B = 20
c , l = TableSize(seq)
t = CreateTable(seq , N , B , pseudocount)
f  =  FindSubSequence(longseq , t , c ,B)
print('---- Result -----')
print(f)
