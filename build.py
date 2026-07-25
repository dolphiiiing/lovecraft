# -*- coding: utf-8 -*-
import json

data = json.load(open('./data/cthulhu_data.json', encoding='utf-8'))

# ---------- 1) 도감 메모(설명이 비었거나 얇은 존재에 정전 기반 참고 메모) ----------
notes = {
 "크투가": "위대한 옛 존재. 살아있는 불꽃의 화신으로 포말하우트 별에 거주한다. 니알라토텝과 적대하며, 부르는 자를 정화의 화염으로 태운다.",
 "림 샤이코스": "시간과 죽음, 엔트로피를 상징하는 태고의 존재. 만물의 소멸을 관장하는 개념적 신격.",
 "골 고로스": "시간을 관장하는 존재. 어둠 속에서만 현현하며 빛에 노출되면 형체를 유지하지 못한다.",
 "즈스트룰": "별들 사이를 떠도는 태고의 우주 존재. 기록은 단편적으로만 남아 있다.",
 "차르(Xar)": "벌레(연충) 형태의 태고 존재. 심연과 연관된 하위 신격.",
 "아브호스": "원시 생명의 근원. 끊임없이 자식을 낳고 다시 삼키는, 우보 사스라와 유사한 원초적 생명 덩어리.",
 "히드라": "다곤과 짝을 이루는 딥 원의 여왕. 심해에서 딥 원을 다스리며 다곤과 함께 숭배받는다.",
 "조스 오므그": "태평양 심연에 잠든 존재. 딥 원 계열 신화와 얽힌다.",
 "드홀": "꿈의 세계 지하에 서식하는 거대 연충형 생명체. 그 크기는 산맥에 비견된다.",
 "미고": "유고스(명왕성)에서 온 균류·갑각류 혼합 외계 종족. 인간의 뇌를 금속 원통에 담아 우주로 옮기며 지구의 희귀 광물을 채굴한다. 『어둠 속의 속삭임』.",
 "조그": "꿈의 세계 숲에 사는 소형 지성 종족. 구울과 교류한다.",
 "구울": "시체를 먹는 지하 종족. 개를 닮은 형상으로 묘지·지하에 서식하며, 인간이 구울로 변하기도 한다.",
 "검은 날개 종족": "렝 고원의 '나이트건트' 계열. 뿔과 가시 꼬리, 박쥐 날개를 지녔다.",
 "달짐승": "달의 어두운 면에 서식하며 렝의 상인과 결탁해 노예를 사냥한다.",
 "네크로노미콘": "미친 아랍인 압둘 알하즈레드의 금단의 마도서 『알 아지프(Al Azif)』. 738년 그가 다마스쿠스에서 보이지 않는 존재에게 삼켜진 뒤 남은 기록으로, 950년 그리스어 번역본이 '네크로노미콘'이라는 이름으로 처음 알려졌다. 금서로 지정될 때마다 판본은 오히려 늘어났다.",
 "에이본의 서": "하이퍼보리아의 대마법사 에이본의 마도서. 차토구아 숭배와 태고의 마법 지식을 담았다.",
 "황색의 인(Yellow Sign)": "하스터(황색의 왕)와 카르코사를 상징하는 저주받은 표식. 목격한 자는 황색의 왕의 영향 아래 광기에 빠진다.",
 "엘더 사인": "고신들이 만든 봉인의 상징. 외신과 위대한 옛 존재의 침입을 막는 보호 문양.",
 "은열쇠": "랜돌프 카터의 은빛 열쇠. 꿈의 세계와 시공간의 관문을 여는 유물로, 요그 소토스의 영역과 통한다.",
 "빛나는 트라페조헤드론": "어둠 속에서 니알라토텝의 화신 '어둠 속을 방황하는 자'를 불러내는 외계의 결정 렌즈. 빛이 사라지면 그것이 강림한다. 별의 지혜파가 숭배했다.",
 "우나우스프레클리헨 쿨텐": "프리드리히 폰 윤츠의 『이름 없는 교단(Unaussprechlichen Kulten)』. 전 세계 비밀 사교를 기록한 금서.",
 "드 에르미스 미스테리스": "루드비히 프린의 『벌레의 신비(De Vermis Mysteriis)』. 흑마술과 소환술의 마도서.",
 "틴달로스": "각(角)을 통해 시간을 가로질러 사냥하는 '틴달로스의 사냥개'. 곡선이 아닌 예각의 시간에서 먹잇감을 쫓는다.",
 "차원 사냥개": "틴달로스의 사냥개 계열. 시간의 각진 틈으로 침입해 표적을 추격하는 포식자.",
 "노인종": "『광기의 산맥에서』의 엘더 씽을 가리키는 다른 이름. 지구 최초의 고등 문명 종족.",
 "다올로스(Daoloth)": "'장막을 걷는 자'. 목격 자체가 정신을 파괴하는 외신으로, 과거와 미래를 드러낸다.",
 "스타리 위즈덤 교단": "니알라토텝의 화신 '어둠의 방황자'를 섬기는 광신도 집단. 빛나는 부등변다면체를 숭배한다.",
 "우보 사스라": "위대한 옛 존재이자 지구 모든 생명의 원형. 유카에의 지하에서 태고의 석판에 둘러싸여 원시 생명을 끝없이 분출한다.",
}

