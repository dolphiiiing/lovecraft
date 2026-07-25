# 크툴루 신화 자료집 (The Cthulhu Archive)

크툴루 신화의 **사건 연대기 + 존재 도감**을 하나로 묶은 인터랙티브 자료집.
사건과 존재가 서로 연결되고, 브라우저에서 직접 편집·추가·JSON 저장이 된다.
디자인은 Pantone 807C(형광 마젠타) 단색 + 흑백의 dossier 스타일.

## 바로 보기
`index.html`을 브라우저로 열면 끝. (별도 서버 불필요)

## 폴더 구조
```
cthulhu-archive/
├─ index.html            ← 완성 결과물 (build.py가 생성). 브라우저로 열면 됨
├─ template.html         ← UI/디자인/로직 템플릿. 데이터는 /*__DATA__*/ 자리에 주입됨
├─ build.py              ← data + template → index.html 생성 스크립트
└─ data/
   ├─ cthulhu_data.json  ← 원본 노드/링크 (Kumu에서 추출·정리)
   └─ kumu-source.json   ← Kumu 원본 export (참고용)
```

## 다시 빌드하기
데이터(`data/cthulhu_data.json`)나 디자인(`template.html`)을 고친 뒤:
```bash
python3 build.py
```
→ `index.html`이 다시 생성된다.

## 편집 방법 3가지
1. **브라우저에서 직접** — index.html을 열고 항목/관계를 편집·추가 → 우상단 「JSON 저장」으로 Kumu 형식 파일 내려받기. 편집은 localStorage에도 자동 저장됨.
2. **데이터 파일 수정** — `data/cthulhu_data.json`의 노드/링크를 고치고 `python3 build.py`.
3. **콘텐츠 보강** — `build.py` 안의 `notes`(도감 메모)와 `ADD`(조직·존재 추가) 목록을 편집.

## 데이터 스키마
- 노드: `{ id, label, type, desc, note, tags[], meta[[k,v]...] }`
  - type: 사건 / 개체 / 종족 / 장소 / 유물 / 조직 / 개념 / 작품 / 기타
- 링크: `{ from, to, type, dir }`  (type 예: 선행, 원인, 숭배, 참여, 거주, 적대 …)
- `timeline`: 사건 연대기 표시 순서 (label 배열)

## 출처
- 관계 데이터: Kumu 지도 「크툴루」 (사용자 제공 export)
- 존재/조직 보강 및 디자인: 사용자 제공 자료집 PDF, H.P. 러브크래프트 정전 참고
