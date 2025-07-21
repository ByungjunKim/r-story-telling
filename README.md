
# 프로젝트 : Solo Leveling 선택지 시뮬레이션

---

##  디렉토리 구성

```
Solo_Leveling/
├── ep1_dongseok.tsv
├── ep2_hidden.tsv
├── ep3_job_quest.tsv
├── sl_dialogue.tsv
├── sl_personality.tsv
├── sl_situation.tsv
├── sl_skill.tsv
├── ep1_dongseok_prompt.jsonl
├── ep2_hidden_prompt.jsonl
├── ep3_job_quest_prompt.jsonl
├── sl_choice_simulation.ipynb
└── prompt_output/
    ├── ep1_dongseok_result.md
    ├── ep2_hidden_result.md
    └── ep3_job_quest_result.md
```

---

## 에피소드 정리

| 에피소드 | 설명 |
|----------|------|
| **ep1: 황동석 편** | 긴급 퀘스트 발생 → 적을 모두 처치할 것인가? |
| **ep2: 히든 퀘스트 편** | 일일 퀘스트 이후 히든 퀘스트 발생 → 랜덤 박스 선택 |
| **ep3: 전직 퀘스트 편** | 히든 클래스 ‘네크로맨서’ 전직 여부 선택 |

---

## 주요 데이터 파일 설명

| 파일명 | 설명 |
|--------|------|
| `sl_dialogue.tsv` | 성진우의 주요 대사 원문 |
| `sl_personality.tsv` | 성격  |
| `sl_situation.tsv` | 각 에피소드의 상황 요약 |
| `sl_skill.tsv` | 사용된 스킬 및 부가 설명 정리 |
| `ep*.tsv` | 에피소드별 선택지 실험용 데이터 |
| `ep*_prompt.jsonl` | LLM 입력용 포맷 |
| `prompt_output/*.md` | 실험 결과(markdown 파일) |
| `sl_choice_simulation.ipynb` | 전체 실행 코드 |

---

## 실험 방식 요약
1. `.tsv` 기반으로 LLM 입력용 `.jsonl` 생성
2. `kanana-nano-2.1b-instruct` 모델을 사용하여 선택지에 대한 결과 생성
3. 결과는 `.md` 파일로 저장

---

## 📌 사용 모델
- [`kakaocorp/kanana-nano-2.1b-instruct`](https://huggingface.co/kakaocorp/kanana-nano-2.1b-instruct)
