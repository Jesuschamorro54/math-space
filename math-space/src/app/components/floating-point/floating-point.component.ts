import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'floating-point',
  templateUrl: './floating-point.component.html',
  styleUrls: ['./floating-point.component.scss']
})
export class FloatingPointComponent implements OnInit {

  decimalToFloat: boolean  = true;
  precision = [
    {value: 'none', label: 'Precisión'}, // 0
    {value:'simple', label: 'Simple precisión'},  // 1
    {value: 'doble', label: 'Doble precisión'},  // 2
  ]
  selected = 0

  constructor() { }

  ngOnInit(): void {
  }

  open (as:any){
    console.log(as)
  }

}
