import { Component, OnInit } from '@angular/core';
import { AppService } from 'src/app/app.service';

@Component({
  selector: 'app-bisection',
  templateUrl: './bisection.component.html',
  styleUrls: ['./bisection.component.scss']
})
export class BisectionComponent implements OnInit {

  constructor(
    private _appService: AppService
  ) { }

  selected = 0
  sending: boolean = false;
  results: Array<BisectionResult> = []

  tolerancia = [
    { value: 0.001, label: '<p>Tolerancia</p>' },
    { value: 0.001, label: '<p>10<sup>-2</sup></p>' },
    { value: 0.0001, label: '<p>10<sup>-3</sup></p>' },
    { value: 0.00001, label: '<p>10<sup>-4</sup></p>' },
    { value: 0.000001, label: '<p>10<sup>-5</sup></p>' },
    { value: 0.0000001, label: '<p>10<sup>-6</sup></p>' },
    { value: 0.00000001, label: '<p>10<sup>-7</sup></p>' },
    { value: 0.000000001, label: '<p>10<sup>-8</sup></p>' },
    { value: 0.0000000001, label: '<p>10<sup>-9</sup></p>' },
    { value: 0.00000000001, label: '<p>10<sup>-10</sup></p>' },
  ]

  initialValues = {
    equation: '',
    error: this.tolerancia[this.selected].value,
    value_a: 0,
    value_b: 0
  }



  ngOnInit(): void {
  }

  onSubmit() {

    this.initialValues.error = this.tolerancia[this.selected].value;
    const {equation, error, value_a, value_b} = this.initialValues;
    
    let isvalid = (equation != '' && value_a != null && value_b != null && value_a != value_b)

    console.log(this.initialValues);
    console.log(isvalid);

    if (!this.sending && isvalid) {

      this.sending = true;

      let body =  this.initialValues

      this._appService.searchMethod(body, "/biseccion").subscribe(response => {
        this.sending = false;
        const { valid, result } = response

        if (valid) {
          this.results = result;
        }

      });

    }

  }


}
