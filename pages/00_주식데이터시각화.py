import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
from datetime import datetime, timedelta

st.set_page_config(page_title="글로벌 시총 Top 10 주가 변화", layout="wide")

st.title("🌍 글로벌 시가총액 Top 10 기업의 최근 3년 주가 변화")

# 시총 Top 10 기업 및 티커
companies = {
    "Apple": "AAPL",
    "Microsoft": "MSFT",
    "Saudi Aramco": "2222.SR",
    "Alphabet (Google)": "GOOGL",
    "Amazon": "AMZN",
    "Nvidia": "NVDA",
    "Berkshire Hathaway": "BRK-B",
    "Meta (Facebook)": "META",
    "Tesla": "TSLA",
    "TSMC": "TSM",
}

# 날짜 설정 (최근 3년)
end_date = datetime.today()
start_date = end_date - timedelta(days=3*365)

# 사용자 선택 (멀티 선택)
selected = st.multiselect("📌 시각화할 기업을 선택하세요:", options=list(companies.keys()), default=list(companies.keys())[:5])

# 데이터 가져오기 및 시각화
if selected:
    fig = go.Figure()
    for name in selected:
        ticker = yf.Ticker(companies[name])
        hist = ticker.history(start=start_date.strftime('%Y-%m-%d'), end=end_date.strftime('%Y-%m-%d'))
        if not hist.empty:
            fig.add_trace(go.Scatter(x=hist.index, y=hist["Close"], name=name))
        else:
            st.warning(f"⚠️ {name} ({companies[name]})의 데이터를 불러오지 못했습니다.")
    
    fig.update_layout(
        title="최근 3년간 종가 비교",
        xaxis_title="날짜",
        yaxis_title="종가 (USD 또는 현지통화)",
        height=600
    )
    st.plotly_chart(fig, use_container_width=True)
else:
    st.info("👆 하나 이상의 기업을 선택해 주세요.")
