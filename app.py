from flask import Flask, request, render_template
from transformers import BlenderbotTokenizer, BlenderbotForConditionalGeneration
import datetime

app = Flask(__name__)

# Load BlenderBot model and tokenizer
model_name = "facebook/blenderbot-400M-distill"
tokenizer = BlenderbotTokenizer.from_pretrained(model_name)
model = BlenderbotForConditionalGeneration.from_pretrained(model_name)

# Store chat history
chat_history = []

@app.route("/chat", methods=["GET", "POST"])
def chat():
    global chat_history
    if request.method == "POST":
        user_input = request.form["user_input"]
        chat_history.append({"role": "user", "content": user_input})
        
        # Handle specific queries
        if "your name" in user_input.lower():
            bot_reply = "I’m Grok, created by xAI. What’s your name?"
        elif "time" in user_input.lower():
            current_time = datetime.datetime.now().strftime("%H:%M:%S %Z on %B %d, %Y")
            bot_reply = f"The current time is {current_time}."
        elif "where are you" in user_input.lower():
            bot_reply = "I’m Grok, an AI, so I exist in the cloud. Where are you?"
        elif "update" in user_input.lower():
            bot_reply = "Did you mean ‘what are the latest updates’? I don’t have specifics handy, but I can search the web or X for you. What’s on your mind?"
        else:
            # Build conversation history with stronger identity
            history = "I am Grok, an AI assistant created by xAI.\n" + "\n".join(
                [f"{msg['role']}: {msg['content']}" for msg in chat_history[-3:]]
            )
            inputs = tokenizer(history, return_tensors="pt", truncation=True, max_length=512)
            reply_ids = model.generate(
                **inputs,
                max_length=60,
                pad_token_id=tokenizer.eos_token_id,
                no_repeat_ngram_size=3,
                temperature=0.7,
                top_p=0.9,
                do_sample=True
            )
            bot_reply = tokenizer.decode(reply_ids[0], skip_special_tokens=True)
            # Expanded filter for persona-like statements
            unwanted_phrases = [
                "I work", "I live", "I’m a", "I am a", "as an", "by profession", "I am doing",
                "hanging out", "my dog", "my best friend"  # New additions
            ]
            for phrase in unwanted_phrases:
                if phrase in bot_reply.lower() and "Grok" not in bot_reply:
                    cleaned_part = bot_reply.split(phrase)[-1].strip(" .,")
                    bot_reply = f"Hi, I’m Grok—let’s keep it simple. {cleaned_part}"
        
        chat_history.append({"role": "assistant", "content": bot_reply})
    
    return render_template("chat.html", chat_history=chat_history)

if __name__ == "__main__":
    app.run(debug=False)