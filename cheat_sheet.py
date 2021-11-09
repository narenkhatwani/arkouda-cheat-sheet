import streamlit as st
from pathlib import Path
import base64

# Initial page config

st.set_page_config(
     page_title='Arkouda Cheat Sheet',
     layout="wide",
     initial_sidebar_state="expanded",
)

st.title("Arkouda Cheat Sheet")
st.markdown("")

def main():
    cs_sidebar()
    cs_body()

    return None


def cs_sidebar():

    #st.sidebar.markdown('''[<img src='data:image/png;base64,{}' class='img-fluid' width=32 height=32>](https://streamlit.io/)'''.format(img_to_bytes("logomark_website.png")), unsafe_allow_html=True)
    st.sidebar.title('Arkouda cheat sheet')

    st.sidebar.markdown('''<small>Summary of the [docs](https://arkouda.readthedocs.io/en/latest/index.html), as of Arkouda v1.0.0</small>''', unsafe_allow_html=True)
    #how to download
    st.sidebar.markdown('__How to Download and Install__')
    st.sidebar.markdown('Follow the steps given at [link](https://github.com/Bears-R-Us/arkouda/blob/master/README.md#build-ak)')
    #how to import
    st.sidebar.markdown('__How to import__')
    st.sidebar.code('>>> import arkouda as ak')
    #how to launch
    st.sidebar.markdown('__Launch arkouda_server__')
    st.sidebar.code('./arkouda_server')
    st.sidebar.markdown('__Multi-locale startup__')
    st.sidebar.code('./arkouda_server -nl 2')
    #how to conect to arkouda
    st.sidebar.markdown('__Connecting to Arkouda__')
    st.sidebar.code('''
#format 1
arkouda.connect(server='localhost', port=5555)
#format 2
arkouda.connect(connect_url='tcp://localhost:5555') 
    ''')

    return None

def cs_body():
    # Main body arkouda details

    col1, col2, col3 = st.columns(3)

    col1.subheader('Reading Data')
    col1.code('''#.hdf5 file
ak.read_all('PATH/FILENAME.hdf')
ak.get_datasets('PATH/FILENAME.hdf')
    ''')

    # Display data

    col1.subheader('Display data')
    col1.code('''
data['column_name']
    ''')

    # Arithmetic Operations

    col2.subheader('Arithmetic Operations')
    col2.code('''
>>>A = ak.arange(10)
>>>A += 2
>>>A
array([2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
>>>A + A
array([4, 6, 8, 10, 12, 14, 16, 18, 20, 22])
>>>2 * A
array([4, 6, 8, 10, 12, 14, 16, 18, 20, 22])
>>>A == A
array([True, True, True, True, True, True, True, True, True, True])
    ''')

    return None

# Run main()

if __name__ == '__main__':
    main()