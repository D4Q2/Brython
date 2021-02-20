from browser import document

document <= "File: "

f = open("/database.txt","w+")
f.write("It worked!!!!!")
f.close()


document <= "File Edited and Closed"

r = open("database.txt","r")
for line in r:
  data = r.read(line)
  print(data)

r.close()

document <= "File Read and Closed"
