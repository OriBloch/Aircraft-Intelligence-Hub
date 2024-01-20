import streamlit as st

linkedin_link = "https://www.linkedin.com/in/ori-bloch-312768207/"
github_link = "https://github.com/OriBloch"
github_repo = "https://github.com/OriBloch/Aircraft-Intelligence-Hub"

st.set_page_config(page_icon="images/Aircraft Intelligence Hub Badge.ico")

# About Author Section
st.header("About Author and Program", divider="blue")

## About Ori Bloch
left_col, mid_col, right_col = st.columns(3)
with left_col:
    st.subheader("About Ori Bloch")

with mid_col:
    st.image("images/linkedin image-circle.png")


st.write(
    "Greetings 👋, I am Ori Bloch, a Space Industry professional with an extensive 7-year tenure in the Remote Sensing industry.\n\n"
    "In my current serve as Space Business Development Lead, strategically transitioning into a role focused on Algorithm Development 🧠.\n\n"
    "Simultaneously, I am pursuing a Bachelor's degree in ⚡ Electrical and Computer Engineering.\n\n"
    "I created this platform to solve a real-life problem and demonstrate how algorithm development can reduce the headcount for analysis, "
    "save time and money for decision-makers, and leverage the important and rising resource of Remote Sensing data.\n\n"
    "For inquiries, collaboration opportunities, or more detailed information, please feel free to connect with me on:\n"
    f"[![LinkedIn](https://img.shields.io/badge/LinkedIn-Ori_Bloch-blue?style=flat-square&logo=linkedin)]({linkedin_link})\n"
    f"[![GitHub](https://img.shields.io/badge/GitHub-Ori_Bloch-black?style=flat-square&logo=github)]({github_link})"
)
## About Aircraft Intelligence Hub

left_col2, mid_col2, right_col2 = st.columns(3)
with left_col2:
    st.subheader("About Aircraft Intelligence Hub")

with mid_col2:
    st.image("images/Aircraft Intelligence Hub Badge Small.jpg")

st.write(
    "🚀 **Problem Solved:** In response to the surge in satellite imagery in the 'New-Space' era, "
    "the Aircraft Intelligence Hub addresses the challenges of time-consuming and resource-intensive image analysis. \n\n"
    "🌍 **Use Cases:** Facilitating commercial decisions and providing intelligence insights by analyzing imagery, airport density, aircraft flow, "
    "and changes between airports. Understanding metrics like daily aircraft counts is paramount for "
    "grasping economic factors.\n\n"
        "💡 **Benefits:** This project underscores the potential of algorithms to automate and optimize the entire satellite image analysis process, delivering precision, "
    "fast insights, and easily understandable visualizations while decreasing the need for expertise in image and data anylsis.\n\n"
    f"🔍 **Source Code:** Explore the [source code on GitHub]({github_repo})"
)


st.write(

)
