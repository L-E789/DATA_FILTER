import { Injectable } from '@angular/core';
import { CanActivate, ActivatedRouteSnapshot, RouterStateSnapshot, UrlTree } from '@angular/router';
import { Observable } from 'rxjs';
import { AuthadminService } from '../service/authadmin.service';
import { Router } from '@angular/router';

@Injectable({
  providedIn: 'root'
})
export class LAdminGuard implements CanActivate {
  constructor( public auth : AuthadminService, private route: Router ) {
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
          this.route.navigate(['3RjZgfU&rZVRLC7fzTNf1IRgxRFPvQ5G1ekFXJZ9/Sd89AsYwD912']);
          resolve(false);
        }
      });
    });
  }

}
