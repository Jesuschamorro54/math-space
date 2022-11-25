class Calculate:
    def __init__(self):
        # Define si el la parte entera es cero
        self.isZero = False

        # Signo por defualt es positivo
        self.x_sign = 0

        # Longitud del exponente por default
        self.x_exponent = 5

        # Longitud de la mantisa por default
        self.len_mantissa = 10  

        # Longitud por defecto del numero de bit a guardar
        self.long_number = 16  



    def set_params(self, precision):

        self.x_exponent = 8 if precision == "simple" else 11

        self.len_mantissa = 23 if precision == "simple" else 52


    def get_number(self):
        
        number = input("Number: ")

        if number[0] == "-":
            self.x_sign = 1

        return number


    # Convierte la parte entera de un numero decimal a binario
    def to_binary_integer(self, number: int, p = True):
        
        result = ""

        if number == 0:
            self.isZero = True
            return "0"

        while number >= 1:

            resto = int(number%2)

            number = number/2

            n = resto
        
            result = str(n) + result

        if result:
            self.len_mantissa = self.len_mantissa - len(result) + 1

        if p:
            # print("PARTE ENTERA BINARIA")
            self.print_binary_number(result, False)
        return result


    # Convierte la parte flotante de un numero decimal a binario
    def to_binary_float(self, number: int, iteration = None, last=None):
        
        # Variable que valida si hay que hacer nuevamente el proceso para agregar más bits a la mantisa
        extra = 0

        # El resultado que voy a devolver
        result = last if last else ''

        # Variable que me valida si los numeros que iré recorriendo son ceros consecutivos
        zero = False if iteration else True

        # Cuantas veces voy a iterar para generar bit en la mantisa
        iteration = iteration if iteration else self.len_mantissa
        
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
        if (self.isZero):

            # Valido cuantas veces voy a volver a hacer la operación para optener más bit
            extra += 1

            # Genero el resto de bits para completar los espacios en memoria
            result = self.to_binary_float(number, extra, result)
        

        # Muestro el numero en formato punto flotante
        # print("PUNTO FLOTANTE")
        self.print_binary_number(result, False)

        # Retornar el valor
        return result


    # Convertir numero binario a decimal
    def to_decimal(self, number: str, floatPoint: bool):

        # Decimal que se va a retornar
        decimal = 0

        for index, bit in enumerate(number[::-1] if not floatPoint else number):
            decimal += int(bit) * 2 ** index if not floatPoint else int(bit) * 1/(2 **index*2)

        return decimal


    # Normalización del punto flotante
    def to_normalized_form(self, number: str, rever = {}):

        # print("\n------\nNumero a normalizar: ", number)

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
            # print(f"NORMALIZADA: {number} x 2^{e}")

        else:

            # Extraigo el exponente en formato decimal
            e = rever['e']  

            # Declaro el signo del numero
            sign = "-" if int(rever['sign']) == 1 else ""

            # Muestro el numero Normalizado
            # print(f"NORMALIZADA: {sign}1.{number} x 2^{e}")

            # Extraigo la parte entera del numero en decimal
            _int = "1" + number[:e] if e > 0 else "0"

            # Extraigo la parte flotante del numero en decimal
            _float = number[e:] if e > 0 else f"{'0'*(abs(e)-1)}1{number}"

            # Concateno para formar el numero en punto flotante
            number = _int + "." +  _float

        # Reetornar el valor
        return number, e
            

    def get_exp(self, e: int):
        
        expMax = (2**self.x_exponent) - 1

        exp = e + int(expMax/2)

        result = str(self.to_binary_integer(exp, False))

        if len(result) < self.x_exponent:
            result = "0"+result

        return result


    def get_e(self, exp: str):
        expMax = (2**(len(exp) - 1 )) - 1

        e = self.to_decimal(exp, False) - int (expMax)

        return int(e)


    def print_binary_number(self, number, jump):
        index = 0
        result = ''
        for i, bit in enumerate(number):

            result += f"{bit}"

            if ((i == 0) or (i == self.x_exponent)) and jump:
                result += " "
        
        return result


    def minor(self, number:str):
        new = None

        aux = list((number[::-1]).replace('1', '0', 1)[::-1])
        
        new = "".join(aux[:-1]) + "1"

        return new


    def major(self, number:str):

        aux = list(number)

        return "".join(aux[:len(aux)-1]) + "1"
