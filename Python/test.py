from selenium import webdriver

# Inicializa el controlador del navegador
options = webdriver.ChromeOptions()
# options.binary_location = '/ruta/al/binario/de/chrome'
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options=options)

# Realiza la prueba
driver.get('https://www.example.com')
print(driver.title)

# Cierra el navegador
driver.quit()
