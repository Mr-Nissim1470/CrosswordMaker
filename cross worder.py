
count = 0

def match(x,y):
    start = 0
    mark = 0
    found = 0
    word1L = len(x)
    word2L = len(y)
    #print("comparing ",x,word1L," and ",y,word2L,"")
    while word1L>0:
        for z in range(mark,word2L):
            #print ("checking ",x[start]," - ",y[z])
            if x[start]==y[z]:
                #print("match found")
                found+=1
                mark = z+1
                break
            
            
        start+=1
        word1L-=1
    return found

def rewrite():
    
    test = "For a love that will never die oh and happy anniversary"
    bank = ["fuckboy","ginger tea","prozac","bugging","if it means a lot to you","allforyou","in bloom","put you through me","venus fly trap","caffeine","deepfake","hypochondriac","intelectual greed","introvert","stung","i revolve around you","sauceintherough","doritos and fritos","dumbest girl alive","haunted","hollywood baby","money machine","stupid horse","teeth","saltines"]
    score = []
    Mwords = test.split()
    print(Mwords)
    print(bank)

    for W in bank:
        words = []
        for Ms in Mwords:
            C = match(W,Ms)
            if(C>0):
                words.append(Ms) 
            print ("for ",Ms," to ",W," ",C," matches")
        score.append(words)


    for o in range(0, len(bank)):
        print(bank[o]," Matched to ", score[o])
    
            
    
rewrite()

#def looper
