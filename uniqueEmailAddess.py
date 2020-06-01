from collections import defaultdict

emails= ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
uniqueEmails = defaultdict()
for email in emails:
    userID,a,domain = email.partition('@')
    if '+' in userID:
        userID = userID[:userID.index('+')]
    userID = userID.replace('.', '')
    print userID
    uniqueEmail = userID +'@' + domain
    uniqueEmails[uniqueEmail] = 1
print uniqueEmails
    
