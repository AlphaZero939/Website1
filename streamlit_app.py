import streamlit as st
import requests
from streamlit_lottie import st_lottie 
from PIL import Image

from streamlit_option_menu import option_menu

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
lottie_coding = load_lottieurl("https://lottie.host/a46363a5-a123-4a0e-917a-3daf035a0a09/XLBe6YSBDY.json")
#lottie_pics = Image.open("images\WTF.jpg")



st.set_page_config(page_title="Website1", page_icon=":tada:", layout="wide")

menu_bar_selected = option_menu(
    menu_title=None,
    options=["Home", "Education Background", "Curriculum Vitae", "Others"],
    icons=["house", "book", "trophy"],
    orientation="horizontal",
        styles={
            "container": {"padding": "0!important", "background-color": "#1b1f1b"}, 
            "icon": {"color": "orange", "font-size": "25px"},
            "nav-link": {"font-size": "25px", "text-align": "center", "margin": "0px", "--hover-color": "#406340", "color": "white"},
            "nav-link-selected": {"background-color": "gray"},
        }
)

if menu_bar_selected == "Home":
    with st.container():
        st.subheader("Hello World :smile:")
        st.title("Welcome to my website!:smile:")
        st.write("How do you like it? :apple:")

elif menu_bar_selected == "Education Background":
    st.subheader("I got a degree in Computer Science :smile:")
    st.title("Not to brag:smile:")
    st.write("HAHAHAhAhahAHAHA :apple:")

elif menu_bar_selected == "Curriculum Vitae":
    st.subheader("I ran 100m in the Olympics LMAO :smile:")
    st.title("I diffed the other runners GG EZ:smile:")
    st.write("HAHAHAhAhahAHAHA :apple:")
else:
    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.header("This is left!")
            st.lottie(lottie_coding, height=300, width=500, key="coding", speed=1, loop=True)
            #st.image(lottie_pics, width=500, )
        with right_column:
            st.header("This is right!")
            st.write("This is below right!")
            st.write("[YT >](https://www.youtube.com/)")

with st.container():
    st.write("---")
    st.write("Developed by K.K :brain:")




