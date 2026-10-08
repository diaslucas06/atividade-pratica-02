from sqlalchemy import select

from models import Autor, Livro


def listar_livros(session):
    """Liste todos os livros com o nome do autor e o status de disponibilidade."""
    # TODO: use select(Livro) e acesse livro.autor.nome.
    
    livros = session.scalars(select(Livro)).all()
    for livro in livros:
        if livro.disponivel:
            status = 'Disponível'
        else:
            status = 'Não disponível'
            
        print(f"Livro: {livro.titulo}")
        print(f"Autor: {livro.autor.nome}")
        print(f"Status: {status}")


def listar_livros_disponiveis(session):
    """Liste apenas os livros disponíveis."""
    # TODO: filtre Livro.disponivel igual a True.
    livros = session.scalars(select(Livro).where(Livro.disponivel == True))
    for livro in livros:
        print(f"Livro: {livro.titulo}")


def buscar_livros_por_titulo(session, trecho):
    """Busque livros por parte do título."""
    # TODO: use contains ou like no título.
    livros = session.scalars(select(Livro).where(Livro.titulo.like(f"%{trecho}%")))
    for livro in livros:
        print(f"Livro: {livro.titulo}")

def listar_livros_por_autor(session, nome_autor):
    """Liste os livros de um autor informado pelo nome."""
    # TODO: busque o autor e navegue por autor.livros.
    autores = session.scalars(select(Autor).where(Autor.nome == nome_autor))
    for autor in autores:
        for livro in autor.livros:
            print(f"Livro: {livro.titulo}")
