#primeira lida pra contar quantas linhas tem o texto, eu nao sei porque dava problema
#mas fazer isso resolveu
f = open('entrada01.txt','r')
contador_de_linha=0 #variavel que conta quantas linhas o arquivo tem
#pra cada linha acresce 1 ao contador assim tendo o num total de linhas
for line in f:
    contador_de_linha +=1
print (contador_de_linha) #MOSTRA QUANTAS LINHAS FORAM LIDAS, PRA GARANTIR
f.close()  
#segunda lida do arquivo
f = open('entrada01.txt','r')
#CRIA 2 VETORES COM O TAMANHO DO TEXTO E UM TERCEIRO PRA COMPARAR MUDANCAS
instrucoes=[0]*contador_de_linha
enderecos=[0]*contador_de_linha
compara=[0]*contador_de_linha
#PREENCHE ELES COM O CONTEUDO DO ARQUIVO
for n in range(0,contador_de_linha):
   a=f.read(3) #LE 3 CARACTERES (INCLUINDO O ESPACO VAZIO)
   a=int(a,16) #CONVERTE PRA INTEIRO DE BASE HEXADECIMAL
   enderecos[n]=hex(a)
   b=f.read(3)
   b=int(b,16)
   instrucoes[n]=hex(b)
   compara[n]=instrucoes[n] #CRIA UMA COPIA DO VETOR DAS INSTRUCOES
#PRINTA TODOS OS VALORES SEPARADOS PRA TESTAR SE TA TUDO CERTO
for n in range(0,contador_de_linha):
    print(enderecos[n]," ",instrucoes[n]) 
pc=0 #program counter
z=0 #   variavel auxiliar
ac=0 #acum
ci=0 #cont de instrucoes
#COMECO DAS INSTRUCOES
print("Input file:",(f.name),"\n") #MOSTRA O NOME DO ARQUIVO
while(1>0): #SEMPRE VAI EXECUTAR, SAI DO LAÇO COM A FUCNAO HLT
    e=instrucoes[pc]
    if(e==hex(0xf0)): #HLT ENCERRA O PROGRAMA
        ci+=1
        pc+=1
        print("HLT")
        break

    if(e==hex(0x10)): #LDR CARREGA UM VALOR NO AC
        ci+=1
        pc+=1
        z=instrucoes[pc] #z recebe o endereco da instrucao
        for n in range(contador_de_linha):
            if(enderecos[n]==z): #procura um endereço condizente
                ac = instrucoes[n] 
                pc+=1
                print("LDR",enderecos[n])
                break

    if(e==hex(0x20)): #STR GUARDA UM VALOR 
        ci+=1 
        pc+=1
        z=instrucoes[pc] 
        for n in range(contador_de_linha):
            if(enderecos[n]==z):   
                instrucoes[n]=ac  
                pc+=1  
                print("STR",enderecos[n])
                break

f.close()