import { Component, OnInit } from '@angular/core';
import { AppService } from 'src/app/app.service';

@Component({
  selector: 'floating-point',
  templateUrl: './floating-point.component.html',
  styleUrls: ['./floating-point.component.scss']
})
export class FloatingPointComponent implements OnInit {

  decimal_number = ''

  binary_number = ['', '', '']

  decimalToFloat: boolean  = true
  precision = [
    {value: 'none', label: 'Precisión'}, // 0
    {value:'simple', label: 'Simple precisión'},  // 1
    {value: 'doble', label: 'Doble precisión'},  // 2
  ]
  selected = 0

  constructor(
    public _appService: AppService
  ) { }

  ngOnInit(): void {
  }

  convert (){
    let body = {
      data: {
        precision: this.precision[this.selected],
        type: (this.decimalToFloat)  ? 'decimal' : 'binary',
        number: this.decimal_number
      }
    }

    this._appService.convertNumber(body).subscribe(response => {

      let array_result = []
      const {valid, result} = response

      if (valid) {
        if (this.decimalToFloat) {
          this.binary_number = result.split(" ")
        }
      }

    })

  }

}
