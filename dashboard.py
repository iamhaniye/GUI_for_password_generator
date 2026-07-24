import streamlit as st
import nltk
from password_ggenerator import PinGenerator , RandomPasword , MemorablePassword

st.image("streamlit-dashboard.png.jpeg")
st.title(":zap: PASSWORD GENERATOR")

option = st.radio("select password generator: ",
    ("PIN CODE", "RANDOM PASSWORD" , "MEMORABLE PASSWORD")
)


if option == "PIN CODE":
    length = st.slider("select the length of pin code: ", 4, 32)
    generator = PinGenerator(length)


elif option == "RANDOM PASSWORD":
    length = st.slider("select the length of random password: ", 8, 32)
    include_number = st.toggle("INCLUDE NUMBER?")
    include_symbol = st.toggle("INCLUDE SYMBOLS?")
    generator = RandomPasword(length, include_number, include_symbol)


elif option == "MEMORABLE PASSWORD":
    num_of_word = st.slider("select the length of pin code: ", 3, 10)
    generator = MemorablePassword(num_of_word)





password = generator.generate()
st.success(f"your password is : {password}")