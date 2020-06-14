#primeira lida pra contar quantas linhas tem o texto, eu nao sei porque dava problema
#mas fazer isso resolveu
f = open('entrada01.txt','r')
contador_de_linha=0 #variavel que conta quantas linhas o arquivo tem
#pra cada linha acresce 1 ao contador assim tendo o num total de linhas
for line in f:
    contador_de_linha +=1
#print (contador_de_linha) #MOSTRA QUANTAS LINHAS FORAM LIDAS, PRA GARANTIR
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
#for n in range(0,contador_de_linha):
    #print(enderecos[n]," ",instrucoes[n]) 
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
    if(e==hex(0x30)): #ADD SOMA UM VALOR AO AC
        ci+=1
        pc+=1
        z=instrucoes[pc]
        for n in range(contador_de_linha):
            if(enderecos[n]==z):
                ac=int(ac,16)
                valor=instrucoes[n]
                valor=int(valor,16)
                ac=hex(ac+valor)
                pc+=1
                print("ADD",enderecos[n])
                break

    if(e==hex(0x40)):#SUB SUBTRAI UM VALOR DO AC
        ci+=1
        pc+=1    
        z=instrucoes[pc]
        for n in range(contador_de_linha):
            if(enderecos[n]==z):
                ac=int(ac,16)
                valor=instrucoes[n]
                valor=int(valor,16)
                ac=hex(ac-valor)
                pc+=1
                print("SUB",enderecos[n])
                break

    if(e==hex(0x50)): #MUL MULTIPLICA
        ci+=1
        pc+=1    
        z=instrucoes[pc]
        for n in range(contador_de_linha):
            if(enderecos[n]==z):
                ac=int(ac,16)
                valor=instrucoes[n]
                valor=int(valor,16)
                ac=hex(ac*valor)
                pc+=1
                print("MUL",enderecos[n])
                break
    
    if(e==hex(0x60)): #DIV DIVIDE
        ci+=1
        pc+=1    
        z=instrucoes[pc]
        for n in range(contador_de_linha):
            if(enderecos[n]==z):
                ac=int(ac,16)
                valor=instrucoes[n]
                valor=int(valor,16)
                ac=hex(ac/valor)
                pc+=1
                print("DIV",enderecos[n])
                break
    
    if(e==hex(0x70)): #NOT bitwise
        ci+=1
        pc+=1 
        ac=int(ac,16)   
        ac=hex(~ac)
        print("NOT")

    if(e==hex(0x80)): #AND bitwise
        ci+=1
        pc+=1
        z=instrucoes[pc]
        for n in range(contador_de_linha):
            if(enderecos[n]==z):
                ac=int(ac,16)
                valor=instrucoes[n]
                valor=int(valor,16)
                ac=hex(ac & valor)
                pc+=1
                print("AND",enderecos[n])
                break

    if(e==hex(0x90)): #OR bitwise
        ci+=1
        pc+=1
        z=instrucoes[pc]
        for n in range(contador_de_linha):
            if(enderecos[n]==z):
                ac=int(ac,16)
                valor=instrucoes[n]
                valor=int(valor,16)
                ac=hex(ac | valor)
                pc+=1
                print("OR",enderecos[n])
                break

    if(e==hex(0xa0)): #XOR bitwise
        ci+=1
        pc+=1
        z=instrucoes[pc]
        for n in range(contador_de_linha):
            if(enderecos[n]==z):
                ac=int(ac,16)
                valor=instrucoes[n]
                valor=int(valor,16)
                ac=hex(ac ^ valor)
                pc+=1
                print("XOR",enderecos[n])
                break

    if(e==hex(0xb0)): #JMP PULA PRA
        ci+=1
        pc+=1
        pc=instrucoes[pc]
        print("JMP")

    if(e==hex(0xc0)): #JEQ PULA SE IGUAL 0
        ci+=1
        ac=int(ac,16)
        if(ac==0):
            pc+=1
            pc=instrucoes[pc]
            print("JEQ")
        else:
            pc+=2

    if(e==hex(0xd0)): #JG PULA SE MAIOR 0
        ci+=1
        ac=int(ac,16)
        if(ac>0):
            pc+=1
            pc=instrucoes[pc]
            print("JG")
        else:
            pc+=2

    if(e==hex(0xe0)): #JL PULA SE MENOR 0
        ci+=1
        ac=int(ac,16)
        if(ac<0):
            pc+=1
            pc=instrucoes[pc]
            print("JL")
        else:
            pc+=2
#PRINT FINAIS
pc=hex(pc)
print()
print(ci,"instructions executed\n")
print("REGISTERS:")
print("AC:",ac)
print("PC:",pc,"\n")
print("MEMORY:")
#COMPARA O VETOR DAS INSTRUCOES DO FINAL COM A COPIA INICIAL SE FOR DIFERENTE EXIBE 
for n in range(0,contador_de_linha):
    if(instrucoes[n]!=compara[n]):
        print(enderecos[n]," ",instrucoes[n])

f.close()