by_label = {}
for n in data['nodes']:
    n.setdefault('note','')
    n.setdefault('meta',[])
    by_label.setdefault(n['label'], n)
for n in data['nodes']:
    if n['label'] in notes:
        n['note'] = notes[n['label']]

def find(label_opts):
    # 1) 정확 일치  2) 시작 일치  3) 부분 일치 (가장 짧은 라벨 우선)
    for lb in label_opts:
        for n in data['nodes']:
            if n['label']==lb: return n
    for lb in label_opts:
        cands=[n for n in data['nodes'] if n['label'].startswith(lb)]
        if cands: return min(cands,key=lambda n:len(n['label']))
    for lb in label_opts:
        cands=[n for n in data['nodes'] if lb in n['label']]
        if cands: return min(cands,key=lambda n:len(n['label']))
    return None

def newid():
    import random; return 'add-'+''.join(random.choice('abcdefghijklmnop') for _ in range(6))

def link(from_label, to_label, rtype):
    a=find([from_label]); b=find([to_label])
    if not a or not b:
        # print('link skip', from_label, to_label);
        return
    data['links'].append({'from':a['id'],'to':b['id'],'type':rtype,'dir':'directed'})

# ---------- 2) PDF 자료집 기반: 비밀결사(조직) & 존재 추가/보강 ----------
# 형식: label, type, match(기존 병합 후보), desc, meta[[k,v]...], links[[to_label, rtype]...]
ADD = [
 {"label":"별의 지혜파 (Starry Wisdom Sect)","type":"조직","match":["스타리 위즈덤 교단","별의 지혜파"],
  "desc":"프로비던스 페더럴 힐의 '프리 월 처치'를 본거지로 삼은 광신 교단. 어둠 속에서만 빛나는 부등변다면체를 사용해 니알라토텝의 화신을 불러들였다. 1877년 연쇄 실종 뒤 주민들이 교회를 습격해 소탕했으나, 1884년 프로비던스에서 재발견된 이래 같은 이름의 종파가 세계 각지에서 주기적으로 다시 나타난다.",
  "meta":[["설립","1844 / 1884 재발견"],["거점","로드아일랜드 프로비던스"],["현재 상태","공식 소탕 · 동명 종파 출현 중"],["관련 신격","니알라토텝"],["관련 유물","빛나는 부등변다면체"]],
  "links":[["니알라토텝","숭배"],["빛나는 트라페조헤드론","사용"]]},

 {"label":"다곤 교단 (Order of Dagon)","type":"조직","match":["다곤 비밀 교단","다곤 교단"],
  "desc":"1829년 오베드 마쉬 선장이 남태평양 섬에서 가져온 신앙에서 비롯된 인스머스의 비밀결사. 심해인에게 산 제물을 바치는 대가로 무한한 어획량과 황금을 받았고, 대가로 딥 원과의 교배가 시작되어 '인스머스 룩'이 퍼졌다. 1928년 미 해병대·FBI의 급습으로 공식 괴멸되었으나 혈족은 여전히 남아 있다.",
  "meta":[["설립","1829년경"],["거점","매사추세츠 인스머스"],["현재 상태","공식 괴멸 · 실질 불명"],["관련 신격","다곤 · 히드라 · 크툴루"],["관련 종족","딥 원(Deep Ones)"]],
  "links":[["다곤(Dagon)","숭배"],["히드라","숭배"],["크툴루(Cthulhu)","숭배"],["인스머스 사건","참여"]]},

 {"label":"검은 형제단 (Black Brotherhood)","type":"조직","match":["검은 형제단"],
  "desc":"크툴루 신화에 기록된 모든 흑마술 결사가 이 조직과 연결되어 있다고 전해지는 세계적 그물. 총수는 니알라토텝의 화신 '검은 남자'로 알려져 있다. 그와의 만남 이후 모든 증언자의 삶이 이전으로 돌아가지 못했다는 공통점만이 확인된다. 목표가 없다는 견해와, 인간의 시간 감각으로는 진행이 보이지 않을 만큼 목표가 거대하다는 견해가 갈린다.",
  "meta":[["설립","불명"],["거점","전 세계"],["현재 상태","활동 중"],["관련 신격","니알라토텝"],["총수","검은 남자 (니알라토텝의 화신)"]],
  "links":[["니알라토텝","숭배"]]},

 {"label":"툴레 협회 (Thule Gesellschaft)","type":"조직","match":["툴레 협회"],
  "desc":"게르만 민족주의와 신비주의를 결합한 뮌헨의 단체. 표면은 강연과 출판이었으나, 실질적으로 아우터 갓과 그레이트 올드 원의 힘으로 독일을 지배하려 했다고 전해진다. 제2차 세계대전 중 나치는 점령지에서 네크로노미콘 판본을 비롯한 신화 문서를 체계적으로 약탈했다. 아돌프 히틀러가 가입했고 디트리히 에크하르트가 이끌었다.",
  "meta":[["설립","1918년, 독일 뮌헨"],["거점","독일 뮌헨"],["현재 상태","공식 해산"],["관련 신격","아우터 갓 · 그레이트 올드 원"],["주요 인물","에크하르트 · 히틀러"],["관련 사건","제2차 세계대전"]],
  "links":[["네크로노미콘","대상"]]},

 {"label":"은빛 여명의 주관자 (Silver Twilight Lodge)","type":"조직","match":["은빛 여명","실버 트와일라잇"],
  "desc":"1657년 보스턴에 설립된 것으로 확인되는 가장 오래된 크툴루 숭배 조직. 목적은 단 두 가지 — 르뤼에를 대양에서 부상시키는 것과 크툴루를 해방시키는 것. 다수의 일원이 불사체로 알려져 있어, 1657년부터 같은 자들이 조직을 이끌고 있다는 의미가 된다. R'lyeh의 좌표(남위 47°9′, 서경 126°43′)를 오래전부터 알고 있었을 것이다.",
  "meta":[["설립","1657년, 보스턴"],["거점","미국·유럽 전역"],["현재 상태","활동 중"],["관련 신격","크툴루"],["목적","르뤼에 부상 · 크툴루 해방"],["특이사항","다수 회원이 불사체"]],
  "links":[["크툴루(Cthulhu)","숭배"],["르뤼에","대상"],["크툴루 각성 시도","참여"]]},

 {"label":"녹색 불꽃의 형제단 (Green Flame)","type":"조직","match":["녹색 불꽃","그린 플레임"],
  "desc":"아자토스의 왕좌 곁에서 타오르는 녹색 불꽃 툴차를 숭배하는 세계적 조직. 17세기 후반 킹스포트에서 확립되었고, 당국이 소탕했다는 공식 기록과 달리 관련자 다수는 비이야키의 등에 올라타 툴차를 만나러 떠났다고 전해진다. 북쪽 스웨덴에서 남쪽 뉴질랜드까지 회원을 두며 세력이 다시 소생 중이다.",
  "meta":[["설립","17세기 후반, 킹스포트"],["거점","전 세계(스웨덴–뉴질랜드)"],["현재 상태","활동 중 · 세력 확장"],["관련 신격","툴차(Tulzscha)"],["특이사항","비이야키 탑승 구성원 존재"]],
  "links":[["트룰차(Tulzscha)","숭배"]]},

 {"label":"황색 사인 형제회 (Yellow Sign Brotherhood)","type":"조직","match":["황색 사인 형제회"],
  "desc":"'이름 없는 자' 하스터와 아우터 갓을 섬기는 결사. 황색 사인을 서로를 알아보는 표식으로 삼으며, 이스의 위대한 종족을 적극적으로 사냥한다. 왜 사냥하는지는 여러 설이 갈린다 — 하스터의 명령, 하스터의 귀환을 방해하기 때문, 혹은 단지 본성. 하스터의 이름을 세 번 부르면 소환된다는 전승이 있다.",
  "meta":[["설립","불명"],["거점","불명"],["현재 상태","활동 중"],["관련 신격","하스터 · 아우터 갓"],["목적","하스터 숭배 · 이스 사냥"],["관련 유물","황색의 인"]],
  "links":[["하스터(Hastur)","숭배"],["황색의 인(Yellow Sign)","사용"],["위대한 종족 오브 이스","적대"]]},

 {"label":"황색 표식의 형제단 (Brotherhood of the Yellow Sign)","type":"조직","match":["황색 표식의 형제단"],
  "desc":"황색 사인 형제회와 이름이 유사하나 더 잔혹한 종파. 숭배가 아니라 '행동'이 목적으로, 이스의 위대한 종족을 고문하고 미 고와 전쟁을 수행한다. 시간 여행이 가능한 존재를 고문한다는 것이 무엇을 의미하는지는 자료집의 이해 범위 밖이라 기록된다.",
  "meta":[["설립","불명"],["거점","불명"],["현재 상태","활동 중"],["관련 신격","하스터 · 아우터 갓"],["목적","이스 고문 · 미 고와의 전쟁"],["특이사항","황색 사인 형제회보다 잔혹"]],
  "links":[["하스터(Hastur)","숭배"],["위대한 종족 오브 이스","적대"],["미고","적대"]]},

 {"label":"검은 파라오의 형제단 (Black Pharaoh)","type":"조직","match":["검은 파라오"],
  "desc":"고대 이집트에서부터 이어졌다 전해지는, 숙면 중인 네프렌-카를 보호하는 형제단. 네프렌-카는 니알라토텝의 화신 '검은 파라오'로, 공식 역사에는 이름조차 지워진 채 남아 있다. 그가 깨어나면 무슨 일이 벌어지는지에 대한 기록은 자료집에 수록되지 않았다.",
  "meta":[["설립","고대 이집트(추정)"],["거점","불명"],["현재 상태","활동 중"],["관련 인물","네프렌-카"],["관련 신격","니알라토텝"]],
  "links":[["니알라토텝","숭배"],["네프렌-카 (Nephren-Ka)","보호"]]},

 {"label":"델타 그린 (Delta Green)","type":"조직","match":["델타 그린"],
  "desc":"1928년 인스머스 급습 이후, 진실을 목격한 미국 정부 내 인사들이 만든 '공식적으로 존재하지 않는' 조직. 예산은 다른 항목에 분산 기록되고 요원들은 다른 직책을 유지한다. 임무는 하나 — 바깥 신들과 그 추종자들이 인간 사회에 침투하는 것을 막는 것. 신화 세계에 맞서는 인간 측의 유일한 방벽에 가깝다.",
  "meta":[["설립","1928 비공식 / 이후 재편"],["거점","미국 정부 내 비공식"],["현재 상태","존재 자체가 비공식"],["목적","바깥 신들의 침투 방지"],["특이사항","공식적으로 존재하지 않는 조직"]],
  "links":[["인스머스 사건","선행"],["딥 원(Deep Ones)","적대"]]},

 # 존재 추가
 {"label":"네프렌-카 (Nephren-Ka)","type":"개체","match":["네프렌"],
  "desc":"'검은 파라오'. 니알라토텝의 화신이라 전해지는 고대 이집트의 파라오. 공식 역사에서 이름이 지워졌으나 — 아크나톤과 달리 지워진 흔적조차 없다 — 여러 단편적 기록에 서로 어긋나는 방식으로 존재한다. 어딘가에서 숙면 중이며, 검은 파라오의 형제단이 그를 지킨다.",
  "meta":[["분류","니알라토텝의 화신"],["별칭","검은 파라오"]],
  "links":[["니알라토텝","분류"]]},

 {"label":"비이야키 (Byakhee)","type":"종족","match":["비이야키"],
  "desc":"우주 공간을 날 수 있는 거대 생물. 하스터·툴차 계열 신화에 등장하며, 숭배자를 등에 태우고 별 사이로 실어 나른다. 어떻게 탑승이 가능한지, 스스로 허용하는 것인지 통제되는 것인지는 알려져 있지 않다.",
  "meta":[["서식","성간 공간"]],
  "links":[["트룰차(Tulzscha)","소속"]]},

 {"label":"크토니안 (Chthonian)","type":"종족","match":["크토니안"],
  "desc":"지하에 서식하는 거대 지렁이형 존재. 지진과 화산 활동을 유발하는 것으로 알려져 있으며, 지표의 인류 문명에 잠재적 위협이 된다. 월머스 재단이 이들과 전쟁을 벌였다는 기록이 단편적으로 남아 있다.",
  "meta":[["서식","지하 심부"]],
  "links":[]},
]

