import streamlit as st
import folium
from streamlit_folium import st_folium

# 주요 관광지 정보
tourist_spots = {
    "암스테르담": {
        "위치": [52.3676, 4.9041],
        "설명": "네덜란드의 수도이자, 운하와 자전거로 유명한 도시입니다. 반 고흐 미술관, 안네 프랑크의 집 등을 방문해 보세요.",
        "이미지": "https://upload.wikimedia.org/wikipedia/commons/8/80/Amsterdam_-_Damrak.jpg"
    },
    "로테르담": {
        "위치": [51.9225, 4.47917],
        "설명": "현대적인 건축과 유럽에서 가장 큰 항구로 유명한 도시입니다. 큐브 하우스와 마르크탈을 구경해 보세요.",
        "이미지": "https://upload.wikimedia.org/wikipedia/commons/e/e2/Rotterdam_Skyline.jpg"
    },
    "킨더다이크": {
        "위치": [51.8833, 4.6333],
        "설명": "세계문화유산에 등재된 전통 풍차 마을입니다. 아름다운 풍경과 역사적인 풍차를 감상할 수 있습니다.",
        "이미지": "https://upload.wikimedia.org/wikipedia/commons/0/00/Kinder1.JPG"
    },
    "델프트": {
        "위치": [52.0116, 4.3571],
        "설명": "도자기로 유명하며 요한 페르메르의 고향입니다. 아름다운 운하와 전통 건축물이 인상적입니다.",
        "이미지": "https://upload.wikimedia.org/wikipedia/commons/4/4d/Delft_view.jpg"
    },
    "위트레흐트": {
        "위치": [52.0907, 5.1214],
        "설명": "중세 건축물이 잘 보존된 대학교 도시입니다. 돔 타워와 운하 카페가 유명합니다.",
        "이미지": "https://upload.wikimedia.org/wikipedia/commons/5/58/Utrecht_Oudegracht.jpg"
    }
}

st.set_page_config(page_title="네덜란드 관광 가이드", layout="wide")
st.title("🇳🇱 네덜란드의 주요 관광지 안내")

# 지도 생성
st.subheader("📍 관광지 지도")
m = folium.Map(location=[52.1326, 5.2913], zoom_start=8)

# 마커 추가
for name, data in tourist_spots.items():
    folium.Marker(
        location=data["위치"],
        popup=f"<strong>{name}</strong><br>{data['설명']}",
        tooltip=name,
        icon=folium.Icon(color="blue", icon="info-sign")
    ).add_to(m)

st_data = st_folium(m, width=700, height=500)

# 관광지 상세 정보
st.subheader("🌆 관광지 상세 정보")

for name, data in tourist_spots.items():
    with st.expander(name):
        st.image(data["이미지"], use_column_width=True)
        st.write(data["설명"])
