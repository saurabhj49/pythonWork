def remove_duplicates(li):
    dupli = []
    for l in li:
        dupli.append(l)
    print ("Original List")
    print (li)
    print ("duplicate List")
    print (dupli)
    new_li = []
    cou = 0
    size = len(li)
    size_1 = len(li)
    print (size)
    for i in range(0, size):
        print("Orig list ")
        print(li)
        print("New list ")
        print(new_li)
        print("Dupli list ")
        print(dupli)
        print ("iteration for i " + str(i) + "for element " + str(li[i]))
        cou = 0
        for j in range(0, len(dupli)):
            print ("iteration for j " + str(j) + "for element " + str(li[j]))
            if li[i] == dupli[j]:
                cou = cou +1
        print ("For "+ str(li[i]) + " "+ str(cou))
        if cou == 1:
            print ("Append in new list "+ str(li[i]))
            new_li.append(li[i])
        else:
            if cou == 2:
                cou = 1
            else:
                cou = cou-1
            for c in range(0, cou):
                print ("Pop from dupli "+ str(li[i]))
                dupli.remove(li[i])
            
    print(dupli)
    print(new_li)
        
        
            
        
        
    
remove_duplicates([1,2,1,3])
