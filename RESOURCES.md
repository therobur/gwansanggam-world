# 관상감 "페르소나 살아가는 세상" — Open Source 에셋 & 라이브러리 목록

> Bruno Simon 수준 퀄리티를 9일 안에 달성하기 위해 활용할 수 있는 무료 리소스

---

## 🎨 3D 모델 에셋 (CC0 / Free)

### 1. Kenney.nl ⭐ 가장 추천 (CC0 — 완전 무료, attribution 불필요)
**URL:** https://kenney.nl/assets/category:3D

**관련 팩:**
- **City Kit (Commercial)** — 상업 빌딩, 빌딩 키트
- **City Kit (Suburban)** — 주거 건물
- **City Kit (Roads)** — 도로, 인도, 신호등, 가드레일
- **Blocky Characters** — 3D 캐릭터 (남/여, 다양한 직업)
- **Car Kit** — 자동차, 트럭, 버스
- **Furniture Kit** — 가구 (실내 씬용)
- **Nature Kit** — 나무, 식물

**파일 형식:** OBJ, FBX, GLTF/GLB (Three.js 직접 로드 가능)

**다운로드 후:** `apps/web/public/assets/kenney/` 에 배치

---

### 2. Quaternius ⭐ 추천 (대부분 CC0, 일부 CC-BY)
**URL:** https://quaternius.com

**관련 팩:**
- **Downtown City MegaKit** — 도시 환경 모듈 (300+ 모델)
- **Modular Streets Pack** — 도로, 인도, 횡단보도
- **Universal Base Characters** — 리깅된 휴머노이드 (애니메이션 가능)
- **Animated Men Pack** / **Animated Women Pack** — 애니메이션 캐릭터
- **Background Posed Humans Pack** — 군중 캐릭터 (군중씬에 최고)
- **Cars Pack** — 다양한 차량
- **Public Transport Pack** — 버스, 지하철

**가장 큰 장점:** 캐릭터에 walk/idle/run 애니메이션 포함

---

### 3. Poly Pizza (CC-BY 또는 CC0)
**URL:** https://poly.pizza

검색 추천: "korean street", "asian shop", "street vendor", "scooter"

---

### 4. Sketchfab (필터: CC0/Free)
**URL:** https://sketchfab.com/3d-models?features=downloadable&licenses=322a749bcfa841b29dff1e8a1bb74b0b

검색 추천: "seoul", "korean architecture", "hanok"

---

## 🌳 환경 / 라이팅

### 5. Poly Haven (CC0)
**URL:** https://polyhaven.com

- **HDRI 환경맵** (skybox / 조명) — sunset, dawn, urban 등
- **PBR 텍스처** — concrete, asphalt, brick, wood
- **3D 식물** — 가로수, 화분

### 6. AmbientCG (CC0)
**URL:** https://ambientcg.com — PBR 텍스처 + 머티리얼

---

## 🎵 오디오 (Bruno처럼 사운드가 핵심 임팩트)

### 7. Freesound.org (CC0 / CC-BY)
**URL:** https://freesound.org

검색: "seoul ambient", "city walking", "korean market", "footsteps concrete"

### 8. Pixabay Music (Royalty Free)
**URL:** https://pixabay.com/music

검색: "korean ambient", "lo-fi", "city background"

### 9. Howler.js (Bruno가 사용)
**URL:** https://howlerjs.com — Web audio 라이브러리. 공간 사운드 지원.

---

## 🛠 Three.js 생태계 라이브러리

### 10. React Three Fiber + Drei (강력 추천)
```bash
npm install three @react-three/fiber @react-three/drei @react-three/postprocessing
```
- **R3F**: Three.js를 React 컴포넌트로
- **Drei**: 헬퍼 모음 (OrbitControls, Sky, Environment, useGLTF, Html overlay 등)
- **Postprocessing**: Bloom, DepthOfField, Vignette, ChromaticAberration

### 11. Rapier (Bruno가 사용하는 물리엔진)
```bash
npm install @react-three/rapier
```
사람과 환경 충돌, 차량 물리

