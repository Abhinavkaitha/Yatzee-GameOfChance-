#!/usr/bin/env python
import sys
d1=int(sys.argv[1])
d2=int(sys.argv[2])
d3=int(sys.argv[3])

if d1==d2==d3:
    print("you won")
else:

    # This function returns the sum of the dice or 25 if all the numbers are equal
    def heuristic(L):
        if L[0]==L[1]==L[2]:
            return 25
        else:
            return L[1]+L[2]+L[0]

    # Am generating all the possible successors for the given combination
    def successors(L):
        ds0=[]
        ds1=[]
        ds2=[]
    #ds0 will contain all the possible successors when dice one is rerolled
    #Similarly ds1,ds2
        for i in range(len(L)):
            for j in range(1,7):
                if i==0: #and j!=L[0]:
                    ds0.append([j,L[1],L[2]])
                if i==1: #and j!=L[1]:
                    ds1.append([L[0],j,L[2]])
                if i==2: #and j!=L[2]:
                    ds2.append([L[0],L[1],j])
    #ds01 will contain all the possible successors when dice first and second dice are rerolled
    #Similarly ds12 and ds20
        ds01=[]
        ds12=[]
        ds20=[]
        for i in range(len(L)):
            for j in range(len(L)):
                if i==0 and j==1:
                    for k in range(1,7):
                        for l in range(1,7):
                                ds01.append([k,l,L[2]])
                if i==1 and j==2:
                    for k in range(1,7):
                        for l in range(1,7):
                                ds12.append([L[0],k,l])
                if i==2 and j==0:
                    for k in range(1,7):
                        for l in range(1,7):
                                ds20.append([k,L[1],l])
    #ds012 will have all the successors when all the three ddice are rerolled
        ds012=[]
        for i in range(1,7):
            for j in range(1,7):
                for k in range(1,7):
                        ds012.append([i,j,k])
    #s0 will have the expected value when dice one is rerolled
    #Similarly s1,s2,s01,s12,s20,s012
        s0=0
        for i in ds0:
            s0+=heuristic(i)
        s0=s0/6
        s1=0
        for i in ds1:
            s1+=heuristic(i)
        s1=s1/6
        s2=0
        for i in ds2:
            s2+=heuristic(i)
        s2=s2/6
        s01=0
        for i in ds01:
            s01+=heuristic(i)
        s01=s01/36
        s12=0
        for i in ds12:
            s12+=heuristic(i)
        s12=s12/36
        s20=0
        for i in ds20:
            s20+=heuristic(i)
        s20=s20/36
        s012=0
        for i in ds012:
            s012+=heuristic(i)
        s012=s012/216
        return s0,s1,s2,s01,s12,s20,s012


    def printer(argument):
        switcher = {
            "s0": "Reroll the first dice",
            "s1": "Reroll the second dice",
            "s2": "Reroll the third dice",
            "s01":"Reroll the first and second dice",
            "s12":"Reroll the second and third dice",
            "s20":"Reroll the first and third dice",
            "s012":"Reroll all the dice",
        }
        return switcher.get(argument, "nothing")


    #Am storing all the values in a dictionary and taking the max will give the key with maximum expected value
    d={}
    d["s0"],d["s1"],d["s2"],d["s01"],d["s12"],d["s20"],d["s012"]=successors([d1,d2,d3])

    print(printer(max(d)))

