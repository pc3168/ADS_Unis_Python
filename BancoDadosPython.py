import sqlite3
from sqlite3 import Error

from numpy.distutils.command.config import config


def conexaoBD():
    nome_banco = "mmc.db"
    print(f'Criando BD Sqlite, {nome_banco}')
    conn = None
    try:
        conn = sqlite3.connect(nome_banco)
    except Error as e:
        print(f'Error: {e}')
    return conn


def criarTabela(conexao, sql):
    try:
        cur=conexao.cursor()
        cur.execute(sql)
    except Error as e:
        print(f'Error : {e}')

vsql="""CREATE TABLE IF NOT EXISTS mmc(
     ID INTEGER PRIMARY KEY AUTOINCREMENT,
     NOME VARCHAR(80),
     ENDERECO VARCHAR(80),
     ALTURA VARCHAR(5),
     PESO VARCHAR(5),
     INFO VARCHAR(30)
     )"""

def inserir(conexao, sql):
    try:
        cur=conexao.cursor()
        cur.execute(sql)
        conexao.commit()
    except Error as e:
        print(f'Error : {e}')

def inserirDados(conexao, nome, endereco,altura,peso,info):
    inserir(conexao, "INSERT INTO MMC(NOME, ENDERECO, ALTURA, PESO, INFO) VALUES ('"+nome+"','"+endereco+"','"+altura+"','"+peso+"','"+info+"')")


def fecharConexao(conn):
    if conn:
        conn.close()



#if __name__ == '__main__':
    #dbName = "C:\\teste\\mmc.db"
    #conn = conexaoBD()
    #criarTabela(conn, vsql)
    #fecharConexao(conn)
    #inserirDados(conn, "nome", "endereco","altura","peso","info")