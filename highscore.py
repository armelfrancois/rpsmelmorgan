   f=open("Highscore.txt","a+")
    f.close()
    f=open("Highscore.txt","r+")
    
    data=f.read().split('\n')
    if not ((len(data)-1)==0):
        for i in range(0,len(data)-1):
            data[i]=data[i].split(',')
            data[i][1]=int(data[i][1])
    data[len(data)-1]=[name,score]
    for i in range(0, len( data)-1 ):
        for k in range( len( data ) -1, i, -1 ):
          if ( data[k][1] < data[k - 1][1] ):
            tmp=data[k]
            data[k]=data[k-1]
            data[k-1]=tmp
    i=0
    while(len(data)>i and i <10):
        f.write(data[i][0])
        f.write(',')
        f.write(str(data[i][1]))
        f.write('\n')
        i+=1
    f.close()
