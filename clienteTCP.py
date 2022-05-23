import socket
HOST = input("digite IP do servidor que voce quer se conectar\n")     # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)
print ('Para sair use CTRL+X\n')
msg = input("digite sua mensagem\n")
while msg != '\x18':
    tcp.send (msg.encode('ascii'))
    msg = input("digite sua mensagem\n")
tcp.close()