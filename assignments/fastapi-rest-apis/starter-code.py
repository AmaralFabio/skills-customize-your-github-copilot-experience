"""
FastAPI REST API Starter Code
Construindo APIs REST com framework FastAPI

Este arquivo contém o código inicial para a tarefa de FastAPI.
Você deve completar a implementação dos endpoints.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

# Inicializar a aplicação FastAPI
app = FastAPI(
    title="Gerenciador de Tarefas API",
    description="Uma API REST simples para gerenciar tarefas",
    version="1.0.0"
)

# Modelos Pydantic (schemas)
# TODO: Defina o modelo TaskCreate com os campos necessários
# class TaskCreate(BaseModel):
#     title: str
#     completed: bool = False

# TODO: Defina o modelo Task com todos os campos incluindo id
# class Task(BaseModel):
#     id: int
#     title: str
#     completed: bool


# Dados em memória (para fins de demonstração)
# Em uma aplicação real, você usaria um banco de dados
tasks_db: List[dict] = []
next_task_id = 1


# Rotas da API

@app.get("/tasks", response_model=List[dict])
def list_tasks():
    """
    Retorna a lista de todas as tarefas.
    
    Returns:
        List[dict]: Lista de tarefas
    """
    # TODO: Implemente esta rota
    return tasks_db


@app.post("/tasks", response_model=dict)
def create_task(task: dict):
    """
    Cria uma nova tarefa.
    
    Args:
        task (dict): Dados da tarefa a ser criada
        
    Returns:
        dict: A tarefa criada com id atribuído
    """
    # TODO: Implemente esta rota
    pass


@app.get("/tasks/{task_id}", response_model=dict)
def get_task(task_id: int):
    """
    Retorna uma tarefa específica pelo ID.
    
    Args:
        task_id (int): ID da tarefa
        
    Returns:
        dict: A tarefa encontrada
        
    Raises:
        HTTPException: Se a tarefa não for encontrada (404)
    """
    # TODO: Implemente esta rota
    pass


@app.put("/tasks/{task_id}", response_model=dict)
def update_task(task_id: int, updated_task: dict):
    """
    Atualiza uma tarefa existente.
    
    Args:
        task_id (int): ID da tarefa
        updated_task (dict): Dados atualizados da tarefa
        
    Returns:
        dict: A tarefa atualizada
        
    Raises:
        HTTPException: Se a tarefa não for encontrada (404)
    """
    # TODO: Implemente esta rota
    pass


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    """
    Deleta uma tarefa pelo ID.
    
    Args:
        task_id (int): ID da tarefa
        
    Returns:
        dict: Mensagem de confirmação
        
    Raises:
        HTTPException: Se a tarefa não for encontrada (404)
    """
    # TODO: Implemente esta rota
    pass


# Rota de teste
@app.get("/")
def read_root():
    """Rota de teste para verificar se a API está funcionando."""
    return {"message": "Bem-vindo ao Gerenciador de Tarefas API!"}
