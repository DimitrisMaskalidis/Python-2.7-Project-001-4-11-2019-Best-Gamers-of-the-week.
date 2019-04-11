def LeaderBoard(L,L2,x,y):
    i=0
    while i<10:
        if L2[i]<y:
            L2.insert(i,y)
            L.insert(i,x)
            L2.pop()
            L.pop()
            i=10
        i+=1
def Lsort(L,L2):
    for i in range(10):
        L.insert(i," ")
        L2.insert(i,0)
             
Names=[];Scores=[];YNames=[];YScores=[]
Lsort(Names,Scores);Lsort(YNames,YScores)
for i in range(52):
    name=raw_input("Write Your NickName: ")
    while name!='END':
        score=input("White Your Score: ")
        LeaderBoard(Names,Scores,name,score)
        name=raw_input("Write Your NickName: ")
    for i in range(10):    
        print 'The number',i+1,'player of the week',Names[i],'with',Scores[i],'score'

    for i in range(10):
        j=0
        while j<10:
            if YScores[j]<Scores[i]:
                YScores.insert(j,Scores[i])
                YNames.insert(j,Names[i])
                YScores.pop()
                YNames.pop()
                j=10
            j+=1
    Names=[];Scores=[]
    Lsort(Names,Scores)
print "AND"    
for i in range(10):    
        print 'The number',i+1,'player of the year',YNames[i],'with',YScores[i],'score'
