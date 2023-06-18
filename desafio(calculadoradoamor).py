print(""" Calculdora do amor
<3 <3 <3 <3 <3 <3 <3 <3 <3 <3 <3 """)

def calcular_placar(mensagem):
    placar = 0
    letras_encontradas = []

    for char in mensagem:
        if char in "aeiou" and char not in letras_encontradas:
            placar += 10
            letras_encontradas.append(char)
        if char in "amor" and char not in letras_encontradas:
            placar += 10
            letras_encontradas.append(char)
        elif placar < 10:
            print(" Esqueça esta pessoa ! , Nunca vai dar certo ! ")
        elif placar > 50:
            print(" Vocês terão um relacionamento muito intenso ! <3")
            

    return placar

mensagem = input(" Digite o nome de duas pessoas : ")

placar = calcular_placar(mensagem)

print("Seu placar de compatibilidade : ", placar)


