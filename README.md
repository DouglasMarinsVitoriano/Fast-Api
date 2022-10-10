# FastApi


## Criando o embiente virtual (venv) no Windows

Caso esteja no windows, rode o comando a seguir na raiz do projeto para criar o ambiente, caso não tenha criado antes:
```

python -m venv "seu_projeto"
```
Caso esteja utilizando o PowerShell, ative com o comando abaixo:
```

seu_projeto\Scripts\Activate.ps1
```

Caso o PowerShell bloquei seu venv, clique com o botão direito no menu Windows e clique em Windowns PowerShell(Admin) e digite o comando:
```

Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

Se necessário desativar seu venv, digite no PowerShell:
```

deactivate
```

## Instalando as dependências

Utilize o pip para baixar as dependências do projeto:

```
pip install -r requirements.txt
```
Se precisar verificar as dependências instaladas:
```

pip freeze
```
Se necessario atualizar suas dependêncisa no decorrer do seu projeto:
```
pip freeze > requeriments.txt
```

## Execução

Para executar o projeto, utilize o comando abaixo na raiz do projeto:

```
uvicorn main:app --reload 
```

Para gerar um arquivo SQLite com as tabelas do projeto, rode o script cria_tabelas.py  

```
python cria_tabelas.py    
```

## Testes

Para executar os testes rode no PowerShell do Windowns

```
python -m pytest tests/
```

## Métodos de requisição 
```
POST
Método usado para enviar informações ao servidor, é utilizado de forma mais popular em cadastros de dados
retirados de um formulário, e também quando enviamos um arquivo para o servidor: 
seja isso uma foto de perfil, um post no Instagram, tudo isso é usado o método POST.
```
```
PUT
O PUT é responsável por editar arquivos e informações já existentes. E
sse método usa-se juntamente com um parâmetro na URL da requisição, 
que ajudará a identificar através de uma chave única (id) qual elemento ele está referenciando.
```
```
DELETE
Esse método é bem autoexplicativo, deleta arquivos ou informações presentes no banco de dados. 
Igual o PUT, é recomendável que utilize-o usando um parâmetro na URL da requisição, 
para que evite problemas de deletar dois arquivos/informações ao mesmo tempo
```
```
HEAD
Esse método é muito similar com o GET, a diferença é que esse retorna apenas o cabeçalho da resposta, 
enquanto o GET retorna tanto o cabeçalho quanto o corpo da resposta.
```
```
OPTIONS
É responsável por retornar as informações referentes ao servidor. 
Esse método é muitíssimo importante para ferramentas de deploy como o Heroku, pois ele pega todas as 
informações necessárias para o deploy de forma automática por meio desse método, o que facilita 
a vida do programador.
```
```
TRACE
Funciona bem mais como uma ferramenta de debug para as API‘s. 
Ele reenvia a última requisição para o servidor e verifica se houve alguma interferência 
de servidores de terceiros.
```
```
CONNECT
Dentre os métodos, esse é o mais específico e impopular, é responsável por conectar a API 
com algum servidor proxy. É mais utilizado para tentar a conexão com sites que possuem segurança e que não
permitem conexão direta, dessa forma, é preciso que se conecte a um servidor proxy para depois conseguir 
acessar seu destino.
```


Para consultar a documentação da API, acesse http://localhost:8000/docs e para interomper a execução pressione «Ctrl»+«C».
