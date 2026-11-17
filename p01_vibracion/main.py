from Python_POO.p01_vibracion.iiot.vibracion import SensorVibracion
from Python_POO.p01_vibracion.diagnostico.analizador import AnalizadorVibracion

def ejecutar_aplicacion():
  print("=== MONITOR IIOT VIBRACIÓN ISO 10816 ===")
  id_motor = input("Introduce ID del Motor Industrial: ")
  vibracion_rms_val = float(input("Introduce lectura de Vibración RMS (mm/s): "))

  sensor_obj = SensorVibracion(id_motor, vibracion_rms_val)
  analizador = AnalizadorVibracion()
  estado = analizador.evaluar_estado(sensor_obj)

  print("-------------------------------------------")
  print(f"⚙️ [MOTOR {id_motor}] RMS: {vibracion_rms_val} mm/s | Estado Diagnóstico: {estado}")

if __name__=="__main__":
  ejecutar_aplicacion()