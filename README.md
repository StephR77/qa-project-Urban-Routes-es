# Proyecto Urban Grocers 
**Yury Stefany Rodriguez R, grupo 29, sprint 8**

# ## PROYECTO URBAN ROUTES

#### El archivo README debe incluir el nombre del proyecto, una descripción del proyecto, una descripción de las tecnologías y técnicas utilizadas, e instrucciones sobre cómo ejecutar las pruebas.
#### Recuerda que para ejecutar con PyTest, se utiliza el comando pytest folder/del/proyecto en la terminal.

Primero se debe configurar el proyecto lo cual debemos ir a nuestra terminal, crear un directorio si no se ha hecho, de lo contrario, clonar el repositorio que se llama Urban Routes, de esta manera ya se podra abrir Pycharm y empezar a trabajar alli con el proyecto.

Primero debemos abrir un archivo llamado helpers.py en donde vamos a alojar la información de cómo capturar el número de código de teléfono, cuando se llena el campo de teléfono y este envía un codigo SMS.

Luego en un archivo data.py se ingresará la información de la URL, la información de los campos 'desde' y 'hasta', número de teléfono, número y código de la tarjeta de crédito y un mensaje para el conductor.

Enseguida, el archivo method.py incluiremos los localizadores y los métodos que se ejecutarán en la siguiente página llamada main.py, en esta página empezarán a desarrollar todas las pruebas de forma automatizada.

Para ejecutar las pruebas en la página donde se escribirán los métodos se importarán los archivos: By, Expected Conditions y WebDriverWait; después de esto, debemos crear una función de clase llamada UrbanRoutesPage, que más adelante será utilizada en las pruebas, bajo esta función empezaremos a escribir todos los localizadores que necesitamos para que las pruebas las ejecuten. Enseguida, colocamos el constructor, para luego empezar a desarrollar los métodos que queremos que se desarrollen en las pruebas, por ejemplo, para el punto número 1 de nuestro proyecto se necesitaba llenar los campos 'desde' y 'hasta', luego hacer click en el boton para solicitar un taxi; para esto se crean funciones con nombres muy similares como: set_from_field, set_to_field y click_in_botton_taxi, hacemos la comprobación de estos campos con la palabra get en la función, y como estos tres pasos se deben repetir continuamente para cada selección de la aplicación se creará un "paso" que significa que esta función alojará estos tres procedimientos sin necesidad de escribir lo mismo las veces que hagan falta, -lo que significa que es en la mayoría de veces-.

Después de esto, empezamos a desarrollar los métodos punto por punto. En cada uno de estos métodos se recomienda colocar un WebDriverWeb para que las funciones tengan el tiempo para ejecutarse, de la misma manera, se coloca un return para asegurarnos que el campo al que vamos a desarrollar una automatización este acuerde al parametro el cual se le esta exigiendo, por ejemplo, si el botón al que se tiene que hace clic esta habilitado. 
De igual manera, se deben colocar los localizadores dentro de estas funciones que son la parte más importante al momento de hacer la automatización, puesto que, como su nombre lo indica localizan el lugar y la actividad a realizar.

En el siguiente archivo que es main.py se importa webdriver, UrbanRoutesPage que es el método que se colocó en el archivo anterior, data y el archivo helpers con la importación de la función retrieve_phone_code, la cual su función en darnos el código de SMS que se le transmite al cliente en el momento de llenar el campo de número de teléfono.




Primero se tiene que abrir una archivo llamado configuration.py para alojar las URL del servidor, la dirección API para crear un usuario y la dirección API para crear un kit.

Luego en otro archivo llamado data.py vamos a alojar los parámetros requeridos para la creación de un usario que los requerimientos son: un encabezado en "content-Type" y un diccionario con los datos del usuario, por lo que los datos mínimos son: firstname, phone, address. Además de esto, se necesitan los requerimientos para crear un kit que son: "obligatorio pasar el encabezado Authorisation O el parámetro cardId, para crear la kit".

En seguida, debemos abrir un archivo llamado sender_stand_request.py para importar los datos del archivo configuration, data y requests de python para luego asi poder correr los tests.

En este archivo se empiezan a diseñar las funciones para crear un usuario y dentro de este crear un kit, de la misma manera se crea la copia de un diccionario para realizar las pruebas negativas y positivas de la aplicación de Urban Grocers.

Para crear un usuario se necesita traer la información desde el archivo configuration.py con la URL del servidor y el end point de API para crearlo, de esta manera como el requerimiento es que el usuario contenga un content-type y un encabezado, alli lo mencionamos con las variables json y headers para que no nos de un error.

Luego para crear un kit diseñamos una función con el nombre de post_create_new_kit y dentro de esta llamamos a la función de crear un usuario con la variable 'response', para que podamos conseguir el autotoken, a continuación para la creación de un kit se necesita un content-type y un authoken que el usario no los da al ser una respuesta positiva, de esta manera comprobamos la creacion del kit. Luego le decimos a la función de post_create_new_kit que retorne esta información desde la pagina configuración URL y la API kits_path.

Para poder empezar a realizar los tests de comprobación, se creó una función a parte para poder modificar el kit con los diferentes parámetros propuestos por la aplicación llamada modify_body la cual, se inserta tambien en la función post_create_new_kit llamandola con la variable new_body y json para las pruebas positivas y negativas de nuestro kit.  

