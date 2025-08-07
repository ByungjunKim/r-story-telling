import gradio as gr
from langchain_community.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
import torch

# 벡터 DB
embeddings = HuggingFaceEmbeddings(model_name="jhgan/ko-sroberta-multitask")
vectorstore = FAISS.load_local("solo_leveling_faiss_ko", embeddings, allow_dangerous_deserialization=True)

# 모델 로딩
model_name = "kakaocorp/kanana-nano-2.1b-instruct"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.float16).to("cuda")
pipe = pipeline("text-generation", model=model, tokenizer=tokenizer, max_new_tokens=200)
lm = pipe

# 선택지
choices = [
    "1-1. 황동석 무리를 모두 처치한다.",
    "1-2. 황동석 무리와 진호를 포함하여 모두 처치한다.",
    "2. 황동석 무리를 기절시키고 살려둔다.",
    "3-1. 마정석을 들고 도망친다.",
    "3-2. 시스템을 거부하고 그냥 도망친다."
]

# RAG + 대사 생성 함수
def rag_answer(message, history):
    try:
        user_idx = int(message.strip()) - 1
        user_choice = choices[user_idx]
    except:
        return "❗올바른 번호를 입력해주세요. (예: 1 ~ 5)"

    docs = vectorstore.similarity_search(user_choice, k=3)
    context = "\n".join([doc.page_content for doc in docs])

    prompt = f"""
당신은 웹툰 '나 혼자만 레벨업'의 성진우입니다.

현재 상황:
{context}

사용자 선택: {user_choice}

성진우의 말투로 간결하고 자연스러운 대사를 1~2문장 생성하세요.
중복된 내용이나 비슷한 문장은 만들지 마세요.
"""
    response = lm(prompt)[0]["generated_text"]
    return response

# Gradio 인터페이스
demo = gr.ChatInterface(
    fn=rag_answer, 
    title="🔥 성진우 선택형 RAG 대사 생성기",
    description="1~5 중 번호를 입력하면 해당 선택에 따른 성진우의 대사를 생성합니다."
)
demo.launch(share=True)
