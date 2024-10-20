def faces():
        x=input()
        print(convert(x))

def convert(x):
        x=x.replace(":)","🙂")
        x=x.replace(":(","🙁")
        return x

faces()
