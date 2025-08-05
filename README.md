# Documentação do Projeto WhatsApp AI Bot

## Visão Geral

Este projeto implementa um bot de inteligência artificial para WhatsApp, utilizando técnicas de RAG (Retrieval-Augmented Generation) para responder perguntas com base em documentos fornecidos (PDFs e textos). O sistema utiliza o LangChain, OpenAI e ChromaDB para processamento de linguagem natural, armazenamento vetorial e recuperação de informações.

---

## Estrutura de Diretórios

.env                      # Variáveis de ambiente
.gitattributes, .gitignore
app.py                    # Ponto de entrada principal do bot
chains.py                 # Cadeias de processamento RAG e conversacional
config.py                 # Configurações globais do projeto
docker-compose.yml, Dockerfile
evolution_api.py          # API de evolução (não detalhado)
LICENSE                   # Licença MIT
memory.py                 # Gerenciamento de histórico de sessões
message_buffer.py         # Buffer de mensagens (não detalhado)
prompts.py                # Prompts customizados para LLM
requirements.txt          # Dependências do projeto
transcribe_audio.py       # Transcrição de áudio (não detalhado)
vectorstore.py            # Carregamento de documentos e armazenamento vetorial
rag_files/                # Arquivos para RAG (PDFs, textos)
vectorstore_data/         # Dados persistidos do ChromaDB

---

## Principais Componentes

1. app.py

Arquivo principal do bot. Inicializa o sistema, integra os módulos e gerencia a comunicação com o WhatsApp.

2. chains.py

Define as cadeias de processamento para RAG e conversação:

- get_rag_chain: Cria uma cadeia de recuperação baseada em documentos.
- get_conversational_rag_chain: Cria uma cadeia que utiliza histórico de mensagens para respostas contextuais.

Utiliza:
- LangChain (create_history_aware_retriever, create_retrieval_chain)
- Prompts customizados de prompts.py
- Histórico de sessão de memory.py
- Vetorstore de vectorstore.py

3. vectorstore.py

Gerencia o armazenamento vetorial e o carregamento de documentos:

- load_documents: Carrega arquivos PDF e TXT de rag_files, move para rag_files/processed após processamento.
- get_vectorstore: Cria ou carrega o banco vetorial ChromaDB com embeddings OpenAI.

Utiliza:
- PyPDFLoader e TextLoader para leitura de arquivos.
- RecursiveCharacterTextSplitter para dividir documentos em chunks.
- Chroma para armazenamento vetorial.

4. config.py

Armazena configurações globais, como nomes de modelos, temperatura do modelo, caminhos de diretórios, etc.

5. memory.py

Gerencia o histórico de sessões para conversas contextuais.

6. prompts.py

Define prompts customizados para contextualização e perguntas/respostas.

---

## Como Funciona

1. Carregamento de Documentos: Coloque arquivos PDF ou TXT em rag_files. Eles serão processados e movidos para rag_files/processed.
2. Indexação Vetorial: Os documentos são divididos em chunks e indexados no ChromaDB usando embeddings da OpenAI.
3. Recuperação e Geração: O bot utiliza cadeias RAG para buscar informações relevantes nos documentos e gerar respostas usando LLMs.
4. Conversação Contextual: O histórico de mensagens é utilizado para manter contexto em conversas prolongadas.

---

## Como Executar

1. Instale as dependências:
    pip install -r requirements.txt

2. Configure variáveis no .env.

3. Execute o bot:
    python app.py

4. (Opcional) Use Docker:
    docker-compose up --build

---

## Licença

Este projeto está sob a Licença MIT.

---

## Referências de Código

- Cadeias RAG: get_rag_chain, get_conversational_rag_chain
- Carregamento de documentos: load_documents
- Vetorstore: get_vectorstore
- Configurações: config.py
- Prompts: prompts.py
- Histórico: memory.py

---

## Observações

- Para adicionar novos documentos, coloque-os em rag_files.
- O banco vetorial é persistido em vectorstore_data.
- O projeto pode ser expandido para outros tipos de arquivos e integrações.

