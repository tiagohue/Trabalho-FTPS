import os

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

# Manipula as autorisacoes e usuarios do server
authorizer = DummyAuthorizer()

# Criacao de um novo usuario
dir_path = os.path.dirname(os.path.realpath(__file__)) + "/dir_vigno"
authorizer.add_user('vigno', 'tux', dir_path, perm='elradfmwMT')

# Classe que manipula os comandos vindos do cliente
handler = FTPHandler
handler.authorizer = authorizer
handler.timeout = 1800

# Aparece quando o cliente conecta
handler.banner = "Bem vindo ao servidor FTP."

# Apagar depois:
# Specify a masquerade address and the range of ports to use for
# passive connections.  Decomment in case you're behind a NAT.
#handler.masquerade_address = '151.25.42.11'
#handler.passive_ports = range(60000, 65535)

# Instancia o servidor e define seu endereco
address = ('', 2121)
server = FTPServer(address, handler)

# define o limite de conexoes
server.max_cons = 256
server.max_cons_per_ip = 5

# inicia o ftp server
server.serve_forever()