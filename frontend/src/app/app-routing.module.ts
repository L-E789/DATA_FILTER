import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import {IndexComponent} from './index/index.component'
import {RegisterComponent} from './register/register.component'
import {LoginComponent} from './login/login.component'
import {RecoveryComponent} from './recovery/recovery.component'
import {CodeclientComponent} from './codeclient/codeclient.component'
import {WorkEnvironmentsComponent} from './work-environments/work-environments.component'

const routes: Routes = [
  {path: '', component: IndexComponent},
  {path: 'register', component: RegisterComponent},
  {path: 'login', component: LoginComponent},
  {path: 'recovery', component: RecoveryComponent},
  {path: 'consult', component: CodeclientComponent},
  {path: 'environments', component: WorkEnvironmentsComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
