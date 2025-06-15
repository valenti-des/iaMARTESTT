import streamlit as st
import groq
MODELOS = ['llama3-8b-8192', 'llama3-70b-8192','mixtral-8x7b-32768']

#configurar pagina

def configurar_pagina():
    st.set_page_config(page_title="Mi Pirmer ChatBot con Python")
    st.title("Bienvenidos a mi Chatbot")
    
    
    
    
    
#crear cliente groq

def crear_cliente_groq():
    groq_api_key = st.secrets["GROQ_API_KEY"]
    return groq.Groq(api_key=groq_api_key)
    

        
#mostrar la barra lateral 

def mostrar_sidebar():
    st.sidebar.title("Elegí tu modelo de IA favorito")
    modelo = st.sidebar.selectbox('elegí tu modelo',MODELOS,index=0)
    st.write(f'**Elegiste el modelo** {modelo}')
    return modelo



#inicializar el estado del chat
def inicializar_estado_chat():
    if "mensajes" not in st.session_state:
        st.session_state.mensajes = []



#mostra mensajes previos 
def obtener_mensajes_previos():
    for mensaje in st.session_state.mensajes: # recorrer los mensajes de st.session_state.mensaje
        with st.chat_message(mensaje["role"]): #quien lo envia ??
            st.markdown(mensaje["content"]) #que envia



#obtener mensaje usuario
def obtener_mensaje_usuario():
    return st.chat_input("Envia tu mensaje")


#guardar los mensajes
def agregar_mensajes_previos(role, content):
    st.session_state.mensajes.append({"role": role , "content": content})
    



#mostrar los mensajes en pantalla 

def mostrar_mensaje(role, content):
    with st.chat_message(role):
        st.markdown(content)
        
        
        

   
#llamar del modelo de groq

def obtener_respuesta_modelo(cliente, modelo, mensaje):
    respuesta =  cliente.chat.completions.create(
        model = modelo,
        messages = mensaje,
        stream= False
    )
    return respuesta.choices[0].message.content


    
    
    





#ejecutar chat

def ejecutar_chat():
    configurar_pagina()
    cliente = crear_cliente_groq()
    modelo = mostrar_sidebar()
    
    
    inicializar_estado_chat()
    mensaje_usuario = obtener_mensaje_usuario()
    obtener_mensajes_previos()
    
    if mensaje_usuario:
        agregar_mensajes_previos("user",mensaje_usuario)
        mostrar_mensaje("user",mensaje_usuario)
        
        respuesta_contenido = obtener_respuesta_modelo(cliente, modelo,st.session_state.mensajes )
        agregar_mensajes_previos("assistant",respuesta_contenido)
        mostrar_mensaje("assistant",respuesta_contenido)
        
        
    
    
    
    

    
#EJECUTAR LA APP

if __name__ == '__main__':
    ejecutar_chat()
    
    
    
    
    
    
    

    
    

    
