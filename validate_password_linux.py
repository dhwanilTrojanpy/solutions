import subprocess
import getpass
FAIL = 'Password: \r\nsu: Authentication failure'

def validate_pass(passwd):
    ret = 0
    try:
        cmd = '{ sleep 1; echo "%s"; } | script -q -c "su -l root -c ls /root" /dev/null' % passwd
        ret = subprocess.check_output(cmd, shell=True)
        return ret
    except:
        return 1



passwd = getpass.getpass(prompt='Password: ', stream=None)
res = validate_pass(passwd).strip()
if FAIL == res:
    print(res)
    print ("Invalid paasword")
else:
    print(res)
    print ("Valid paasword")
