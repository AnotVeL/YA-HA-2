import streamlit as st

# Header
st.header('Wira :sparkles:')
st.subheader('Calculator')

c1, c2, c3 = st.columns(3)

with c1:
  x = st.number_input('Number ',value=100)
  st.write('=>: ')
with c2:
  satuan = st.selectbox(
    'Operator',
    ('+', '-', 'x', ':'),key='k1')
  st.write(':sparkles:')
with c3:
  y = st.number_input('Number ',value=100)

  
st.write(x,satuan,y,' = ')

st.caption('Copyright @ AVL Corp. 2024')
