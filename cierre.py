import webbrowser
import time
import pandas as pd
import urllib.parse

# Aquí leemos quienes NUNCA confirmaron segun tu Excel actualizado
# Puedes exportar el Google Sheets a .csv este día
df = pd.read_csv('recientes.csv')
p_olvidados = df[df['Confirmado'] != "SI"]

print("Enviando advertencias de cierre perentorio...")
time.sleep(10)

for idx, f in p_olvidados.iterrows():
    m = (f"¡Holi {f['Nombre']}! 👋 de este lado los prometidos. Vimos que no pudiste confirmar a tiempo y hoy tristemente "
         f"el tiempo ya terminó. ⏲️ Nos parte el alma cerrar la lista del salón sin ti, pero nos encantará "
         f"mandarte el *ÁLBUM DIGITAL* de las fotos una vez que termine la fiesta. 📸✨ \n¡Pasala padre y nos vemos prontito!")
    
    webbrowser.open(f"https://web.whatsapp.com/send?phone={f['Telefono']}&text={urllib.parse.quote(m)}")
    time.sleep(18)