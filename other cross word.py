
#create chart
rows = 4
collums = 15 
chart = [[" " for i in range(collums)] for j in range(rows)]
chart[2][2]="hi"

'''print(chart)'''


#breakdown chart
phrase = "For a love that will never die oh and happy friend-aversary"
Pbank = phrase.split()

locX = 0
locY = 0
score = collums

WA = False

for W in Pbank:
    WA = False
    '''print("reviewing ",W,"-",len(W))'''
    while(WA == False):
        '''print("adding ",W)'''
        if(len(W)<=score):
            for w in range(0,len(W)):
                chart[locY][locX]=W[w]
                '''print("printed ",W[w]," in ",locX,",",locY,"[",(score-1),"]")'''
                locX+=1
                score-=1
                
            if(score > 0):
                '''print("added space ",locX,",",locY,"[",score,"]")'''
                chart[locY][locX]=" "
                locX+=1
                score-=1
                
            WA = True
        else:
            WA = False
            locY+=1
            '''print("broken - next line")'''
            locX=0
            score = collums   
    
        

#print(Pbank)
# print chart
for row in range(0,rows):
    print(chart[row])
'''
checking 

for R in rows:
    for C in collums:
        print(R,C)
'''
