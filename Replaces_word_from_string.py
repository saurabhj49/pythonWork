def censor(text, word):
    print ( text+" "+word)
    ast = []
    fin = []
    new = []
    new_text=""
    for t in range(0, len(text)):
        new.append(text[t])
        print ("Round "+ str(t))
        print (ast)
        ast = []
        c=0
        for w in range(0, len(word)):
            
            if text[t]==word[w]:
                c=c+1
                ast.append(t)
                t=t+1
        print (c)
        if c == len(word):
            fin.append(ast)
    print (fin)
    print (new)

    for i in fin:
        for j in i:
            new [j]= '*'

    for t1 in new:
        new_text+= t1

                
    print (new_text)

censor("hey hey hey","hey")
		




