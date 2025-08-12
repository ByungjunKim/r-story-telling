
# 프로젝트 : Solo Leveling 선택지 시뮬레이션
---

##  실험 진행 흐름

1. **TSV 정리**: 각 에피소드별 상황/스킬/대사 데이터 구성
2. **프롬프트 설계**: 선택지 구성 및 출력 형식 통제 (`prompts/`)
3. **모델 실행**: `kanana-nano-2.1b-instruct` 모델로 대사/이유/선택 생성
4. **결과 저장**: `results/` 버전별 기록


---
## 사용 모델
- [`kakaocorp/kanana-nano-2.1b-instruct`](https://huggingface.co/kakaocorp/kanana-nano-2.1b-instruct)
---

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
│ ├── ep1_dongseok/ # 1편: 황동석 편, 현재 ep1 만 실험 
│ │ ├── ep1_dongseok.tsv # 원본 TSV
│ │ ├── notes.md # 실험 버전별 메모
│ │ ├── prompts/ # 실험 프롬프트 (v1v14)
│ │ ├── results/ # 결과 (v1v14)
│ │ └── run.ipynb # 실험 실행 파일
│ │
│ ├── ep2_hidden/ # 2편: 히든 퀘스트 편 
│ │ ├── ep2_hidden.tsv
│ │ ├── notes.md
│ │ ├── prompts/
│ │ └── results/
│ │
│ ├── ep3_job_quest/ # 3편: 전직 퀘스트 편
│ │ ├── ep3_job_quest.tsv
│ │ ├── notes.md
│ │ ├── prompts/
│ │ └── results/
│
├── inference/
│ └── sl_choice_simulation.ipynb # 초기 실험 (prompt_output 관련 파일 ), 이후 에피소드별로 실험
│
├── evaluation/ # 평가 지표/후속 분석 예정
│
├── prompt_output/ # 초기 실험 
│ ├── ep1_dongseok_result.md
│ ├── ep2_hidden_result.md
│ └── ep3_job_quest_result.md
│
└── README.md

```

---

## 에피소드 정리

| 에피소드 | 설명 |
|----------|------|
| **ep1: 황동석 편** | 긴급 퀘스트 발생 → 적을 모두 처치할 것인가? |
| **ep2: 히든 퀘스트 편** | 일일 퀘스트 이후 히든 퀘스트 발생 → 랜덤 박스 선택 |
| **ep3: 전직 퀘스트 편** | 히든 클래스 ‘네크로맨서’ 전직 여부 선택 |

---
