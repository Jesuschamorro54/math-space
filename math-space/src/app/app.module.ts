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

@NgModule({
  declarations: [
    AppComponent,
    FloatingPointComponent,
    GaussSeidelComponent,
    GaussJordanComponent,
    InterpolationComponent
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
