import streamlit as st
import yfinance as yf

st.title("My First Web Application")

# var_symbol = st.text_input("Enter Stock Symbol:")

var_symbol = st.multiselect("what do you want?",["MSFT", "GOOGLE", "LOL"],["GOOGLE"])

# ticker = yf.Ticker(var_symbol)
# data = ticker.history(start="2019-01-01")
# st.line_chart(data.Close)
                                                                # knopka
st.button("LOL", on_click=print('lol'))
if st.button('Не нажимай на меня'):
    st.write('Желтик, я же просил...')
else:
    st.write('Не стоит рил...')
                                                                # skachat knopka
st.download_button("Download", "alo", help="Press me b*tch")
                                                                # checkbox
st.checkbox("checkbox")
st.checkbox("checkbox2")
agree = st.checkbox('I agree')
if agree:
    st.write('Great!')
                                                                # radio = vibiralki
st.radio("what do you want", ("cola", "sprite", "fanta"))

st.header("What do you have to buy for Liliia?")
lol = st.radio(
    " ",
    ('Airpods', 'BMW M4 Competition', 'i dunno, whatever'))
if lol == 'Krossovki':
    st.write('kaef bil bi')
elif lol == "BMW M4 Competition":
    st.write("YESSSSSSSS:)")
else:
    st.write("yes please")

# Store the initial value of widgets in session state
if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False
    st.session_state.horizontal = False

col1, col2 = st.columns(2)

with col1:
    st.checkbox("Disable radio widget", key="disabled")
    st.checkbox("Orient radio options horizontally", key="horizontal")

with col2:
    st.radio(
        "Set label visibility 👇",
        ["visible", "hidden", "collapsed"],
        key="visibility",
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
        horizontal=st.session_state.horizontal,
    )



                                                                # selectbox
option = st.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone'))
st.write('You selected:', option)


                                                                # multi-select
options = st.multiselect(
    'What are your favorite colors',
    ['Green', 'Yellow', 'Red', 'Blue'],
    ['Yellow', 'Red'])
st.write('You selected:', options)


                                                                # slider
age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')

values = st.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)

from datetime import time
appointment = st.slider(
    "Schedule your appointment:",
    value=(time(11, 30), time(12, 45)))
st.write("You're scheduled for:", appointment)

from datetime import datetime
start_time = st.slider(
    "When do you start?",
    value=datetime(2020, 1, 1, 9, 30),
    format="MM/DD/YY - hh:mm")
st.write("Start time:", start_time)


                                                                # select slider
color = st.select_slider(
    'Select a color of the rainbow',
    options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'])
st.write('My favorite color is', color)

start_color, end_color = st.select_slider(
    'Select a range of color wavelength',
    options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'],
    value=('red', 'blue'))
st.write('You selected wavelengths between', start_color, 'and', end_color)


                                                                # text_input
title = st.text_input('Movie title', 'Life of Brian')
st.write('The current movie title is', title)

# # Store the initial value of widgets in session state
# if "visibility" not in st.session_state:
#     st.session_state.visibility = "visible"
#     st.session_state.disabled = False

# col1, col2 = st.columns(2)

# with col1:
#     st.checkbox("Disable text input widget", key="disabled")
#     st.radio("Set text input label visibility 👉",
#         key="visibility",
#         options=["visible", "hidden", "collapsed"],
#     )
#     st.text_input(
#         "Placeholder for the other text input widget",
#         "This is a placeholder",
#         key="placeholder",
#     )

# with col2:
#     text_input = st.text_input(
#         "Enter some text 👇",
#         label_visibility=st.session_state.visibility,
#         disabled=st.session_state.disabled,
#         placeholder=st.session_state.placeholder,
#     )

#     if text_input:
#         st.write("You entered: ", text_input)


                                                                # number input
number = st.number_input('Insert a number')
st.write('The current number is ', number)


                                                                # text area
txt = st.text_area('Text to analyze', '''
    It was the best of times, it was the worst of times, it was
    the age of wisdom, it was the age of foolishness, it was
    the epoch of belief, it was the epoch of incredulity, it
    was the season of Light, it was the season of Darkness, it
    was the spring of hope, it was the winter of despair, (...)
    ''')
st.write('Sentiment:', txt)


                                                                # date input
d = st.date_input("When's your birthday")
st.write('Your birthday is:', d)


                                                                # time input
t = st.time_input('Set an alarm for')
st.write('Alarm is set for', t)


                                                                # upload file
import pandas as pd
from io import StringIO
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    st.write(bytes_data)

    # To convert to a string based IO:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    st.write(stringio)

    # To read file as string:
    string_data = stringio.read()
    st.write(string_data)

    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)


uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
    st.write(bytes_data)


                                                                # camera
# picture = st.camera_input("Take a picture")
# if picture:
#     st.image(picture)


# img_file_buffer = st.camera_input("Take a picture")

# if img_file_buffer is not None:
#     # To read image file buffer as bytes:
#     bytes_data = img_file_buffer.getvalue()
#     # Check the type of bytes_data:
#     # Should output: <class 'bytes'>
#     st.write(type(bytes_data))


import streamlit as st
from PIL import Image
import numpy as np

img_file_buffer = st.camera_input("Take a picture")

if img_file_buffer is not None:
    # To read image file buffer as a PIL Image:
    img = Image.open(img_file_buffer)

    # To convert PIL Image to numpy array:
    img_array = np.array(img)

    # Check the type of img_array:
    # Should output: <class 'numpy.ndarray'>
    st.write(type(img_array))

    # Check the shape of img_array:
    # Should output shape: (height, width, channels)
    st.write(img_array.shape)


                                                                # color picker
color = st.color_picker('Pick A Color', '#00f900')
st.write('The current color is', color)