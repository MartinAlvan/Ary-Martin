import pywhatkit
import pandas as pd
import time

# Cargar Excel
df = pd.read_csv('lista.csv')
url_base = "https://martinalvan.github.io/Ary-Martin/?id="

print("ADVERTENCIA: Deja el manos libres. El script controlará tu teclado.")
time.sleep(20)

for index, row in df.iterrows():
    nombre = row['Nombre']
    tel = "+" + str(row['Telefono']) # Requiere el signo + y código de país (Ej: +521...)
    link = url_base + str(row['ID'])
    
    mensaje = f"¡Hola {nombre}! 👰🤵 Ary y Martin te enviamos tu invitación digital {link} \n🇲🇽 Te esperamos en esta noche mexicana especial. Confírmanos antes de caducar la invitación."
    #mensaje = f"¡Qué onda {f['Nombre']}! 👰🤵 Ary y Martin te enviamos esto porque ¡nos casamos! Nuestra historia resumida y tu invitación digital acá: {url_base}{f['ID']}\n🇲🇽 Te esperamos en esta noche mexicana especial. Confírmanos antes de caducar la invitación."
   
    
    # sendwhatmsg_instantly(teléfono, mensaje, tiempo_espera, cerrar_pestaña)
    # espera 15 seg para que cargue y a los 2 seg después de enviar cierra la pestaña
    pywhatkit.sendwhatmsg_instantly(tel, mensaje, 15, True, 3) 
    
    print(f"Mensaje enviado automáticamente a: {nombre}")