import streamlit as st

# 상태관리 로직
# 1. 상태 여부 체크
if 'counter' not in st.session_state:
    st.session_state.counter = 0

# 2. 상태 변경
if st.button('Increment', type='primary'):
    st.session_state.counter += 1

# 3. 상태 출력/활용
st.write('현재 Counter: {}'.format(
    st.session_state.counter))