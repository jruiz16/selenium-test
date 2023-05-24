# Establecer la imagen base
FROM node:14

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar el archivo package.json y package-lock.json al directorio de trabajo
COPY package*.json ./

# Instalar las dependencias del proyecto
RUN npm install

# Copiar el resto de los archivos del proyecto al directorio de trabajo
COPY . .

# Exponer el puerto que necesites para acceder a tu aplicación (si es necesario)
# EXPOSE 3000

# Comando para ejecutar las pruebas en Selenium
CMD ["npm", "test"]
