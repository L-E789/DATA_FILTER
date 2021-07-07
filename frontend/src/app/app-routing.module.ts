import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import {IndexComponent} from './index/index.component'
import {RegisterComponent} from './register/register.component'
import {LoginComponent} from './login/login.component'
import {RecoveryComponent} from './recovery/recovery.component'
import {CodeclientComponent} from './codeclient/codeclient.component'
import {WorkEnvironmentsComponent} from './work-environments/work-environments.component'
import {ActivatedEmailComponent} from './activated-email/activated-email.component'
import {RecoverPasswordComponent} from './recover-password/recover-password.component'
import { ProfileComponent }  from './profile/profile.component'
import {AddUsersEnvironmentComponent} from './add-users-environment/add-users-environment.component'
import {AboutUsComponent} from './about-us/about-us.component'
import {EnvironmentsComponent} from './environments/environments.component'
import {JoinEnvironmentComponent} from './join-environment/join-environment.component'
import {EnvironmentReportComponent} from './environment-report/environment-report.component';
import { ContactUsComponent } from './contact-us/contact-us.component';
import { LoginAdminComponent } from './login-admin/login-admin.component';
import { PanelAdminComponent } from './panel-admin/panel-admin.component';


import { LUsersGuard } from './guards/l-users.guard';
import { LAdminGuard } from './guards/l-admin.guard';

const routes: Routes = [
  {path: '', component: IndexComponent},
  {path: 'register', component: RegisterComponent},
  {path: 'login', component: LoginComponent},
  {path: 'activated-account/:id', component: ActivatedEmailComponent},
  {path: 'recovery/:id', component: RecoverPasswordComponent},
  {path: 'recovery', component: RecoveryComponent},
  {path: 'consult', component: CodeclientComponent},
  {path: 'environments', component: WorkEnvironmentsComponent, canActivate:[LUsersGuard]},
  {path: 'profile', component: ProfileComponent, canActivate:[LUsersGuard]},
  {path: 'environments/users/:id', component: AddUsersEnvironmentComponent, canActivate:[LUsersGuard]},
  {path: 'about-us', component: AboutUsComponent},
  {path: 'environment/:id', component: EnvironmentsComponent, canActivate:[LUsersGuard]},
  {path: 'environment/join/:code',component:JoinEnvironmentComponent, canActivate:[LUsersGuard]},
  {path: 'environments/report/:id',component:EnvironmentReportComponent, canActivate:[LUsersGuard]},
  {path: 'contact_us',component: ContactUsComponent},
  {path: '3RjZgfU&rZVRLC7fzTNf1IRgxRFPvQ5G1ekFXJZ9/Sd89AsYwD912',component: LoginAdminComponent},
  {path: '3RjZgfU&rZVRLC7fzTNf1IRgxRFPvQ5G1ekFXJZ9/Sd89AsYwD912/4dm1n',component: PanelAdminComponent, canActivate:[LAdminGuard]}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
