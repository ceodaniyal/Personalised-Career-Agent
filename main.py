from vectordb import create_vector_db
import app

if __name__ == "__main__":
    create_vector_db()
    me = app.Me()
    import gradio as gr
    gr.ChatInterface(me.chat, type="messages").launch()
