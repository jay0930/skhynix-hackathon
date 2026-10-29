# SK Hynix 해커톤 준비 키트

초안은 Jay와 함께 다듬고, 확정한 방향의 구현과 검증은 AI에 맡기는 공개 준비 키트입니다. 특정 과제의 답안이나 완성 앱은 포함하지 않습니다. [confidence: high]

## 시험 환경에서 가져오기

아래 명령은 개인 PC가 아니라 **시험 플랫폼 안의 터미널**에서 실행합니다. 기존 과제 폴더는 그대로 두고, 참고 키트만 임시 경로에 내려받습니다. `/tmp` 사용이 허용되는지는 사전 체험에서 확인하세요. [confidence: medium]

```bash
git clone https://github.com/jay0930/skhynix-hackathon.git /tmp/sk-hynix-kit
```

파일을 복사·업로드하거나 GitHub에 로그인할 필요가 없는 공개 저장소 주소입니다. Clone(저장소 내려받기)은 준비 자료를 가져오는 동작이며, 시험 결과를 보내는 Push와 다릅니다. [confidence: high]

다운로드 확인:

```bash
git -C /tmp/sk-hynix-kit remote get-url origin
git -C /tmp/sk-hynix-kit rev-parse HEAD
ls -a /tmp/sk-hynix-kit
```

`origin`이 위 저장소이고 `README.md`, `AGENTS.md`, `templates/`, `.agents/`가 있는지 확인합니다. 기존 과제의 작업 위치에서 제공된 Codex를 사용하고, 작업 디렉터리를 키트 폴더로 바꾸지 않습니다. Clone만으로 Skill이 자동 설치되지는 않습니다. [confidence: high]

### Codex에 넣을 시작 요청

```text
/tmp/sk-hynix-kit/README.md와 AGENTS.md를 읽어주세요.
필요한 Skill은 준비 키트의 .agents/skills/ 경로에서 직접 읽어 적용해주세요.
시험 단계로 취급하고 실제 과제 지침을 우선해주세요.
기존 과제 지침·파일·플랫폼 설정을 덮어쓰지 마세요.

먼저 현재 과제의 README, 제출 조건, 기존 코드와 실행 환경을 확인해주세요.
제가 초안을 제공하면 idea-partner로 함께 검토해주세요.
제가 방향을 확정하고 구현을 요청하면 명세→테스트→구현→검증을 진행해주세요.
기술 선택은 확인한 환경 안에서 판단하고, 중요한 이유와 한계만 설명해주세요.
에이전트 분담이 미지원이면 단일 Codex로 진행해주세요.
문서는 과제 작업 공간에 작성하고 준비 키트 자체를 수정하지 마세요.
```

이미 구현 방향과 실행을 승인했다면 그 사실을 함께 알려주면 됩니다. 같은 승인을 반복해서 받을 필요는 없습니다. [confidence: medium]

### 다운로드가 실패하면

| 상황 | 다음 행동 |
|---|---|
| 경로가 이미 존재 | 삭제·덮어쓰기·자동 Pull을 하지 않습니다. 위 확인 명령으로 출처와 커밋을 확인하고, 같은 키트면 기존 복사본을 읽습니다. 다르면 새로 받을 경로를 정하고 요청문의 경로도 함께 바꿉니다. |
| 인증 요청 | 비밀번호·개인 토큰을 넣지 않습니다. 공개 HTTPS 주소가 맞는지 확인합니다. |
| Git 없음·네트워크 차단·권한 오류 | 오류를 기록합니다. 플랫폼에서 허용한 다운로드 방법만 확인하며, 프록시·터널·개인 파일 업로드로 우회하지 않습니다. |
| Skill이 보이지 않음 | Codex에 해당 `SKILL.md`의 절대 경로를 직접 읽도록 요청합니다. 전역 설정을 바꾸지 않습니다. |

문제가 반복되면 플랫폼의 문제 신고를 이용합니다. 사용법·제출 절차는 Cofa Helper에 확인합니다. [confidence: high]

## 초안을 함께 고민하기

아직 방향을 확정하지 않았다면 다음 요청을 사용합니다.

