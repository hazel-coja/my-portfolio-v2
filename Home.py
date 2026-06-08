import streamlit as st

st.set_page_config(page_title="My Multipage App", page_icon= "🌐", layout="wide")

#=======================================================================================
#SIDEBAR STYLE
#=======================================================================================

st.markdown(""" <style>
            /* This targets the entire sidebar background */
            [data-testid="stSidebar"]){
            backgroung:linear-gradient(135deg,#4A00E0, #8E2DE2 100%);
            }

            /* This makes the navigation text and icons white */ 
            [data-testid="stSidebarNav"] span{
            color:white !important;
            font-weightr:500;
            }

            /* This changes the color of the active page link background*/
            [data-testid="stSidebarNav"] a:hover{
            background-color:rgba(255, 255, 255,0.1);
            border-radius:10px
            }

            /* This hides the default 'Made with Streamlit' footer if you want a cleaner look */
            footer{visibility: hidden;}
            </style>
            """, unsafe_allow_html=True)

st.markdown("<div class='title'>🌐 My Portfolio</div>", unsafe_allow_html=True)
            
st.title("👋 Hello! I am Hazel Ann F. Coja")
st.write("A student learning Streamlit and building interactive web applications.")
st.divider()

#==============================================================================================
#ROW1:GRADIENT CARDS
#==============================================================================================

col1, col2, col3, col4 = st.columns(4)

#==============================================================================================
#CSS MIXIN FOR CONSISTENT CARD STYLE
#==============================================================================================
#This style uses a linear gradient(purple to blue) and white text 
card_style = """ display: flex;
                flex-direction:column;
                justify-content:space-between;
                padding:20px;
                border-radius:15px;
                color:white; /* one color for all text inside */
                height:220px; /* uniform height */
                margin-bottom:15px;
                box-shadow:0 4px 8px rgba(0,0,0,0.1);"""
gradient_background="background: linear -gradient(135deg,#8E2DE2 0%, #4A00E0 100%);"

with col1:
        st.markdown(f"""
                <div style={card_style} {gradient_background:}">
                    <h2 style="color:white; margin:0;">👤 About Me</h2>
                    <p style="color:white; font-size 14px; margin:0;">Learn more about my background, passion, and future goals in technology.</p>
                </div>
                """, unsafe_allow_html=True)
        
with col2:
        st.markdown(f"""
                <div style={card_style} {gradient_background:}"">
                     <h3>💻 Projects</h3>
                     <p>Explore the projects I have created using Python and Streamlit.</p>
                </div>
                """, unsafe_allow_html=True)
        
with col3:
        st.markdown(f""" 
                <div style={card_style} {gradient_background}> 
                    <h3>📞 Contact</h3>
                    <p>Find ways to connect with me through social media.</p>
                </div>
                """, unsafe_allow_html=True)
        
with col4:
        st.markdown(""" 
                <div class={card_style} {gradient_background}>
                    <h3>🛠 Skills</h3>
                    <p>Check out my technical stack and tools.</p>
                </div>
                """, unsafe_allow_html=True)
st.divider()
st.subheader("🚀 Quick Navigation")
col1, col2, col3, col4 = st.columns(4)

with col1: 
        st.page_link("pages/About.py", label="📄 About")

with col2:
        st.page_link("pages/Projects.py", label="💻 Projects")
         

with col3: 
            st.page_link("pages/Contact.py",label="📞 Contact")

with col4:
            st.page_link("pages/Skills.py", label="🛠 Skills")


