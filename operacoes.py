from sqlalchemy import select

from models import Livro


def emprestar_livro(session, titulo):
    """Marque um livro como indisponível."""
    # TODO: busque o livro pelo título.
    livros = session.scalars(select(Livro).where(Livro.titulo == titulo)).all()
    
    # TODO: se o livro não existir, exiba uma mensagem.
    # TODO: se já estiver indisponível, exiba uma mensagem.
    # TODO: se estiver disponível, altere disponivel para False e faça commit.
    
    for livro in livros:
        if not livro:
            print('Livro inexistente.')
        else:
            if livro.disponivel == False:
                print('Livro indisponível.')
            else:
                livro.disponivel = False
                session.commit()
                print(f'Livro {livro.titulo} emprestado.')

def devolver_livro(session, titulo):
    """Marque um livro como disponível."""
    # TODO: busque o livro pelo título.
    livros = session.scalars(select(Livro).where(Livro.titulo == titulo)).all()
    
    # TODO: se o livro não existir, exiba uma mensagem.
    # TODO: se já estiver disponível, exiba uma mensagem.
    # TODO: se estiver indisponível, altere disponivel para True e faça commit.
    
    for livro in livros: 
        if not livro:
            print('Livro inexistente.')
        else:
            if livro.disponivel == True:
                print('Livro já está disponível.')
            else:
                livro.disponivel = True
                session.commit()
                print(f'Livro {livro.titulo} devolvido.')
