import streamlit as st
from PIL import Image
import time

default_img_path = "hymnals/BH001.jpg"
image_path = ""

def get_hymn_num():
    hymn_num = st.session_state["hymn_num"]
    hymn_num = hymn_num.strip(" ").lstrip("0")
    if len(hymn_num) == 1:
        hymn_num = "BH00" + hymn_num + ".jpg"
    elif len(hymn_num) == 2:
        hymn_num = "BH0" + hymn_num + ".jpg"
    elif len(hymn_num) == 3:
        hymn_num = "BH" + hymn_num + ".jpg"
    return (f"hymnals/{hymn_num}")

user_input = st.text_input(label="Enter a hymn number (1 ~ 414)",
              placeholder="196",
              max_chars=3,
              # on_change=display_hymn,
              key="hymn_num")
print("User Input = ", user_input)

if user_input:
    image_path = get_hymn_num()
    try:
        if image_path:
            st.image(image_path, caption=(f"Image for {user_input}"))
        else:
            st.warning("No image found for the given keyword.")
    except:
        st.error(f"Invalid Input: '{user_input}'")

st.write("Copyright @ KApe Technologies 2025")
