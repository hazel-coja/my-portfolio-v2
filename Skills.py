import streamlit as st

#=======================================================================================
#SIDEBAR STYLE
#=======================================================================================

st.markdown(""" <style>
            /* Sidebar background */
            [data-testid="stSidebar"]){
            background:linear-gradient(to bottom, #4FACFE, #00F2FE);
            }

            /* Sidebar text color*/
            [data-testid="stSidebar"] .css=-17l744{
            color:white !important;
            }

            /* Selected page highlight*/
            [data-testid="stSidebarNav"]{
            background-color:transparent;
            border-radius:10px
            }
            </style>
            """, unsafe_allow_html=True)

st.title("🛠 My Skills")

st.write("Here are some of the skills I have leraned and continue to improve.")

st.divider()

#==============================================================================
# TECHNICAL SKILLS
#==============================================================================

st.subheader("💻 Technical Skills")

st.write("Python Programming")
st.progress(80)

st.write("Streamlit Framework")
st.progress(75)

st.write("Web Development")
st.progress(0.8)

st.write("Data Analysis")
st.progress(0.8)

st.divider()

#==============================================================================
#SOFT SKILLS
#==============================================================================

st.subheader("🤝 Soft Skills")

col1, col2, = st.columns(2)

with col1:
    st.success("✔ Communication")
    st.success("✔ Teamwork")

with col2:
    st.success("✔ Time Management")
    st.success("✔ Creativity")

st.divider()

#==============================================================================
#INTERACTIVE PART
#==============================================================================

st.subheader("📊 Rate My Skills")

options=["Python", "Communication", "Problem Solving", "Creativity"]
skill = st.selectbox("Which skill do you think is most important?", options)
                     
st.info("✨ You Selected:{skill}")

st.divider()

#==============================================================================
#FOOTER
#==============================================================================

st.caption("🚀 Continuously learning and improving every day!")