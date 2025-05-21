import customtkinter as ctk
from googletrans import Translator

# Initialize translator
translator = Translator()

# Set appearance
ctk.set_appearance_mode("dark")  # Modes: "System" (default), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (default), "green", "dark-blue"

# App Window
app = ctk.CTk()
app.title("Language Translator")
app.geometry("600x500")

# Language codes list (you can add more)
LANGUAGES = {
    "Auto Detect": "auto",
    "English": "en",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Hindi": "hi",
    "Chinese (Simplified)": "zh-cn",
    "Japanese": "ja",
    "Korean": "ko",
    "Arabic": "ar",
    "Urdu": "ur"
}

# Functions
def translate_text():
    src_lang = LANGUAGES.get(source_lang_option.get(), "auto")
    tgt_lang = LANGUAGES.get(target_lang_option.get(), "en")
    text = input_text.get("1.0", "end").strip()
    if text:
        try:
            translated = translator.translate(text, src=src_lang, dest=tgt_lang)
            output_text.delete("1.0", "end")
            output_text.insert("1.0", translated.text)
        except Exception as e:
            output_text.delete("1.0", "end")
            output_text.insert("1.0", f"Error: {str(e)}")

# Widgets
title_label = ctk.CTkLabel(app, text="🌐 Language Translator", font=("Helvetica", 24, "bold"))
title_label.pack(pady=15)

frame = ctk.CTkFrame(app)
frame.pack(padx=20, pady=10, fill="x")

source_lang_option = ctk.CTkOptionMenu(frame, values=list(LANGUAGES.keys()))
source_lang_option.set("Auto Detect")
source_lang_option.grid(row=0, column=0, padx=10, pady=10)

target_lang_option = ctk.CTkOptionMenu(frame, values=list(LANGUAGES.keys()))
target_lang_option.set("English")
target_lang_option.grid(row=0, column=1, padx=10, pady=10)

# Input box
input_label = ctk.CTkLabel(app, text="Enter text to translate:")
input_label.pack(pady=(10, 0))

input_text = ctk.CTkTextbox(app, height=100)
input_text.pack(padx=20, pady=10, fill="both", expand=False)

# Translate button
translate_button = ctk.CTkButton(app, text="Translate", command=translate_text)
translate_button.pack(pady=10)

# Output box
output_label = ctk.CTkLabel(app, text="Translated text:")
output_label.pack(pady=(10, 0))

output_text = ctk.CTkTextbox(app, height=100)
output_text.pack(padx=20, pady=10, fill="both", expand=False)

# Run App
app.mainloop()
