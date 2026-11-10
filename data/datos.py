USUARIO_VALIDO = "standard_user"
PASSWORD_VALIDO = "secret_sauce"

login_parametrized = [
    (USUARIO_VALIDO, PASSWORD_VALIDO, "Login exitoso"),
    ("usuario_invalido", PASSWORD_VALIDO, "Epic sadface: Username and password do not match any user in this service"),
    (USUARIO_VALIDO, "password_invalido", "Epic sadface: Username and password do not match any user in this service"),
    ("usuario_invalido", "password_invalido", "Epic sadface: Username and password do not match any user in this service"),
    ("", PASSWORD_VALIDO, "Epic sadface: Username is required"),
    (USUARIO_VALIDO, "", "Epic sadface: Password is required"),
    ("", "", "Epic sadface: Username is required") 
]