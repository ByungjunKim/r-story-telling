

# 프로젝트 : Solo Leveling 선택지 시뮬레이션

## 사용 모델
- [`kakaocorp/kanana-nano-2.1b-instruct`](https://huggingface.co/kakaocorp/kanana-nano-2.1b-instruct)

---

## 실험 구성

### 1. 프롬프트 기반 실험 (Prompt-based)
- **목적**: 동일한 상황에서 프롬프트를 변경하며, 성진우 캐릭터의 대사 생성과 선택 이유를 비교
- **진행 내용**:
  - `ep1_dongseok.tsv`를 기반으로 버전별 프롬프트(v1~v21) 작성
  - 각 버전마다:
    1. 선택지 제시
    2. 선택지별 대사와 이유 생성
    3. 최종 선택(번호 및 이유) 출력

---

### 2. RAG 기반 실험 (RAG-based)
- **목적**: 전체 웹툰 대사 데이터에서 관련 장면을 검색해 프롬프트에 포함시킨 뒤, 주어진 선택지에 맞는 캐릭터 대사를 생성
- **진행 내용**:
  1. `sl_webtoon_full_data_sequential.tsv`에서 대사만 필터링
  2. Ko-SBERT(`jhgan/ko-sroberta-multitask`) 임베딩으로 변환
  3. FAISS 벡터DB 생성 및 저장 (`index.faiss`, `index.pkl`)
  4. 실험 시 사용자 선택지 입력 → 관련 대사 검색 → 프롬프트 포함 → 모델이 새로운 대사 생성
- **결과물**:
  - 선택지 기반 캐릭터 대사 생성까지 수행  
  - 평가 지표 분석은 미진행 상태
#### 데이터 처리 흐름
![RAG Data Flow](images/image%20(2).png)

## 디렉토리 구성

```

Solo\_Leveling/
├── data/                   # 공통 데이터 및 RAG 관련 파일
│   ├── sl\_dialogue.tsv
│   ├── sl\_personality.tsv
│   ├── sl\_situation.tsv
│   ├── sl\_skill.tsv
│   ├── sl\_webtoon\_full\_data\*.tsv
│   ├── \*.faiss / *.pkl
│   ├── rag\_gradio*.py
│   └── selection.ipynb
│
├── episodes/               # 에피소드별 프롬프트 기반 실험
│   ├── ep1\_dongseok/
│   │   ├── ep1\_dongseok.tsv
│   │   ├── notes.md
│   │   ├── prompts/        # 버전별 프롬프트
│   │   ├── results/        # 버전별 결과
│   │   └── run.ipynb
│   ├── ep2\_hidden/
│   └── ep3\_job\_quest/
│
├── prompt\_output/           # 초기 프롬프트 실험 결과
├── inference/               # 초기 실행 
├── sl\_selection/             # RAG 기반 실험
│   ├── sl\_selection.ipynb
│   ├── jinwoo\_faiss/         # FAISS 인덱스
│   └── solo\_leveling\_faiss\_ko/
│
├── evaluation/               # 평가 지표/후속 분석 예정
└── README.md

```
---

## 에피소드 설명

| 에피소드 | 설명 |
|----------|------|
| **ep1: 황동석 편** | 긴급 퀘스트 발생 → 적을 모두 처치할 것인가? |
| **ep2: 히든 퀘스트 편** | 일일 퀘스트 이후 히든 퀘스트 발생 → 랜덤 박스 선택 |
| **ep3: 전직 퀘스트 편** | 히든 클래스 ‘네크로맨서’ 전직 여부 선택 |
