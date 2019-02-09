import time


inicio = time.time()

arq = open('dataset-2-a.csv', 'r')
texto = arq.read().split('\n')

resposta=max(texto)
print(resposta+"--------teste-------")
arq.close()
arquivoFinal=open("resposta 2-A.txt","w")


segundos = time.time()
milissegundos = segundos * 1000
print(milissegundos)
arquivoFinal.write("Maior numero:" + str(resposta)+ "\n"+ "Tempo gasto em milissegundos:"+str(milissegundos))
arquivoFinal.close()
