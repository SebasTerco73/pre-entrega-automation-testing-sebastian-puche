from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class LoginPage:
    # 1. IDENTIDAD DE LA PÁGINA
    # URL absoluta de la página de login; si cambia, solo toca este valor.
    URL = "https://www.saucedemo.com/"

    # 2. LOCATORS (privados y centralizados)
    # Define aquí todos los selectores; si el front cambia,
    # solo modificas estas tres tuplas.
    _USER_INPUT = (By.ID, "user-name")
    _PASS_INPUT = (By.ID, "password")
    _LOGIN_BUTTON = (By.ID, "login-button")
    _ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    def __init__(self, driver):
        """
        3. INYECCIÓN DE DEPENDENCIAS
        Recibe la instancia de WebDriver (Chrome, Firefox…)
        desde tu fixture en conftest.py.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # 4. MÉTODOS DE NAVEGACIÓN Y ACCIÓN
    def abrir(self):
        """Carga la URL de login en el navegador."""
        self.driver.get(self.URL)
        return self
    
    def _completar_usuario(self, usuario: str):
        """Escribe el nombre de usuario."""
        campo = self.wait.until(EC.visibility_of_element_located(self._USER_INPUT))
        campo.clear() # Limpia antes de escribir
        campo.send_keys(usuario)
        return self
    
    def _completar_clave(self, clave: str):
        """Escribe la contraseña."""
        campo = self.wait.until(EC.visibility_of_element_located(self._PASS_INPUT))
        campo.clear()
        campo.send_keys(clave)
        return self
    
    def _hacer_clic_login(self):
        """Hace clic en el botón Login."""
        self.wait.until(EC.element_to_be_clickable(self._LOGIN_BUTTON)).click()
        return self
    
    def login_completo(self, usuario, clave):
        """Método de conveniencia para hacer login completo."""
        self._completar_usuario(usuario)
        self._completar_clave(clave)
        self._hacer_clic_login()
        return self
    
    # 5. MÉTODOS DE VERIFICACIÓN (opcionales)
    def _esta_error_visible(self) -> bool:
        """
        Comprueba si aparece un mensaje de error en la página
        tras un intento de login fallido.
        """
        try:
            self.wait.until(EC.visibility_of_element_located(self._ERROR_MESSAGE))
            return True
        except TimeoutException:
            return False
        
    def obtener_mensaje_error(self) -> str:
        """Obtiene el texto del mensaje de error."""
        if self._esta_error_visible():
            return self.wait.until(EC.visibility_of_element_located(self._ERROR_MESSAGE)).text
        return ""