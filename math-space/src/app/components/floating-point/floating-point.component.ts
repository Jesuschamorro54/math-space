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

  decimalToFloat: boolean = true
  precision = [
    { value: 'none', label: 'Precisión' }, // 0
    { value: 'simple', label: 'Simple precisión' },  // 1
    { value: 'doble', label: 'Doble precisión' },  // 2
  ]

  selected = 0
  sending = false

  constructor(
    public _appService: AppService
  ) { }

  ngOnInit(): void {
  }

  convert() {

    let number = this.decimalToFloat ? this.decimal_number : this.binary_number.join(" ");

    if (!this.sending && number != '' && number != null) {
      this.sending = true

      let body = {
        data: {
          precision: this.precision[this.selected].value,
          type: this.decimalToFloat ? 'decimal' : 'binary',
          number: number
        }
      }

      this._appService.convertNumber(body).subscribe(response => {
        this.sending = false;
        const { valid, result } = response

        if (valid) {
          if (this.decimalToFloat) {
            this.binary_number = result.split(" ")
          } else {
            this.decimal_number = result
          }
        }

      })
    }
  }

}
