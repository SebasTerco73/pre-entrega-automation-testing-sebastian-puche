@login
Feature: Inicio de sesión

    Background:
        Given Estoy en la pagina de Login

    @smoke
    Scenario: Login exitoso
        When Ingreso el usuario "standard_user"
        And Ingreso la contraseña "secret_sauce"
        And Presiono el boton de Login
        Then Debo visualizar la pagina de productos

    @regression
    Scenario: Login con usuario incorrecto
        When Ingreso el usuario "usuario_incorrecto"
        And Ingreso la contraseña "secret_sauce"
        And Presiono el boton de Login
        Then Debo visualizar un mensaje de error
         
    Scenario: Multiples logins incorrectos
        When Ingreso el usuario "<usuario>"
        And Ingreso la contraseña "<password>"
        And Presiono el boton de Login
        Then Debo visualizar un mensaje de error

        Example:
            | usuario            | password         |
            | usuario_incorrecto | secret_sauce     |
            | standard_user      | clave_incorrecta |
            | usuario_prueba     | clave_prueba     |

    Scenario: Login en un paso 
        When Ingreso las siguientes credenciales
            | usuario       | password     |
            | standard_user | secret_sauce |
        Then Debo visualizar la pagina de productos

