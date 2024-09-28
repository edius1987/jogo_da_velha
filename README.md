# Jogo da Velha em Flet

Aqui está um simples código em Python que implementa o jogo da velha usando a biblioteca Flet.
As principais partes do código:

Importamos a biblioteca Flet.
Criamos uma classe JogoDaVelha que gerencia a lógica do jogo.
A função main configura a interface gráfica usando Flet.
Criamos botões para representar cada célula do tabuleiro.
Implementamos a lógica para alternar entre jogadores e verificar vitórias.

Criamos o projeto com o `Poetry` com o comando `poetry new jogo_da_velha`, acessamos o projeto pelo terminal e instalamos a biblioteca `Flet` pelo comando `poetry add flet` com esse comandos já está pronto o ambiente de trabalho.
```bash
.
├── app.py
├── jogo_da_velha
│  ├── __init__.py
├── poetry.lock
├── pyproject.toml
├── README.md
└── tests
   └── __init__.py
```

Logo temos que escrever o código, que pode ser feito por qualquer editor de texto ou código, eu usei o `nano`, mas use o editor que mais for confortável programar, pela integração sugerimos o Pycharm que tem uma excelente integração com o Poetry.

![](/jogo_da_velha.png)
