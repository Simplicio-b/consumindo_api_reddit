### Projeto analisando api do reddit

#### Pré-requisitos

##### Tecnicos
    * Python
    * Jupyter 
    * NodeJS (Não obrigatorio) 
##### Requisitos não tecnicos
    * Conta no reddit
    * Gerar uma chave no reddit
    
#### Como gerar uma chave na API do reddit

Primeiro vá até o a [pagina de apps do reddit](https://old.reddit.com/prefs/apps/) então seguia os passos abaixo. 
![Print pagina da api](https://raw.githubusercontent.com/Simplicio-b/consumindo_api_reddit/master/imgs/cadastrar_key.png).

Preencha todos os campos marcados com vermelhor e então voce obterar os dados como mostra a imagem a seguir. 

![Print pagina da api](https://raw.githubusercontent.com/Simplicio-b/consumindo_api_reddit/master/imgs/sucesso-ao-cadastrar-key.png).

#### Como rodar o projeto

Ao baixar o repositorio em sua maquina, basta entrar no mesmo via termina e executar o comando abaixo.

```
jupyter notebook
```

O projeto iriar iniciar e a depender de suas configurações, você tera acesso ao mesmo, na url abaixo.

```
http://localhost:8888/tree
```

A maior parte dos notebooks vão funcionar, menos os que chamam o endpoint privado do reddit,
para que esté funcione você precisa renomear o arquivo <b>env_qa.py</b> para <b>env.py</b>, e adicionar nele todoas as chaves obtidas no passo <b>Como gerar uma chave na API do reddit</b>,
feito isso o projeto estará funcionando. 