def main():
    x=str(input())
    print(playback(x))

def playback(x):
    x=x.replace(" ","...")
    return x

main()
