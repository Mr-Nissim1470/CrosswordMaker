import os

#given Phrase
phrase = "for a love that will never die oh and happy friend-aversary"

#create chart
rows = 4
collums = 15 
chart = [[" " for i in range(collums)] for j in range(rows)]
chart[2][2]="hi"

'''print(chart)'''

#breakdown chart
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

# match bassed on bank
MatchBankT = ["fuckboy"]
MatchBank = ["fuckboy","ginger tea","prozac","bugging","if it means a lot to you","allforyou","in bloom","put you through me","venus fly trap","caffeine","deepfake","hypochondriac","intelectual greed","introvert","stung","i revolve around you","sauceintherough","doritos and fritos","dumbest girl alive","haunted","hollywood baby","money machine","stupid horse","teeth","saltines"]


CBank = []

class identifier:
    def __init__ (LCD,name,Letters,matches,fill):
        LCD.name = name
        LCD.Letters = Letters
        LCD.matches = matches
        LCD.fill = fill

#Create bank of all collums
for S in range(0,collums):
    slit =[]
    for R in range (0,rows):
        if(chart[R][S]==" "):
            continue
        else:
            slit.append(chart[R][S])
    CBank.append(slit)
    #print(slit)

#classify words with points
COB = []
for i in range(0,len(CBank)):
    ScoreBank = []
    Matts = 0
    RO = identifier(("Colum "+str(i)),CBank[i],ScoreBank,Matts)
    COB.append(RO)

#Compare colum to word
def compare(CLM,WRD):
    String = WRD
    #print(String)
    SC=0
    for L in range(0,len(CLM.Letters)):
        strt=0
        for l in range(strt,len(String)):
            #print("looking at "+CLM.Letters[L]+" and "+String[l])
            if(CLM.Letters[L] == String[l]):
                #print("match Found")
                CLM.fill+=1
                SC+=1
                #print("letter added and reduction done")
                String = String.replace(String[l],"",1)
                strt = l+1
                break
    if(CLM.fill>0):
        CLM.matches.append((WRD+" ("+str(SC)+")"))
    #print("Finalized - "+(WRD+" ("+str(SC)+")"))

for C in COB:
    #print(C.name,C.Letters,C.matches,C.fill)
    for W in MatchBank:
        #print("checking ",C.name,"-",C.Letters," and ",W)
        compare(C,W)

print("results")
for F in COB:
    File = open("/Users/yosefnissim/Desktop/My stuff/Friendaversary/Files/"+str(F.name),"w")
    File.write(F.name+" - "+ str(F.fill)+"\n")
    File.write(str(F.Letters)+"\n")
    for i in F.matches:
        File.write(str(i)+"\n")
    print(str(F.name)+" file compiled")
    File.close()
    
#/Users/yosefnissim/Desktop/My stuff/Friendaversary/Files
'''
checking 

for R in rows:
    for C in collums:
        print(R,C)
'''
