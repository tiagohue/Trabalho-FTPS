from pyftpdlib.servers import FTPServer
from pyftpdlib.handlers import TLS_FTPHandler
from pyftpdlib.authorizers import DummyAuthorizer

# Configura o autorizer com usuário e senha
def setup_authorizer():
    authorizer = DummyAuthorizer()
    # Adiciona um usuário com permissão total ("elradfmw")
    authorizer.add_user("ftpuser", "senha123", "/home", perm="elradfmw")
    # Permite conexões anônimas (opcional, remova se não quiser)
    # authorizer.add_anonymous("/home/ftpuser")
    return authorizer

# Configura o handler para usar SSL/TLS
def setup_handler(authorizer):
    handler = TLS_FTPHandler
    handler.authorizer = authorizer
    handler.certfile = "server.pem"  # Caminho para o certificado SSL
    handler.tls_control_required = True
    handler.tls_data_required = True
    return handler

# Função principal para iniciar o servidor
def start_ftp_server():
    # Certifique-se de que o certificado SSL existe
    import os
    if not os.path.exists("server.pem"):
        print("Gerando certificado SSL...")
        os.system("openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout server.pem -out server.pem -subj '/CN=localhost'")

    authorizer = setup_authorizer()
    handler = setup_handler(authorizer)
    
    # Configura o servidor para ouvir em um endereço e porta
    server = FTPServer(("0.0.0.0", 2121), handler)  # Porta 2121 (ou escolha outra)
    print("Servidor FTP com SSL iniciado em porta 2121")
    server.serve_forever()

if __name__ == "__main__":
    start_ftp_server()
