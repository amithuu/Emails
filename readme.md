
#### We Have Learnt about Sending Email in all the Email Format, 

#### Now We Learn Celery, Using which we can send emails and  Schedule as well using the Celery_Beat Libraries, 

* We need to install celery and redis and celery_beat libraries..

* Once we are done with that adding a refresh token to the User, when he registers..
  
* we need to make some changes after installing, we need to install pip install pyjwt==v1.7.1 -? [This_one_we_get_error_as_'str'_object_cannot_decode] 
* [so we need to degrade the version]

* We need to make rest_framework_simplejwt/token_blacklist/admin.py and setting 
* def has_delete_permission(self, *args, **kwargs): 
    * return False to True 
* -> [this_one_is_for_deleting_users_from_admin_table..]



### Today i have learnt about signals, how it works, when we needed any other api's related to a Model, we can use Signals.., 
* so when that model gets created we can using that data, we can created more api..
[ex:when_User_is_created]  ----------> [we_can_create_his_profile_using_{User}_model]  ----------> [Creating_Profile_Model]


