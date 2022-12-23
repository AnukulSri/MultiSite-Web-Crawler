import streamlit as st
import mysql.connector
import base64

st.set_page_config(page_title="Web Crawler",layout="centered",page_icon=":bar_chart:")
st.markdown("""
<style>
.css-9s5bis.edgvbvh3{
    visibility :hidden;
}
.css-1q1n0ol.egzxvld0{
    visibility : hidden;
}
</style>
""",unsafe_allow_html=True)
tabs_font_css = """
<style>


div[class*="stTextInput"] label {
  font-size: 2opx;
  color: black;
}
div[class*="stDateInput"]label{
    font-size:22px
    
}
</style>
"""
st.write(tabs_font_css, unsafe_allow_html=True)

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('back.jpg') 




st.markdown("<h1 style='text-align:center;color:White'>User Detail</h1>",unsafe_allow_html=True)

# Get values from database
with st.form("Information Form",clear_on_submit=True):
        Name = st.text_input("Enter Name")
        Email = st.text_input("Enter Your Email")
        Date = st.date_input("Enter todays date")
        Password=st.text_input("Enter Password")

        button = st.form_submit_button("Submit") 


        # Store the data in the database
        if button == True:
            conn = mysql.connector.connect(
                host="localhost",
                user="sqluser",
                password="password",
                database="python_db")
            cursor = conn.cursor()
            cursor.execute("INSERT INTO user_table (Name,Email,T_Date,password) VALUES (%s, %s, %s, %s)", (Name,Email,Date,Password))
            conn.commit()
            conn.close()
            st.success("Data saved successfully!")
            st.write(f''' <a target="_self" href="http://localhost:8502/">
                <button>Login</button>
                </a>
                ''',
                unsafe_allow_html=True)

