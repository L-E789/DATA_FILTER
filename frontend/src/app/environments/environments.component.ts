import { Component, OnInit } from '@angular/core';
import { ActivatedRoute , ParamMap } from '@angular/router';
import {environment} from '../../environments/environment';
import { ClientService} from '../service/client.service';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import {AuthService} from '../service/auth.service';
import { Router } from '@angular/router';

import { ToastrService } from 'ngx-toastr';

@Component({
  selector: 'app-environments',
  templateUrl: './environments.component.html',
  styleUrls: ['./environments.component.css']
})
export class EnvironmentsComponent implements OnInit {


  id_environment;
  btnregisterdevice : boolean = false;
  btnregisterclient : boolean = false;
  mydashboard : boolean = false;
  btnpending : boolean = false;
  btnprogress : boolean = false;
  btnfinished : boolean = false;

  date_environment;

  constructor(
    private fb: FormBuilder,
    private routes : ActivatedRoute,
    private client: ClientService,
    private auth: AuthService,
    private route: Router,
    private toastr: ToastrService
  ) { }


  mydashboardv(){
    this.btnfinished = false;
    this.btnpending = false;
    this.mydashboard = false;
    this.btnregisterclient = false;
    this.btnregisterdevice = false;
    this.mydashboard = true;
  }

  registerdevice(){
    this.btnfinished = false;
    this.btnprogress = false;
    this.btnpending = false;
    this.mydashboard = false;
    this.btnregisterclient = false;
    this.btnregisterdevice = true;
  }

  registerclient(){
    this.btnfinished = false;
    this.btnprogress = false;
    this.btnpending = false;
    this.mydashboard = false;
    this.btnregisterdevice = false;
    this.btnregisterclient = true;
  }

  pendingDevices(){
    this.btnfinished = false;
    this.btnprogress = false;
    this.mydashboard = false;
    this.btnregisterdevice = false;
    this.btnregisterclient = false;
    this.btnpending = true
  }

  progressDevices(){
    this.btnfinished = false;
    this.mydashboard = false;
    this.btnpending = false;
    this.btnregisterdevice = false;
    this.btnregisterclient = false;
    this.btnprogress = true;
  }

  finishedDivices(){
    this.btnprogress = false;
    this.mydashboard = false;
    this.btnpending = false;
    this.btnregisterdevice = false;
    this.btnregisterclient = false;
    this.btnfinished = true;
  }
  
  

  ngOnInit(): void {
    this.routes.paramMap
    .subscribe((params : ParamMap) => {
    let id = + params.get('id');
    this.id_environment = id;
    });

    if(localStorage.getItem("token")){
      this.client.getRequest(`${environment.BASE_API_REGISTER}/authorization`,localStorage.getItem('token')).subscribe(
        (response: any) => {
          this.client.getRequestId(`${environment.BASE_API_REGISTER}/environment/main/` + this.id_environment).subscribe(
            (Response : any) => {
              this.date_environment = Response;
              this.mydashboardv();
              localStorage.setItem('environment',this.id_environment);
            },(error) => {
              console.log(error);
            }
          )
          console.log(response);
        },(error) => {
          console.log(error);
          this.auth.logout();
          this.route.navigate(['/login'])
        });
    }else{
      this.route.navigate(['/login']);
    }

  }
}
