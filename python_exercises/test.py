name='Bob'
file = open("names.txt", "w")
file.write(name)
file.close()


file = open("names.txt", "r")
contents = file.readline()
print(contents)
file.close()


#read lines
with open("names.txt", "r") as file:
        print(len(file.readlines()))

#ou
with open('myfile.txt','r') as f:
    N=0
    for line in f:
        N+=1
print('number of lines', N)
