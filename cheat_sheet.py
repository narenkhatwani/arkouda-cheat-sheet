#importing all necessary dependencies
import streamlit as st
from pathlib import Path
import base64

#initial page configuration
st.set_page_config(
     page_title='Arkouda Cheat Sheet',
     layout="wide",
     initial_sidebar_state="expanded",
)
#title
st.title("Arkouda Cheat Sheet")

#description
st.markdown("<h4 style='text-align: justify;font-size:110%;font-family:Arial,sans-serif;line-height: 1.3;'>A software package that allows a user to interactively issue massive parallel computations on distributed data using functions and syntax that mimic NumPy, the underlying computational library used in most Python data science workflows</h4>",unsafe_allow_html=True)

#main driver code
def main():
    cs_sidebar()
    cs_body()
    return None


def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded


#sidebar function
def cs_sidebar():

    st.sidebar.title('Arkouda cheat sheet')
    st.sidebar.markdown('''[<img src='data:image/png;base64,{}' class='img-fluid' width=330 height=210>](https://github.com/Bears-R-Us/arkouda)'''.format(img_to_bytes("arkouda_transparent.png")), unsafe_allow_html=True)
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
    st.sidebar.markdown('__Connecting to Arkouda Server__')
    st.sidebar.code('''
#format 1
arkouda.connect(server='localhost', port=5555)
#format 2
arkouda.connect(connect_url='tcp://localhost:5555') 
    ''')
    #return
    return None

def cs_body():
    # Main body arkouda details

    col1, col2, col3 = st.columns(3)
    #reading data
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
    #return
    return None

# Run main()
if __name__ == '__main__':
    main()