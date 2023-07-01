# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 02:33:58 2023

@author: Santhosh T N
"""

import streamlit as st

def main():
    st.title("Webinar App")
    st.write("Welcome to the webinar!")

    # Get user input
    name = st.text_input("Your Name:")
    email = st.text_input("Your Email:")
    webinar_topic = st.text_input("Webinar Topic:")

    # Submit button
    if st.button("Register"):
        if name and email and webinar_topic:
            # Save registration details
            save_registration(name, email, webinar_topic)
            st.success("Registration successful!")
        else:
            st.warning("Please fill in all fields.")

def save_registration(name, email, webinar_topic):
    # Save registration details to a database or file
    # Implement your saving logic here
    pass

if __name__ == '__main__':
    main()
