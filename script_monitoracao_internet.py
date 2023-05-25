import urllib.request
import time

# URL para teste de conexão com a internet
url = 'https://www.google.com.br'

# Loop infinito para monitorar a conexão com a internet
while True:
try:
# Tentativa de conexão com a internet
urllib.request.urlopen(url)
print('Conectado à internet')

except urllib.error.URLError:
# Exceção caso não haja conexão com a internet
print('Sem conexão com a internet')

# Tempo de espera antes da próxima verificação de conexão
time.sleep(5)