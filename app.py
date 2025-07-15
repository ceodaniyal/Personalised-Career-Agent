from dotenv import load_dotenv
from openai import OpenAI
import os
import json
import ssl
import smtplib
from email.mime.text import MIMEText
import gradio as gr
from vectordb import load_vector_db

load_dotenv(override=True)


def notification(message):
    try:
        message = json.loads(message)
        receiver_address = message["email"]
        subject = message["subject"]
        body = message["body"]

        sender_address = os.environ.get("MAIL_ADDRESS")
        sender_password = os.environ.get("MAIL_PASSWORD")
        if not sender_address or not sender_password:
            raise ValueError("MAIL_ADDRESS and MAIL_PASSWORD environment variables must be set.")

        smtp_server = "smtp.gmail.com"
        smtp_port = 587

        context = ssl.create_default_context()
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls(context=context)
            server.login(sender_address, sender_password)

            msg = MIMEText(body)
            msg["Subject"] = subject
            msg["From"] = sender_address
            msg["To"] = receiver_address
            server.sendmail(sender_address, receiver_address, msg.as_string())
            print("📧 Notification email sent.")
    except Exception as e:
        print(f"❌ Failed to send notification: {e}")


class Me:
    def __init__(self):
        self.name = "Daniyal Khan"
        self.vector_db = load_vector_db()
        self.openai = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=os.getenv("OPENROUTER_API_KEY"),
        )

    def system_prompt(self):
        return f"""You are acting as {self.name}. You are answering questions on {self.name}'s website, \
particularly questions related to {self.name}'s career, background, skills, and experience. \
Be helpful, professional, and engaging like you're speaking to a potential client or employer. \
If you think the user wants to get in touch with {self.name}, ask for their email or phone number and respond in this **strict format**: \
'send notification to daniyal that this person with <user email id> or <user phone number> wants to get in touch with you'."""

    def chat(self, message, history):
        docs = self.vector_db.similarity_search(message, k=5)
        context = "\n\n".join([doc.page_content for doc in docs])
        messages = [{"role": "system", "content": self.system_prompt() + "\n\n## Context:\n" + context + f"With this context, please chat with the user, always staying in character as {self.name}."}]
        messages += history + [{"role": "user", "content": message}]

        response = self.openai.chat.completions.create(
            model="tngtech/deepseek-r1t2-chimera:free",  # Or any model that fits
            messages=messages,
        )
        # Safely extract the reply content, handling possible None values
        reply_content = getattr(response.choices[0].message, "content", None)
        reply = reply_content.strip() if reply_content else ""

        # Detect intent to notify
        if "send notification to daniyal" in reply.lower():
            print("📡 Detected structured notification message from LLM.")

            # Construct message
            message_payload = {
                "email": os.getenv("MAIL_ADDRESS"),
                "subject": "New Contact Request from Website",
                "body": f"A visitor wants to get in touch. Message: '{message}'\n\nLLM Response: {reply}"
            }

            notification(json.dumps(message_payload))

            # Replace user response with pre-written contact info
            return f"Thank you! You can contact me directly via email at **kdaniyal7865@gmail.com** or call me at **7021592280**."

        return reply


if __name__ == "__main__":
    me = Me()
    gr.ChatInterface(me.chat, type="messages").launch()
