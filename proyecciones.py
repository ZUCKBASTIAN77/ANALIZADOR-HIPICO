import streamlit as st

st.set_page_config(page_title="ANALIZADOR HIPICO PRO", page_icon=":horse_racing:")


st.write("---BIENVENIDO AL ANALIZADOR HIPICO :chart_whit_upwards_trend:---")

nombre = st.text_input("NOMBRE DEL CABALLO:")
peso =st.number_input("PESO DEL CABALLO:(kg):", value=470)
distancia =st.number_input("DISTANCIA (METROS):", value=1200)
jinete =st.text_input("NOMBRE DEL JINETE:")
edad =st.number_input("EDAD DEL JINETE:", value=25)
peso_j =st.number_input("PESO DEL JINETE:", value=52)

rango = "NOVATO :hactching_chick:" if edad < 25 else "EXPERTO:star:"

if peso <= 475 and peso_j <= 54:
    st.success(f"PROYECCION DE ORO {nombre}: joven y ligero :trophy:")

elif peso <= 510 and peso_j <= 57:
     st.info("PROYECCION DE PLATA {nombre}: buen perfil competitivo :second_place_medal:")
else:
     st.warning(f"PROYECCION DE BRONCE: no cumple con el perfil optimo:third_place_medal:")

     st.write(f"jinete analizado: {jinete} - Rango: {rango}")  



