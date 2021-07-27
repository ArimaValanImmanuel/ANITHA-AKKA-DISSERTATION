f = open("A:\\Arima\\PROJECTS\\Outbox\\Anitha Akka\\Animals\\VGG19\\newhis.txt", "r")
nf = open("A:\\Arima\\PROJECTS\\Outbox\\Anitha Akka\\Animals\\VGG19\\acc.txt", "w+")
content = f.readlines()

content_acc = [x.strip() for x in content[1::3]]

content_acc = [x.split('-') for x in content_acc]

for j in content_acc:
    j.pop(0)
    j.pop(0)      
            


for i in content_acc:
    for j in i:
        nf.write(j)
        nf.write("\n")
    nf.write("\n")
nf.close()
