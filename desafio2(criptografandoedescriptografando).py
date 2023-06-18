# uma lista de letras para criptografar

alfabeto = "abcdefghijklmnopqrstuvwxyz"

# capture a mensagem do usuário

mensagem = input("Por favor, entre com a mensagem a ser criptografada : ").lower()

# esta variável armazena a mensagem criptografada

mensagemCriptografada = ""

# capture a chave secreta

chave = input("Por favor, entre a chave : ")

# esta chave é necessária porque o programa não lê o valor da chave como um número

chave = int(chave)

# percorra cada caractere na mensagem

for char in mensagem:
    if char in alfabeto:

        #encontre a posição de caractere em alfabeto
        # por exemplo, 'a' está na posição 0, 'e' está na posição 4, etc

        posicao = alfabeto.find(char)

        #some a chave secreta para encontrar a posição do caractere criptografado
        # %26 significa ' volte para 0 quando voce atingir 26'

        novaPosicao = (posicao + chave) % 26

        # acrescente a letra descriptografada à mensagem
        # a letra criptografada está em alfabeto na novaPosicao

        mensagemCriptografada = mensagemCriptografada + alfabeto[novaPosicao]

    else:

        # alguns caracteres por exemplo (por exemplo : '&' , '?') não estão no alfabeto,
        # então simplesmente adicione a letra criptografada à mensagem

        mensagemCriptografada = mensagemCriptografada + char

print("Sua mensagem criptografada é : ", mensagemCriptografada)
        
