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

CENTROID = (37.5665, 126.9780)

places = [
    {"name": "Gyeongbokgung Palace (경복궁)","lat":37.579617,"lon":126.977041,"desc":"조선 시대 대표 궁궐"},
    {"name": "Changdeokgung & Secret Garden (창덕궁/후원)","lat":37.5795,"lon":126.9910,"desc":"유네스코 세계유산, 비밀정원"},
    {"name": "N Seoul Tower (남산타워)","lat":37.5511694,"lon":126.9882266,"desc":"서울 전체 조망"},
    {"name": "Bukchon Hanok Village (북촌한옥마을)","lat":37.5826,"lon":126.9830,"desc":"한옥 거리 산책"},
    {"name": "Myeongdong (명동)","lat":37.560974,"lon":126.986036,"desc":"쇼핑, 스트리트푸드 중심"},
    {"name": "Insadong (인사동)","lat":37.5744,"lon":126.9849,"desc":"전통 공예, 찻집"},
    {"name": "Hongdae (홍대)","lat":37.5572,"lon":126.9226,"desc":"젊은층 문화, 공연, 카페"},
    {"name": "DDP (동대문 디자인 플라자)","lat":37.5663,"lon":127.0090,"desc":"현대 디자인 랜드마크"},
    {"name": "Lotte World Tower / Mall (잠실)","lat":37.5131,"lon":127.1025,"desc":"전망대, 쇼핑몰, 타워"},
    {"name": "Hangang (한강공원)","lat":37.5172,"lon":126.9368,"desc":"야경, 유람선, 자전거"},
]

m = folium.Map(location=CENTROID, zoom_start=12, control_scale=True)
for p in places:
    popup_html = f"<b>{p['name']}</b><br>{p['desc']}"
    folium.Marker(
        location=(p["lat"], p["lon"]),
        popup=popup_html,
        tooltip=p["name"],
        icon=folium.Icon(color="blue", icon="info-sign")
    ).add_to(m)

folium.LayerControl().add_to(m)

map_html = m._repr_html_()

# height 줄였다 (원래 650 → 520)
html(map_html, height=520)

# ===== 여기 추가: 10곳 요약 소개 =====
st.subheader("10개 관광지 요약")
for idx, p in enumerate(places, start=1):
    st.markdown(f"**{idx}. {p['name']}** — {p['desc']}")

# ===== 코드 보기 =====
with open(__file__, "r", encoding="utf-8") as f:
    code_contents = f.read()

st.subheader("앱 코드 (복사해서 사용)")
st.code(code_contents, language="python")

requirements_txt = """streamlit
folium
"""

st.download_button("Download requirements.txt", data=requirements_txt, file_name="requirements.txt", mime="text/plain")
st.download_button("Download this app (app.py)", data=code_contents, file_name="app.py", mime="text/x-python")
