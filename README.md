# authdemo
Demo of Django 2 authentication

### Notes:

* python-ldap requires a binary (wheel) package to avoid needing a c++ compile
  * https://www.lfd.uci.edu/~gohlke/pythonlibs/

### Current plans:
* move main functions to member app (modularise)
* implement password reset properly [DONE]
  * implement warning that LDAP users cannot change password
  * check whether password reset works with server infrastructure
* examine page restrictions
* look and feel [DONE]
* openauth?
* LDAP authentication [DONE]

