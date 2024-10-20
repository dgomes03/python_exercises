filename = input("File name: ").lower().strip()
#usar lower para ignorar casos tipo ".JPG" ou ".TXT"

#selecionar o "." como separador do string
dot=filename.rfind('.')

#selecionar os caracteres psteriores ao "."
filetype=filename[dot:]
#NOTA: dot e a variavel criada acima. os : significam para buscar os caracteres posteriores ao "dot". os [] fazem slicing da string.


if filetype == '.jpg' or filetype == '.jpeg':
    print('image/jpeg')
elif filetype == '.gif':
    print('image/gif')
elif filetype == '.png':
    print('image/png')
elif filetype == '.pdf':
    print('application/pdf')
elif filetype == '.txt':
    print('text/plain')
elif filetype == '.zip':
    print('application/zip')
else :
    print('application/octet-stream')

