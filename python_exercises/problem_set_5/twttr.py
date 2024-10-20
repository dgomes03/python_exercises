def main():
    resposta = str(input("Input: "))
    print(f"{shorten(resposta)}")  # Print the returned shortened string

def shorten(word):
    shortened_word = ""  # Initialize an empty string to collect non-vowel characters
    for c in word:
        if c.lower() not in ['a', 'e', 'i', 'o', 'u']:  # Exclude vowels
            shortened_word += c  # Append consonants to the string
    return shortened_word  # Return the final shortened string

if __name__ == "__main__":
    main()
