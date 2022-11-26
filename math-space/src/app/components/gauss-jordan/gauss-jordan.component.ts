import { Component, OnInit } from '@angular/core';
import { AppService } from 'src/app/app.service';

@Component({
  selector: 'gauss-jordan',
  templateUrl: './gauss-jordan.component.html',
  styleUrls: ['./gauss-jordan.component.scss']
})
export class GaussJordanComponent implements OnInit {

  constructor(
    private _appService: AppService
  ) { }


  placeholders = [
    "Escribe el sistema de ecuaciones ej: \n\n\
         3x +  y -  z = 1 \n\
          x -  y +  z = -3 \n\
         2x -  y +  z = 0 \n\n\
      Entre cada uno de los numeros y signos debe haber solo un espacio",

    "Escribe la matriz dada ej: \n\n\
      # matriz \n\
      3  1 -1\n\
      1 -1  1\n\
      2 -1  1\n\
      #end\n\
      \n\
      # b_array \n\
        1\n\
       -3\n\
        0\n\
      #end\n\n\
    Entre cada uno de los numeros y signos debe haber solo un espacio",
  ]

  precision = [
    { value: 'ec', label: 'Sistema de ecuación' },  // 1
    { value: 'mt', label: 'Matriz' },  // 2
  ]

  selected = 1
  textArea = ""
  sending = false;

  matriz: Array<any> = []
  b_array: Array<any> = []

  solution: Array<any> | null = [];


  ngOnInit(): void {
  }


  readMatriz () {

    this.matriz = []
    this.b_array = []

    let take_matrix_data = false
    let take_barray_data = false

    let lines = this.textArea.split("\n")

    if (this.selected == 1) {
      lines.forEach(line => {

        if (line.includes('#end')){
          take_matrix_data = false
          take_barray_data = false
        }
  
        if (take_matrix_data) {
          this.matriz.push(line.split(" ").map(Number))
        }
  
        if (take_barray_data) {
          this.b_array.push(parseFloat(line))
        }
  
        if (line.includes('name: A')){
          take_matrix_data = true
        }
  
        if (line.includes('name: b')){
          take_barray_data = true
        }
      });
    }
  }

  applyStyle(isVector?: boolean) {

    const size = 100 / this.matriz.length

    let styles = {'width': isVector ? `100%` : `${size}%`, 'height': `${size*2}px`}

    return styles
  }

  resolve() {

    let b_array_body: Array<any> = []

    this.b_array.forEach(number => b_array_body.push([number]))

    if (!this.sending && this.matriz.length != 0) {
      this.sending = true

      let body = {
        data: {
          matriz: this.matriz,
          b_array: b_array_body,
        }
      }

      this._appService.resolveGaussJordan(body).subscribe(response => {
        this.sending = false;
        const { valid, result, Mstate } = response

        if (valid) {
          
          let temp_solution = result.solution

          temp_solution = temp_solution.split("\n").join(",").match(/\d+(?:\.\d+)?/g)?.map(Number)

          this.solution = temp_solution

          console.log(this.solution)
        }

      })
    }
  }

}
