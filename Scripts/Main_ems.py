import streamlit as st

from streamlit_option_menu import option_menu
import re
import account 
import home
st.set_page_config(
    page_title="Employee Management System",
)


class MultiApp:

    def __init__(self):
        self.apps = []

    def run(self):
        with st.sidebar:
            app = option_menu(
                menu_title='EMS',
                options=['Home', 'Login'],
                icons=['house-fill', 'person-circle'],
                menu_icon='people-fill',
                default_index=0,
                styles={
                    "container": {"padding": "5!important", "background-color": '#0A0808'},
                    "icon": {"color": "white", "font-size": "20px"},
                    "nav-link": {"color": "white", "font-size": "20px",
                                 "text-align": "left", "margin": "0px",
                                 "--hover-color": "blue"},
                    "nav-link-selected": {"background-color": "#02ab21"},
                    "menu-title": {"color": "white"},
                }
                
            )
        
        if app == "Home":
            home.app()
        elif app == "Login":
            account.app1()
    

if __name__ == "__main__":

    app = MultiApp()
    app.run()
