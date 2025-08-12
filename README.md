
# 프로젝트 : Solo Leveling 선택지 시뮬레이션
---

## 사용 모델
- [`kakaocorp/kanana-nano-2.1b-instruct`](https://huggingface.co/kakaocorp/kanana-nano-2.1b-instruct)
---
## 실험 구성
### 1. 프롬프트 기반 실험 (Prompt-based)
- 목적: 동일한 상황에서 프롬프트를 변경하며, 성진우 캐릭터의 대사 생성과 선택 이유를 비교
- 진행 내용:
ep1_dongseok.tsv를 기반으로 버전별 프롬프트(v1~v21) 작성
각 버전마다: 선택지 제시 선택지별 대사와 이유 생성 & 최종 선택(번호 및 이유) 출력

### 2. RAG 기반 실험 (RAG-based)
- 목적: 전체 웹툰 대사 데이터에서 관련 장면을 검색해 프롬프트에 포함시킨 뒤, 주어진 선택지에 맞는 캐릭터 대사를 생성
- vectordb에서 관련 컨텍스트 검색 후 선택지
- 진행 내용:
sl_webtoon_full_data_sequential.tsv에서 대사만 필터링
대사 텍스트를 Ko-SBERT(jhgan/ko-sroberta-multitask) 임베딩으로 변환
FAISS 벡터DB 생성 및 저장 (index.faiss, index.pkl)
실험 시 사용자 선택지 입력 → 벡터DB에서 관련 대사 검색 → 검색 결과를 프롬프트에 포함 → 모델이 새로운 대사 생성
- 결과물:
선택지에 기반한 캐릭터 대사 생성까지 수행,  평가 지표 분석은 미진행 상태

##  디렉토리 구성

```
Solo_Leveling/
├── data/ # 공통 데이터
│ ├── sl_dialogue.tsv # 대사
│ ├── sl_personality.tsv # 성격 정보
│ ├── sl_situation.tsv # 상황 설명
│ └── sl_skill.tsv # 스킬 모음
│
├── episodes/ # 에피소드별 실험 관리
│ ├── ep1_dongseok/ # 1편: 황동석 편, 현재 ep1 만 실험 (Prompt-based)
│ │ ├── ep1_dongseok.tsv # 원본 TSV
│ │ ├── notes.md # 실험 버전별 메모
│ │ ├── prompts/ # 실험 프롬프트 (v1v14)
│ │ ├── results/ # 결과 (v1v14)
│ │ └── run.ipynb # 실험 실행 파일


├── data
│   ├── ngrok
│   ├── ngrok-stable-linux-amd64.zip
│   ├── rag_gradio2.py
│   ├── rag_gradio.py
│   ├── requirements.txt
│   ├── selection.ipynb
│   ├── sl_dialogue.tsv
│   ├── Sl_lizard.tsv
│   ├── sl_personality.tsv
│   ├── sl_situation.tsv
│   ├── sl_skill.tsv
│   ├── sl_webtoon_full_data_sequential.tsv
│   ├── sl_webtoon_full_data.tsv
│   ├── solo_leveling_faiss.index
│   ├── solo_leveling_faiss_ko.index
│   └── solo_leveling_texts.pkl
├── episodes
│   ├── ep1_dongseok #ep1 만 실험 완료
│   │   ├── context
│   │   │   └── ep1_context.ipynb
│   │   ├── ep1_dongseok.tsv
│   │   ├── ep1_lizard.tsv
│   │   ├── notes.md #메모
│   │   ├── prompts #버전별 기록 
│   │   ├── results #버전별 기록
│   │   └── run.ipynb #prompt & result 실행 파일 
│   ├── ep2_hidden
│   └── ep3_job_quest
│    
├── evaluation  # 평가 지표/후속 분석 예정
├── inference
│   └── sl_choice_simulation.ipynb # 초기 실험 (prompt_output 관련 파일 ), 이후 에피소드별로 실험
├── prompt_output # 초기 실험 
│   ├── ep1_dongseok_result.md
│   ├── ep2_hidden_result.md
│   └── ep3_job_quest_result.md
├── README.md
└── sl_selection  #rag_based 
    ├── jinwoo_faiss
    │   ├── index.faiss
    │   └── index.pkl
    ├── r-story-test.ipynb
    ├── sl_selection.ipynb
    ├── sl_webtoon_full_data_sequential.tsv
    └── solo_leveling_faiss_ko
        ├── index.faiss
        └── index.pkl
```

---

## 에피소드 정리

| 에피소드 | 설명 |
|----------|------|
| **ep1: 황동석 편** | 긴급 퀘스트 발생 → 적을 모두 처치할 것인가? |
| **ep2: 히든 퀘스트 편** | 일일 퀘스트 이후 히든 퀘스트 발생 → 랜덤 박스 선택 |
| **ep3: 전직 퀘스트 편** | 히든 클래스 ‘네크로맨서’ 전직 여부 선택 |

---
