import streamlit as st

# Header
st.header('Wira :t-rex:')
st.subheader('Calculator')

c1, c2, c3 = st.columns(3)

with c1:
  x = st.number_input('Number ',value=100)
  st.write('=>: ')
with c2:
  satuan = st.selectbox(
    'Operator',
    ('+', '-', 'x', ':'),key='k1')
  st.write(':sword:')
with c3:
  y = st.number_input('Number  ',value=100)

# Operasi matematika dan penampilan hasil
if satuan == '+':
  result = x + y
elif satuan == '-':
  result = x - y
elif satuan == 'x':
  result = x * y
elif satuan == ':':
    if y != 0:
      result = x / y
    else:
      result = "Tidak bisa melakukan pembagian dengan nol"

  
st.write(x,satuan,y,' = ',result)

st.caption('Copyright @ AVL Corp. 2024')
