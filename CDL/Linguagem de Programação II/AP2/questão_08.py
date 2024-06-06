def VerificarString(texto):

    if len(texto) >= 3 and len(texto) <= 20:
        print("String aceita!")
    else:
        print("String Recusada, não cumpriu os requisitos!")

print("-="*15)
insertText = input("Digite uma frase que deve ter no mínimo 3 e no máximo 20 caracteres: ")
print("-="*15)
VerificarString(insertText)