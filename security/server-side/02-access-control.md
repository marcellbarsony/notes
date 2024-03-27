# Access Control

**Access control** determines whether the user is allowed to carry out the action that they are attempting to perform.

- **Authentication** confirms that the user is who they say they are.
- **Session management** identifies which subsequent HTTP requests are being made by that same user.

## Vertical privilege escalation

If a user can gain access to functionality that they are not permitted to access then this is vertical privilege escalation.

### Unprotected functionality

Sensitive website functionality is exposed
```
https://insecure-website.com/admin
```

Administrative URLs might be exposed in `robots.txt`
```
https://insecure-website.com/robots.txt
```

### Parameter-based access control methods

Some applications determine the user's access rights or role at login, and then store this information in a user-controllable location:

- A hidden field
- A cookie
- A preset query string parameter

The application makes access control decisions based on the submitted value
```
https://insecure-website.com/login/home.jsp?admin=true
https://insecure-website.com/login/home.jsp?role=1
```

This approach is insecure because a user can modify the value and access functionality they're not authorized to

## Horizontal privilege escalation

Horizontal privilege escalation occurs if a user is able to gain access to resources belonging to another user

Insecure direct object reference (IDOR) vulnerability
```
https://insecure-website.com/myaccount?id=123
```
