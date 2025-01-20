import openai
import streamlit as st

def transcribe_to_txt_with_api(audio_file, api_key):
    """
    MP3 파일을 OpenAI Whisper API로 변환하고 TXT로 반환하는 함수.

    Parameters:
        audio_file (file): MP3 파일
        api_key (str): OpenAI API 키

    Returns:
        str: 변환된 텍스트
    """
    # OpenAI API 키 설정
    openai.api_key = api_key

    # 오디오 파일 읽기
    response = openai.Audio.transcribe("whisper-1", audio_file)
    script = response["text"]

    return script

def run(api_key):
    # Streamlit 앱
    st.title("MP3 to Text 변환기")

    # 파일 업로드
    audio_file = st.file_uploader("MP3 파일을 업로드하세요", type=["mp3"])

    if audio_file:
        # 변환 버튼
        if st.button("텍스트로 변환"):
            with st.spinner("텍스트 변환 중..."):
                try:
                    # 텍스트 변환
                    script = transcribe_to_txt_with_api(audio_file, api_key)
                    # 원본 텍스트를 세션 상태에 저장
                    if "original_text" not in st.session_state:
                        st.session_state.original_text = script
                    # 수정된 텍스트를 별도로 세션 상태에 저장
                    if "edited_text" not in st.session_state:
                        st.session_state.edited_text = script
                except Exception as e:
                    st.error(f"오류 발생: {e}")
                    return

    # 변환된 원본 텍스트가 세션 상태에 저장되어 있으면 출력
    if "original_text" in st.session_state:
        with st.expander(f"변환 텍스트", expanded=False):
            st.markdown(st.session_state.original_text)

        # 원본 텍스트를 바탕으로 수정할 수 있도록 text_area에 표시
        edited_text = st.text_area("변경된 텍스트 (파일로 저장될 내용)", value=st.session_state.edited_text, height=200)

        # 수정된 텍스트가 변경될 때마다 세션 상태 업데이트
        if edited_text != st.session_state.edited_text:
            st.session_state.edited_text = edited_text

        # 다운로드 버튼을 누르면 수정된 텍스트를 다운로드하도록 설정
        st.download_button(
            label="TXT 파일로 다운로드",
            data=st.session_state.edited_text,  # 수정된 텍스트가 다운로드됨
            file_name="transcribed_text.txt",
            mime="text/plain"
        )
