import streamlit as st
st.title('Title -> title')
st.header('Header -> header')
st.subheader('Subheader -> header')
st.text('Text -> text')

st.markdown('# Hi')
st.markdown('## Hi')
st.markdown('### Hi')
st.markdown('#### Hi')
st.markdown('##### Hi')

st.success('Success')
st.info('Information!')
st.warning('Warning')
st.error('Error')

st.write("range(1, 10)")
st.write(range(1, 10))


st.checkbox('Female')

if(st.checkbox('Male')):
    st.write("Nahi tu female hai..")


st.subheader('Radio Button')                            # Radio Button
radioButton = st.radio('Select : ', ('Male','Female','Other','Khali dabba'))
if(radioButton == 'Male'):
    st.write("Nahi tu female hai..")
elif(radioButton == 'Female'):
    st.write("Pata hai tu female hai..")
elif(radioButton == 'Other'):
    st.error("Kiyaa..!! baat kr raha hai..!!")
elif(radioButton == 'Khali dabba'):
    st.write(" ")


st.subheader('Select Box')                              # SelectBox
selectBox =  st.selectbox("Data Science : ", [  'Data Analsis', 'Web Scraping','Machine Learning',
                                                'Deep Learning','Natural Language Processing',
                                                'Computer Vision','Image Processing'])
st.write("You've selected : ", selectBox)


st.subheader('MultiSelect Box')                         # MultiSelectBox
multiSelBox = st.multiselect("Data Science : ", [  'Data Analsis', 'Web Scraping','Machine Learning',
                                                    'Deep Learning','Natural Language Processing',
                                                    'Computer Vision','Image Processing'])
st.write("You've selected : ", len(multiSelBox) , 'courses')


st.subheader("Button")                                  # Button
if(st.button('Click me')):
    st.write('Thanks for clicking me')

st.subheader("Slider")                                  # Slider
vol = st.slider('Select the volume',0,100,step = 1)
st.write('Volume is : ',vol)

st.subheader("Text Input")                              # Text-Input
username = st.text_input('Username : ')
password = st.text_input('Password : ', type = 'password')

st.subheader("Text Area")                              # Text-Area
st.text_area('Write something interesting about yourself')

st.subheader("Input Number")                           # Input-Number
st.number_input('Select your age',18,110)

st.subheader("Input Date")                              # Input-Date
st.date_input('Date')

st.subheader("Input Time")                              # Input-Time
st.time_input('Time')
