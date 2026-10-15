
# Projeto-REST

# Sistema de Críticas de Jogos

Este documento descreve a especificação inicial e a arquitetura do sistema de cadastro e avaliação de jogos. A solução é baseada em uma arquitetura de **microserviços**, orquestrada por um **API Gateway** e consumida por uma **Aplicação Cliente Web**.

## 📌 Visão Geral do Sistema

- O servidor registra os jogos publicados na plataforma.
- Usuários autorizados (avaliadores) podem deixar suas impressões sobre os títulos.
- **Acesso Público:** Qualquer usuário (visitante ou autenticado) tem a permissão de visualizar a nota de um jogo.
- **Sistema de Feedback:** As avaliações são baseadas em um sistema de recomendação binária (Nota Positiva ou Nota Negativa).

## 🏗️ Arquitetura do Sistema

O ecossistema é estruturado em uma arquitetura desacoplada e escalável, utilizando uma interface frontend, um ponto único de entrada (API Gateway) e microserviços especializados na camada de backend.

```text
               ┌────────────────────────┐
               │ Aplicação Cliente Web  │
               └───────────┬────────────┘
                           │ (HTTP / REST / JWT)
                           ▼
               ┌────────────────────────┐
               │      API Gateway       │
               └────┬──────────────┬────┘
                    │              │
      ┌─────────────┘              └─────────────┐
      ▼                                          ▼
┌────────────────────────┐            ┌────────────────────────┐
│ Microserviço Gerência  │            │ Microserviço Interação │
└────────────────────────┘            └────────────────────────┘
```

## 1. Aplicação Cliente (Web)

Interface gráfica interativa desenvolvida para ser utilizada pelos usuários finais no navegador.

- **Público-alvo:** Visitantes, Avaliadores e Publicadores.
- **Funcionalidades:**
  - **Cadastro e Autenticação:** Permite que novos usuários façam seu cadastro na plataforma (definindo seu perfil de uso) e realizem login para obter seus tokens de acesso.
  - **Interface Dinâmica:** Adapta a visualização e formulários de acordo com o perfil do usuário (exibe telas de avaliação para Avaliadores e gerenciador de catálogo para Publicadores).
  - **Consumo de APIs:** Realiza requisições HTTP/REST direcionadas exclusivamente ao **API Gateway**, abstraindo a complexidade do backend.

## 2. API Gateway

Atua como o ponto único de entrada (*Single Point of Entry*) para todas as chamadas vindas da aplicação cliente.

- **Responsabilidades:**
  - **Roteamento de Requisições:** Direciona o tráfego de entrada para o microserviço correspondente com base no *endpoint* chamado (ex.: envia requisições de `/api/v1/jogos` para o Microserviço de Gerência e de `/api/v1/avaliacoes` para o de Interação).
  - **Autenticação e Autorização Centralizada:** Valida os tokens de segurança (como JWT) enviados pelo cliente web antes de repassar a requisição aos microserviços internos.
  - **Recursos Cross-Cutting:** Gerencia políticas de CORS (*Cross-Origin Resource Sharing*), limite de taxa de requisições (*Rate Limiting*) e padronização de respostas/erros.

## 3. Microserviço de Interação

Responsável por toda a camada de engajamento social e processamento das avaliações dos usuários.

- **Público-alvo:** Usuários cadastrados como **Avaliadores**.
- **Funcionalidades:**
  - Avaliar jogos (atribuir nota positiva ou negativa).
  - Comentar nas páginas dos jogos.
  - Ler críticas e comentários de outros usuários.
  - Filtrar e buscar jogos com base em critérios de avaliação.

## 4. Microserviço de Gerência

Responsável pela administração do ciclo de vida dos jogos e do controle editorial por parte dos desenvolvedores.

- **Público-alvo:** Usuários cadastrados como **Publicadores**.
- **Funcionalidades:**
  - Cadastrar novos jogos no servidor.
  - Atualizar informações, dados técnicos e mídias dos jogos existentes.
  - Responder às críticas e comentários deixados pelos avaliadores em seus respectivos jogos.

## 🔒 Regras de Permissão (Matriz de Acessos)

| Ação | Visitante Anônimo | Usuário Avaliador | Usuário Publicador |
|---|---|---|---|
| Cadastrar-se na aplicação web | ✅ | ✅ | ✅ |
| Visualizar nota do jogo | ✅ | ✅ | ✅ |
| Filtrar e ler jogos/críticas | ❌ | ✅ | ✅ |
| Avaliar e comentar | ❌ | ✅ | ❌ |
| Cadastrar e atualizar jogos | ❌ | ❌ | ✅ (Apenas os próprios) |
| Responder críticas | ❌ | ❌ | ✅ (Apenas no próprio jogo) |
