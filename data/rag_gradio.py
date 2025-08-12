# rag_gradio.py

import gradio as gr
import torch
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.prompts import PromptTemplate
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from langchain_community.llms import HuggingFacePipeline

# 🔹 1. 벡터DB 로드
embeddings = HuggingFaceEmbeddings(model_name="jhgan/ko-sroberta-multitask")
vectorstore = FAISS.load_local("solo_leveling_faiss_ko", embeddings, allow_dangerous_deserialization=True)

# 🔹 2. Kanana 모델 로드
model_name = "kakaocorp/kanana-nano-2.1b-instruct"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.float16).to("cuda")
pipe = pipeline("text-generation", model=model, tokenizer=tokenizer, max_new_tokens=512)
llm = HuggingFacePipeline(pipeline=pipe)

# 🔹 3. 프롬프트 템플릿 정의
template = """
다음은 배경 지식입니다:
{context}

사용자 질문:
{question}

친절하고 정확하게 한국어로 답변해 주세요.
"""
prompt = PromptTemplate(input_variables=["context", "question"], template=template)

def rag_answer(message, history):
    docs = vectorstore.similarity_search(message, k=3)
    context = "\n".join([doc.page_content for doc in docs])
    final_prompt = prompt.format(context=context, question=message)
    response = llm(final_prompt)
    return response


# 🔹 5. Gradio 인터페이스 정의
demo = gr.ChatInterface(fn=rag_answer, title="🧠 Kanana 기반 RAG 질의응답")
demo.launch(share=True)  # 🔗 외부 접속 주소 자동 생성