for a in ADD:
    ex = find(a.get("match",[])) if a.get("match") else None
    if ex:
        # 기존 노드 보강
        ex['type'] = a['type']
        if len(a['desc']) > len(ex.get('desc','')): ex['desc']=a['desc']
        ex['meta']=a.get('meta',[])
        ex['label']=a['label']
    else:
        data['nodes'].append({'id':newid(),'label':a['label'],'type':a['type'],
            'desc':a['desc'],'note':'','tags':[],'meta':a.get('meta',[])})

for a in ADD:
    for to_label, rtype in a.get('links',[]):
        link(a['label'], to_label, rtype)

# ---------- 3) 연대기 순서 ----------
timeline = [
 "엘더 씽의 지구 도착","남극 고대도시 건설","쇼고스 창조","쇼고스 반란",
 "크툴루의 지구 도착","르뤼에 건설","엘더 씽 - 크툴루 전쟁","르뤼에 침몰","스타 스폰 봉인",
 "이스 종족의 지구 정착","플라잉 폴립 전쟁","뱀 인간의 몰락","사르나스의 멸망(Doon of Sarnath)",
 "인간 문명","딥 원과 인간의 혼혈 시작","던위치 사건","인스머스 사건","남극 탐사","크툴루 각성 시도",
]

# 중복 링크 제거 (from,to,type 동일)
seen=set(); dedup=[]
for l in data['links']:
    key=(l['from'],l['to'],l['type'])
    if key in seen: continue
    seen.add(key); dedup.append(l)
