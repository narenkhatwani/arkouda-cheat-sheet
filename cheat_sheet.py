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


def main():
    cs_sidebar()
    cs_body()

    return None


def cs_sidebar():

    #st.sidebar.markdown('''[<img src='data:image/png;base64,{}' class='img-fluid' width=32 height=32>](https://streamlit.io/)'''.format(img_to_bytes("logomark_website.png")), unsafe_allow_html=True)
    st.sidebar.title('Arkouda cheat sheet')

    st.sidebar.markdown('''<small>Summary of the [docs](https://docs.streamlit.io/en/stable/api.html), as of [Streamlit v1.0.0](https://www.streamlit.io/).</small>''', unsafe_allow_html=True)

    st.sidebar.markdown('__How to import__')

    st.sidebar.code('>>> import arkouda as ak')

    st.sidebar.markdown('__Running arkouda_server__')
    st.sidebar.code('>>> import streamlit as st')

    st.sidebar.markdown('__Command line__')
    st.sidebar.code('''
$ streamlit --help
$ streamlit run your_script.py
    ''')

    return None

def cs_body():
    # Magic commands

    col1, col2, col3 = st.columns(3)

    col1.subheader('Magic commands')
    col1.code('''# Magic commands implicitly `st.write()`
\'\'\' _This_ is some __Markdown__ \'\'\'
a=3
'dataframe:', data
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