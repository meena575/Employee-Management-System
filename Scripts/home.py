import streamlit as st
def app():
    st.markdown("<h1 style='text-align: center;'>Employee Management System</h1>", unsafe_allow_html=True)

         # Load the image
    image="https://www.pockethrms.com/wp-content/uploads/2022/01/Happy-Workforce.jpg"    
        # Get the width of the image
    image_width = 500
        
        # Calculate the left margin to center the image
        #left_margin = (st.sidebar.columns[0].width - image_width) / 2
        
        # Center the image using Streamlit layout options
    st.markdown(
            f'<div style="text-align:center;">'
            f'<img src="{image}" style="width:500px">'
            '</div>',
            unsafe_allow_html=True
        )
        #st.image("https://global-uploads.webflow.com/625d567276661e857102867d/63cd55af57b94e9886e36427_A%20Beginners%20Guide%20to%20Employee%20Management%20System.png",width=400)
    
    st.markdown("<p style='text-align: center;'>This is a web Application developed by Meena Reddimpalli</h1>", unsafe_allow_html=True)
