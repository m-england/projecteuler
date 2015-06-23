def findthenumber(nomulti):
    a = 200000000
    
    while True:
    #for a in range(200000000,500000000):
        for i in range(1,21):
            if (a % i != 0):
                #print str(i) + " was found to not be a multiple of " + str(a)
                nomulti = 1
                #print str(a) + " was not divisible by" + str(i)
                break
            #else:
                #print str(i) + " was found to be a multiple of " + str(a)

            #print str(nomulti)
            
        if nomulti != 1:
            print str(a) + " MET THE CRITERIA"
            return a

        nomulti = 0
        a += 1


findthenumber(0)
print "loop done"
