import streamlit as st
from string import Template


def local_css(file_name):
    """
    Injects custom CSS from the file you give it.
    """
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


def remote_css(url):
    """
    Injects css from the web
    """
    st.markdown(f'<link href="{url}" rel="stylesheet">',
                unsafe_allow_html=True)


class stNotification:
    def build_style(self):
        "Getting theme colors"
        pc = st.get_option('theme.primaryColor')
        bc = st.get_option('theme.backgroundColor')
        sbc = st.get_option('theme.secondaryBackgroundColor')
        tc = st.get_option('theme.textColor')
        return {'pc': pc, "bc": bc, "sbc": sbc, "tc": tc}

    def __init__(self, text="lorem", spinner=True):
        "Getting default theme and building style"
        styles = self.build_style()

        "Spinner"
        if spinner:
            loader = f'<div ><div class = "loader" style ="line-height: 2rem;text-align: center;border-left: 0.3em solid {styles["pc"]};" ></div></div>'
        else:
            loader = '<br>'

        "Building notification object"
        self.notification = f'''
            <div class="custom-notification" style="top:0rem;background-color: #0E1117;border-bottom-right-radius: 9px;border-bottom-left-radius: 9px;padding: 0.5rem;position: fixed;line-height: 2rem;text-align: center;border-left: 3px solid {styles['pc']};border-right: 3px solid {styles['pc']};border-bottom: 3px solid {styles['pc']}">
                <div style="display: flex;flex-wrap: nowrap;">
                    {loader}
                    <div style="margin-left:1rem;">
                        {text}
                    </div>
                </div>
            </div>
            '''

    def __enter__(self):
        self.notification_object = st.markdown(
            self.notification, unsafe_allow_html=True)

    def __exit__(self, *args, **kwargs):
        self.notification_object.empty()
