# Vertical privilege escalation

If a user can gain access to functionality that they are not permitted to access
then this is vertical privilege escalation.

## Unprotected functionality

Sensitive website functionality is exposed
```
https://insecure-website.com/admin
```

Administrative URLs might be exposed in `robots.txt`
```
https://insecure-website.com/robots.txt
```

## Parameter-based access control methods

Some applications determine the user's access rights or role at login, and then
store this information in a user-controllable location:

- A hidden field
- A cookie
- A preset query string parameter

The application makes access control decisions based on the submitted value
```
https://insecure-website.com/login/home.jsp?admin=true
https://insecure-website.com/login/home.jsp?role=1
```

This approach is insecure because a user can modify the value and access
functionality they're not authorized to
