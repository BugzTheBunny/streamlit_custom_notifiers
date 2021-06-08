import streamlit as st
import components as cc
import time


def main():
    # Settings
    st.set_page_config(layout="wide", page_title='Inshop Analytics tool')
    st.set_option('deprecation.showPyplotGlobalUse', False)

    # Loading CSS
    cc.local_css("css/styles.css")
    cc.remote_css('https://fonts.googleapis.com/icon?family=Material+Icons')

    st.sidebar.write('Sidebar to take space.')

    st.write('Test of counting without spinner')
    # Testing stNotification
    with cc.stNotification("Counting till 5... without spinner", spinner=False):
        for i in range(5):
            st.write(i+1)
            time.sleep(1)

    st.write('Test of counting with spinner')

    with cc.stNotification("Counting till 5... with a spinner"):
        for i in range(5):
            st.write(i+1)
            time.sleep(1)


if __name__ == '__main__':
    main()
