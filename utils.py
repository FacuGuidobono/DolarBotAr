import requests
from datetime import datetime

#url de la api
base_url = 'https://dolarapi.com/v1/dolares/'

# string con iconos que se utilizan en varias funciones
tipo_dato = ['🏦 Oficial','🔷 Blue','💳 Tarjeta','📚 Menú']

#mensaje de bienvenida
start_msg = f'''
💵Bienvenido al bot de cotizacion de dólar💵
Para ver la cotizacion de un dolar en particular, elija una opción:\n\n
▫️ {tipo_dato[0]}
▫️ {tipo_dato[1]}
▫️ {tipo_dato[2]}
.
'''

# selecciona el icono correspondiente a la url
def select_icon (tipoDeDolar):
    match(tipoDeDolar):    
        case 'oficial':
            return '🏦'
        case'tarjeta':
            return '💳'
        case 'blue':
            return '🔷'


#formatea la fecha y hora recibida
def formatearFecha(fecha:str) -> str :
    fecha_dt = datetime.fromisoformat(fecha.replace("Z", "+00:00"))
    fecha_formateada = fecha_dt.strftime("%d/%m/%Y %H:%M")
    return fecha_formateada






# recibe la info de la api y devuelve un string con los datos
def tipo_dolar(tipoDeDolar):
    icon = tipoDeDolar # guardamos el icono
    url = base_url + tipoDeDolar  #url completa de la api
    
    dolar = requests.get(url)
        
    if dolar.status_code == 200:   
            
            dolar = dolar.json()
            icon = select_icon(icon)  # seleccionamos el icono de acuerdo a la url
            
    elif dolar.status_code == 404:
            return '⛔⛔Sin Conexión por el momento, intentelo más tarde!⛔⛔'
    else:
            return "sin respuesta 🤖🤖⛔"
    
    

    return f"""
        \n\t{icon}  DOLAR {dolar['nombre'].upper()} {icon}
   
▫️ 🗓️ Fecha Cotización: {formatearFecha(dolar['fechaActualizacion'])}\n
▫️ ➡️Compra: ${dolar['compra']}\n
▫️ ⬅️Venta: ${dolar['venta']}
\n\n
"""

