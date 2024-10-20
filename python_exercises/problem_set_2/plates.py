def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    #verificar tamanho da string e se n tem caracteres especiais
    if 2 <= len(s) <= 6 and s.isalnum():
        #verificar se a string nao tem digitos
        if s.isalpha():
            return True
        else:
            #verificar se 2 primeiros caracteres sao letras
            if s[:2].isalpha():
                #criar loop que analisa cada caracter do string
                for i in range(len(s)):
                    #verificar se o caracter e um digito
                    if s[i].isdigit():
                        #verificar se primeiro digito = 0 e se apenas digitos sao seguidos apos o primeiro
                        if s[i] == "0" or not s[i:].isdigit():
                            return False
                        else:
                            return True
            else:
                return False
    else:
        return False


main()
