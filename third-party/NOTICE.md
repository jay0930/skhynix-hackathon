# 외부 자료 출처와 변경 범위

기준 확인일: 2026-10-29. 파일별 기준 커밋·SHA-256·원본 URL은 [sources.json](sources.json)에 기록했습니다. [confidence: high]

| 원본 | 처리 | 공개 배포 |
|---|---|---|
| DietrichGebert/ponytail | 원본 `skills/ponytail/SKILL.md`를 변경 없이 포함 | Skill과 [MIT 라이선스](ponytail/LICENSE) |
| obra/superpowers | brainstorming·TDD·systematic-debugging·verification-before-completion을 참고해 독립적인 짧은 Skill로 재작성 | 자체 Skill과 [MIT 라이선스](superpowers/LICENSE) |
| garrytan/gstack | office-hours·plan-eng-review·review의 질문·리뷰 관점을 참고해 독립 작성 | 자체 Skill과 [MIT 라이선스](gstack/LICENSE) |
| claude-code-expert/example | docs/PRD.md·REQUIREMENTS.md·TRD.md의 역할·일반 항목을 참고해 빈 양식 작성 | 자체 양식과 원본 URL. 예제 원문은 공개 복제하지 않음 |

원본 라이선스·포함 방식은 가져온 파일을 기준으로 확인했습니다. example 저장소에서는 명시적인 라이선스 파일을 찾지 못했으며 공개 열람 가능함을 재배포 허가로 간주하지 않았습니다. [confidence: high]

원본 참고 문서와 Skill 스냅샷은 작성자의 `local/upstream/`에만 보존합니다. 공개 키트는 그 경로의 존재에 의존하지 않습니다. `sources.json`의 `local_path`는 작성 시 보관 위치이며 `redistributed: false` 파일은 Clone에 포함되지 않습니다. [confidence: high]

## 자체 작성·변경 내용

- `idea-partner`: 초안 소유권·질문 하나씩·요약/확정/구현 구분을 추가한 텍스트 전용 대화 절차.
- `hackathon-start`: 제공 환경과 제출 조건을 우선하는 착수 절차.
- `tdd-delivery`: 동작 테스트·원인 조사·제한적 분담·단일 실행 대체 절차.
- `delivery-review`: 로컬 검증·수동 미리보기·AI 도움 없는 후속 서술형 경계.
- 템플릿: 예제 앱·스택·수치·완성 코드를 제거하고 실제 과제 작성용 항목을 독립적으로 구성.
- gstack·Superpowers 실행기·훅·자동 업데이트·외부 리뷰·시각 도우미는 포함하지 않음. [confidence: high]

Ponytail의 지침도 실제 과제·플랫폼 경계보다 우선하지 않습니다. 템플릿·자체 지침을 원본 프로젝트의 공식 기능이나 공식 시험 승인 도구로 표시하지 않습니다. [confidence: high]
