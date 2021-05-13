from Controllers.UsersController import Register,Login, ValidateAccount, SentRecoverPassword, RecoverPasssword, ModificationPassword, profileedis, ChangePassword, ModifyImg, ModifyName

from Controllers.work_environment import CreateEnvironment, ShowEnvironment, RemoveEnvironment, SearchEnvironment, ManageUsers, ManageUsersRemove, JoinByCode, SearchManage, SendMailCollaborators, ChangeStatus

from Controllers.DispositivosController import add_dis

from Controllers.authenticationController import AuthorizationControllers


users = {
    "create_user":"/api/v01/register","create_user_controllers": Register.as_view("create_api"),
    "Login_user":"/api/v01/login","login_user_controllers": Login.as_view("login_api"),
    "validate_account_user":"/api/v01/activated/<id>","validate_account": ValidateAccount.as_view("validate_api"),
    "recover_email_user":"/api/v01/recover","recover_email": SentRecoverPassword.as_view("recover_email_api"),
    "recover_password_user":"/api/v01/recover/pass/<id>","recover_password": RecoverPasssword.as_view("Recover_pass_api"),
    "modification_password_user":"/api/v01/recover/modification","modification_password": ModificationPassword.as_view("modification_pass_api"),
    "authorization_user":"/api/v01/authorization","authorization_user_controller": AuthorizationControllers.as_view("authorization_api"),
    "editProfile_user":"/api/v01/editprofile/<id>","editprofile_user_controller": profileedis.as_view("editprofile_api"),
    "profile_img":"/api/v01/edit_img","profile_img_controller": ModifyImg.as_view("Modify_img_api"),
    "profile_name":"/api/v01/edit_name","profile_name_controller": ModifyName.as_view("Modify_name_api"),
    "profile_change_password":"/api/v01/change_password","profile_change_password_controller": ChangePassword.as_view("profile_password_api"),
}

environment = {
    "create_environment":"/api/v01/environment/create","create_environment_controller": CreateEnvironment.as_view("create_environment_api"),
    "show_environment":"/api/v01/environment/show","show_environment_controller": ShowEnvironment.as_view("show_environment_api"),
    "remove_environment":"/api/v01/environment/remove","remove_environment_controller": RemoveEnvironment.as_view("remove_environment_api"),
    "search_environment":"/api/v01/environment/search","search_environment_controller": SearchEnvironment.as_view("search_environment_api"),
    "manage_users_environment":"/api/v01/environment/manage/<id>","manage_users_controller": ManageUsers.as_view("manage_users_api"),
    "manage_users_remove_environment":"/api/v01/environment/manage/remove","manage_users_remove_controller": ManageUsersRemove.as_view("manage_users_remove_api"),
    "manage_join_by_code_environment":"/api/v01/environment/code","manage_join_by_code_controller": JoinByCode.as_view("manage_join_by_code_api"),
    "manage_search_environment":"/api/v01/environment/manage/search","manage_search_controller": SearchManage.as_view("manage_search_api"),
    "manage_send_email_environment":"/api/v01/environment/manage/send","manage_send_email_controller": SendMailCollaborators.as_view("manage_send_email_api"),
    "manage_change_status_environment":"/api/v01/environment/manage/status","manage_change_status_controller": ChangeStatus.as_view("manage_change_status_api"),
}



device = {
    "device_add":"/api/v01/create","device_add_controllers": add_dis.as_view("device_api")
}
