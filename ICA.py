import streamlit as st
import seaborn as sns
import pandas as pd

df=pd.read_csv('/Users/neeljoshi/Downloads/data.csv')

lst=[]
for i in df.columns:
    lst.append(i)
lst.pop(0)
lst.pop(-1)
option = st.selectbox(
    'Which column you wanna plot???',
    lst)

plot=sns.histplot(df[option])

st.pyplot(plot.get_figure())