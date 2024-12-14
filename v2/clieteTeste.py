from ftplib import FTP_TLS

# Configurações do servidor FTP
HOST = "0.0.0.0"
PORT = 2121
USERNAME = "ftpuser"
PASSWORD = "senha123"

def connect_to_ftp():
    try:
        # Inicializa a conexão FTPS
        ftps = FTP_TLS()
        ftps.connect(HOST, PORT)
        ftps.login(USERNAME, PASSWORD)

        ftps.prot_p()

        print("Conexão estabelecida com sucesso!")

        # Lista arquivos no diretório raiz
        print("Conteúdo do diretório:")
        ftps.retrlines("LIST")

        # Faz logout e encerra a conexão
        #ftps.quit()
        #print("Conexão encerrada.")
    except Exception as e:
        print(f"Erro ao conectar: {e}")

if __name__ == "__main__":
    connect_to_ftp()