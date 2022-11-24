import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { FloatingPointComponent } from './components/floating-point/floating-point.component';
import { GaussJordanComponent } from './components/gauss-jordan/gauss-jordan.component';
import { GaussSeidelComponent } from './components/gauss-seidel/gauss-seidel.component';
import { InterpolationComponent } from './components/interpolation/interpolation.component';


const routes: Routes = [
  { path: 'floating-point', component: FloatingPointComponent },
  { path: 'interpolation', component: InterpolationComponent },
  { path: 'gauss-jordan', component: GaussJordanComponent },
  { path: 'gauss-seid', component: GaussSeidelComponent },
];


@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
