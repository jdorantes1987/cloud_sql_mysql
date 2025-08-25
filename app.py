import streamlit as st

# Conectarse a la base de datos usando st.connection
conn = st.connection("sql", type="sql")

# Ejecutar una consulta y cargar los datos en un DataFrame
df = conn.query("SELECT * FROM tbl_creyente;", ttl=600)

st.dataframe(df)

# Puedes usar el objeto de conexión para otras operaciones
# with conn.session as s:
#     s.execute("INSERT INTO my_table (col1, col2) VALUES ('value1', 'value2');")
