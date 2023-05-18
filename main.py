import psycopg2 as pc

#variavel de controle
sair = False

#con com o bd
#con = pc.connect(dbname="py_crud_simples", user="postgres", password="admin")
#cur = con.cursor() #abertura do cursor para operacoes

def menu():
    esc = int(input('1 - Mostrar todos os usuarios\n2 - Pesquisar um usuario\n3 - Alterar um usuario\n4 - Adicionar um usuario\n5 - Excluir um usuario\n0 - Sair\n'))
    return esc

def mostrarTodos():
    con = pc.connect(dbname="py_crud_simples", user="postgres", password="admin")
    cur = con.cursor()

    cur.execute("SELECT * FROM usuario")
    res = cur.fetchall()

    for i in res:
        print(f"ID: {i[0]} Nome: {i[1]} Idade: {i[2]}")

    cur.close()
    con.close()

def pesquser():
    con = pc.connect(dbname="py_crud_simples", user="postgres", password="admin")
    cur = con.cursor()

    nome = str(input('Digite o nome do usuario\n'))

    cur.execute(f"select * from usuario where nome like '{nome}%'")

    res = cur.fetchall()

    for i in res:
        print(f"ID: {i[0]} Nome: {i[1]} Idade: {i[2]}")

    cur.close()
    con.close()

def altuser():
    con = pc.connect(dbname="py_crud_simples", user="postgres", password="admin")
    cur = con.cursor()

    id = int(input("Digite o ID do usuario que deseja alterar\n"))
    esc = int(input("1 - Para alterar nome\n2 - Para alterar idade\n"))
    if esc == 1:
        nnome = str(input("Digite o nome novo\n"))
        cur.execute(f"update usuario set nome = '{nnome}' where id = {id}")
        con.commit()
    elif esc == 2:
        nidade = int(input("Digite sua idade\n"))
        cur.execute(f"update usuario set idade = {nidade} where id = {id};")
        con.commit()
    else:
        print("Opcao invalida")

    cur.close()
    con.close()

def adduser():
    con = pc.connect(dbname="py_crud_simples", user="postgres", password="admin")
    cur = con.cursor()

    nnome = str(input("Digite o nome do novo usuario\n"))
    nidade = int(input("Digite a idade do novo usuario\n"))

    cur.execute(f"insert into usuario(nome, idade) values('{nnome}', {nidade})")
    con.commit()

    cur.close()
    con.close()

def deluser():
    con = pc.connect(dbname="py_crud_simples", user="postgres", password="admin")
    cur = con.cursor()

    id = int(input("Digite o id do usuario que deseja excluir\n"))

    cur.execute(f"delete from usuario where id = {id}")
    con.commit()

    cur.close()
    con.close()

#MAIN
while(sair!=True):
    esc = menu()

    if esc == 1:
        mostrarTodos()
    elif esc == 2:
        pesquser()
    elif esc == 3:
        altuser()
    elif esc == 4:
        adduser()
    elif esc == 5:
        deluser()
    elif esc == 0:
        sair = True
    else:
        print("Opcao invalida")