```text
/tmp/sk-hynix-kit/.agents/skills/idea-partner/SKILL.md를 읽고 적용해주세요.
아래 초안을 함께 검토해주세요. 먼저 이해한 내용을 짧게 확인하고,
가장 중요한 질문을 하나씩 해주세요. 약한 전제나 놓친 점은 지적하되
해결책을 먼저 확정하지 마세요. 대안이 필요하면 요청하겠습니다.

[여기에 본인의 초안 입력]
```

`정리해줘`는 논의 요약, `이 방향으로 확정`은 명세 반영입니다. 둘 다 코딩 시작 요청과 구분합니다. `이 방향으로 확정하고 구현해줘`처럼 함께 요청할 수도 있습니다. [confidence: high]

## 문서와 Skill의 역할

| 파일 | 용도 |
|---|---|
| [PRD](templates/PRD.md) | 무엇을 왜 해결하는지, 사용자·목표·범위 |
| [TRD](templates/TRD.md) | 확인한 환경에서 어떻게 설계할지 |
| [REQUIREMENTS](templates/REQUIREMENTS.md) | 지금 구현할 조건과 수용 기준 |
| [TASKS](templates/TASKS.md) | 다음 할 일·우선순위·진행 상태 |
| [DECISIONS](templates/DECISIONS.md) | 선택한 이유·대안·한계 |
| [VERIFICATION](templates/VERIFICATION.md) | 실행한 검사·결과·미검증 항목 |

기본 문서 위치는 **과제 작업 공간의 `docs/hackathon/`**이며 실제 과제의 지정 경로가 우선합니다. AI가 내용을 작성·갱신하고 Jay는 핵심 판단을 확인합니다. 불필요한 항목은 사유와 함께 ‘해당 없음’으로 남깁니다. [confidence: medium]

| Skill | 쓰는 시점 |
|---|---|
| [idea-partner](.agents/skills/idea-partner/SKILL.md) | 초안을 함께 검토할 때 |
| [hackathon-start](.agents/skills/hackathon-start/SKILL.md) | 과제와 환경을 파악할 때 |
| [tdd-delivery](.agents/skills/tdd-delivery/SKILL.md) | 구현·오류 수정을 요청했을 때 |
| [delivery-review](.agents/skills/delivery-review/SKILL.md) | 완료·제출 준비를 검증할 때 |
| [Ponytail](.agents/skills/ponytail/SKILL.md) | 최소 구현과 기존 기능 재사용을 판단할 때 |

SDD(명세 주도 개발)는 요구사항을 먼저 정하는 방식이고, TDD(테스트 주도 개발)는 실패하는 동작 테스트부터 구현하는 방식입니다. 다중 에이전트는 지원될 때만 제한적으로 사용하며 필수 조건이 아닙니다. [confidence: medium]

## 시험 중 경계

공개 자료를 가져오는 것은 허용 범위 안에서만 수행합니다. 제공된 Codex·허용 모델을 사용하고 외부 전송·Git Push·외부 모델·Computer Use(화면 자동 조작)·감독 설정 변경·제한 우회를 하지 않습니다. 브라우저 미리보기와 제출 버튼은 Jay가 직접 조작합니다. 후속 서술형은 AI 없이 직접 답변합니다. [confidence: high]

세부 지침은 [AGENTS.md](AGENTS.md), 준비 점검은 [사전 체험 안내](docs/REHEARSAL.md), 도구 비교·출처는 [도구 구성](docs/TOOLING.md)에서 확인합니다. PDF 원본과 개인 자료는 공개하지 않습니다. [confidence: high]

## 준비 키트 자체 검사

아래 명령은 준비 키트 폴더에서 Python 3.9 이상으로 실행합니다. 추가 패키지는 필요하지 않습니다. 시험 환경에서 키트만 검사하려면 작업 위치를 바꾸지 않고 `python3 /tmp/sk-hynix-kit/scripts/check_kit.py`를 사용할 수 있습니다. [confidence: high]

```bash
python3 scripts/check_kit.py
python3 -m unittest discover -s scripts -p 'test_*.py' -v
```

이는 준비 키트의 파일·링크·출처 무결성 검사입니다. 실제 과제 테스트나 Skill의 AI 행동을 보장하는 검사가 아닙니다. 검증 범위와 남은 점검은 [검증 기록](docs/VALIDATION.md)에 구분해 기록합니다. [confidence: high]
