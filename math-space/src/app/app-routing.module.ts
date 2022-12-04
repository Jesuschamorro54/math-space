import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { BisectionComponent } from './components/bisection/bisection.component';
import { FloatingPointComponent } from './components/floating-point/floating-point.component';
import { GaussJordanComponent } from './components/gauss-jordan/gauss-jordan.component';
import { GaussSeidelComponent } from './components/gauss-seidel/gauss-seidel.component';
import { InterpolationComponent } from './components/interpolation/interpolation.component';
import { NewthonRaphsonComponent } from './components/newthon-raphson/newthon-raphson.component';
import { RegulaFalsiComponent } from './components/regula-falsi/regula-falsi.component';
import { SecanteComponent } from './components/secante/secante.component';


const routes: Routes = [
  { path: 'floating-point', component: FloatingPointComponent },

  { path: 'biseccion', component: BisectionComponent },
  { path: 'secante', component: SecanteComponent },
  { path: 'newthon-raphson', component: NewthonRaphsonComponent },
  { path: 'regula-falsi', component: RegulaFalsiComponent },

  { path: 'interpolation', component: InterpolationComponent },
  { path: 'gauss-jordan', component: GaussJordanComponent },
  { path: 'gauss-seid', component: GaussSeidelComponent },
];


@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
