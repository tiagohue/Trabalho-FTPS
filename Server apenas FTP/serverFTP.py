import os

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

# Manipula as autorisacoes e usuarios do server
authorizer = DummyAuthorizer()

# Criacao de um novo usuario
dir_path_vigno = os.path.dirname(os.path.realpath(__file__)) + "/dir_vigno"
authorizer.add_user('vigno', 'tux', dir_path_vigno, perm='elradfmwMT', msg_login="Bem vindo, Vigno.", msg_quit="Adeus, Mestre das Redes.")

# Classe que manipula os comandos vindos do cliente
handler = FTPHandler
handler.authorizer = authorizer
handler.timeout = 1800

# Aparece quando o cliente conecta
handler.banner = "Bem vindo ao servidor FTP da UESPI."

# Instancia o servidor e define seu endereco
address = ("192.168.1.103", 2121)
server = FTPServer(address, handler)

# define o limite de conexoes
server.max_cons = 256
server.max_cons_per_ip = 5

# inicia o ftp server
server.serve_forever()