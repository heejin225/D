import streamlit as st
import folium
from streamlit_folium import st_folium

# 관광지 + 해변지 정보 통합
locations = {
    "암스테르담 🛶": {
        "위치": [52.3676, 4.9041],
        "설명": "운하와 자전거 천국인 네덜란드 수도예요! 🚴‍♀️반 고흐 미술관, 안네 프랑크의 집은 필수 방문 🎨",
        "이미지": "https://d2mgzmtdeipcjp.cloudfront.net/files/good/2024/10/10/17285308469954.jpg"
    },
    "로테르담 🏙️": {
        "위치": [51.9225, 4.47917],
        "설명": "현대 건축의 끝판왕! 🏗️ 큐브 하우스, 마르크탈은 꼭 봐야 해요 🧀",
        "이미지": "https://www.google.com/url?sa=i&url=https%3A%2F%2Ftheuhak.com%2Fholland-infom%2F%3Fbmode%3Dview%26idx%3D1786651&psig=AOvVaw0zHaOzsOwbpyh-K0y5Xp9-&ust=1749633411451000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCICu88LC5o0DFQAAAAAdAAAAABAE"
    },
    "킨더다이크 🌬️": {
        "위치": [51.8833, 4.6333],
        "설명": "전통 풍차가 가득한 동화 같은 마을! 🌾 UNESCO 세계유산이기도 해요 🌍",
        "이미지": "https://img.freepik.com/premium-photo/windmills-kinderdijk-holland-netherlands_163782-7155.jpg"
    },
    "델프트 🏺": {
        "위치": [52.0116, 4.3571],
        "설명": "도자기와 요한 페르메르의 도시 🎨 운하와 고풍스런 거리 풍경이 아름다워요 🏘️",
        "이미지": "https://d3b39vpyptsv01.cloudfront.net/photo/1/2/bf4e65182175c1beabda099c11888504.jpg"
    },
    "위트레흐트 ⛪": {
        "위치": [52.0907, 5.1214],
        "설명": "중세 느낌 물씬 나는 대학교 도시 🎓 돔 타워 꼭 올라가보세요! 🏰",
        "이미지": "https://d3b39vpyptsv01.cloudfront.net/photo/1/2/973fe7ff8817d3db52588a866ce9581a.jpg"
    },
    "스헤베닝겐 🌊": {
        "위치": [52.1115, 4.2843],
        "설명": "🎡 부두 걷고, 해산물 먹고, 노을 지는 바다 꼭 보세요 🌅",
        "이미지": "https://mediaim.expedia.com/destination/1/7a8dffe86334c582e5ea0ba2f8856b42.jpg"
    }
}

st.set_page_config(page_title="🇳🇱 네덜란드 여행 가이드", layout="wide")
st.title("📍 네덜란드 여행 가이드 🧳")
st.markdown("풍차, 예술, 운하, 해변까지 완벽한 네덜란드 여행을 소개합니다!🤗")

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
