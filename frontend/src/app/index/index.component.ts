import { Component, OnInit, AfterViewInit } from '@angular/core';
import {AuthService} from '../service/auth.service';
import {environment} from '../../environments/environment';
import { ClientService} from '../service/client.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-index',
  host: {
    'autoplay': '',
    'oncanplay': 'this.play()',
    'onloadedmetadata': 'this.muted = true'
  },
  templateUrl: './index.component.html',
  styleUrls: ['./index.component.css']
})
export class IndexComponent implements OnInit {

  constructor(
    private client: ClientService,
    private auth: AuthService,
    private route: Router
  ) {}

  ngOnInit(): void {
    this.client.getRequest(`${environment.BASE_API_REGISTER}/authorization`,localStorage.getItem('token')).subscribe(
      (response: any) => {
        if(response.status == 403){
          this.auth.logout()
        this.route.navigate(['/']);
        }else{
          this.route.navigate(['/environments']);
        }
      },(error) => {
        this.auth.logout()
        this.route.navigate(['/']);
      });
  }

  ngAfterViewInit(){
    let myVideo = document.getElementById('homeVideo') as HTMLFormElement;
    myVideo.muted = false;
    myVideo.loop = true;

    if (myVideo){
      setTimeout(() => {
        myVideo.play();
      }, 1000);
    }
  }
}
