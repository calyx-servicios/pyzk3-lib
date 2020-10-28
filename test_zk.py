from zk3 import ZK, const
zk = ZK('192.168.8.8', port=4370, timeout=20)
conn = zk.connect()
attendances = conn.get_attendance()
attendances = conn.get_attendance()
attendances.sort(key=lambda x: x.timestamp)
for att in attendances:
    print (att)
    print (att.timestamp)
users = zk.get_users()
for user in users:
    privilege = 'User'
    if user.privilege == const.USER_ADMIN:
        privilege = 'Admin'

    print ('- UID #{}'.format(user.uid))
    print ('  Name       : {}'.format(user.name))
    print ('  Privilege  : {}'.format(privilege))
    print ('  Password   : {}'.format(user.password))
    print ('  Group ID   : {}'.format(user.group_id))
    print ('  User  ID   : {}'.format(user.user_id), type(user.user_id))
print ('Enabling device ...')
ret = conn.enable_device()
print (ret)
