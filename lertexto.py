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
   enderecos[n]=f.read(3)
   instrucoes[n]=f.read(2)


#AQUI É SÓ UM TESTE PRA VER SE ELE PEGA O VALOR PS. PRA PEGAR OS ENDERECOS PRECISA CONTAR O 
#ESPACO DEPOIS ENTAO O ENDERECO "10"  É NA VERDADE "10 "
if(instrucoes[0]=="10"):
    print("ook")

#AQUI É O COMECO DO CODIGO DE VERDADE QUE A PRINCIPIO LE TODAS AS LINHAS E TESTA AS INSTRUCOES
#for n in range(0,contador_de_linha):
#    if(instrucoes[n]=="")

    
   

f.close()
    

   

    
