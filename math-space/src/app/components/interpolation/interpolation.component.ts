import { Component, ElementRef, OnInit, ViewChild } from '@angular/core';
import { AppService } from 'src/app/app.service';

@Component({
  selector: 'interpolation',
  templateUrl: './interpolation.component.html',
  styleUrls: ['./interpolation.component.scss']
})
export class InterpolationComponent implements OnInit {

  constructor(
    private _appService: AppService
  ) { }


  placeholders = [
    "",

    "Escribe los valores de los puntos ej: \n\n\
      # x = [1, 2, 3, 4] \n\
      # y = [5, 6, 7, 8]"
  ]

  precision = [
    { value: 'ec', label: 'Sistema de ecuación' },  // 1
    { value: 'mt', label: 'vector_x' },  // 2
  ]

  selected = 1
  textArea = ""
  sending = false;

  vector_x: Array<any> = []
  vector_y: Array<any> = []

  solution = "";


  ngOnInit(): void {
  }


  readData () {

    this.vector_x = []
    this.vector_y = []

    let lines = this.textArea.split("\n")

    if (this.selected == 1) {
      lines.forEach(line => {

        if (line.includes('x=') || line.includes('x =')){
          this.vector_x = line.split("=")[1].split("[").join("").split("]").join("").split(",")
        }

        if (line.includes('y=') || line.includes('y =')){
          this.vector_y = line.split("=")[1].split("[").join("").split("]").join("").split(",")
        }
      });
    }

    console.log(this.vector_x)
    console.log(this.vector_y)
  }

  applyStyle(isVector?: boolean) {

    const size = 100 / this.vector_x.length

    let styles = {'width': isVector ? `100%` : `${size}%`, 'height': `${size*2}px`}

    return styles
  }

  resolve() {

    if (!this.sending && this.vector_x.length != 0) {
      this.sending = true

      let body = {
        data: {
          vector_x: this.vector_x,
          vector_y: this.vector_y,
        }
      }

      this._appService.resolveInterpolation(body).subscribe(response => {
        this.sending = false;
        const { valid, result } = response

        if (valid) {

          this.solution = result.solution
          console.log(this.solution)
        }

      })
    }
  }

}