data['links']=dedup

# ---------- 4) 이미지 배정 (아카이빙된 사진들 + 핑핑 포트레이트) ----------
PORTRAITS = [f"assets/portraits/portrait-{i:02d}.jpg" for i in range(1,17)]
ARCHIVE = ["archive/13.jpg","archive/14.jpg","archive/15.jpg","archive/32.jpg","archive/5.jpg",
 "archive/검은형제단.jpg","archive/나치.jpg","archive/문양.jpg","archive/미라.jpg","archive/보석.jpg",
 "archive/빈방.jpg","archive/사람.jpg","archive/사무실.jpg","archive/새.jpg","archive/서류책.jpg",
 "archive/심해인.jpg","archive/의식사제.jpg","archive/이집트_지하.jpg","archive/자료.jpg","archive/작전도.jpg",
 "archive/작전임무회의.jpg","archive/조직도.jpg","archive/조직도1.jpg","archive/집.jpg","archive/탐사.jpg",
 "archive/티티.jpg","archive/황색.jpg","archive/황색유물.jpg","archive/황표의식.jpg"]
GLYPHS = ["glyphs/10.jpg","glyphs/11.jpg","glyphs/12.jpg","glyphs/16.jpg","glyphs/2.jpg","glyphs/3.jpg",
 "glyphs/4.jpg","glyphs/6.jpg","glyphs/7.jpg","glyphs/8.jpg","glyphs/9.jpg","glyphs/Untitled-1.jpg",
 "glyphs/군중.jpg","glyphs/의식.jpg","glyphs/이집트돌.jpg","glyphs/인물.jpg","glyphs/표식.jpg","glyphs/황표.jpg"]
