import socket
HOST = socket.gethostbyname(socket.gethostname())    # Endereco IP do Servidor
print ('IP do servidor: ', HOST,'\n')
PORT = 5000            # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)
while True:
    con, cliente = tcp.accept()
    print ('Concetado por', cliente)
    while True:
        msg = con.recv(1024)
        if not msg: break
        print ('Recebido de',cliente,' : ',msg.decode('ascii'))
    print ('Finalizando conexao do cliente', cliente)
    con.close()