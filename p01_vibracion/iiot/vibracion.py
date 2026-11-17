class SensorVibracion:
  def __init__(self, id_motor: str, vibracion_rms_val: float):
    self.id_motor=id_motor
    self._vibracion_rms=vibracion_rms_val

  @property
  def vibracion_rms(self):
    return self._vibracion_rms
  
  @vibracion_rms.setter
  def vibracion_rms(self, nuevo_valor: float):
    if nuevo_valor < 0.0:
       raise ValueError("La vibración no puede ser inferior a 0.0 mm/s")
    self._vibracion_rms = nuevo_valor
