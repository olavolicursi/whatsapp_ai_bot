from langchain.chains import create_history_aware_retriever, create_retriever_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.runnables import RunnableWithMessageHistory
from langchain_openai import ChatOpenAI

from config import (
    OPENAI_MODEL_NAME,
    OPENAI_MODEL_TEMPERATURE,
)

from vectorstore import get_vectorstore
from prompts import contextualize_prompt, qa_prompt

def get_rag_chain():
    llm=ChatOpenAI(
        model_name=OPENAI_MODEL_NAME,
        temperature=OPENAI_MODEL_TEMPERATURE
    ),
    retriever = get_vectorstore().as_retriever()
    history_aware_chain = create_history_aware_retriever(llm, retriever, contextualize_prompt)
    question_answer_chain = create_stuff_documents_chain(llm, qa_prompt)

    return create_retriever_chain(history_aware_chain, question_answer_chain)