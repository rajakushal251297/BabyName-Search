import pandas as pd
import streamlit as st
df=pd.read_csv("name.csv",names=["name"])
name_list=df["name"].values.tolist()
name_list=[i.upper() for i in name_list]
st.title("Baby Names Search Here")
option=st.text_input("search with starting alphabate/alphabates").upper()
result = [i for i in name_list if i.startswith(option)]
length = len(result)
if st.button("Search"):
    if option!="":
        if length!=0:
            st.write(f"Congratulations for your Baby, you found {length} names")
            for i in list(result):
                st.write(i)
        else:
            st.write("Sorry No data found, You can search with another alphabate")
    else:
        st.write("Please Enter Starting alphabate/alphabates")