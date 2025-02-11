from all_scripts import astrometria as astrom
from all_scripts import archivos as arch


# Variable global para la ruta principal de la organización de carpetas
route = "./"

# Bloque principal: se usan las rutas construidas a partir de la variable global 'route'
if __name__ == "__main__":
    
        # Primero se ejecuta consultas.py (opcional, según tu flujo)
    
        coords = astrom.get_coordinates_from_name("algol")

        #print("Las coordenadas de algol son:", coords)

        astrom.save_to_csv()
        #arch.ejecutar_curl_desde_archivo()

        # Una vez que el script de Bash se detenga por alcanzar el umbral, se procede a fotometría

        astrom. rutina_astrometica()
# Observatorio Astronómico Nacional 2025 #

