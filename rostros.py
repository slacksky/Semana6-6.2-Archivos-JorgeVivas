""" Modulo para el manejo de rostros de
    los habitantes del planeta ASCII
    Oscar Franco-Bedoya
    Junio 2-2021 """

#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================

#----------Definición de Funciones (Dividir)------------

def imprimir_rostro(rostro):

  """ 
  Parameters
  ----------
  Rostro:[[[]]]
    Una lista de 3 niveles con el rostro codificado en el archivo
  
  Returns
  -------
  Ninguno
    Presenta el rostro en la consola    
  """ 
  for linea_codigo in rostro: #recorre cada linea del rostro
    for codigo in linea_codigo: #recorre cada codigo de la linea
       imprimir_linea(codigo) #imprime el caracter un numero de veces
    print("\n")


def imprimir_linea(codigo):

  """ 
  Parameters
  ----------
  codigo: string
  un codigo (numero, letra)  
  Returns
  -------
  Ninguno
    imprime en la consola el caracter del codigo la cantidad de veces en numero    
  """ 
  print(codigo)
  numero=int(codigo[0])
  caracter=codigo[1]
  for i in range(0,numero):
    print(caracter,end="") 
  
  
#----------------------------------------------------------------------------

def cargar_rostro(archivo_rostro):

  """ 
  Parameters
  ----------
  archivo:string
    El identificador del archivo y la ubicación  del mismo
  Returns
  -------
  Rostro:[[[]]]
    Una lista de 3 niveles con el rostro codificado en el archivo    
  """  
  #fh= open(archivo)
  rostro = []  #estructura para el rostro completo que esta formado por 5 lineas
  archivo_rostro = archivo_rostro.lstrip().rstrip()
  for linea in archivo_rostro: #recorre el archivo
    codigos_linea= linea.rstrip().split(',') #obtiene la lista de codigos por cada linea
    linea=[]
    for codigo in codigos_linea: #separa el numero del caracter 
      linea.append(codigo.split('\t')) 
    rostro.append(linea)
  
  return rostro 

  def calcular_estadisticas(rostros, ndia):
    """ 
    Parameters
    ----------
    rostros:[(namedtuple)]
      Una estructura de datos con los rostros de asciianos codificados   
    ndia: string 
      Una cadena con el dnia que se desea dibujar
    Returns
    -------
    Ninguna
     Dibuja el rostro del asciiano con el ndia del ascciano

    """  
  return "No implementado"