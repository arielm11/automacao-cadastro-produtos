# Automação de Cadastro de Produtos com Python

Este projeto demonstra como automatizar o cadastro de produtos em um sistema utilizando Python, a biblioteca **PyAutoGUI** e uma base de dados. É ideal para tarefas repetitivas, como preenchimento de formulários, economizando tempo e reduzindo erros.

## 🚀 Objetivo
Automatizar o processo de cadastro de produtos de uma base de dados em um sistema web, simulando as ações humanas de interação com o computador.

## 🛠️ Funcionalidades
- Abrir o navegador e acessar o sistema.
- Realizar login automaticamente.
- Cadastrar produtos de forma automática, preenchendo informações como:
  - Código do produto
  - Marca
  - Tipo
  - Preço unitário
  - Custo
  - Observações
- Repetir o processo até cadastrar todos os produtos da base de dados.

## 📋 Pré-requisitos
Antes de começar, você precisará instalar as seguintes ferramentas:
- **Python 3.x**: [Instalar Python](https://www.python.org/)
- Biblioteca **pandas** para manipulação de dados:
  ```bash
  pip install pandas
  ```
- Biblioteca **PyAutoGUI** para manipulação de dados:
  ```bash
  pip install pyautogui
  ```

## 📁 Estrutura do Projeto
- `produtos.csv`: Base de dados com as informações dos produtos.
- `pegar_posicao.py`: Script para capturar a posição do mouse no monitor.
- `main.py`: Código principal da automação.

## 🔧 Como Usar
1. Clone este repositório:
  ```bash
  git clone https://github.com/seu-usuario/seu-repositorio.git
  cd seu-repositorio
  ```

2. Certifique-se de ter o arquivo produtos.csv no mesmo diretório do script.

3. Execute o script para capturar a posição do mouse:
  ```bash
  pip install pyautogui
  ```
  Use este script para obter as coordenadas dos cliques necessários para o cadastro.

4. Atualize as posições no código principal (`main.py`) com base nas coordenadas capturadas.

5. Execute o script principal:
  ```bash
  python main.py
  ```

## 🖥️ Tecnologias Utilizadas
- Python
- Pandas
- PyAutoGUI