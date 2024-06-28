# Jogoteca Amiga

**Jogoteca Amiga** é uma biblioteca onde você e seus amigos podem salvar os jogos que zeraram, obter estatísticas sobre eles e ver quais jogos seus amigos completaram. 

## Funcionalidades

- **Adicionar jogos que você completou**: Mantenha um registro de todos os jogos que você já zerou.
- **Organizar jogos em pastas personalizadas**: Crie pastas para organizar seus jogos como preferir.
- **Categorizar jogos por plataforma**: Filtre e organize seus jogos por diferentes plataformas de jogo.
- **Buscar jogos e ver detalhes**: Utilize a barra de pesquisa para encontrar jogos e ver detalhes como capa e nome.
- **Ver jogos que seus amigos completaram**: Compartilhe sua biblioteca de jogos com amigos e veja quais jogos eles completaram.
- **Obter estatísticas gerais**: Visualize estatísticas gerais sobre sua biblioteca de jogos, como o número total de jogos completados, plataformas mais utilizadas, entre outras.

## Tecnologias Utilizadas

- **FastAPI**: Framework para construir APIs rápidas e eficientes.
- **Uvicorn**: Servidor ASGI para execução da aplicação FastAPI.
- **Requests**: Biblioteca para realizar requisições HTTP.
- **Jinja2**: Motor de templates para renderização de páginas HTML.
- **HTML/CSS**: Linguagens de marcação e estilo para o frontend.
- **JavaScript**: Utilizado para interatividade no frontend.

## Como Executar

1. Clone o repositório:

   ```bash
   git clone https://github.com/SEU_USUARIO/jogoteca-amiga.git
   cd jogoteca-amiga
   
2. Crie e ative um ambiente virtual (opcional, mas recomendado):
   ```bash
   pip install -r requirements.txt

4. Configure as credenciais da API no arquivo config.json
   ```bash
   {
    "client_id": "YOUR_CLIENT_ID",
    "client_secret": "YOUR_CLIENT_SECRET"
   }

6. Execute a aplicação
   ```bash
   uvicorn app.main:app --reload

8. Acesse a aplicação em http://127.0.0.1:8000.
