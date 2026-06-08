import streamlit as st

#=======================================================================================
#SIDEBAR STYLE
#=======================================================================================

st.markdown(""" <style>
            /* Sidebar background */
            section [data-testid="stSidebar"]){
            backgroung:linear-gradient(to bottom, #4F46E5, #6366F1);
            color white:
            }
            /* Sidebar text */ 
            section[data-testid="stSidebar"]* {
            color:white !important;
            }
            /* Selected page highlight*/
            section[data-testid="stSidebar"] .css-1d391kg{
            background-color:rgba(255, 255, 255,0.1);
            border-radius:10px
            }
            /* Hover Effect */
            section[data-testid="stSidebar"] a.hover{
            background-color:rgba(255, 255, 255,0.1);
            border-radius10px;
            }
            </style>
            """, unsafe_allow_html=True)

st.title("👤 About Me")

col1, col2 = st.columns([1,2])

with col1:
    st.image("pages/received_24377354578593263.jpeg", width=300)

with col2:
    st.subheader("Hazel Ann F. Coja")
    st.write("🎓 Student | 💻 Aspiring Developer")
        

st.divider()

st.markdown("📝 Introduction")
st.write("""I am a student taking a Bachelor of Science in Computer Science in DEBESMSCAT. I enjoy building simple applications using Python and Streamlit.""")
st.markdown("🛠️ Skills")
st.write("""
         Python
         Streamlit
         Basic Web Development
         Programming
         Html
         CSS
         Bootsrap
         JavaScript
         Mysql""")

st.markdown("🎯 Goals")
st.write(""" 
         Improve my programming skills, Build real_world applications, Become a professional developer in the future""")

name = st.text_input("👋 What's your name?")
if name:
    st.success(f"Nice to meet you, {name}! 👋 Get ready to learn with me.")
