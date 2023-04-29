import streamlit as st
from bs4 import BeautifulSoup
import requests
import base64
from streamlit_option_menu import option_menu
#import mysql.connector



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
add_bg_from_local('abstract.jpg') 
with st.sidebar:
 selected= option_menu(
        menu_title="Main Menu",
        options=["Amazon","FlipKart","Compare Product","About","Admin"],
        default_index=0,
        icons=["cart-dash-fill","cart","cart-check-fill","file-text","person-fill"],
        menu_icon="cast",
)


##############################################
##############################################
if selected == "Amazon":
  
    st.markdown("<h1 style='text-align:center; color:Black'>Web Scrapper</h1>",unsafe_allow_html=True)
    with open("myStyle.css") as myStyle:
              st.markdown(f"<style>{myStyle.read()}</style>",unsafe_allow_html=True)
            
    with st.form("Search"):
      query = st.text_input("Enter a Product name")
      btn = st.form_submit_button("Submit") 
    st.markdown("<h3>At Amazon</h3>",unsafe_allow_html=True)
    url2 = f'https://www.amazon.in/s?k={query}'
    response = requests.get(url2)
    htmlcontent = response.content
    soup = BeautifulSoup(htmlcontent, 'html.parser')
    titles1 = []
    prices1 = []
    images = []
    linker=[]
    rating=[]
    for d in soup.find_all('div', attrs={'class':'s-card-container s-overflow-hidden aok-relative puis-include-content-margin puis s-latency-cf-section s-card-border'}):
      title = d.find('span', attrs={'class':'a-size-medium a-color-base a-text-normal'})

      price = d.find('span', attrs={'class':'a-offscreen'})

      image = d.find('img', attrs={'class':'s-image'})
      linkk= d.find('a',attrs={'class':'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'})
      rate = d.find('span',attrs={'class':'a-icon-alt'})
    
      titles1.append(title.string)
      prices1.append(price.string)
      images.append(image.get('src'))
      linker.append(linkk.get('href'))
      rating.append(rate.string)

    if btn:

        list_of_tup = list(zip(titles1,prices1))
        for j in range(0,len(titles1)):
           with open("myStyle.css") as myStyle:
              st.markdown(f"<style>{myStyle.read()}</style>",unsafe_allow_html=True)
            
           st.markdown(
            f"""<table class="table-borderless" style="width:1000px;">
              <tbody>
                <tr>
                    <td style="width:15%">
                        <img src="{images[j]}"style="width:65px;height:100px;">
                    </td>
                    <td style="width:45%">
                    {titles1[j]}
                    </td>
                    <td style="width:10%">
                    {prices1[j]}
                    </td>
                    <td style="width:15%">
                    {rating[j]}
                    </td>
                    <td style="width:15%">
                        <a href="https://www.amazon.in{linker[j]}">Read More</a>
                    </td>
                </tr>
              </tbody>
            </table>""",unsafe_allow_html=True)
###################################################

###################################################
if selected == "FlipKart":
    st.markdown("<h1 style='text-align:center; color:Black'>Web Scrapper</h1>",unsafe_allow_html=True)
    with open("myStyle.css") as myStyle:
              st.markdown(f"<style>{myStyle.read()}</style>",unsafe_allow_html=True)
    with st.form("Search",):
      query = st.text_input("Enter a Product name")
      btn = st.form_submit_button("Submit") 
    st.markdown("<h3>At Flipkart</h3>",unsafe_allow_html=True)
    url1 = f'https://www.flipkart.com/search?q={query}'
    response = requests.get(url1)
    htmlcontent = response.content
    soup = BeautifulSoup(htmlcontent, 'html.parser')
    titles = []
    prices = []
    images1 = []
    linker = []
    rating=[]
    for d in soup.find_all('div', attrs={'class':'_2kHMtA'}):
        title = d.find('div', attrs={'class':'_4rR01T'})

        price = d.find('div', attrs={'class':'_30jeq3 _1_WHN1'})

        image = d.find('img', attrs={'class':'_396cs4'})
        linkk = d.find('a',attrs={'class':'_1fQZEK'})
        rate = d.find('div',attrs={'class':'_3LWZlK'})
        

        titles.append(title.string)
        prices.append(price.string)
        images1.append(image.get('src'))
        linker.append(linkk.get('href'))
        rating.append(rate.text)
    if btn:

        list_of_tup = list(zip(titles,prices))
        for j in range(0,len(titles)):
            st.markdown(
            f"""<table class="table-borderless" style="width:1000px;">
                <tr>
                    <td style="width:15%">
                        <img src="{images1[j]}"style="width:65px;height:100px;">
                    </td>
                    <td style="width:45%">
                    {titles[j]}
                    </td>
                    <td style="width:10%">
                    {prices[j]}
                    </td>
                    <td style = "width:15%">
                    {rating[j]}
                    </td>
                    <td style="width:15%">
                        <a href="https://www.flipkart.com{linker[j]}">Read More</a>
                    </td>
                </tr>
            </table>""",unsafe_allow_html=True)
####################################################
####################################################


