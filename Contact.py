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

st.title("📞 Contact Me")

st.write("Feel free to send a message!")

name = st.text_input("Name")
email = st.text_input("Email")
message = st.text_area("Your Message")

if st.button("Submit"):
    if name and email and message:
        st.success("✅ Message sent successfully!")
    else:
        st.error("⚠️ Please fill out all fields.")

st.divider()

st.subheader("🌐 Let's connect on social media!")

st.write("📧 Email: cojahazel737@gmail.com")
st.write("🐙Github: https://github.com/hazel-coja")
st.write("📱 Phone: +639485137157")

st.caption("✨ Thanks for visting my portfolio!")


