import streamlit as st
import pandas as pd

st.title("Análisis de Datos de Educación en Colombia")

uploaded_file = st.file_uploader("Sube un archivo CSV", type=["csv"])

if uploaded_file is not None:
    # Lee el archivo CSV en un DataFrame de Pandas
    df = pd.read_csv(uploaded_file)

    st.table(df)

  # Crear los filtros en la barra lateral
    st.sidebar.header("Filtros")

    nivel_educativo = st.sidebar.multiselect(
        "Nivel educativo", df["Nivel educativo"].unique()
    )

    carrera = st.sidebar.multiselect(
        "Carrera", df["Carrera"].unique()
    )

    institucion = st.sidebar.multiselect(
        "Institución", df["Institución"].unique()
    )

    # Filtrar los datos en base a los filtros seleccionados
    df_filtrado = df.copy()

    if nivel_educativo:
        df_filtrado = df_filtrado[df_filtrado["Nivel educativo"].isin(nivel_educativo)]

    if carrera:
        df_filtrado = df_filtrado[df_filtrado["Carrera"].isin(carrera)]

    if institucion:
        df_filtrado = df_filtrado[df_filtrado["Institución"].isin(institucion)]

    # Mostrar el DataFrame filtrado
    st.dataframe(df_filtrado)

    # Mostrar estadísticas descriptivas de los datos filtrados
    st.subheader("Estadísticas Descriptivas")
    st.write(df_filtrado.describe())

    # Mostrar el conteo de estudiantes por Nivel educativo
    st.subheader("Conteo de Estudiantes por Nivel Educativo")
    if not df_filtrado.empty:
        st.bar_chart(df_filtrado["Nivel educativo"].value_counts())
    else:
        st.write("No hay datos disponibles para los filtros seleccionados.")

    # Mostrar el histograma de la distribución de la edad
    st.subheader("Distribución de la Edad")
    if not df_filtrado.empty:
        st.bar_chart(df_filtrado["Edad"].value_counts(bins=10))
    else:
        st.write("No hay datos para mostrar el histograma.")
else:
    st.write("Por favor, sube un archivo CSV.")