from models import Autor, Livro


def popular_banco(session):
    """Cadastre autores e livros iniciais para testar a aplicação."""
    
    # TODO: crie pelo menos 3 autores.
    autor1 = Autor(nome='Suzanne Collins', pais='EUA')
    autor2 = Autor(nome='Machado de Assis', pais='Brasil')
    autor3 = Autor(nome='Clarice Lispector', pais='Brasil')
    
    # TODO: crie pelo menos 6 livros.
    # TODO: inclua livros disponíveis e indisponíveis.
    livro1 = Livro(titulo='Jogos Vorazes', ano=2008, disponivel=True, autor_id=1)
    livro2 = Livro(titulo='Dom Casmurro', ano=1899, disponivel=False, autor_id=2)
    livro3 = Livro(titulo='Perto do Coração Selvagem', disponivel=True, ano=1943, autor_id=3)
    livro4 = Livro(titulo='Em Chamas', ano=2009, disponivel=False, autor_id=1)
    livro5 = Livro(titulo='Memórias Póstumas de Brás Cubas', disponivel=True, ano=1881, autor_id=2)
    livro6 = Livro(titulo='A Hora da Estrela', ano=1977, disponivel=False, autor_id=3)
  
    # TODO: use session.add ou session.add_all e finalize com session.commit().     
    session.add_all([autor1, autor2, autor3, livro1, livro2, livro3, livro4, livro5, livro6])
    session.commit()
