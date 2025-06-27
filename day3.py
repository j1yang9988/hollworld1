import streamlit as st
st.write('Hi, hello world')

import streamlit as st
st.header('st.button')

if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')

import streamlit as st

st.header('st.selectbox')

option = st.selectbox(
     '가장 좋아하는 색상은 무엇인가요?',
     ('파랑', '빨강', '초록'))

st.write('당신이 좋아하는 색상은 ', option)