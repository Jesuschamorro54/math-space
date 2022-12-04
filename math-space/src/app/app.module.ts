import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { FloatingPointComponent } from './components/floating-point/floating-point.component';
import { GaussSeidelComponent } from './components/gauss-seidel/gauss-seidel.component';
import { GaussJordanComponent } from './components/gauss-jordan/gauss-jordan.component';
import { InterpolationComponent } from './components/interpolation/interpolation.component';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { BisectionComponent } from './components/bisection/bisection.component';
import { SecanteComponent } from './components/secante/secante.component';
import { NewthonRaphsonComponent } from './components/newthon-raphson/newthon-raphson.component';
import { RegulaFalsiComponent } from './components/regula-falsi/regula-falsi.component';

@NgModule({
  declarations: [
    AppComponent,
    FloatingPointComponent,
    GaussSeidelComponent,
    GaussJordanComponent,
    InterpolationComponent,
    BisectionComponent,
    SecanteComponent,
    NewthonRaphsonComponent,
    RegulaFalsiComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule, ReactiveFormsModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
