# 📘 Assignment: Construindo APIs REST com FastAPI

## 🎯 Objective

Nesta tarefa, você aprenderá a construir APIs REST profissionais usando o framework FastAPI. Você implementará endpoints para operações CRUD (Create, Read, Update, Delete) com validação de dados, tratamento de erros e documentação automática.

## 📝 Tasks

### 🛠️ Tarefa 1: Criar uma API REST Básica

#### Description
Crie uma aplicação FastAPI básica com endpoints GET e POST para gerenciar uma lista de tarefas em memória. Os estudantes devem compreender como definir rotas, aceitar parâmetros e retornar respostas JSON.

#### Requirements
Completed program should:

- Implementar um endpoint GET `/tasks` que retorna a lista de todas as tarefas
- Implementar um endpoint POST `/tasks` que adiciona uma nova tarefa à lista
- Cada tarefa deve ter um `id`, `title` e `completed` status
- As tarefas devem ser armazenadas em uma lista Python em memória
- A aplicação deve executar sem erros com `uvicorn main:app --reload`


### 🛠️ Tarefa 2: Validação de Dados com Pydantic

#### Description
Adicione validação de dados robusta usando modelos Pydantic. Os estudantes devem aprender a definir schemas para validar entrada de dados e garantir consistência na API.

#### Requirements
Completed program should:

- Criar um modelo Pydantic `Task` com campos `id`, `title` e `completed`
- Criar um modelo Pydantic `TaskCreate` com apenas os campos necessários para criação
- Validar que `title` não está vazio e tem no máximo 255 caracteres
- Retornar erros HTTP 422 quando dados inválidos são enviados
- Usar modelos Pydantic para documentação automática


### 🛠️ Tarefa 3: Implementar Operações Completas CRUD

#### Description
Estenda a API para suportar todas as operações CRUD: Read (GET individual), Update (PUT) e Delete (DELETE). Os estudantes devem trabalhar com identificadores de recursos e manipulação de estado.

#### Requirements
Completed program should:

- Implementar endpoint GET `/tasks/{task_id}` para recuperar uma tarefa específica
- Implementar endpoint PUT `/tasks/{task_id}` para atualizar uma tarefa existente
- Implementar endpoint DELETE `/tasks/{task_id}` para deletar uma tarefa
- Retornar erro HTTP 404 quando uma tarefa não for encontrada
- Retornar a tarefa atualizada após operações PUT
- Cada tarefa deve manter um `id` único que persiste durante a sessão
