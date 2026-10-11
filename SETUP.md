# Korea Culture Shorts (English) - 새 레포 세팅

## 1. 레포 만들기
1. GitHub에서 새 레포를 만들고(예: `korea-shorts`) 이 폴더의 파일을 전부 올립니다.
   - `.github/workflows/korea-shorts-pipeline.yml` 은 경로까지 그대로 올려야 합니다.
2. 레포 Settings > Actions > General > Workflow permissions 를 **Read and write**로 설정합니다. (결과 DB 커밋용)

## 2. Secrets (Settings > Secrets and variables > Actions > Secrets)
| 이름 | 필수 | 설명 |
|---|---|---|
| GROQ_API_KEY | 필수 | console.groq.com/keys 에서 무료 발급 |
| PIXABAY_API_KEY | 권장 | pixabay.com 로그인 후 pixabay.com/api/docs 에서 확인 (없으면 색 카드로 대체) |
| DISCORD_WEBHOOK_URL | 선택 | 완료 알림 + 아티팩트 링크 + 제목/설명/썸네일 |
| YT_CLIENT_ID, YT_CLIENT_SECRET, YT_REFRESH_TOKEN | 선택 | 유튜브 자동 업로드(비공개). 안 하면 mp4 아티팩트만 남음 |

## 3. Variables (같은 화면의 Variables 탭, 선택)
- `CHANNEL_NAME` : 영상 위쪽에 표시될 채널 이름
- `CHANNEL_HANDLE` : 예) `@mychannel`

## 4. 프로필 이미지
- 루트의 `avatar.png`(정사각형 권장)를 새 채널 프로필 이미지로 교체하세요. 영상 헤더와 썸네일에 자동으로 들어갑니다.

## 5. 실행 (아이폰 GitHub 앱 > Actions > korea-shorts-pipeline > Run workflow)
- 처음: `stage=prepare`, `count=2`, `start_index=0`, `auto_verify=true`
  - 소재 12개 생성 -> 2개 승인 -> 영어 대본/제목/핵심 문구/이미지 검색어 생성 -> `review.txt`
- `review.txt`를 열어 제목1/제목2/핵심[n]을 고치고 저장(Commit)
  - `(사실 확인용 검색어)` 줄의 키워드로 내용이 맞는지 한 번 검색해 보세요. (LLM이 만든 사실입니다)
- `stage=render` 로 실행 -> 음성(영어) -> 이미지 -> 영상 -> 썸네일 -> (업로드) -> 디스코드 알림
- 검수 없이 한 번에: `stage=all`
- 하루 1~2개 권장. 자동 일정(schedule)은 넣지 않았습니다.

## 6. 유튜브 채널 (새 채널)
- 한국어 채널과 분리하세요. 채널 설정에서 기본 언어/국가를 영어/한국으로 두고 영어 설명을 넣으세요.
- 자동 업로드를 쓰려면 새 채널 계정으로 `get_refresh_token.py` 를 실행해 refresh token을 받으세요.

## 7. 주의
- 소재/대본은 LLM이 만든 것이라 사실 오류가 있을 수 있습니다. 올리기 전에 확인하세요.
- 똑같은 형식의 대량 영상은 수익화 심사에서 불리할 수 있으니, 소재 선택과 해설에 본인의 관점을 더하세요.
