import streamlit as st
import folium
from streamlit_folium import st_folium

# 관광지 + 해변지 정보 통합
locations = {
    "암스테르담 🛶": {
        "위치": [52.3676, 4.9041],
        "설명": "운하와 자전거 천국인 네덜란드 수도예요! 🚴‍♀️\n반 고흐 미술관, 안네 프랑크의 집은 필수 방문 🎨",
        "이미지": "https://upload.wikimedia.org/wikipedia/commons/8/80/Amsterdam_-_Damrak.jpg"
    },
    "로테르담 🏙️": {
        "위치": [51.9225, 4.47917],
        "설명": "현대 건축의 끝판왕! 🏗️ 큐브 하우스, 마르크탈은 꼭 봐야 해요 🧀",
        "이미지": "https://upload.wikimedia.org/wikipedia/commons/e/e2/Rotterdam_Skyline.jpg"
    },
    "킨더다이크 🌬️": {
        "위치": [51.8833, 4.6333],
        "설명": "전통 풍차가 가득한 동화 같은 마을! 🌾 UNESCO 세계유산이기도 해요 🌍",
        "이미지": "https://upload.wikimedia.org/wikipedia/commons/0/00/Kinder1.JPG"
    },
    "델프트 🏺": {
        "위치": [52.0116, 4.3571],
        "설명": "도자기와 요한 페르메르의 도시 🎨\n운하와 고풍스런 거리 풍경이 아름다워요 🏘️",
        "이미지": "https://upload.wikimedia.org/wikipedia/commons/4/4d/Delft_view.jpg"
    },
    "위트레흐트 ⛪": {
        "위치": [52.0907, 5.1214],
        "설명": "중세 느낌 물씬 나는 대학교 도시 🎓\n돔 타워 꼭 올라가보세요! 🏰",
        "이미지": "https://upload.wikimedia.org/wikipedia/commons/5/58/Utrecht_Oudegracht.jpg"
    },
    # 해변들
    "스헤베닝겐 🌊": {
        "위치": [52.1115, 4.2843],
        "설명": "가장 인기 많은 해변이에요! 🎡\n부두 걷고, 해산물 먹고, 노을 지는 바다 꼭 보세요 🌅",
        "이미지": "https://upload.wikimedia.org/wikipedia/commons/b/b6/Scheveningen_Pier%2C_The_Hague.jpg"
    },
    "잔드보르트 안 제이 🏖️": {
        "위치": [52.3740, 4.5332],
        "설명": "암스테르담에서 30분! 🚆 활기차고 젊은 분위기의 해변 🎶",
        "이미지": "https://upload.wikimedia.org/wikipedia/commons/b/b3/Zandvoort_beach_view.jpg"
    },
    "에그몬트 안 제이 🐚": {
        "위치": [52.6183, 4.6201],
        "설명": "조용하고 아기자기한 가족형 해변 마을 🧸",
        "이미지": "https://upload.wikimedia.org/wikipedia/commons/5/54/Egmond_aan_Zee_beach.jpg"
    },
    "노르트베이크 🌺": {
        "위치": [52.2393, 4.4339],
        "설명": "고급 리조트 스타일의 도시 🛎️\n우주 박물관과 꽃길도 있어요! 🚀🌷",
        "이미지": "https://upload.wikimedia.org/wikipedia/commons/3/3e/North_Sea_Coast_at_Noordwijk.jpg"
    },
    "텍셀 섬 🐑": {
        "위치": [53.0565, 4.8040],
        "설명": "양과 맥주가 유명한 자연 천국 🐑🍺\n자전거 타고 섬 한 바퀴 돌아보세요 🚲",
        "이미지": "https://upload.wikimedia.org/wikipedia/commons/f/f4/Texel_Beach.jpg"
    }
}

st.set_page_config(page_title="🇳🇱 네덜란드 여행 가이드", layout="wide")
st.title("📍 네덜란드 여행 가이드 🧳")
st.markdown("풍차, 예술, 운하, 해변까지 완벽한 네덜란드 여행을 소개합니다! 🇳🇱")

# 지도 그리기
st.subheader("🗺️ 지도에서 관광지와 해변 보기")
map_center = [52.4, 5.2]
m = folium.Map(location=map_center, zoom_start=8)

for name, data in locations.items():
    folium.Marker(
        location=data["위치"],
        popup=f"<strong>{name}</strong><br>{data['설명']}",
        tooltip=name,
        icon=folium.Icon(color="blue", icon="info-sign")
    ).add_to(m)

st_data = st_folium(m, width=700, height=500)

# 상세 정보 표시
st.subheader("📝 관광지 및 해변 정보 자세히 보기")

for name, data in locations.items():
    with st.expander(name):
        st.image(data["이미지"], use_column_width=True)
        st.write(data["설명"])