### 12. Three.js Examples (이미 사용 중)
- `OrbitControls`, `PointerLockControls`, `FirstPersonControls`
- `Sky` (절차적 하늘)
- `EffectComposer` + `UnrealBloomPass` ← v2 데모에 이미 적용
- `GLTFLoader`, `DRACOLoader` (압축 모델)

---

## 🌐 Bruno Simon's Code (MIT — 직접 fork 가능)

### 13. Bruno's GitHub
**URL:** https://github.com/brunosimon/folio-2019
- 전체 소스코드 + Blender 파일 포함
- MIT 라이선스 (상업적 사용 가능)
- Vite + Three.js + Cannon.js (현재는 Rapier로 마이그레이션)

**활용법:**
1. Fork → 자동차/지형/UI를 관상감 컨셉으로 교체
2. Blender 파일 가지고 한국 도시로 리모델링
3. 캐릭터 시스템을 1.78M 페르소나 풀과 연결

**리스크:** 코드 베이스가 복잡함. 학습 곡선 필요.

---

## 🎮 게임 엔진 대안 (Three.js보다 빠른 prototyping)

### 14. Babylon.js
**URL:** https://www.babylonjs.com
Three.js와 유사하지만 더 완성도 높은 default UI/controls.

### 15. PlayCanvas
**URL:** https://playcanvas.com
브라우저에서 작업하는 풀 게임 엔진. 무료.

### 16. Needle Engine (Unity → Web)
**URL:** https://needle.tools
Unity로 작업한 씬을 웹으로 export. Bruno 퀄리티 빠르게 도달 가능.

---

## 🚀 9일 스프린트 추천 스택

```
Frontend:        Next.js 15 + R3F + Drei + Postprocessing
Physics:         @react-three/rapier (필요시)
Models:          Kenney City Kit + Quaternius Characters (Animated)
Audio:           Howler.js + Freesound Korean ambient
Lighting:        Poly Haven HDRI sunset
Post-processing: Bloom + Vignette + Color Grading
3D Editor:       Blender (수정/커스터마이즈 필요시)
```

---

## 📥 즉시 가능한 다음 단계

### Phase A: 에셋 다운로드 (30분)
```bash
# Kenney City Kit
curl -L https://kenney.nl/data/uploads/blocks/city-kit-commercial.zip -o /tmp/city.zip
unzip /tmp/city.zip -d apps/web/public/assets/kenney/

# Quaternius Animated Men/Women
# (수동 다운로드 from quaternius.com)
```

### Phase B: 데모 업그레이드 (2-3시간)
- 현재 procedural 빌딩 → Kenney City Kit GLB 로드
- 현재 procedural 캐릭터 → Quaternius Animated Characters
- 추가: 한국식 간판 (한글/한자 텍스처)
- 추가: 한국 음악 ambient loop

### Phase C: Bruno fork (1-2일)
- folio-2019 fork
- Vite + R3F 구조 학습
- 자동차/씬/UI 교체

---

## 💰 비용

- Kenney: 무료 (옵션 후원)
- Quaternius: 무료 (Patreon 지원 시 더 많은 팩)
- Poly Haven: 무료 (구독 시 4K HDRI)
- Freesound: 무료 (CC 라이선스 확인 필수)
- Three.js / R3F / Rapier: 무료 (MIT)
- 도메인/호스팅: 기존 Vercel 사용
- **총 추가 비용: $0**

---

## ⚖️ 라이선스 안전성

| 리소스 | 라이선스 | 상업적 사용 | Attribution |
|---|---|---|---|
| Kenney | CC0 | ✅ | 불필요 |
| Quaternius | 대부분 CC0 | ✅ | 일부 필요 |
| Poly Haven | CC0 | ✅ | 불필요 |
| Sketchfab CC0 | CC0 | ✅ | 불필요 |
| Freesound CC0 | CC0 | ✅ | 불필요 |
| Bruno folio-2019 | MIT | ✅ | 필요 |
| Three.js | MIT | ✅ | 필요 |
| Howler.js | MIT | ✅ | 필요 |

**관상감 사이트 푸터에 attribution 섹션 추가 권장:**
"Built with Three.js · 3D models by Kenney · Sound by Freesound · Inspired by bruno-simon.com"
