# 📄 Indexing Algorithm

Este repositório contém um projeto desenvolvido para simular um algoritmo de indexação de documentos, similar ao utilizado pelo Google. O programa é capaz de identificar ocorrências de termos em arquivos de texto (formato `.txt`), oferecendo funcionalidades de gerenciamento de arquivos e busca.

---

## 📝 Sobre o Projeto

O **Indexing Algorithm** é dividido em dois módulos principais:

1. **Módulo de Gerenciamento de Arquivos**:
   - Permite anexar arquivos de texto (formato `.txt`) ao sistema.
   - Garante o gerenciamento eficiente dos arquivos adicionados.

2. **Módulo de Buscas**:
   - Realiza operações de busca nos arquivos anexados.
   - Retorna as ocorrências dos termos pesquisados.

**Nota**: Este projeto não realiza análise de significados ou busca por sinônimos.

---

## 🚵 Habilidades Exercitadas

Durante o desenvolvimento deste projeto, as seguintes habilidades foram exercitadas:

- Manipulação de **Pilhas**;
- Manipulação de **Deque**;
- Manipulação de **Nós e Listas Ligadas**;
- Manipulação de **Listas Duplamente Ligadas**.

---

## 📂 Estrutura do Projeto

A estrutura do projeto está organizada da seguinte forma:

```plaintext
📁 statics/
   ├── arquivo_teste.csv               # Arquivo CSV de exemplo
   ├── arquivo_teste.txt               # Arquivo TXT de exemplo
   ├── nome_pedro.txt                  # Arquivo TXT de exemplo
   ├── novo_paradigma_globalizado-min.txt
   └── novo_paradigma_globalizado.txt  # Arquivos TXT adicionais

📁 tests/                              # Testes automatizados
   └── priority_queue/
       ├── __init__.py
       └── test_priority_queue.py      # Testes para filas de prioridade (não implementado)

📁 ting_file_management/
   ├── __init__.py
   ├── abstract_queue.py           # Estrutura de fila abstrata (não implementado)
   ├── file_management.py          # Gerenciamento de arquivos
   ├── file_process.py             # Processamento de arquivos
   ├── priority_queue.py           # Implementação de filas de prioridade
   └── queue.py                    # Implementação de filas

📁 ting_word_searches/
   ├── __init__.py
   └── word_search.py              # Funções de busca em arquivos
```

---

## 🛠️ Como Rodar o Projeto

1. Clone este repositório:

    ```bash
    git clone https://github.com/vicentevendramin/restaurant-orders.git
    cd restaurant-orders
    ```

2. Crie e ative um ambiente virtual:

    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    venv\Scripts\activate     # Windows
    ```

3. Instale as dependências:

    ```bash
    pip install -r requirements.txt # Production
    pip install -r dev-requirements.txt # Development
    ```

4. Execute os testes para verificar o funcionamento:

    ```bash
    pytest # Development
    ```