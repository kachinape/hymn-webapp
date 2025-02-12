import streamlit as st

st.set_page_config(page_title="Responsive Readings")

default_img_path = "responsive_readings/BRR001.jpg"
image_path = ""

def get_num():
    hymn_num = st.session_state["rr_num"]
    hymn_num = hymn_num.strip(" ").lstrip("0")
    if len(hymn_num) == 1:
        hymn_num = "BRR00" + hymn_num + ".jpg"
    elif len(hymn_num) == 2:
        hymn_num = "BRR0" + hymn_num + ".jpg"
    elif len(hymn_num) == 3:
        hymn_num = "BRR" + hymn_num + ".jpg"
    return (f"responsive_readings/{hymn_num}")

st.markdown("<h3 style='text-align: center;'>Responsive Scripture Readings</h3>", unsafe_allow_html=True)

user_input = st.text_input(label="Enter a responsive reading number (1 ~ 52)",
              placeholder="1",
              max_chars=3,
              # on_change=display_hymn,
              key="rr_num")
print("User Input = ", user_input)

if user_input:
    image_path = get_num()
    try:
        if image_path:
            st.image(image_path, caption=(f"Image for {user_input}"))
        else:
            st.warning("No image found for the given keyword.")
    except:
        st.error(f"Invalid Input: '{user_input}'")

# st.write("Copyright @ KApe Technologies 2025")