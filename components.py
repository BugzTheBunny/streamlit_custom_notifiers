import streamlit as st

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
    st.markdown(f'<link href="{url}" rel="stylesheet">', unsafe_allow_html=True)


class stNotification:
    def __init__(self,text,spinner=True):
        if spinner:
            self.notification = f'''
            <div class="custom-notification">
                <div class="flex-container">
                    <div>
                        <div class="loader"></div>
                    </div>
                    <div style="margin-left:1rem;">
                        {text}
                    </div>
                </div>
            </div>'''
        else:
            self.notification = f'''
            <div class="custom-notification">
                <div class="flex-container">
                    <div style="margin-left:1rem;margin-right:1rem;">
                        {text}
                    </div>
                </div>
            </div>'''
            
    def __enter__(self):
        self.notification_object = st.markdown(self.notification, unsafe_allow_html=True) 

    def __exit__(self, *args, **kwargs):
        self.notification_object.empty()