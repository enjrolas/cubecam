import pexpect

child = pexpect.spawn('spark cloud login')
print "logging in"
child.expect('Could I please have an email address?')
print "sending email address"
child.sendline('alex@lookingglassfactory.com')
child.expect('and a password?')
print "sending password"
child.sendline('lookatthatglass')
