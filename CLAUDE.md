# 프로젝트 컨텍스트 (Claude Code용)

크툴루 신화 인터랙티브 자료집. 정적 단일 HTML 앱이며 빌드는 파이썬 스크립트 하나로 끝난다.

## 빌드
```bash
python3 build.py   # data/cthulhu_data.json + template.html → index.html
```
서버·의존성 없음. `index.html`을 브라우저로 직접 연다.

## 파일 역할
- `template.html` — 모든 UI/CSS/JS. 데이터가 들어갈 자리는 `/*__DATA__*/` 플레이스홀더. **여기서 디자인/기능을 고친다.**
- `build.py` — 데이터 로드 → `notes`(도감 메모)·`ADD`(조직/존재 추가) 병합 → 링크 dedup → 템플릿에 주입 → `index.html` 출력.
- `data/cthulhu_data.json` — 노드/링크 원본. `data/kumu-source.json` 은 Kumu export 원본(참고).
- `index.html` — 생성물. **직접 수정하지 말 것.** template/build를 고치고 재빌드한다.

## 디자인 규칙
- 메인 컬러는 Pantone 807C 근사값 `--pink:#EB0FBE` 하나. 나머지는 흑백(#000/#fff)만.
- 폰트: 라틴 제목 Yellowtail(스크립트), 한글 제목 Black Han Sans, 본문 Nanum Myeongjo, 라벨 Nanum Gothic (Google Fonts).

## 데이터 스키마
- node: `{ id, label, type, desc, note, tags[], meta:[[k,v]...] }`
  - type ∈ 사건/개체/종족/장소/유물/조직/개념/작품/기타
- link: `{ from, to, type, dir }`
- `timeline`: 사건 연대기 순서(label 배열), build.py 하단에서 관리.

## 자주 하는 작업
- 존재/조직 추가 → `build.py`의 `ADD` 리스트에 항목 추가(label/type/desc/meta/links) 후 재빌드.
- 설명 보강 → `build.py`의 `notes` 딕셔너리(도감 메모) 편집.
- 링크 대상 지정은 label로 하며 `find()`가 정확→시작→부분 순으로 매칭. 모호하면 정식 label 전체를 쓴다(예: `크툴루(Cthulhu)`).
