import socket
import json

ip = "192.168.3.3"
porta = 80
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, porta))


usuarios = []


email = input('Email: ')
senha = input('Senha: ')


usuarios.append({'email': email, 'senha': senha})


usuarios_json = json.dumps(usuarios)


s.sendall(usuarios_json.encode())

s.close()
