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



