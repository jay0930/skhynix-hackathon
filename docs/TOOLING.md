# 도구 구성과 출처

준비 키트는 별도 실행 프레임워크 없이 Markdown과 Python 표준 라이브러리를 사용합니다. 과제 스택은 실제 제공 환경 확인 후 결정합니다. [confidence: high]

| 후보 | 확인한 특징 | 반영 범위 |
|---|---|---|
| [Ponytail](https://github.com/DietrichGebert/ponytail) | 최소 변경·기존 기능 재사용 중심의 Skill | 원본 `SKILL.md`와 MIT 라이선스 포함 |
| [Superpowers](https://github.com/obra/superpowers) | 질문·명세·TDD·디버깅·검증·작업 분담 절차 | 자체 Skill의 대화·테스트·검증 원칙에 선별 반영 |
| [gstack](https://github.com/garrytan/gstack) | 제품·설계·코드 리뷰와 브라우저 QA·배포 절차 | 자체 Skill의 질문·리뷰 관점만 참고 |
| [문서 예제](https://github.com/claude-code-expert/example) | TODO 앱 PRD·TRD·구현 요구사항 예제 | 역할·일반적인 항목을 참고한 독립 빈 양식 |

위 특징은 고정한 원본에서 확인했습니다. [confidence: high]

전체 gstack에는 브라우저 조작·외부 리뷰·Push와 연결되는 절차가 있습니다. Superpowers 전체 흐름에도 별도 설계·worktree·완료 절차가 있습니다. 시험 준비 키트는 이 실행 흐름과 설치기·훅·업데이트·시각 도우미를 가져오지 않습니다. [confidence: high]

Codex 호환 표기가 있어도 시험 플랫폼에서 설치·실행 가능함을 뜻하지는 않습니다. 제한적인 Skill 파일 읽기와 단일 Codex 흐름을 기본값으로 둡니다. [confidence: medium]

## 필요할 때 검토할 추가 도구

- 언어·프레임워크 공식 문서 조회: 과제에 필요하고 플랫폼이 허용하는 경로에서만 사용합니다. 작업 코드·데이터가 외부로 전달되는 도구는 사용하지 않습니다.
- 개인 MCP: 기본 설치하지 않습니다. 기존 터미널·파일·검사 기능으로 해결 가능한지 먼저 확인합니다.
- 브라우저 자동화·외부 AI·외부 저장소·배포 Plugin: 시험 키트에 포함하지 않습니다. [confidence: medium]

## 문서 사용 순서

초안 논의 → PRD 확정 → TRD와 REQUIREMENTS → TASKS 순서로 진행합니다. DECISIONS와 VERIFICATION은 실제 선택·실행 시 갱신합니다. 템플릿 전체를 채우기 위한 개발은 하지 않습니다. [confidence: medium]

기준 커밋·파일 해시·라이선스·변경 범위는 [출처 고지](../third-party/NOTICE.md)와 [출처 목록](../third-party/sources.json)에 기록합니다. 준비 키트에서 추가한 규정과 순서는 원본 프로젝트의 공식 동작과 구분합니다. [confidence: high]
