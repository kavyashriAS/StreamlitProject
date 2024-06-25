import streamlit as st
import datetime

# Sample credentials
USERNAME = "admin"
PASSWORD = "password"

# Function to validate login credentials
def validate_login(username, password):
    return username == USERNAME and password == PASSWORD

# Login Page
def login():
    st.title("Login Page")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if validate_login(username, password):
            st.session_state["logged_in"] = True
            st.session_state["username"] = username
            st.success("Login successful!")
            st.experimental_rerun()
        else:
            st.error("Incorrect username or password")

# Date and Time Input
def date_time_input():
    st.title("Date and Time Selection")
    date = st.date_input("Select a date", datetime.date.today())
    time = st.time_input("Select a time", datetime.datetime.now().time())
    if st.button("Submit"):
        st.session_state["date"] = date
        st.session_state["time"] = time
        st.session_state["submitted"] = True
        st.experimental_rerun()

# Display Section
def display_section():
    st.title("Display Section")
    if "date" in st.session_state and "time" in st.session_state:
        st.write(f"Selected Date: {st.session_state['date']}")
        st.write(f"Selected Time: {st.session_state['time']}")
        
        if st.checkbox("Show additional information"):
            st.write("Here is some additional information about the user.")
        
        text_size = st.slider("Adjust text size", 10, 50, 20)
        st.markdown(f"<h1 style='font-size:{text_size}px;'>This is a text with varying size click on the slider to increse or decrease the size</h1>", unsafe_allow_html=True)

        # Animation (using a simple spinner)
        with st.spinner("Loading..."):
            import time
            time.sleep(2)
        st.success("Animation completed!")

# Profile Picture Upload
def profile_picture():
    st.title("Profile Picture")
    profile_pic = st.file_uploader("Upload your profile picture", type=["jpg", "png"])
    if profile_pic is not None:
        st.image(profile_pic, caption="Profile Picture", use_column_width=True)

# Main application logic
def main():
    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False
    
    if not st.session_state["logged_in"]:
        login()
    else:
        st.sidebar.success(f"Welcome {st.session_state['username']}!")
        profile_picture()
        date_time_input()
        
        if "submitted" in st.session_state and st.session_state["submitted"]:
            display_section()

if __name__ == "__main__":
    main()
