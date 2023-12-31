import streamlit as st

st.title("Streamlit demo Marce AI ")
st.header("Mi primera vez Streamlit")
st.subheader("Dec 31, 2023 :) "  )
st.text("This is some basic text")

st.warning("This is a warning")
st.info("This is some info")
st.success("This is some sucess")
st.error("This us a error")

if st.checkbox("Select/Unselect"):
    st.text("User selected the text box")
else:
    st.text("User has not selected the text box")

state = st.radio("What is your fav color?", ("red", "green", "blue"))

if state == "green":
    st.success("That is my fav color")

occupation = st.selectbox("What do you do?", ["Student", "Vlogger", "Other"])
st.text(f"Selected option is {occupation}")

if st.button("Example button"):
    st.error("You clicked it")

st.sidebar.header("Heading of sidebar")
st.sidebar.text("Created by Marcela HB")
