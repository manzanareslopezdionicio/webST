import streamlit as st 
from PIL import Image

#tilula del web
#mg = Image.open("img/chatbot.png")
#st.set_page_config(page_title='Mi APP', page_icon=img)

#Mostrar textos
st.title("Mi sitio web en Streamlit")
st.header("hola")
st.subheader("sub encabezado")
st.caption("Etiqueta de la web")
st.text("Este es un texto")
nombre = "Dionicio Manzanares Lopez"
st.text(f"Hola {nombre} Bienvenido")
# streamlit run app.py para lenvantar la pagina web
st.markdown("# Este es un texto h1 \n ## Este es otro texto h2 \n ### Este es un H3")
st.write("Este es un mensaje Write")
st.write("La su es ",5+10)

#Alectas
st.success("Los Datos de guardaron satistactoriamente")
st.error("Error se puede conectar la base de datos")
st.warning("Esta es una Advertancia")
st.info("Esto es un mensaje de informacion")
st.exception("Este es un mensaje de Excepcion")

#Entrada de datos input
nombre = st.text_input("Ingresar su nombre:")
st.write(nombre)
numero = st.number_input("Ingresar edad",16,60)
st.write(numero)
fecha = st.date_input("Ingresar la fecha")
st.write(fecha)
hora=st.time_input("Seleccionar la hora")
st.write(hora)
color = st.color_picker("Seleccionar el color")
st.write(color)

#botones
st.button("Enviar", type="primary")
st.button("Mostrar", icon="☠", use_container_width=True, type="primary")

#abril archivos video, imagen y audio
st.image("img/proceso.jpg")
st.audio("musica/elton john - sacrifice.mp3")
st.video("video/video_streamlit.mp4")
st.image("img/ses.png")
st.subheader("Titulo de la imagen")
st.image("img/ses.png", width=300, caption="Imagen Pequeña")
