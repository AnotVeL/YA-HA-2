import streamlit as st

# Header
st.header('Wira :sparkles:')
st.subheader('Plot')

c1, c2 = st.columns(2)

with c1:
  x = st.number_input('Suhu ',value=100)
  st.write('=>: ')
with c2:
  satuan = st.selectbox(
    'Satuan',
    ('+', '-', 'x', ':'),key='k1')
    st.write(':sparkles: ')
st.write(x,'',satuan,' = ',' ')

st.caption(Copyright)
