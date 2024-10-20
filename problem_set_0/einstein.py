#function that asks for mass in kg and returns energy in joules using eisteins's formula

'''
def energy(m):
    c=300000000
    return m*c*c
e = energy(m)
m=int(input("m: "))
print(f"E: {e}",sep="", end="")
'''


def energy(m):
    c=300000000
    return m*c*c

m=int(input("m: "))
print("E:",energy(m))
