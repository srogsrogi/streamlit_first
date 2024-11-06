import streamlit as st

# 버튼
if st.button('click me'):
    st.write('you clicked')

# 버튼(하이퍼링크)
if st.button('Go to NAVER'):
    st.markdown('[naver](https://www.naver.com)')

# 버튼처럼 보이는 하이퍼링크
st.markdown(
    """
    <a href="https://www.naver.com" target="_blank">
        <button style="background-color: #4CAF50; color: white; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer;">
            Go to naver.com
        </button>
    </a>
    """,
    unsafe_allow_html=True)

# 슬라이드
age = st.slider('Select Age', 0, 120, 0, 1)
st.write('Your age : ', age)

# 셀렉트박스
option = st.selectbox("Select your gender", ["Male", "Female"])
st.write("You selected:", option)

# 멀티셀렉트
options = st.multiselect('Select your options', ['blind', 'deaf', 'mobility impairment', 'others'])
if options:
    st.markdown("**Selected options:**")
    st.markdown(", ".join([f"`{option}`" for option in options]))
else:
    st.markdown("No options selected.")

# 체크박스를 이용한 다중선택 만들기
options_ = ["blind", "deaf", "mobility impairment", "others"]
selected_options = []

for option_ in options_:
    if st.checkbox(option_):
        selected_options.append(option_)

st.write("Selected options:", selected_options)


# 탭 레이아웃
tab1, tab2 = st.tabs(["Tab 1", "Tab 2"])
with tab1:
    st.write("Content for Tab 1")
with tab2:
    st.write("Content for Tab 2")

# progress bar
import time
progress_bar = st.progress(0)
for percent in range(100):
    time.sleep(0.01)
    progress_bar.progress(percent + 1)

# spinner
with st.spinner("Loading..."):
    time.sleep(2)
st.success("Done!")

# sidebar
st.sidebar.title("Sidebar Title")
st.sidebar.slider("Adjust value", 0, 100, 50)
st.sidebar.button('click me!')