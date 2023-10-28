import selenium
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
import tkinter as tk
from tkinter import ttk

def translate(text, lang_from="auto", lang_to="es"):
   # Inicializa el navegador
    driver = selenium.webdriver.Chrome()

    # Obtiene el idioma de origen del texto
    lang_from = LANGUAGES.get(lang_from, "auto")

    # Abre Google Translate con los idiomas especificados
    driver.get(f'https://translate.google.com/?hl=en&tab=TT&sl={lang_from}&tl={lang_to}&op=translate')

    # Encuentra la caja de texto y escribe el texto a traducir
    driver.find_element(By.XPATH,"/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/span/span/div/textarea").send_keys(text)

    # Espera un poco para que se realice la traducción
    time.sleep(5)

    # Obtiene el texto traducido
    translated = driver.find_element(By.XPATH,"/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[2]/div/div[8]/div/div[1]/span[1]/span/span").text

    # Cierra el navegador
    driver.quit()

    return translated

# Diccionario de códigos ISO-639
LANGUAGES = {
    "Afrikaans": "af",
    "Albanian": "sq",
    "Amharic": "am",
    "Arabic": "ar",
    "Armenian": "hy",
    "Assamese": "as",
    "Aymara": "ay",
    "Azerbaijani": "az",
    "Bambara": "bm",
    "Basque": "eu",
    "Belarusian": "be",
    "Bengali": "bn",
    "Bhojpuri": "bho",
    "Bosnian": "bs",
    "Bulgarian": "bg",
    "Catalan": "ca",
    "Cebuano": "ceb",
    "Chinese (Simplified)": "zh-CN",
    "Chinese (Traditional)": "zh-TW",
    "Corsican": "co",
    "Croatian": "hr",
    "Czech": "cs",
    "Danish": "da",
    "Dhivehi": "dv",
    "Dogri": "doi",
    "Dutch": "nl",
    "English": "en",
    "Esperanto": "eo",
    "Estonian": "et",
    "Ewe": "ee",
    "Filipino (Tagalog)": "fil",
    "Finnish": "fi",
    "French": "fr",
    "Frisian": "fy",
    "Galician": "gl",
    "Georgian": "ka",
    "German": "de",
    "Greek": "el",
    "Guarani": "gn",
    "Gujarati": "gu",
    "Haitian Creole": "ht",
    "Hausa": "ha",
    "Hawaiian": "haw",
    "Hebrew": "he",
    "Hindi": "hi",
    "Hmong": "hmn",
    "Hungarian": "hu",
    "Icelandic": "is",
    "Igbo": "ig",
    "Ilocano": "ilo",
    "Indonesian": "id",
    "Irish": "ga",
    "Italian": "it",
    "Japanese": "ja",
    "Javanese": "jv",
    "Kannada": "kn",
    "Kazakh": "kk",
    "Khmer": "km",
    "Kinyarwanda": "rw",
    "Konkani": "gom",
    "Korean": "ko",
    "Krio": "kri",
    "Kurdish": "ku",
    "Kurdish (Sorani)": "ckb",
    "Kyrgyz": "ky",
    "Lao": "lo",
    "Latin": "la",
    "Latvian": "lv",
    "Lingala": "ln",
    "Lithuanian": "lt",
    "Luganda": "lg",
    "Luxembourgish": "lb",
    "Macedonian": "mk",
    "Maithili": "mai",
    "Malagasy": "mg",
    "Malay": "ms",
    "Malayalam": "ml",
    "Maltese": "mt",
    "Maori": "mi",
    "Marathi": "mr",
    "Meiteilon (Manipuri)": "mni-Mtei",
    "Mizo": "lus",
    "Mongolian": "mn",
    "Myanmar (Burmese)": "my",
    "Nepali": "ne",
    "Norwegian": "no",
    "Nyanja (Chichewa)": "ny",
    "Odia (Oriya)": "or",
    "Oromo": "om",
    "Pashto": "ps",
    "Persian": "fa",
    "Polish": "pl",
    "Portuguese (Portugal, Brazil)": "pt",
    "Punjabi": "pa",
    "Quechua": "qu",
    "Romanian": "ro",
    "Russian": "ru",
    "Samoan": "sm",
    "Sanskrit": "sa",
    "Scots Gaelic": "gd",
    "Sepedi": "nso",
    "Serbian": "sr",
    "Sesotho": "st",
    "Shona": "sn",
    "Sindhi": "sd",
    "Sinhala (Sinhalese)": "si",
    "Slovak": "sk",
    "Slovenian": "sl",
    "Somali": "so",
    "Spanish": "es",
    "Sundanese": "su",
    "Swahili": "sw",
    "Swedish": "sv",
    "Tagalog (Filipino)": "tl",
    "Tajik": "tg",
    "Tamil": "ta",
    "Tatar": "tt",
    "Telugu": "te",
    "Thai": "th",
    "Tigrinya": "ti",
    "Tsonga": "ts",
    "Turkish": "tr",
    "Turkmen": "tk",
    "Twi (Akan)": "ak",
    "Ukrainian": "uk",
    "Urdu": "ur",
    "Uyghur": "ug",
    "Uzbek": "uz",
    "Vietnamese": "vi",
    "Welsh": "cy",
    "Xhosa": "xh",
    "Yiddish": "yi",
    "Yoruba": "yo",
    "Zulu": "zu"
}
# Función para traducir cuando se presiona el botón
def translate_button_clicked():
    text_to_translate = text_entry.get()
    destination_language = destination_language_var.get()
    destination_language = LANGUAGES.get(destination_language)
    
    translation = translate(text_to_translate, lang_to=destination_language)
    result_label.config(text="Traducción: " + translation)

# Crear la ventana tkinter
root = tk.Tk()
root.title("Traductor")

# Etiqueta de texto
text_label = tk.Label(root, text="Introduce el texto a traducir:")
text_label.pack()

# Entrada de texto
text_entry = tk.Entry(root)
text_entry.pack()

# Etiqueta de idioma de destino
destination_label = tk.Label(root, text="Selecciona el idioma de destino:")
destination_label.pack()

# Menú desplegable para seleccionar el idioma de destino
destination_language_var = tk.StringVar()
destination_language_dropdown = ttk.Combobox(root, textvariable=destination_language_var, values=list(LANGUAGES.keys()))
destination_language_dropdown.pack()

# Botón para iniciar la traducción
translate_button = tk.Button(root, text="Traducir", command=translate_button_clicked)
translate_button.pack()

# Etiqueta para mostrar el resultado
result_label = tk.Label(root, text="")
result_label.pack()

# Iniciar la ventana tkinter
root.mainloop()