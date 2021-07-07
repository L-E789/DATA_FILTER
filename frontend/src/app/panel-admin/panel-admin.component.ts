import { AuthadminService } from './../service/authadmin.service';
import { Router } from '@angular/router';
import { Component, OnInit } from '@angular/core';
import { environment } from './../../environments/environment';
import { ClientService} from '../service/client.service';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';

import { ToastrService } from 'ngx-toastr';
import Swal from 'sweetalert2';

@Component({
  selector: 'app-panel-admin',
  templateUrl: './panel-admin.component.html',
  styleUrls: ['./panel-admin.component.css']
})
export class PanelAdminComponent implements OnInit {

  messages : any;
  infoMessagesId : any;
  DataEnvironment : any;
  DataUsers : any;
  option: boolean;
  form : FormGroup;

  btnMessage : boolean = false;
  btnEnvironment : boolean = false;
  btnUsers : boolean = false;

  constructor(
    private client: ClientService,
    private fb : FormBuilder,
    private route: Router,
    public auth : AuthadminService,
    private toastr: ToastrService
  ) { }

  showMessage(){
    this.btnEnvironment = false;
    this.btnUsers = false;
    this.btnMessage = true;
  }

  showEnvironments(){
    this.btnUsers = false;
    this.btnMessage = false;
    this.bringDataEnvironments();
  }

  showUsers(){
    this.btnMessage = false;
    this.btnEnvironment = false;
    this.bringDateUsers()
  }


  deleteUser(id : number){
    let data = ({
      id : id
    })
    this.client.postRequest(`${environment.BASE_API_REGISTER}/32sl4vzvre`, data).subscribe(
      (Resp : any) => {
        this.toastr.success("Usuario borrado");
        this.bringDateUsers();
      },(error) => {
        console.log(error);
      }
    )
  }

  bringDateUsers(){
    this.client.getRequest(`${environment.BASE_API_REGISTER}/32sl4vzvre`).subscribe(
      (Resp : any) => {
        this.DataUsers = Resp;
        this.btnUsers = true;
      },(error) => {
        console.log(error);
      }
    )
  }

  bringDataEnvironments(){
    this.client.getRequest(`${environment.BASE_API_REGISTER}/ejd9ev5adf`).subscribe(
      (Resp : any) => {
        this.btnEnvironment = true;
        this.DataEnvironment = Resp;
      },(error) => {
        console.log(error);
      }
    )
  }

  bringDataEnvId(id : number){
   let data = ({
     id : id
   });
   this.client.postRequest(`${environment.BASE_API_REGISTER}/ejd9ev5adf`,data).subscribe(
     (Resp : any) => {
        Swal.fire(`Numero de clientes: ${Resp[0].clients}, Numero de colaboradores: ${Resp[0].users} `);
     },(error) => {
       console.log(error);
     }
   )
  }

  showMessages(status : number){
    let data = ({
      status : status
    })
    this.client.postRequest(`${environment.BASE_API_REGISTER}/tMN8OoA3kq`, data).subscribe(
      (Resp : any) => {
        this.messages = Resp;
      },(error) => {
        console.error(error);
      }
    )
  }

  InfoMessage(id: number){
    let data = ({
      id: id
    })
    this.client.postRequest(`${environment.BASE_API_REGISTER}/IxYasOUTXH`, data).subscribe(
      (Resp : any) => {
        this.infoMessagesId = Resp;
        this.option = this.infoMessagesId[0].viewed;
      },(error) => {
        console.error(error);
      }
    )
  }


  answerMessage(id: number, email: string){
    if(this.form.valid){
      let data = ({
        answer : this.form.value.answer,
        email : email,
        id : id
      });
      this.client.postRequest(`${environment.BASE_API_REGISTER}/VD0uJM3lvi`, data).subscribe(
        (Resp) => {
          this.form.reset();
          this.toastr.success('Se respondió correctamente');
          this.showMessages(0);
        },(error) => {
          this.toastr.success('Error al enviar');
        }
      )
    }
  }

  ngOnInit(): void {
    if(localStorage.getItem('token_admin')){
      this.form = this.fb.group({
        answer: ['', Validators.required]
      });
      this.client.getRequest(`${environment.BASE_API_REGISTER}/authorization`,localStorage.getItem('token_admin')).subscribe(
        (response: any) => {
          if(response.status == 403){
            this.auth.logout();
            this.route.navigate(['/3RjZgfU&rZVRLC7fzTNf1IRgxRFPvQ5G1ekFXJZ9/Sd89AsYwD912']);
          }else{
            this.showMessages(0);
            this.showMessage();
          }
        },(error) => {
          this.auth.logout();
          this.route.navigate(['/3RjZgfU&rZVRLC7fzTNf1IRgxRFPvQ5G1ekFXJZ9/Sd89AsYwD912'])
        });
    }else{
      this.route.navigate(['/3RjZgfU&rZVRLC7fzTNf1IRgxRFPvQ5G1ekFXJZ9/Sd89AsYwD912']);
    }
  }

}
