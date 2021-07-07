import { Injectable } from '@angular/core';
import { CanActivate, ActivatedRouteSnapshot, RouterStateSnapshot, UrlTree} from '@angular/router';
import { Observable } from 'rxjs';
import { AuthService } from '../service/auth.service';
import { Router } from '@angular/router';

@Injectable({
  providedIn: 'root'
})
export class LUsersGuard implements CanActivate {
  constructor( public auth : AuthService, private route: Router ) {
  }
  canActivate(
    route: ActivatedRouteSnapshot,
    state: RouterStateSnapshot): Observable<boolean | UrlTree> | Promise<boolean | UrlTree> | boolean | UrlTree {
    return new Promise((resolve, reject) => {

      this.auth.isLogin.subscribe(
        admin => {
        if (admin) {
          resolve(true);
        } else {
          this.route.navigate(['']);
          resolve(false);
        }
      });
    });
  }

}
