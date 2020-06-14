#primeira lida pra contar quantas linhas tem o texto, por qlqr razao depois que le
#ficou trancado na ultima linha entao tive que fechar e abrir dnv
f = open('instrucoes.txt','r')
contador_de_linha=0
#p cada linha acresce 1 ao contador assim tendo o num de linhas
for line in f:
    contador_de_linha +=1
print (contador_de_linha)
f.close()  
#SEGUNDA LIDA
f = open('instrucoes.txt','r')
#CRIA 2 VETORES COM O TAMANHO DO TEXTO
instrucoes=[0]*contador_de_linha
enderecos=[0]*contador_de_linha
#PREENCHE ELES COM O CONTEUDO DO ARQUIVO

for n in range(0,contador_de_linha):
   a=f.read(3) #pega os valores
   enderecos[n]=a[0:2]  #corta o espaço em branco
   instrucoes[n]=f.read(2)


#AQUI É SÓ UM TESTE PRA VER SE ELE PEGA O VALOR PS. PRA PEGAR OS ENDERECOS PRECISA CONTAR O 
#ESPACO DEPOIS ENTAO O ENDERECO "10"  É NA VERDADE "10 "
if(instrucoes[0]=="10"):
    print("ook")
if(enderecos[0]=="00"):
    print("ok2")

#AQUI É O COMECO DO CODIGO DE VERDADE QUE A PRINCIPIO LE TODAS AS LINHAS E TESTA AS INSTRUCOES
z=0     #VARIAVEL USADA PRA COMPARACOES
cp=0 #CONTADOR DE ISNTRUCOES
AC=0 #ACUMULADOR
e=instrucoes[0] #RECEBE AS INSTRUCOES E ENDERECOS
while(e!="F0"): #HLT
    e=instrucoes[cp]
    if(e=="10"):    #LDR
        cp+=1
        z=instrucoes[cp]
        for n in range(contador_de_linha):
            if(enderecos[n]==z):
                AC = instrucoes[n]
                cp+=1
                break
    if(e=="20"):    #STR
        cp+=1
    if(e=="30"):    #ADD
        cp+=1
    if(e=="40"):    #SUB
        cp+=1
    if(e=="50"):    #MUL
        cp+=1
    if(e=="60"):    #DIV
        cp+=1
    if(e=="70"):    #NOT
        cp+=1
    if(e=="80"):    #AND
        cp+=1
    if(e=="90"):    #OR
        cp+=1   
    if(e=="A0"):    #XOR
        cp+=1
    if(e=="B0"):    #JMP
        cp+=1
    if(e=="C0"):    #JEQ
        cp+=1   
    if(e=="D0"):    #JG
        cp+=1
    if(e=="E0"):    #JL
        cp+=1
        
    

   

f.close()
    

   

    
