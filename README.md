# 🚀 Backend FastAPI para Geração de QR Codes em Memória

Este projeto é uma API REST desenvolvida em **FastAPI** que tem como principal funcionalidade a **geração eficiente e segura de QR Codes** a partir de URLs fornecidas, utilizando a melhor prática de processamento **em memória**.

A arquitetura foi desenhada para ser limpa, escalável e de fácil manutenção, seguindo o padrão de Separação de Preocupações (Separation of of Concerns).

---

## 🏗️ Arquitetura do Projeto

O projeto utiliza uma estrutura modular, onde cada camada tem responsabilidades bem definidas:

| Pasta/Módulo | Responsabilidade | Tecnologia Chave |
| :--- | :--- | :--- |
| `app/models/` | Define a estrutura dos dados de entrada (Pydantic Schema). | `pydantic` |
| `app/routes/` | Recebe as requisições HTTP (`POST /qrcodes`) e chama o serviço. Atua como o "controlador". | `FastAPI.APIRouter` |
| `app/service/` | Contém a **lógica de negócio** principal: a geração do QR Code. Garante que o código seja reutilizável e fácil de testar. | `qrcode`, `io.BytesIO` |
| `main.py` | Ponto de entrada da aplicação. Inicializa o FastAPI e configura middlewares (e.g., CORS). | `FastAPI`, `uvicorn` |

### ✅ Boas Práticas Adotadas

1.  **Geração em Memória:** Os QR Codes são gerados e retornados usando `io.BytesIO` e `StreamingResponse`, garantindo que **nenhum arquivo seja salvo no disco** do servidor. Isso resolve questões éticas de privacidade e melhora o desempenho.
2.  **Separação de Preocupações:** A lógica de geração foi desacoplada da rota e isolada na camada de serviço (`service/qrcodes.py`).
3.  **CORS Configurado:** O middleware CORS está implementado no `main.py` para permitir a integração segura com um futuro *frontend*.
---

## 🚀 Endpoints da API

| Método | Rota | Descrição |
| :--- | :--- | :--- |
| `POST` | `/qrcodes/` | Gera um QR Code em PNG a partir de uma URL. |
| `POST` | `/qrcodes/ler-qrcode/` | Lê uma imagem enviada e retorna o conteúdo do QR Code em JSON. |
| `POST` | `/qrcodes/scan-and-redirect/` | Lê uma imagem e redireciona (303) se o conteúdo for um link. |

---


# Como Executar o Projeto

Este guia apresenta o passo a passo para rodar a aplicação de duas formas: localmente (sem Docker) e utilizando o Docker.

---

## 💻 Opção 1: Executando SEM Docker (Localmente)

Para executar o projeto diretamente na sua máquina, você precisará do Python (versão 3.11 ou superior recomendada) instalado.

### Passo 1: Abra o terminal no diretório do projeto
Navegue até a pasta raiz do projeto:
```bash
cd "c:\Users\pedro\Desktop\teste python\qrcodeapp\generate_qrcode_backend_fastapi_docker"
```

### Passo 2: Ative (ou crie) o Ambiente Virtual
O projeto já possui uma pasta `venv`. Para ativá-la no Windows:
```powershell
.\venv\Scripts\activate
```
*(Dica: Se der erro de permissão no PowerShell, execute `Set-ExecutionPolicy Unrestricted -Scope CurrentUser` e tente de novo).*

Se a pasta `venv` estiver com problemas ou vazia, recrie o ambiente virtual do zero:
```powershell
python -m venv venv
.\venv\Scripts\activate
```

### Passo 3: Instale as Dependências
Com o ambiente ativado (deve aparecer `(venv)` no seu terminal), instale os pacotes necessários:
```powershell
pip install -r app/requirements/development.txt
```

### Passo 4: Inicie o Servidor
Execute o servidor utilizando o Uvicorn na raiz do projeto:
```powershell
uvicorn app.main:app --reload
```

### Passo 5: Acesse a API
A API estará disponível nas seguintes URLs:
- **API (Base URL):** [http://127.0.0.1:8000](http://127.0.0.1:8000)
- **Documentação interativa (Swagger UI):** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

*(Para parar o servidor, pressione `Ctrl + C`. Para sair do ambiente virtual digite `deactivate`).*

---

## 🐳 Opção 2: Executando COM Docker

Executar com Docker garante que a aplicação rode em um ambiente isolado com todas as configurações idênticas, sem precisar instalar o Python ou configurar ambientes virtuais na sua máquina.

### Pré-requisitos
- Ter o [Docker](https://www.docker.com/products/docker-desktop) instalado e rodando.
- Ter o Docker Compose instalado (geralmente já vem com o Docker Desktop).

### Passo 1: Abra o terminal no diretório do projeto
Da mesma forma, navegue até a raiz:
```bash
cd "c:\Users\pedro\Desktop\teste python\qrcodeapp\generate_qrcode_backend_fastapi_docker"
```

### Passo 2: Construa e inicie o container
Execute o comando abaixo para que o Docker baixe as imagens, instale as dependências e inicie o projeto:
```bash
docker-compose up --build -d
```
*(O parâmetro `-d` faz com que o container rode em segundo plano).*

### Passo 3: Acesse a API
Conforme configurado no `docker-compose.yml`, o servidor interno rodará na porta `80`.
- **API (Base URL):** [http://localhost](http://localhost) (ou `http://127.0.0.1`)
- **Documentação interativa (Swagger UI):** [http://localhost/docs](http://localhost/docs)

### Comandos Úteis do Docker
- **Para ver os logs (caso haja algum erro):**
  ```bash
  docker-compose logs -f
  ```
- **Para parar a aplicação e os containers:**
  ```bash
  docker-compose down
  ```
