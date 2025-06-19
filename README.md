# API de Produtos de Petshop

Esta é uma API simples para cadastro e listagem de produtos de petshop, desenvolvida em Flask e utilizando SQLite como banco de dados.

## Requisitos

- Python 3.8+
- pip

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/MonicaAlvesP/api_produtos_petshop.git
   cd backend_produtos
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Certifique-se de que o arquivo `database.db` está presente na raiz do projeto.  
   Caso não esteja, ele será criado automaticamente ao rodar a aplicação.

4. (Opcional) Crie um arquivo `.env` para variáveis de ambiente:
   ```env
   DEBUG_MODE=False
   ```

## Como rodar

```bash
python app.py
```

A API estará disponível em:  
http://localhost:5000

## Endpoints

### `POST /cadastrar`

Cadastra um novo produto.

**Body (JSON):**
```json
{
  "titulo": "Ração Premium para Cães Adultos",
  "descricao": "Ração completa e balanceada para cães adultos de todas as raças. Sabor carne, 15kg.",
  "preco": 129.90,
  "image_url": "https://exemplo.com/imagens/racao-caes.jpg"
}
```

### `GET /`

Lista todos os produtos cadastrados.

---

### Exemplo de configuração segura no `.env`:
```env
DEBUG_MODE=False
```

E no seu código, converta o valor para booleano:
```python
debug_mode = os.getenv('DEBUG_MODE', 'False').lower() == 'true'
app.run(debug=debug_mode)
```

---

## Exemplo de uso com curl

Cadastrar produto de petshop:
```bash
curl -X POST http://localhost:5000/cadastrar \
-H "Content-Type: application/json" \
-d '{"titulo":"Ração Premium para Cães Adultos","descricao":"Ração completa e balanceada para cães adultos de todas as raças. Sabor carne, 15kg.","preco":129.90,"image_url":"https://exemplo.com/imagens/racao-caes.jpg"}'
```

Listar produtos:
```bash
curl http://localhost:5000/
```

---

## Licença

Este projeto é livre para fins de estudo e uso pessoal.
