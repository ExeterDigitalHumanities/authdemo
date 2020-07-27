[![Gitpod Ready-to-Code](https://img.shields.io/badge/Gitpod-Ready--to--Code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/ExeterDigitalHumanities/authdemo) 

# authdemo
Demo of Django 2 authentication

### Notes:

* python-ldap requires a binary (wheel) package to avoid needing a c++ compile
  * https://www.lfd.uci.edu/~gohlke/pythonlibs/
* place the wheel file (.whl, for your OS and python version) into a 'wheels' folder in directory containing this project, to allow sharing of wheels across projects.

### Current plans:
* move main functions to member app (modularise)
* implement password reset properly [DONE]
  * implement warning that LDAP users cannot change password
  * check whether password reset works with server infrastructure
* examine page restrictions
* look and feel [DONE]
* openauth?
* LDAP authentication [DONE]
* Convert to Django 3.x.x


