import gspread

def obtener_datos():

    cliente = gspread.service_account(filename="credencialess (2).json")
    
    archivo = cliente.open("Copia de Demo Registro de Matrícula (respuestas)")
    
    hoja = archivo.worksheet("Respuestas de matricula")
    
    datos = hoja.get_all_records()
    return datos