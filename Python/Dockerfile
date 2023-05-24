FROM python:3.8

# Instala las dependencias necesarias
RUN pip install selenium



# Descarga el controlador del navegador Chrome
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    libglib2.0-0 \
    libnss3 \
    libgconf-2-4 \
    libfontconfig1 \
    chromium

# Descarga el controlador de ChromeDriver y lo agrega al PATH
RUN wget -O /tmp/chromedriver.zip https://chromedriver.storage.googleapis.com/$(wget -qO- https://chromedriver.storage.googleapis.com/LATEST_RELEASE_$(chromium --version | awk '{print $2}' | awk -F "." '{print $1}'))/chromedriver_linux64.zip \
    && unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/

# Establece la variable de entorno para el navegador Chrome
ENV CHROME_BIN=/usr/bin/chromium

# Copia el código fuente de la aplicación al contenedor
COPY . /app
WORKDIR /app

# Ejecuta la prueba
# CMD ["python", "test.py"]
CMD ["bash"]

