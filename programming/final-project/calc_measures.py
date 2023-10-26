
SEXTO = 1/6
CUARTO = 1/4
TERCIO = 1/3
MITAD = 1/2
COSTURA = 0.75

CRUCE = 2.5
FIT_CINTURA= 1.75
ALTURA_CADERA = 18

def calc_measures(talle, largo, encuentro, l_manga, pecho, cintura, cadera):

  p_sisa = CUARTO * pecho + CUARTO * talle + 1

  # Back jacket measures [esp]
  a_esp = encuentro + 1
  b_esp = SEXTO * pecho + 0.5
  c_esp = CUARTO * b_esp
  d_esp = MITAD * c_esp
  e_esp = CUARTO * p_sisa
  f_esp = e_esp - 2.5
  g_esp = TERCIO * cadera + 1



  # Front jacket measures [del]
  a_del = CUARTO * pecho
  b_del = SEXTO * pecho + 1.5
  c_del = TERCIO * b_del
  d_del = a_del + 3
  e_del = e_esp
  f_del = cadera - g_esp + 4

  angulo_hombro = b_del / c_del