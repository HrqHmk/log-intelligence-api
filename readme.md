# 🚀 Log Intelligence API

API para registro e análise de logs de requisições HTTP, permitindo monitorar métricas como latência, taxa de erro e percentis (p95).

Projeto desenvolvido com foco em observabilidade, organização de dados e análise de performance de serviços.

---

## 📌 Sobre o projeto

Esta API permite registrar logs detalhados de requisições HTTP e gerar métricas importantes para monitoramento de sistemas distribuídos.

Com ela, é possível analisar:

- Latência média por endpoint
- Taxa de erro por serviço
- Percentil 95 (p95) de latência
- Detecção de Anomalias por serviço

---

## 🛠️ Tecnologias utilizadas

- Python
- FastAPI
- SQLAlchemy (assíncrono)
- PostgreSQL
- Docker
- Pytest
- Scikit-learn

---

## ⚙️ Funcionalidades

- [x] Registro de logs de requisições HTTP
- [x] Cálculo de latência média por endpoint
- [x] Cálculo de taxa de erro por serviço
- [x] Cálculo de p95 de latência
- [x] Detecção de anomalias por serviço
- [ ] Autenticação
- [ ] Melhorias de performance
- [ ] Observabilidade avançada

---

## 🔗 Endpoints

| Método | Rota | Descrição |
|------|------|----------|
| POST | /request-logs | Registra um novo log |
| GET | /request-logs/average-latency/{endpoint} | Latência média |
| GET | /request-logs/error-rate/{service} | Taxa de erro |
| GET | /request-logs/p95-latency/{service} | p95 de latência |
| GET | /request-logs/anomalies/{service} | Detecta anomalias nos logs do serviço |

---

## 📥 Exemplo de uso

### Criar log

```json
POST /request-logs

{
  "timestamp": "2024-06-01T12:00:00Z",
  "http_method": "GET",
  "headers": {"Content-Type": "application/json"},
  "service": "user-service",
  "endpoint": "/api/v1/users",
  "request_body": {"id": 1},
  "response_body": {"name": "John Doe"},
  "response_time_ms": 150,
  "status_code": 200,
  "user_id": "123e4567-e89b-12d3-a456-426614174000",
  "request_id": "123e4567-e89b-12d3-a456-426614174001",
  "client_ip": "192.168.1.1",
  "error_message": null
}
```
---

### Detectar anomalias por serviço
```json
GET /request-logs/anomalies/user-service
```
### Resposta Esperada
```json
[
  {
    "response_time_ms": 5000,
    "status_code": 500,
    "anomaly_score": -0.21,
    "is_anomaly": true
  }
]
```
---
## 🤖 Inteligência Artificial aplicada

A funcionalidade de detecção de anomalias utiliza o algoritmo Isolation Forest, capaz de identificar comportamentos incomuns em logs com base em padrões como:

* Tempo de resposta elevado
* Status code fora do padrão
* Requisições discrepantes em relação ao histórico

---
### Como rodar o projeto

Siga os passos abaixo para executar a API localmente

## ▶️ Como rodar o projeto

``` bash
git clone <repo>
cd <repo>
```

## ▶️ Subir Banco com Docker


``` bash
docker-compose up -d
```

## ▶️ Configurar variáveis de ambiente

``` bash
cp .env.example .env
```


## ▶️ Instalar Dependências

``` bash
pip install -r requirements.txt
```
---

## ▶️ Rodar Aplicação

``` bash
python run.py
```
---