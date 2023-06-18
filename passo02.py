#lista de letras para criptografar
alfabeto = "abcdefghijklmnopqrstuvwxyz"
#capture a mensagem do usuário
mensagem = input("Por favor , entre com a mensagem a ser criptografada : ").lower()
# esta variável armazenará a mensagem criptografada
mensagemCriptografada = ""
# capture a chave secreta
chave = input("Por favor, entre com a chave : ")
# esta ação é necessaria porque o programa não lê o valor da chave como um número
chave = int(chave)
# percorra cada caractere na mensagem
for char in mensagem:
    if char in alfabeto:
        posicao = alfabeto.find(char)
        novaPosicao = (posicao + chave) % 26
        mensagemCriptografada = mensagemCriptografada + alfabeto[novaPosicao]
    else:
        mensagemCriptografada = mensagemCriptografada + char
print("Sua mensagem criptografada é :" , mensagemCriptografada)
