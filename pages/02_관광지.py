# app.py
import streamlit as st
import folium
from streamlit.components.v1 import html

st.set_page_config(page_title="Seoul Top10 (Folium)", layout="wide")

st.title("서울 — 외국인들이 좋아하는 주요 관광지 Top 10 (Folium)")
st.markdown(
    "Folium 지도로 서울의 인기 관광지 10곳을 표시합니다. "
    "마커를 클릭하면 간단한 설명이 표시됩니다."
)

# 중심 좌표(서울 시청 근처)
CENTROID = (37.5665, 126.9780)

# Top10 관광지 (이름, 위도, 경도, 짧은 설명)
places = [
    {
        "name": "Gyeongbokgung Palace (경복궁)",
        "lat": 37.579617,
        "lon": 126.977041,
        "desc": "대표적인 조선 시대 궁궐 — 한복 관광객이 많음."
    },
    {
        "name": "Changdeokgung Palace & Secret Garden (창덕궁/후원)",
        "lat": 37.5795,
        "lon": 126.9910,
        "desc": "유네스코 세계유산, 비원(비밀정원) 산책 추천."
    },
    {
        "name": "N Seoul Tower (N서울타워 / 남산)",
        "lat": 37.5511694,
        "lon": 126.9882266,
        "desc": "서울 전경을 한눈에 볼 수 있는 전망명소."
    },
    {
        "name": "Bukchon Hanok Village (북촌한옥마을)",
        "lat": 37.5826,
        "lon": 126.9830,
        "desc": "한옥거리 산책과 전통문화 체험."
    },
    {
        "name": "Myeongdong (명동)",
        "lat": 37.560974,
        "lon": 126.986036,
        "desc": "쇼핑·스트리트푸드의 중심지."
    },
    {
        "name": "Insadong (인사동)",
        "lat": 37.5744,
        "lon": 126.9849,
        "desc": "전통 공예품, 찻집 골목."
    },
    {
        "name": "Hongdae (홍대 / 홍익대학교 주변)",
        "lat": 37.5572,
        "lon": 126.9226,
        "desc": "젊은층 문화·거리공연·카페가 활발한 지역."
    },
    {
        "name": "Dongdaemun Design Plaza (DDP / 동대문 디자인 플라자)",
        "lat": 37.5663,
        "lon": 127.0090,
        "desc": "현대 디자인 랜드마크, 야간 쇼핑과 야경."
    },
    {
        "name": "Lotte World Tower / Mall (잠실)",
        "lat": 37.5131,
        "lon": 127.1025,
        "desc": "초고층 타워·몰·전망대·실내 놀이공원."
    },
    {
        "name": "Hangang (한강공원 — 반포/여의도 등)",
        "lat": 37.5172,
        "lon": 126.9368,
        "desc": "한강 자전거·유람선·야경(반포 달빛무지개분수 등)."
    },
]

# Folium Map 생성
m = folium.Map(location=CENTROID, zoom_start=12, control_scale=True)

# 마커 추가
for p in places:
    popup_html = f"<b>{p['name']}</b><br>{p['desc']}"
    folium.Marker(
        location=(p["lat"], p["lon"]),
        popup=popup_html,
        tooltip=p["name"],
        icon=folium.Icon(color="blue", icon="info-sign")
    ).add_to(m)

# 선호도/그룹별 레이어(예시로 LayerControl 추가)
folium.LayerControl().add_to(m)

# Folium 지도를 Streamlit에 렌더 (html로 변환하여 삽입)
map_html = m._repr_html_()
html(map_html, height=650)

st.sidebar.header("앱 정보")
st.sidebar.markdown(
    "- Folium 기반 지도 표시\n"
    "- 마커 클릭 → 장소 설명 표시\n"
    "- 앱 파일과 requirements.txt는 아래에서 복사/다운로드 가능"
)

# 코드 보기 및 다운로드
with open(__file__, "r", encoding="utf-8") as f:
    code_contents = f.read()

st.subheader("앱 코드 (복사해서 사용하세요)")
st.code(code_contents, language="python")

st.write("아래 버튼으로 `app.py` 및 `requirements.txt` 내용을 클립보드에 복사하거나 파일로 저장하세요.")

# 다운로드용 문자열 생성 (requirements 내용은 아래와 동일하게 작성)
requirements_txt = """streamlit
folium
"""

st.download_button("Download requirements.txt", data=requirements_txt, file_name="requirements.txt", mime="text/plain")
st.download_button("Download this app (app.py)", data=code_contents, file_name="app.py", mime="text/x-python")
