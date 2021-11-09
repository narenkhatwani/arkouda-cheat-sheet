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

    # Display text

    col1.subheader('Display text')
    col1.code('''
st.text('Fixed width text')
st.markdown('_Markdown_') # see *
st.caption('Balloons. Hundreds of them...')
st.latex(r\'\'\' e^{i\pi} + 1 = 0 \'\'\')
st.write('Most objects') # df, err, func, keras!
st.write(['st', 'is <', 3]) # see *
st.title('My title')
st.header('My header')
st.subheader('My sub')
st.code('for i in range(8): foo()')
* optional kwarg unsafe_allow_html = True
    ''')

    # Display data

    col1.subheader('Display data')
    col1.code('''
st.dataframe(my_dataframe)
st.table(data.iloc[0:10])
st.json({'foo':'bar','fu':'ba'})
st.metric(label="Temp", value="273 K", delta="1.2 K")
    ''')

    # Display media

    col2.subheader('Display media')
    col2.code('''
st.image('./header.png')
st.audio(data)
st.video(data)
    ''')

    return None

# Run main()

if __name__ == '__main__':
    main()