delete from pintpointapi_tab
WHERE id > 1

update auth_user
set is_staff = true
where username = 'rolotony'