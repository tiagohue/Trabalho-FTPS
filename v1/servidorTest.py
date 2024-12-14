from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import TLS_FTPHandler
from pyftpdlib.servers import FTPServer
import os
import socket

def get_host_ip():
    """
    Obtém automaticamente o endereço IP local da máquina.
    """
    try:
        # Cria um socket temporário para determinar o IP
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.connect(("8.8.8.8", 80))  # Conecta a um servidor DNS (Google, neste caso)
            return s.getsockname()[0]
    except Exception:
        return "127.0.0.1"  # Caso algo dê errado, retorna localhost como padrão

def start_ftps_server():
    # Configurações do servidor
    host = get_host_ip()   # Obtém o IP automaticamente
    port = 2121            # Porta do servidor FTPS
    username = "user"      # Nome de usuário
    password = "password"  # Senha
    directory = "./ftps_dir"  # Diretório de arquivos

    # Criar o diretório se não existir
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Configurar usuários e permissões
    authorizer = DummyAuthorizer()
    authorizer.add_user(username, password, directory, perm="elradfmw")

    # Configurar o manipulador FTPS
    handler = TLS_FTPHandler
    handler.authorizer = authorizer
    handler.certfile = "cert.pem"  # Certificado SSL (pré-existente)
    handler.tls_control_required = True
    handler.tls_data_required = True

    # Configurar o servidor
    server = FTPServer((host, port), handler)
    print(f"Servidor FTPS iniciado em {host}:{port}")
    print(f"Usuário: {username}, Senha: {password}, Diretório: {directory}")

    # Iniciar o servidor
    server.serve_forever()

if __name__ == "__main__":
    # Gera o certificado SSL, se necessário
    if not os.path.exists("cert.pem"):
        print("Certificado não encontrado. Crie um com o comando:")
        print("openssl req -x509 -newkey rsa:2048 -keyout cert.pem -out cert.pem -days 365 -nodes")
    else:
        start_ftps_server()
