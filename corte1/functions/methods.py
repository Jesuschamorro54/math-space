from time import sleep
from functions import config
from functions.colors import C


def get_params():
    print("-----------------------------------------------------")
    op= int(input("1. Simple precision\n2. Soble Precisión\n:"))

    config.x_exponent = 8 if op == 1 else 11

    config.len_mantissa = 23 if op == 1 else 52
    print("-----------------------------------------------------")


def get_number():
    
    number = input("Number: ")

    if number[0] == "-":
        config.x_sign = 1

    print("")

    return number


# Convierte la parte entera de un numero decimal a binario
def to_binary_integer(number: int, p = True):
    
    result = ""

    if number == 0:
        config.isZero = True
        return "0"

    while number >= 1:

        resto = int(number%2)

        number = number/2

        n = resto
    
        result = str(n) + result

    if result:
        config.len_mantissa = config.len_mantissa - len(result) + 1

    sleep(1)
    if p:
        print("PARTE ENTERA BINARIA")
        print_binary_number(result, False)
    return result


# Convierte la parte flotante de un numero decimal a binario
def to_binary_float(number: int, iteration = None, last=None):
    
    # Variable que valida si hay que hacer nuevamente el proceso para agregar más bits a la mantisa
    extra = 0

    # El resultado que voy a devolver
    result = last if last else ''

    # Variable que me valida si los numeros que iré recorriendo son ceros consecutivos
    zero = False if iteration else True

    # Cuantas veces voy a iterar para generar bit en la mantisa
    iteration = iteration if iteration else config.len_mantissa
    
    # Generación de la mantisa
    for i in range(iteration):
        
        # Operación
        number *= 2
        bit = "0" if number < 1 else "1"  # Definir el bit que se va a guardar dependiendo del resultado obtenido

        # El nuevo numero
        number = float ( "0." + str(number).split(".")[1] ) if number > 1 else number
        
        # Si aún sigo obteniendo ceros, voy aumentando a la variable extra
        if bit == "0" and zero:
            extra += 1
        else:
            zero = False

        # Generando los bits
        result += bit
    
    # En caso de ser una recursividad 
    if last:
        return result
    
    # Si la parte entera fue un cero
    if (config.isZero):

        # Valido cuantas veces voy a volver a hacer la operación para optener más bit
        extra += 1

        # Genero el resto de bits para completar los espacios en memoria
        result = to_binary_float(number, extra, result)
    

    # Muestro el numero en formato punto flotante
    sleep(1)
    print("PUNTO FLOTANTE")
    print_binary_number(result, False)

    # Retornar el valor
    return result


# Convertir numero binario a decimal
def to_decimal(number: str, floatPoint: bool):

    # Decimal que se va a retornar
    decimal = 0

    for index, bit in enumerate(number[::-1] if not floatPoint else number):
        decimal += int(bit) * 2 ** index if not floatPoint else int(bit) * 1/(2 **index*2)

    return decimal


# Normalización del punto flotante
def to_normalized_form(number: str, rever = {}):

    sleep(1)
    print("\n------\nNumero a normalizar: ", number)

    e = None
    # Si hay que convertir de decimal a binario
    if not rever:

        # Extraigo la parte entera
        _int = number.split(".")[0]

        # Extraigo la parte decimal
        _float = number.split(".")[1]

        # Condicional para validar si la parte es 0 u otro numero
        if ('1' in _int):
            
            # Identifico donde está el primer bit 1 ara mover el punto
            bit_one =  _int.index("1") + 1
            
            # Calculo el exponente decimal a partir de cuantas posiciones moví el punto
            e = number.index(".") - bit_one
            
            # Creo el numero normalizado
            number = f"1.{_int[bit_one:]}{_float}"
            
        else:

            # Identifico donde está el primer bit 1 ara mover el punto
            bit_one =  _float.index("1") + 1

            # Calculo el exponente decimal a partir de cuantas posiciones moví el punto
            e = - bit_one

            # Creo el numero normalizado
            number = f"1.{_float[bit_one:]}"

        # Muestro el numero Normalizado
        sleep(1)
        print(f"NORMALIZADA: {number} x 2^{e}")

    else:

        # Extraigo el exponente en formato decimal
        e = rever['e']  

        # Declaro el signo del numero
        sign = "-" if int(rever['sign']) == 1 else ""

        # Muestro el numero Normalizado
        sleep(1)
        print(f"NORMALIZADA: {sign}1.{number} x 2^{e}")

        # Extraigo la parte entera del numero en decimal
        _int = "1" + number[:e] if e > 0 else "0"

        # Extraigo la parte flotante del numero en decimal
        _float = number[e:] if e > 0 else f"{'0'*(abs(e)-1)}1{number}"

        # Concateno para formar el numero en punto flotante
        number = _int + "." +  _float

    # Reetornar el valor
    return number, e
        

def get_exp(e: int):
    
    expMax = (2**config.x_exponent) - 1

    exp = e + int(expMax/2)

    result = str(to_binary_integer(exp, False))

    if len(result) < config.x_exponent:
        result = "0"+result

    return result


def get_e(exp: str):
    expMax = (2**(len(exp) - 1 )) - 1

    e = to_decimal(exp, False) - int (expMax)

    return int(e)


def print_binary_number(number, jump):
    index = 0
    color = C[index]
    for i, bit in enumerate(number):

        print(f"[{color}{bit}{C[-1]}]", end="")

        if ((i == 0) or (i == config.x_exponent)) and jump:
            index += 1
            color = C[index]
    
    print("\n")


def minor(number:str):
    new = None

    aux = list((number[::-1]).replace('1', '0', 1)[::-1])
    
    new = "".join(aux[:-1]) + "1"

    return new


def major(number:str):

    aux = list(number)

    return "".join(aux[:len(aux)-1]) + "1"