if selected == "Compare Product":
    st.markdown("<h1 style='text-align:center; color:Black'>Web Scrapper</h1>",unsafe_allow_html=True)
    with open("myStyle.css") as myStyle:
              st.markdown(f"<style>{myStyle.read()}</style>",unsafe_allow_html=True)
    with st.form("Search"):
      query = st.text_input("Enter a Product name")
      btn = st.form_submit_button("Submit") 

    st.markdown("<h3>At Amazon</h3>",unsafe_allow_html=True)
    url2 = f'https://www.amazon.in/s?k={query}'
    response = requests.get(url2)
    htmlcontent = response.content
    soup = BeautifulSoup(htmlcontent, 'html.parser')
    titles1 = []
    prices1 = []
    images = []
    linker=[]
    rating = []
    for d in soup.find_all('div', attrs={'class':'s-card-container s-overflow-hidden aok-relative puis-include-content-margin puis s-latency-cf-section s-card-border'}):
      title = d.find('span', attrs={'class':'a-size-medium a-color-base a-text-normal'})

      price = d.find('span', attrs={'class':'a-offscreen'})

      image = d.find('img', attrs={'class':'s-image'})
      linkk= d.find('a',attrs={'class':'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'})
      rate = d.find('span',attrs={'class':'a-icon-alt'})
    
      titles1.append(title.string)
      prices1.append(price.string)
      images.append(image.get('src'))
      linker.append(linkk.get('href'))
      rating.append(rate.string)
    if btn:

        list_of_tup = list(zip(titles1,prices1))
        for j in range(0,len(titles1)):
            st.markdown(
            f"""<table class="table-borderless" style="width:1000px;">
                <tr>
                    <td style="width:15%">
                        <img src="{images[j]}"style="width:65px;height:100px;">
                    </td>
                    <td style="width:45%">
                    {titles1[j]}
                    </td>
                    <td style="width:10%">
                    {prices1[j]}
                    </td>
                    <td style="width:15%">
                    {rating[j]}   
                    </td>
                    <td style="width:15%">
                        <a href="https://www.amazon.in{linker[j]}">Read More</a>
                    </td>
                </tr>
            </table>""",unsafe_allow_html=True)
####################################################

    st.markdown("<h3>At Flipkart</h3>",unsafe_allow_html=True)
    url1 = f'https://www.flipkart.com/search?q={query}'
    response = requests.get(url1)
    htmlcontent = response.content
    soup = BeautifulSoup(htmlcontent, 'html.parser')
    titles = []
    prices = []
    images = []
    linker = []
    rating =[]
    for d in soup.find_all('div', attrs={'class':'_2kHMtA'}):
        title = d.find('div', attrs={'class':'_4rR01T'})
        price = d.find('div', attrs={'class':'_30jeq3 _1_WHN1'})
        image = d.find('img', attrs={'class':'_396cs4'})
        linkk = d.find('a',attrs={'class':'_1fQZEK'})
        rate = d.find('div',attrs={'class':'_3LWZlK'})

        titles.append(title.string)
        prices.append(price.string)
        images.append(image.get('src'))
        linker.append(linkk.get('href'))
        rating.append(rate.text)
    if btn:

        list_of_tup = list(zip(titles,prices))
        for j in range(0,len(titles)):
            st.markdown(
            f"""<table class="table-borderless" style="width:1000px;">
                <tr>
                    <td style="width:15%">
                        <img src="{images[j]}"style="width:65px;height:100px;">
                    </td>
                    <td style="width:45%">
                    {titles[j]}
                    </td>
                    <td style="width:10%">
                    {prices[j]}
                    </td>
                    <td style="width:15%">
                    {rating[j]}
                    </td>
                    <td style="width:15%">
                        <a href="https://www.flipkart.com{linker[j]}">Read More</a>
                    </td>
                </tr>
            </table>""",unsafe_allow_html=True)
####################################################
####################################################


if selected =="About":
 st.markdown("<h1 style ='text-align:center;color:Black'>About</h1>",unsafe_allow_html=True)
 st.markdown("<p style = 'color:Black; font-size: 20px;'>A WebCrawler starts with a list of URLs to visit, called the SEEDS. As the crawler visits these URLs, it identifies all the hyperlinks in the page and adds them to the list of URLs to visit, called the CRAWL FRONTIER.</p>",unsafe_allow_html=True)
 st.markdown("<p style = 'color:Black; font-size: 20px;'>URLs from the frontier are recursively visited according to a set of policies. If the crawler is performing archiving of websites it copies and saves the information as it goes. </p>",unsafe_allow_html=True)
 st.markdown("<p style = 'color:Black; font-size: 20px;'>The main purpose of this project is to save the customer’s time and money, as the users gets the information clearly and they can choose their desired books. </p>",unsafe_allow_html=True)
 st.markdown("<p style = 'color:Black; font-size: 20px;'>It provides the comparison of a product to the users so that they can make the best choice.</p>",unsafe_allow_html=True)
 st.markdown("<p style = 'color:Black; font-size: 20px;'>This project also helps the users to find the product from the best websites available for that specific product</p>",unsafe_allow_html=True)

####################################################
####################################################

if selected == "Admin":
    tabs_font_css = """
<style>


div[class*="stTextInput"] label {
  font-size: 21px;
  color: Black;
}
</style>
"""
    st.write(tabs_font_css, unsafe_allow_html=True)
    st.markdown("<h1 style ='text-align:center;color:black' >Admin Portal</h1>",unsafe_allow_html=True)
    
    with st.form("Information Form",clear_on_submit=True):
        Name= st.text_input("Enter Name")
        Password=st.text_input("Enter Password")
        button = st.form_submit_button("Submit")