# 관상감 觀象監 — 페르소나가 살아가는 세상

> 1.78M 합성 한국인이 살아가는 인터랙티브 3D 세계 — bruno-simon.com 영감 받음

## 데모 진입점

- **🎯 메인 (v4):** `/` → `demo-delta-bruno-v4.html`
- 비교 인덱스: `/index.html`
- v3 (Kenney 모델, 애니메이션 없음): `/demo-delta-bruno-v3.html`
- v2 (procedural): `/demo-delta-bruno.html`
- v1 (시네마틱): `/demo-beta-cinematic.html`
- v0 (2D 스프라이트): `/demo-alpha-photo-sprites.html`

## 컨트롤

### 데스크탑
- `W A S D` — 걷기
- `MOUSE` — 둘러보기 (자동 포인터 락)
- `SHIFT` — 달리기
- `E` 또는 `Click` — 가까운 사람과 대화
- `ESC` — 마우스 풀기

### 모바일
- 좌측 조이스틱 — 이동
- 우측 화면 스와이프 — 둘러보기
- "대화" 버튼 — 페르소나와 대화

## 기술 스택

- **Three.js 0.160** — 3D 렌더링
- **Mixamo** — Soldier, Xbot 캐릭터 + walk 애니메이션
- **Kenney.nl** (CC0) — 빌딩, 자동차, 도시 모델
- **PointerLockControls** — 데스크탑 1인칭 카메라
- **Custom touch controls** — 모바일 가상 조이스틱
- **UnrealBloomPass** — 후처리 bloom
- **Sky** (Three.js addon) — 절차적 노을 하늘

## 데이터

- 30명 페르소나 샘플 (실제 1.78M 풀에서 추출)
- 각 페르소나: ID, 이름, 나이, 성별, 주소, 직업, 인생 서사

## 라이선스

- Code: MIT
- Kenney 에셋: CC0
- Mixamo: Adobe 무료 라이선스
- Three.js: MIT
- 관상감 페르소나 데이터: 합성 (실존 인물 아님)

## 배포

- Vercel 정적 호스팅
- 도메인: TBD
