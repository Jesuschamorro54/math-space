from methods import Calculate


# Main debe recibir como parametros 
# number: el numero que se va a convertir  
# type: numero que se pasa (decimal o binario)
# 
#   
#
def main(type):

    number:str = calculate.get_number()

    # Para saber si el numero es 
    if 'decimal' in type:
        calculate.set_params("doble")
        save_in_memory(number) 
    else:
        revert(number)


def save_in_memory(number:str):

    number = number.split(".") if "." in number else [number, "0"]

    if number:

        x_int = int(number[0])
        x_float =  float("0." + number[1])


        integer_part = calculate.to_binary_integer(abs(x_int))

        float_part = calculate.to_binary_float(x_float)

        binary_number = f"{integer_part}.{float_part}"

        normalized_number, e = calculate.to_normalized_form(binary_number)

        exp = calculate.get_exp(e)

        mantissa = normalized_number.split(".")[1]

        print(f"\n|RESULTADO| -> ", end="")
        result = f"{calculate.x_sign}{exp}{mantissa}"
        r = calculate.print_binary_number(result, True)

        return r


def revert(binary: str):
    
    binary = binary.split(" ")
    binaryMax = calculate.major(binary[2])
    binaryMin = calculate.minor(binary[2])


    if binary:
        # Obtener e
        decimal = ''
        e = calculate.get_e(binary[1])

        # Pasar a formula normalizada y obtener el numero en formato punto flotante
        data = {'sign': binary[0], 'e': e}

        float_pointMax, e = calculate.to_normalized_form(binaryMax, data)
        float_point, e = calculate.to_normalized_form(binary[2], data)
        float_pointMin, e = calculate.to_normalized_form(binaryMin, data)


        _intMax = float_pointMax.split(".")[0]
        _floatMax = float_pointMax.split(".")[1]

        _int = float_point.split(".")[0]
        _float = float_point.split(".")[1]

        _intMin = float_pointMin.split(".")[0]
        _floatMin = float_pointMin.split(".")[1]



        sign = "-" if int(data['sign']) == 1 else ""

        print(f"PUNTO FLOTANTE: {sign}{_int}.{_float}")

        _floatMax = calculate.to_decimal(_floatMax, True)
        _intMax = calculate.to_decimal(_intMax, False) + _floatMax

        _float = calculate.to_decimal(_float, True)
        _int = calculate.to_decimal(_int, False) + + _float

        _floatMin = calculate.to_decimal(_floatMin, True)
        _intMin = calculate.to_decimal(_intMin, False) + _floatMin
        

        # Convertir a decimal
        print(f"\n|RESULTADO        | -> {sign}{_int}\n")
        print(f"\n|NUMERO INFERIOR  | -> {sign}{_intMin}\n")
        print(f"\n|NUMERO SUPERIOR  | -> {sign}{_intMax}\n\n")

        decimal = sign + _int

        return decimal



calculate = Calculate()
main('binary')