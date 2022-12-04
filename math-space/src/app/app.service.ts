import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { catchError, map, Observable, of } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class AppService {

  ApiUrl = "https://vvkwd9d9eb.execute-api.us-east-2.amazonaws.com/dev"

  constructor(
    private _http: HttpClient,
  ) { }

  /**Cargar los headers de la petición */
  private getHeaders(): any {
    let headers = new HttpHeaders({
        'Content-Type': 'application/json',
    })

    return ({ headers: headers });
  }

  public convertNumber(body:any): Observable<any> {
    return this._http.post(this.ApiUrl + "/float-point", body, this.getHeaders()).pipe(
      map((response:any) =>{

        const {status, data} = response
        return {valid: status, result: data}

      }),
      
      catchError(this.handleError<any>('getLoans', []))
    );
  }

  public resolveGaussJordan(body:any): Observable<any> {
    return this._http.post(this.ApiUrl + "/gauss-jordan", body, this.getHeaders()).pipe(
      map((response:any) =>{

        const {status, data, is_valid} = response
        return {valid: status, result: data, Mstate: is_valid}

      }),
      
      catchError(this.handleError<any>('getLoans', []))
    );
  }

  public resolveGaussSeidel(body:any): Observable<any> {
    return this._http.post(this.ApiUrl + "/gauss-seidel", body, this.getHeaders()).pipe(
      map((response:any) =>{

        const {status, data} = response
        return {valid: status, result: data}

      }),
      
      catchError(this.handleError<any>('getLoans', []))
    );
  }

  public resolveInterpolation(body:any): Observable<any> {
    return this._http.post(this.ApiUrl + "/lagrange", body, this.getHeaders()).pipe(
      map((response:any) =>{

        const {status, data} = response
        return {valid: status, result: data}

      }),
      
      catchError(this.handleError<any>('getLoans', []))
    );
  }

  public searchMethod(body:any, method: string): Observable<any> {
    return this._http.post(this.ApiUrl + method, body, this.getHeaders()).pipe(
      map((response:any) =>{

        const {status, data} = response
        return {valid: status, result: data}

      }),
      
      catchError(this.handleError<any>('getLoans', []))
    );
  }

  private handleError<T>(operation = 'operation', result?: T) {
    return (error: any): Observable<T> => {

      // TODO: send the error to remote logging infrastructure
      console.log('%cerror::', 'color:red', error); // log to console instead
      
      return of(result as T);
    };
  }

}
