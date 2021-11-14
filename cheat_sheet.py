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
st.markdown("<h6 style='text-align: justify;font-size:110%;font-family:Georgia,sans-serif;line-height: 1.3;'>A software package that allows a user to interactively issue massive parallel computations on distributed data using functions and syntax that mimic NumPy, the underlying computational library used in most Python data science workflows</h6>",unsafe_allow_html=True)

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
    st.sidebar.markdown('''[<img src='data:image/png;base64,{}' class='img-fluid' width=310 height=200>](https://github.com/Bears-R-Us/arkouda)'''.format(img_to_bytes("arkouda_transparent.png")), unsafe_allow_html=True)
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
    #.hdf5 file conversion
    col1.subheader('.hdf5 file conversion')
    col1.markdown('Using formatter file')
    col1.code('''#run the following python script
!python3 {PATH TO ARKOUDA CSV2HDF.PY FILE}\\
--formats-file={PATH TO YOUR FORMATTER FILE}\\
--format=yellow\\
--outdir={DIRECTORTY/FOLDER WHERE YOU WANT THE RESULTANT HDF5 FILE}\\
{PATH TO THE CSV FILE WHICH NEEDS TO BE CONVERTED}
    ''')
    col1.markdown('Alternate way to create dictionary of arrays using Pandas and Arkouda')
    col1.code('''
pdgreen = pd.read_csv('PATH TO YOUR CSV FILE')
# transfer columns of DataFrame to arkouda
def ak_create_akdict_from_df(df):
    akdict = {}
    for cname in df.keys():
        if df[cname].dtype.name == 'object':
            akdict[cname] = ak.from_series(df[cname],dtype=np.str)
        else:
            akdict[cname] = ak.from_series(df[cname])

    return akdict

#Passing the dataframe through the converter function to procure hdf file
green_from_pandas = ak_create_akdict_from_df(pdgreen)
    ''')
    #formatter file example
    col1.subheader("Example of a formatter file")
    col1.markdown("Click on [link](https://render.githubusercontent.com/view/ipynb?color_mode=light&commit=6851eb342c7c5446203e10bd249129f392183e94&enc_url=68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f6e6172656e6b68617477616e692f41726b6f7564614e6f7465626f6f6b732f363835316562333432633763353434363230336531306264323439313239663339323138336539342f4e5943546178695f736d616c6c2e6970796e62&nwo=narenkhatwani%2FArkoudaNotebooks&path=NYCTaxi_small.ipynb&repository_id=415315124&repository_type=Repository#Describe-Data-Format) to redirect")
    col1.markdown("See video explanation [here](https://youtu.be/KjdaQ2Sg_oc?t=569)")
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
    col2.subheader('Basic arithmetic Operations')
    col2.code('''
#create an array with values ranging from 0-10
>>>A = ak.arange(10)
#perform the addition as A=A+2
>>>A += 2
#display the array
>>>A
array([2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
>>>A + A
array([4, 6, 8, 10, 12, 14, 16, 18, 20, 22])
>>>2 * A
array([4, 6, 8, 10, 12, 14, 16, 18, 20, 22])
>>>A == A
array([True, True, True, True, True, True, True, True, True, True])
    ''')
    # Arithmetic Operations in a hdf5 file
    col2.subheader('Arithmetic Operations on a .hdf5 file')
    col2.code('''
#reading in the column to an array
A=data['column_name1']
B=data['column_name2']
#multiplication of arrays
>>>A*B
#Addition of arrays and copying value of C
>>>C=A+B
    ''')
    #return
    return None

# Run main()
if __name__ == '__main__':
    main()