Luego de tener casi todo listo, en el archivo create_kit_name_kit_test.py definimos las funciones de positive_assert y negative_assert en donde empezaremos a realizar los tests de las comprobaciones. Para estas dos funciones le decimos que retome la información del kit que se quiere modificar desde sender_stand_request.post_create_new_kit y le decimos que el assert sea un codigo 201 si es positivo o 400 si es negativo. Para que nuestro archivo de comprobación de pruebas no tuviera datos codificados se realizó en data.py la descripción de cada diccionario acorde a los parámetros de las pruebas.

Al correr las pruebas, se tienen aún fallos en el programa con respecto al test 3 (kit con número de caracteres menor a uno), test 4 (kit con 512 caracteres), test 8 (kit con no caracteres) y test 9 (kit con números) pues nos da un resultado 201 y este debería reflejar un error 400.

Este archivo junto con los demás (configuration.py, data.py, sender_stand_request.py, create_kit_name_kit_test.py, README.md, y .gitignore) estarán guardados en git.hub por medio de la clonación en el terminal de Cmder.

Para ejecutar todo lo anterior, debemos iniciar abriendo nuestro Git Hub, allí en settings vamos a encontrar en la parte izquierda un botón de radio llamado 'SSH and GPG keys'; en este te pedirán el SSH que es la llave pública que ya creaste en el programa de Cmder guardada en el archivo de id_rsa.pub, luego le colocas el nombre que prefieras en la parte que dice 'Title', ya teniendo esto, empiezas a crear tu repositorio.

Para crear el repositorio debe ir a la parte superior izquierda de la página en el logo en forma de gato allí les dice crear 'new', este le mostrará el 'owner'que es el nombre del usuario creador y al lado, separado con un '/', hay un espacio para llenar llamado 'Repositorio name', en este le colocamos qa-project-Urban-Grocers-app-es; cuando le hayas colocado el nombre, este te dirá si esta disponible el nombre. Luego le puedes agregar una descripción, lo puedes dejar público si deseas que otra persona trabaje en este mismo archivo con una URL y a la vez puedes agregar el archivo README.

Luego para clonar, iremos a la terminal, en la terminal debemos colocar la dirección de donde se encuentra nuestro archivo del proyecto, luego este abrirá la carpeta con los repositorios local y remoto que en este caso son main y origin para trabajar en este proyecto. A continuación añadiremos los documentos trabajados en este proyecto con el comando git add . , luego, le daremos git status para verificar el estado y este nos mostrará que los archivos trabajados ya están guardados, en seguida le daremos git commit para confirmar los archivos y finalmente git push para guardar los cambios que se han hecho en el repositorio.

Después de realizar los pasos anteriores, podemos dirigirnos a PyCharm que es la herramienta que vamos a utilizar para automatizar las pruebas de Urban Grocers, allí le damos a la parte superior izquierda, en las tres lineas, 'file' y elegimos abrir la carpeta del proyecto, después debemos seleccionar 'Pure Python' y le diremos que el entorno que queremos utilizar se llamará Virtualenv.

Para empezar a trabajar en PyCharm debemos crear los archivos de configuration.py, data.py, sender_stand_request.py, create_kit_name_kit_test.py que son los que se van a utilizar en la autimatización de pruebas, debemos hacer clic derecho en el nombre del proyecto, luego 'nuevo', le indicamos 'python file' y le escribimos el nombre del documento siempre terminando en py, para que podamos utilizar las herramientas de Python.

Para instalar pytest - que se utiliza para ejecutar los tests de prueba - debemos ir a la parte inferior izquierda y seleccionar 'python packages' buscamos pytest lo descargamos al igual que requests ' que nos sirve para el entorno virtual de pruebas HTTP y API - de igual manera, para empezar a realizar las comprobaciones y que el programa anterior se pueda ejecutar, las pruebas deben llevar como nombre test para que python las pueda ejecutar. 

En el momento de realizar las pruebas y teniendo todo listo para ser usado, en el archivo configuration.py colocaremos las direcciones URL y API; data.py serán para los datos que se utilizaremos en las funciones; sender_stand_request.py importaremos la página de configuration.py, requets que es la librería y data.py en esta página ejecutaremos nuestras primeras funciones para crear un usuario y dentro de este un nuevo kit, aqui mismo se creo la función de un nuevo diccionario de crear un kit con la idea de ser más simplificado y claro la ejecución de las pruebas.

En el último archivo create_kit_name_kit_test.py se encontrarán las funciones de comprobación positivas y negativas y la comprobación de pruebas.

Para ejecutar las pruebas hay dos posibilidades; en la parte superior derecha se encuentra un símbolo triangular de color verde y en la parte inferior izquierda en la terminal se encuentra el mismo botón con el símbolo triangular pero gris. Allí en la terminal te mostrará los tests fallidos y los test que han pasado, y si tienen errores la terminal te mostrará dónde se encuentra el error en color rojo.

Finalmente, para llevar a cabo este proyecto se utilizaron las siguientes herramientas:
1. Python 3.13: Este es el lenguaje de programación para escribir las pruebas.
2. PyTest: Es el framework de Python para ejecutar las pruebas que llevan como nombre test.
3. Requests: Es la libreria de Python para enviar las solicitudes HTTP de la aplicación de Urban Grocers.
4. Git: Es el que gestiona los cambios en el proyecto.
5. GitHub: Es la plataforma remota donde se almacena el repositorio del proyecto.
6. PyCharm: Es el entorno para editar y ejecutar el proyecto.

