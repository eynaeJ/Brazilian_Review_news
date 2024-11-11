import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Home",
    page_icon="📈",
    layout='wide'
)

# arquivo_image= r"repos/proggramacao_python/projeto2/img1_acidente.jpg"
image = Image.open('img1_acidente.jpg')
st.sidebar.image(image, width=120)

st.sidebar.markdown('# Brazil reviews')
st.sidebar.markdown( '##### *Car accidents in Brazil from 2017 to 2021*')
st.sidebar.markdown("""---""")



st.markdown('#')
st.sidebar.markdown('## As 10 maiores e menores causas de acidentes')

st.markdown("""
    The brazilian reviews was be creater to show to brazilian people how is the behavior of the brazilian traffic.
    ### how you can use this information?:
    - the more causes of accidents
    - the less causes of accidents
    - graph's and table's
    - map and more informations
    do you wanna some help?
    send me a message: jjk""")

st.write('# Brazilian Reviews Acidents to period')

