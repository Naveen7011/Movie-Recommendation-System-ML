import streamlit as st
import joblib
import pandas as pd
import numpy as np
import requests

X=joblib.load("movie_vectors.pkl")
df=joblib.load("movie_data.pkl")
model=joblib.load("movie_model.pkl")


st.set_page_config(layout="wide")

# Sidebar Background Color
st.markdown("""
<style>
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg,#1E3C72,#2A5298);
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
h1, h2, h3 {
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)


# Header Background Color
st.markdown("""
<style>
header[data-testid="stHeader"] {
    background: linear-gradient(
        to right,
        rgba(15,32,39,0.6),
        rgba(32,58,67,0.6),
        rgba(44,83,100,0.6)
    );
}
</style>
""", unsafe_allow_html=True)


# Page Background Color
st.markdown("""
<style>
.stApp {
background: linear-gradient(
135deg,
#0B0F2A,
#1A1F5C,
#2B2F77,
#0F5F5A,
#1E8A7A
);
}
</style>
""", unsafe_allow_html=True)


# Sidebar color, font weight and font size
st.markdown("""
<style>
section[data-testid="stSidebar"] * {
    color: white;
    font-weight: bold;
    font-size: 18px;
}
</style>
""", unsafe_allow_html=True)

#Sidebar image down
st.markdown("""
<style>
section[data-testid="stSidebar"] .stImage {
    margin-top: -10px;
}

</style>
""", unsafe_allow_html=True)

st.sidebar.image("Movies.png")

st.sidebar.title("About Project")
st.sidebar.write("Objective of this project is to recommends movies based on user selection along with posters.")

st.sidebar.title("Features")
st.sidebar.write("""
💠 Recommend similar movies \n
💠 Display movie posters using API \n
💠 Interactive movie selection \n
💠 Helps users discover new and similar movies easily.
""")

st.sidebar.title("Libraries")
st.sidebar.markdown("""
⚫ 🔢 Numpy \n
⚫ 🐼 Pandas \n
⚫ 🤖 Scikit(sklearn) \n
⚫ 🎬 OMDb API
""")

st.sidebar.title("Cloud")
st.sidebar.markdown("☁️ Streamlit")

st.sidebar.title("Contact")
st.sidebar.markdown("📞9999999999")


# Header Color
st.markdown("""
<style>
h1, h2, h3, h4, h5, h6 {
    color: white !important;
}
</style>
""", unsafe_allow_html=True)

#Header height reduce and arrow visible
st.markdown("""
<style>
header[data-testid="stHeader"] {
    height: 50px;
}

/* Top gap remove */
.block-container {
    padding-top: 2rem;
}
</style>
""", unsafe_allow_html=True)

#Banner image move
st.markdown("""
<style>
.banner-img img {
    margin-top: -80px;
    border-radius: 10px;
}

/* All images poster normal */
.stImage img {
    margin-top: 0px;
}

</style>
""", unsafe_allow_html=True)

st.markdown('<div class="banner-img">', unsafe_allow_html=True)
st.image("Movies.png", use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)
# <style>


#Image fit
st.markdown("""
<style>
img {
    border-radius:10px;
}
</style>
""", unsafe_allow_html=True)

# Banner Text 
st.markdown("""
<style>
img {
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
.banner {
        background: linear-gradient(to right,#0F2027,#1E4D4D,#2E8B57);
        padding: 15px;
        border-radius: 10px;
        padding: 25px;
        border-radius: 10px;
        text-align: center;
        font-size: 40px;
        font-weight: bold;
        color: white;
    }
</style>
<div class="banner">
Movie Recommendation System
</div>
""", unsafe_allow_html=True)
st.write("\n")


mvname = st.selectbox("Select a movie", ['Choose a movie'] + list(df.name))

if mvname != 'Choose a movie':
    index = df[df.name == mvname].index[0]
    vector = X[index]
    
    distances, indexes = model.kneighbors(vector, n_neighbors=6)
                
    for i in indexes[0][1:]:
        movie_name = df.loc[i]['name']
        st.write(movie_name)
        
        url = f"http://www.omdbapi.com/?t={movie_name}&apikey=edf5d438"
        resp = requests.get(url)
        details = resp.json()
        poster = details.get('Poster', '')
    
        valid = False
        if isinstance(poster, str) and poster.startswith("http"):
            try:
                check = requests.get(poster, timeout=3)
                if check.status_code == 200 and "image" in check.headers.get("Content-Type", ""):
                    valid = True
            except:
                valid=False  
        
    
        # ✅ Poster DISPLAY
        if valid:
            st.image(poster, width=250)
        else:
            st.image("No Image Available.png", width=250)
        

       