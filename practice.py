import streamlit as st

# 버튼
if st.button('click me'):
    st.write('you clicked')

# 버튼(하이퍼링크)
if st.button('Go to NAVER'):
    st.markdown('[](https://naver.com)')

# 슬라이드
age = st.slider('Select Age', 0, 120, 0, 1)
st.write('Your age : ', age)

# 멀티셀렉트
options = st.multiselect('Select your options', ['blind', 'deaf', 'mobility impairment', 'others'])
st.write('You selected : ', options)

# 컬럼 레이아웃
col1, col2 = st.columns(2)
with col1:
    st.write("This is column 1")
with col2:
    st.write("This is column 2")

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