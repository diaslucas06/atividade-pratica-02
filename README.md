# Atividade Prática 02 - Biblioteca Persistente

Complete os arquivos da base usando SQLAlchemy ORM.

## Como executar

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python main.py
```

## Defesa escrita

Responda ao final:

### 1. Para que serve o campo `disponivel` em `Livro`?
Para fazer o empréstimo e a devolução de livros, verificando se ele já foi emprestado e ou se está disponível para o usuário pegá-lo.

### 2. Por que é necessário chamar `session.commit()` após emprestar ou devolver?
Para adicionar as alterações em **livro.disponivel** no banco de dados, caso contrário, o banco não será atualizado e o livro não será marcado como emprestado/devolvido, fazendo com que um livro que era para estar indisponível possa ser pego e que um livro que era para estar disponível não possa ser emprestado.

### 3. Em qual consulta você usa o relacionamento entre `Livro` e `Autor`?
Na consulta **listar_livros_por_autor**, que pega o autor e mostra seus livros, que foram salvos por meio do relationship e back_populates.
