Informações sobre a execução 

 

Inicialmente deve-se ler o arquivo e junto disso realizar a contagem de quantas linhas o mesmo possuía, sendo assim, usou-se um contador no qual a cada linha percorrida acrescentava um valor unitário, logo após a leitura o valor da quantidade de linhas é mostrado a tela, e depois ocorre o fechamento do arquivo. 

Após isso, o documento é  “chamado ” novamente, com isso agora passa a existir mais dois vetores , dois deles com o tamanho do texto lido e um terceiro para verificar se ocorreu mudanças na estrutura. 

 

Agora dentro de um loop for  acontecerá um incremento  com as informações contidas no programa, nessa arquitetura  possui uma variável responsável pela leitura dos 3 caracteres (sempre lembrando que nessa leitura o espaço também é contado), como strings , outro responsável para mudança de bases , convertendo para inteiro de base hexadecimal, por conseguinte será pego os valores representados em hexadecimal e armazenados em  2 vetores distintos , sendo eles um responsável pelo endereço do dado e o outro pela instrução do processamento dele. 

 

Após a arquitetura do loop, possuímos variáveis com seus valores iniciais em 0, sendo elas: 

PC : que será responsável pelos valores contidos no Program Counter  

Z  : Variável auxiliar  

AC : Acumulador  

CI : Contador de instruções  

Seguindo o código, agora iremos passar para o início das instruções. Começaremos mostrando o nome do arquivo e após isso,  iniciaremos um “while” , que sempre será executado , e para única forma de encerra-lo será com a função HLT. 

Agora dentro do while,  possui uma estrutura lógica um pouco mais complexa, tratando-se de várias  estruturas condicionais. No primeiro “if”,  é o responsável pelo termino do “while” , ou seja, a funçao conhecida como HLT , quando entra nessa condição o CI ganhará  mais um valor unitário junto com o PC , após isso mostrará na tela a função no caso “HLT” e encerrara o while. 

Segundo “if” , possui a função LDR o qual é responsável por carregar um valor no AC , quando a condição desse “if” for alcançado o CI e o PC também ganharam um valor unitário, e além disso a variável z receberá   o valor da instrução , dentro disso está contido um “for” , que irá ordenar e verificar o endereço  recebido  ná variável Z, caso ela for condizente o AC receberá o valor contido e o PC receberá  mais um valor unitário. Após ,  mostrar a função na tela “LDR” e o seu endereço e terminará esse “for”.    

 

No terceiro “if”  temos a função STR responsável por armazenar um valor, com isso , caso a acessibilidade a esse elemento for alcançada , as variáveis PC e CI irão receber valores unitários também. Após isso, dentro dessa condição verifica-se se o endereço recebido pela variável Z esta condizente, testando em um “for” , dentro desse for possui um outro “if” , o qual necessita que o endereço recebido por z seja condizente com o do vetor, caso isso ocorra o PC será incrementado com mais um , o  AC recebera o valor que deseja armazenar  , mostrará na tela a função “STR” e encerrará o “for”. 

 

A seguir , os 4 if seguintes buscam o endereço condizente e pegam o valor equivalente, convertem a variável contador para um inteiro de base 16, realiza a operação desejada e guarda o valor em hexadecimal na variável AC. 

Já os próximos  4 if seguintes realizam as operações NOT, AND, OR e XOR. Como nota não precisa de mais outro valor além do contador, trabalha só com ele. Os 3 seguintes pegam o contador e fazem a operação logica com o valor instruído no endereço. 

Os 4 if restantes  são as funções JMP, JEQ, JG e JL.  Como estas funções alteram o program conter o ac não é utilizado, apenas o pc, em JMP o pc recebe o valor do endereço desejado. Como os outros 3 são condicionais, o pc receber o endereço só ocorrera se a devida condição de cada um for cumprida. Caso não entre na condicao o pc aumentara em 2, o que o fara passar para a próxima instrução. 

A seguir vem os prints dos resultados: 

O primeiro mostra o numero de instruções executadas, a variavel ci (contador de instruções) que esta presente em todas as instruções incluindo as funções JMP JEQ JG e JL, caso a condição não se cumpra.  

A seguir mostra os registradores, ac e pc. 

Após os registradores mostra os endereços em que algo foi alterado. Para isso é usado o vetor com a copia do original criado logo no começo do programa.  Para isso dentro de um for com o tamanho do numero de linhas, se a instrução no código final for diferente da na copia inicial, mostra o endereço daquele valor e o valor alterado. 

Fecha o arquivo.