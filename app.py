import streamlit as st
import pandas as pd

st.set_page_config(page_title="CMA • Minimización de Costos", layout="wide")
st.title("5️⃣ CMA • Minimización de Costos")

st.header("5️⃣ Minimización de Costos (CMA)")
df=st.data_editor(pd.DataFrame({'Alt':['A','B'],'Costo':[1000.0,1200.0]}),num_rows='dynamic',key='cma')
if not df.empty:
    m=df.loc[df['Costo'].idxmin()]
    st.success(f"Opción mínima: {m['Alt']} US$ {m['Costo']:,.2f}")
    csv = df.to_csv(index=False).encode("utf-8-sig")
    st.download_button("Descargar CSV", csv, file_name="CMA.csv", mime="text/csv")