ARCHIVE = ["assets/"+p for p in ARCHIVE]
GLYPHS = ["assets/"+p for p in GLYPHS]

KEYWORD_MAP = [
 (["검은 형제단","검은형제단"], "assets/archive/검은형제단.jpg"),
 (["툴레","나치","히틀러","에크하르트"], "assets/archive/나치.jpg"),
 (["네프렌","파라오","이집트"], "assets/archive/이집트_지하.jpg"),
 (["델타 그린"], "assets/archive/작전임무회의.jpg"),
 (["다곤","딥 원","심해","히드라"], "assets/archive/심해인.jpg"),
 (["황색 사인","황색 표식","황색의 인","하스터","카르코사"], "assets/archive/황표의식.jpg"),
 (["별의 지혜","트라페조헤드론"], "assets/archive/보석.jpg"),
 (["은빛 여명"], "assets/archive/문양.jpg"),
 (["녹색 불꽃","비이야키"], "assets/archive/새.jpg"),
 (["남극 탐사","미스캐토닉 대학","탐사"], "assets/archive/탐사.jpg"),
 (["네크로노미콘","에이본의 서","우나우스","드 에르미스","포나코틱"], "assets/archive/서류책.jpg"),
 (["미라"], "assets/archive/미라.jpg"),
 (["스타리 위즈덤","의식"], "assets/archive/의식사제.jpg"),
 (["아자토스"], "assets/portraits/azathoth-glyph.jpg"),
 (["크툴루(Cthulhu)"], "assets/portraits/portrait-06.jpg"),
]

def assign_img(n):
    text = n['label'] + ' ' + (n.get('desc') or '')
    for kws, img in KEYWORD_MAP:
        if any(k in text for k in kws):
            return img
    h = abs(hash(n['id']))
    if n['type'] == '개체':
        return PORTRAITS[h % len(PORTRAITS)]
    if n['type'] in ('조직','사건'):
        return ARCHIVE[h % len(ARCHIVE)]
    if n['type'] in ('유물','개념','작품','종족','장소'):
        return GLYPHS[h % len(GLYPHS)]
    return None

for n in data['nodes']:
    n['img'] = assign_img(n)

payload = {"nodes": data['nodes'], "links": data['links'], "timeline": timeline}
js = json.dumps(payload, ensure_ascii=False)

tpl = open('./template.html', encoding='utf-8').read()
html = tpl.replace("/*__DATA__*/", js)
open('./index.html','w',encoding='utf-8').write(html)
print("nodes:",len(data['nodes']),"links:",len(data['links']),"notes:",sum(1 for n in data['nodes'] if n.get('note')))
