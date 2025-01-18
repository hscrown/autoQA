import streamlit as st
from dotenv import load_dotenv
import os
import audio_text
import ppt_spellchk
# python3.12 -m streamlit run main.py

# .env 파일에서 API 키 로드
load_dotenv()
api_key = os.getenv("openai_key")

# 사이드바 메뉴 버튼
st.sidebar.title("메뉴")
home_button = st.sidebar.button("홈")
audio_to_text_button = st.sidebar.button("Audio to Text")
ppt_spellchk_button = st.sidebar.button("PPT 맞춤법 검사")


# 페이지 이동을 위해 세션 상태를 설정
if home_button:
    st.session_state.page = "home"
elif audio_to_text_button:
    st.session_state.page = "audio_to_text"
elif ppt_spellchk_button:
    st.session_state.page = "ppt_spellchk"


# 페이지 내용 표시
if "page" not in st.session_state:
    st.session_state.page = "home"  # 기본값은 홈 페이지

if st.session_state.page == "home":
    st.title("홈 페이지")
    st.write("여기는 메인 홈 페이지입니다. 사이드바에서 'Audio to Text'를 선택하면 오디오 파일을 텍스트로 변환하는 페이지로 이동합니다.")

elif st.session_state.page == "audio_to_text":
    # st.title("MP3 to Text 변환기")
    audio_text.run(api_key)  # audio_txt의 run() 함수 호출

elif st.session_state.page == "ppt_spellchk":
    ppt_spellchk.run(api_key)