import streamlit as st

st.header('st.selectbox')

option = st.selectbox(
	'What is your fabvorite color?',
	('青','赤','緑'))

st.write('Your favorite color is ', option)

