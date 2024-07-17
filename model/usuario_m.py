import mariadb
import sys

class UsuarioModel:
    def __init__(self, db_name='marcio_db', user='marcio_2182', password='2182', host='localhost', port=3306):
        try:
            self.conn = mariadb.connect(
                user=user,
                password=password,
                host=host,
                port=port,
                database=db_name
            )
        except mariadb.Error as e:
            print(f"Erro de conexão ao MariaDB: {e}")
            sys.exit(1)
       
        self.create_table()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(100) NOT NULL,
                idade INT
            )
        ''')
        self.conn.commit()

    def inserir_usuario(self, nome, idade):
        cursor = self.conn.cursor()
        try:
            cursor.execute('INSERT INTO usuarios (nome, idade) VALUES (?, ?)', (nome, idade))
            self.conn.commit()
        except mariadb.Error as e:
            print(f"Erro ao inserir usuário: {e}")

    def selecionar_usuarios(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM usuarios')
        return cursor.fetchall()

    def deletar_usuario(self, id):
        cursor = self.conn.cursor()
        cursor.execute('''
            DELETE FROM usuarios WHERE id = ?
        ''', (id,))
        self.conn.commit()
    def atualizar_usuario(self,id,nome,idade):
        cursor = self.conn.cursor()
        cursor.execute('''
            UPDATE usuarios
            SET nome = ?, idade = ?
            WHERE id = ?
        ''',(nome,idade,id,))
        self.conn.commit()

    def fechar_conexao(self):
        self.conn.close()