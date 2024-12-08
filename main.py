import streamlit as st
from modules.users import process_user_mode
from modules.recruiters import process_recruiters_mode
from modules.admin import process_admin_mode
from modules.feedback import process_feedback_mode


# Set Streamlit Page Configuration
st.set_page_config(
    page_title="Resume Parser App",
    page_icon="❄️",
    layout="wide"
)

# Load custom background CSS with image
st.markdown("""
<style>

       .st-emotion-cache-13k62yr {
    background-image: url('https://img.freepik.com/free-vector/background-abstract-line-digital-gradient-luxury_483537-2367.jpg?t=st=1733670559~exp=1733674159~hmac=406cfb69c9cad3757f098d67d86f17a73296be5c50992c2e88a820761f85aa9a&w=1060') !important; /* Replace with your image URL or file path */
    background-size: cover;
        background-repeat: no-repeat;
        background-position: center;
        height: 100vh;
        width: 100%;
        
}
     

   
    .st-emotion-cache-m78myu h1 {
    color: #52A6AF; 
    font-size: 2.2rem; 
    font-weight: bold; 
    text-align: center; 
    text-shadow:linear-gradient(135deg, rgba(20, 25, 30, 0.8), rgba(35, 40, 50, 0.9));
    margin-top: 20px; 
    font-family: 'Poppins', sans-serif;
    line-height: 1.5;
}
            
    .st-emotion-cache-m78myu h3{
    color: #52A6AF; 
    font-size: 2rem; 
    font-weight: bold;
    text-align: center; 
    text-shadow:linear-gradient(135deg, rgba(20, 25, 30, 0.8), rgba(35, 40, 50, 0.9));
    margin-top: 20px; 
     font-family: 'Poppins', sans-serif;
    line-height: 1.4; 
}
 .st-emotion-cache-13k62yr h4{
            color: #52A6AF; 
    font-size: 2.8rem; 
    font-weight: bold;
    text-align: center; 
    text-shadow:linear-gradient(135deg, rgba(20, 25, 30, 0.8), rgba(35, 40, 50, 0.9));
    margin-top: 20px; 
     font-family: 'Poppins', sans-serif;
    line-height: 1.4;
            }
            
     .st-emotion-cache-m78myu h2 {
    color: #f5f5f5; 
    font-size: 1.4rem; 
    text-align: center; 
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5); 
    font-family: 'Poppins', sans-serif;
    line-height: 1.3; 
}

   .st-emotion-cache-h4xjwg {
    background: linear-gradient(135deg, rgba(20, 20, 20, 0.95), rgba(45, 45, 45, 0.95)); 
    border-bottom: 1px solid rgba(255, 255, 255, 0.1); /
    box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.5); 
    backdrop-filter: blur(5px); 
}

.st-emotion-cache-h4xjwg:hover {
    background: linear-gradient(135deg, rgba(30, 30, 30, 0.95), rgba(50, 50, 50, 0.95)); /* Slightly lighter on hover */
}



    /* Sidebar style with smooth interactive effects */
    [data-testid="stSidebar"] {
        background: linear-gradient(135deg, rgba(20, 25, 30, 0.8), rgba(35, 40, 50, 0.9));
    }

</style>
""", unsafe_allow_html=True)


def main():
    # Hero Section UI
    st.markdown("<h4 class='fade-in-section'>❄️CVSortify</h4>", unsafe_allow_html=True)
    st.markdown("<h2 class='fade-in-section'>A NLP-Powered Resume Parser</h2>", unsafe_allow_html=True)

    # Sidebar Navigation Logic
    st.sidebar.title("Navigation Panel")
    navigation_option = st.sidebar.radio(
        "**Select a Module:**", 
        ["Users", "Recruiters", "Feedback", "Admin Panel"]
    )

    # Main navigation logic with visual feedback
    if navigation_option == "Users":
        with st.spinner("Loading user features..."):
            process_user_mode()
    elif navigation_option == "Recruiters":
        with st.spinner("Fetching insights for recruiters..."):
            process_recruiters_mode()
    elif navigation_option == "Feedback":
        with st.spinner("Loading user feedback..."):
            process_feedback_mode()
    elif navigation_option == "Admin Panel":
        with st.spinner("Launching the admin dashboard..."):
            process_admin_mode()


if __name__ == "__main__":
    main()
