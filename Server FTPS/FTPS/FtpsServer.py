import os
import socket
from pyftpdlib.handlers import TLS_FTPHandler
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.servers import FTPServer

def main():
    # Configuração do autorizer e usuários
    authorizer = DummyAuthorizer()
    authorizer.add_user('pinguim', 'linux', os.getcwd(), perm='elradfmwMT')
    authorizer.add_anonymous(os.getcwd())

    # Configuração do handler
    handler = TLS_FTPHandler
    handler.certfile = 'C:/Users/olimp/FTPS-cert-key/ftpd.crt'
    handler.keyfile = 'C:/Users/olimp/FTPS-cert-key/ftpd.key'
    handler.tls_control_required = True
    handler.tls_data_required = True
    handler.authorizer = authorizer


    # Obtendo o IP local
    ip = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        ip.connect(("8.8.8.8", 80))
        local_ip = ip.getsockname()[0]
    finally:
        ip.close()

    # Configuração do servidor
    server = FTPServer((local_ip, 2121), handler)
    print(f'SERVIDOR ON: IP: {local_ip}, PORTA: 2121')

    # Inicia o servidor
    server.serve_forever()

if __name__ == '__main__':
    main()
