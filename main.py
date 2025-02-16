from all_scripts import astrometria as astrom
from all_scripts import archivos as arch
from all_scripts import todas_las_rutas as ru

# Variable global para la ruta principal de la organización de carpetas


# Bloque principal: se usan las rutas construidas a partir de la variable global 'route'
if __name__ == "__main__":
                estrella = "algol"
                print(f"Bienvenido al programa para encontrar las curvas de luz de {estrella}")
                print(" ")
                print("a continuación debes seleccionar una de las dos opciones")
                print("1.Si es la primera vez que ejecutas el programa escribe: 1")
                print(" ")
                print("2.Para realizar el proceso de la descarga y luego análisis escribe: 2")
                print(" ")
                print("3.Para realizar solo la fotometría de imagenes descargadas escribe: 3")
                print(" ")
                print("4.Para graficar datos ya analizados escribe: 4")
                opcion = input("opción a escoger: ")
                opcion = int(opcion)
                if opcion == 1:
                #Instalación de librerias desde la ejecución del .sh con el comando pip install lib
                    arch.ejecutar_sh(ru.bash_scripts+"instalacion_librerias.sh")
                    astrom.save_to_csv()
                    arch.ejecutar_curl_desde_archivo()
                    # Una vez que el script de Bash se detenga por alcanzar el umbral, se procede a fotometría
                    
                    astrom.rutina_astrometica()
                elif opcion == 2:
                    arch.ejecutar_curl_desde_archivo()
                    astrom.rutina_astrometica()
                elif opcion == 3:
                    astrom.rutina_astrometica()
                elif opcion == 4:
                    astrom.curvas_de_luz_estrella()
                else:
                      print("Porfavor escribe solo el numero sin espacios ni otros numeros o valores")
                    
                        


