from functions.methods import *
from functions.colors import G, RS
from functions import config

def save_in_memory(number:str):
    # Obtener parametros si es necesario+
    get_params()


    number = number.split(".") if "." in number else [number, "0"]

    if number:

        x_int = int(number[0])
        x_float =  float("0." + number[1])


        integer_part = to_binary_integer(abs(x_int))

        float_part = to_binary_float(x_float)

        binary_number = f"{integer_part}.{float_part}"

        normalized_number, e = to_normalized_form(binary_number)

        exp = get_exp(e)

        mantissa = normalized_number.split(".")[1]

        sleep(1)        

        print(f"{G}\n|RESULTADO| -> {RS}", end="")
        result = f"{config.x_sign}{exp}{mantissa}"
        print_binary_number(result, True)


def revert(binary: str):
    
    binary = binary.split(" ")
    binaryMax = major(binary[2])
    binaryMin = minor(binary[2])


    if binary:
        # Obtener e
        e = get_e(binary[1])

        # Pasar a formula normalizada y obtener el numero en formato punto flotante
        data = {'sign': binary[0], 'e': e}

        float_pointMax, e = to_normalized_form(binaryMax, data)
        float_point, e = to_normalized_form(binary[2], data)
        float_pointMin, e = to_normalized_form(binaryMin, data)


        _intMax = float_pointMax.split(".")[0]
        _floatMax = float_pointMax.split(".")[1]

        _int = float_point.split(".")[0]
        _float = float_point.split(".")[1]

        _intMin = float_pointMin.split(".")[0]
        _floatMin = float_pointMin.split(".")[1]



        sign = "-" if int(data['sign']) == 1 else ""

        print(f"PUNTO FLOTANTE: {sign}{_int}.{_float}")

        _floatMax = to_decimal(_floatMax, True)
        _intMax = to_decimal(_intMax, False) + _floatMax

        _float = to_decimal(_float, True)
        _int = to_decimal(_int, False) + + _float

        _floatMin = to_decimal(_floatMin, True)
        _intMin = to_decimal(_intMin, False) + _floatMin
        

        # Convertir a decimal
        print(f"{G}\n|RESULTADO        | -> {sign}{_int}{RS}\n")
        print(f"{G}\n|NUMERO INFERIOR  | -> {sign}{_intMin}{RS}\n")
        print(f"{G}\n|NUMERO SUPERIOR  | -> {sign}{_intMax}{RS}\n\n")



if __name__ == "__main__":

    number:str = get_number()

    if "." in number or len(number.split(" ")) == 1:
        save_in_memory(number) 
    else:
        revert(number)