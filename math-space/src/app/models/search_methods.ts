interface BisectionResult {
    i_value? : number,
    a_value: number,
    b_value: number,
    c_value: number,
    fa_value: number,
    fb_value: number,
    fc_value: number,
    error_value: number,
}

interface SecanteResult {
    i_value?: number | null,
    xi_value: number | null,
    fxi_value: number | null,
    error_value: number | null,
}

interface NewtonResults {
    i_value?: number,
    xi_value: number,
    xiplus1_value: number,
    fxi_value: number,
    fxi_derivative_value: number,
    e_value: number,
}

interface ReguleFalsi {
    i_value? : number,
    a_value: number,
    b_value: number,
    x_value: number,
    fa_value: number,
    fb_value: number,
    fx_value: number,
    error_value: number,
}