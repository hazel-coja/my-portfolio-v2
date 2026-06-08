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

st.title("💻 My Projects")

project = st.selectbox("Choose a project to view:", ["Writer App"])

# ===================================================================================
# WRITER APP PROJECT
# ===================================================================================

if project == "Writer App":
    st.subheader("📝 Writer App")

    st.write("""This is my personal writing application where users can:
             write notes or short content,
             count words and characters,
             preview their writing instantly""")
    
    st.divider()

    text = st.text_area("✍️ Start Writing Here:", height=200)

    if text:
        words = len(text.split())
        characters = len(text)

        col1, col2,= st.columns(2)
        col1.metric("📝 Word Count", words)
        col2.metric("🔤 Characters Count", characters)

        st.divider()

        st.subheader("📖 Preview")
        st.write(text)

    if text:
        st.download_button(
            label="💾 Download as Text File",
            data=text,
            file_name="my_writing.txt",
            mime="text/plain"
        )