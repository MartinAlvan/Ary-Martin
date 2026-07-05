import webbrowser
import time
import pandas as pd
import urllib.parse

df = pd.read_csv('lista.csv') # Asegúrate que tu CSV sea ID,Nombre,Telefono,Confirmado...

url_base = "https://tu-github-link.github.io/index.html?id="

print("Preparando invitaciones... Abre WhatsApp Web primero.")
time.sleep(10)

for idx, f in df.iterrows():
    m = f"¡Qué onda {f['Nombre']}! 👰🤵 Ary y Martin te enviamos esto porque ¡nos casamos! Nuestra historia resumida y tu invitación digital acá: {url_base}{f['ID']}\n🇲🇽 Te esperamos en esta noche mexicana especial. Confírmanos antes de caducar la invitación."
    webbrowser.open(f"https://web.whatsapp.com/send?phone={f['Telefono']}&text={urllib.parse.quote(m)}")
    time.sleep(15)