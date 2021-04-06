fp=open("data.text")
x=0

while 1:
    try:
        content = fp.readline()
        if content[0].lower() in ('a','t'):
            print (content[0])
            x+=1
    except:
        break
    
print(x)
fp.close()