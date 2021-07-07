import { Injectable } from '@angular/core';
import { BehaviorSubject, Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class AuthadminService {

  constructor() { }

  isLogin = new BehaviorSubject<boolean>(this.checkToken());

  private checkToken() : boolean {
    return !! localStorage.getItem('token_admin');
  }

  login(token:string) : void {
    localStorage.setItem('token_admin', token);
    this.isLogin.next(true);
  }

  isLoggedIn() : Observable<boolean> {
    return this.isLogin.asObservable();
  }

  logout() : void {
    localStorage.removeItem('token_admin');
    this.isLogin.next(false);
  }
}
