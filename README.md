# Projeto-REST
# Sistema de Críticas de Jogos

Este documento descreve a especificação inicial e a arquitetura do sistema de cadastro e avaliação de jogos. A solução é baseada em uma arquitetura de **microserviços**, dividindo as responsabilidades entre o processamento das interações dos usuários e a gerência dos projetos por parte dos criadores.

## 📌 Visão Geral do Sistema

* O servidor registra os jogos publicados na plataforma.
* Usuários autorizados (avaliadores) podem deixar suas impressões sobre os títulos.
* **Acesso Público:** Qualquer usuário (visitante ou autenticado) tem a permissão de visualizar a nota de um jogo.
* **Sistema de Feedback:** As avaliações são baseadas em um sistema de recomendação binária (Nota Positiva ou Nota Negativa).

---

## 🏗️ Arquitetura de Microserviços

O ecossistema do sistema é dividido atualmente em dois microserviços principais:

### 1. Microserviço de Interação
Responsável por toda a camada de engajamento social e processamento das avaliações dos usuários.
* **Público-alvo:** Usuários cadastrados como **Avaliadores**.
* **Funcionalidades:**
  * Avaliar jogos (atribuir nota positiva ou negativa).
  * Comentar nas páginas dos jogos.
  * Ler críticas e comentários de outros usuários.
  * Filtrar e buscar jogos com base em critérios de avaliação.

### 2. Microserviço de Gerência
Responsável pela administração do ciclo de vida dos jogos e do controle editorial por parte dos desenvolvedores.
* **Público-alvo:** Usuários cadastrados como **Publicadores**.
* **Funcionalidades:**
  * Cadastrar novos jogos no servidor.
  * Atualizar informações, dados técnicos e mídias dos jogos existentes.
  * Responder às críticas e comentários deixados pelos avaliadores em seus respectivos jogos.

---

## 🔒 Regras de Permissão (Matriz de Acessos)

| Ação | Visitante Anônimo | Usuário Avaliador | Usuário Publicador |
| :--- | :---: | :---: | :---: |
| Visualizar nota do jogo | ✅ | ✅ | ✅ |
| Filtrar e ler jogos/críticas | ❌ | ✅ | ✅ |
| Avaliar e comentar | ❌ | ✅ | ❌ |
| Cadastrar e atualizar jogos | ❌ | ❌ | ✅ (Apenas os próprios) |
| Responder críticas | ❌ | ❌ | ✅ (Apenas no próprio jogo) |
