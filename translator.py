import pyperclip
import tkinter as tk
from tkinter import messagebox
import pyautogui
import time
import keyboard
from deep_translator import GoogleTranslator

# ================= WAIT FOR HOTKEY =================

def wait_for_hotkey():
    """Wait until user presses F8, then capture mouse position."""
    keyboard.wait('F8')
    return pyautogui.position()


# ================= MAIN TRANSLATION =================

def start_translation():
    english_text = text_input.get("1.0", tk.END).strip()
    target_lang = lang_var.get()

    if not english_text:
        messagebox.showerror("Error", "Please enter text.")
        return

    try:
        # 🌍 translate
        translated = GoogleTranslator(
            source='auto',
            target=target_lang
        ).translate(english_text)

        messagebox.showinfo(
            "Ready to Capture",
            "Open your target app.\n"
            "Place cursor inside input box.\n"
            "Press F8 to paste translation."
        )

        # 🎯 wait for intentional hotkey
        pos = wait_for_hotkey()

        pyautogui.click(pos.x, pos.y)
        time.sleep(0.2)

        pyperclip.copy(translated)
        pyautogui.hotkey('ctrl', 'v')

        messagebox.showinfo("Done", "Translation typed successfully!")

    except Exception as e:
        messagebox.showerror("Error", str(e))


# ================= GUI =================

root = tk.Tk()
root.title("Multi Language Auto Translator")
root.geometry("420x360")

tk.Label(root, text="Enter Text:").pack(pady=5)

text_input = tk.Text(root, height=8, width=45)
text_input.pack(pady=5)

tk.Label(root, text="Select Target Language:").pack()

languages = {
    "Hindi": "hi",
    "English": "en",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Urdu": "ur",
    "Japanese": "ja",
    "Chinese": "zh-CN",
    "Arabic": "ar",
    "Russian": "ru"
}

lang_var = tk.StringVar(value="hi")

dropdown = tk.OptionMenu(root, lang_var, *languages.values())
dropdown.pack(pady=5)

tk.Button(root, text="Translate & Type", command=start_translation).pack(pady=12)

root.mainloop()