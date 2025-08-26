# PROYECTO URBAN ROUTES
## DESCRIPTION 📖

Primero se debe configurar el proyecto, lo cual debemos ir a nuestra terminal, crear un directorio si no se ha hecho, de lo contrario, clonar el repositorio que se llama Urban Routes, de esta manera ya se podra abrir **Pycharm** y empezar a trabajar alli con el proyecto.

Primero debemos abrir un archivo llamado `helpers.py` en donde vamos a alojar la información de cómo capturar el número de código de teléfono, cuando se llena el campo de teléfono y este envía un codigo SMS.

Luego en un archivo `data.py` se ingresará la información de la URL, la información de los campos 'desde' y 'hasta', número de teléfono, número y código de la tarjeta de crédito y un mensaje para el conductor.

Enseguida, el archivo `method.py` incluiremos los localizadores y los métodos que se ejecutarán en la siguiente página llamada `main.py`, en esta página empezarán a desarrollar todas las pruebas de forma automatizada.

Para ejecutar las pruebas en la página donde se escribirán los métodos se importarán los archivos: *By*, *Expected Conditions* y *WebDriverWait*; después de esto, debemos crear una función de clase llamada `UrbanRoutesPage`, que más adelante será utilizada en las pruebas, bajo esta función empezaremos a escribir todos los localizadores que necesitamos para que las pruebas las ejecuten. Enseguida, colocamos el constructor, para luego empezar a desarrollar los métodos que queremos que se desarrollen en las pruebas, por ejemplo, para el punto número 1 de nuestro proyecto se necesitaba llenar los campos 'desde' y 'hasta', luego hacer click en el boton para solicitar un taxi; para esto se crean funciones con nombres muy similares como: `set_from_field`, `set_to_field` y `click_in_botton_taxi`, hacemos la comprobación de estos campos con la palabra **get** en la función, y como estos tres pasos se deben repetir continuamente para cada selección de la aplicación se creará un "paso" que significa que esta función alojará estos tres procedimientos sin necesidad de escribir lo mismo las veces que hagan falta, -lo que significa que es en la mayoría de veces-.

Después de esto, empezamos a desarrollar los métodos punto por punto. En cada uno de estos métodos se recomienda colocar un *WebDriverWeb* para que las funciones tengan el tiempo para ejecutarse, de la misma manera, se coloca un return para asegurarnos que el campo al que vamos a desarrollar una automatización este acuerde al parametro el cual se le esta exigiendo, por ejemplo, si el botón al que se tiene que hace clic esta habilitado. 
De igual manera, se deben colocar los localizadores dentro de estas funciones que son la parte más importante al momento de hacer la automatización, puesto que, como su nombre lo indica localizan el lugar y la actividad a realizar.

En el siguiente archivo que es `main.py` se importa webdriver, *UrbanRoutesPage* que es el método que se colocó en el archivo anterior, `data` y el archivo `helpers` con la importación de la función *retrieve_phone_code*, la cual su función en darnos el código de *SMS* que se le transmite al cliente en el momento de llenar el campo de número de teléfono.

Empezamos a definir una clase llamada *setup_class* donde incluiremos nuestro Sistema Operativo, luego definimos una función para traer la clase UrbanRoutesPage del archivo anterior (method.py) que es la que contiene los contenedores y los métodos, después de esto ya podemos empezar a desarrollar nuestros tests.

Estos tests, son muy similares a nuestros métodos, la diferencia es que en las pruebas introducimos todos los datos que queremos que sean escritos y las acciones que estas tienen que ejecutarse durante el proceso de la automatización, para poderlas ejercutarlas, en la parte izquierda de la pantalla al lado de cada función llamada test se encontrará una flecha de color verde la cual realizará la ejecución de la prueba, en estos casos es muy remomendable ejecutar la prueba en modo 'debug' para que poco a poco se vayan evidenciando los errores y corregirlos durante la marcha.

Finalmente, debemos colocar la función *teardown_class* para que la ejecución de las pruebas se cierren correctamente. 

## TOOLS 🛠️

Las herramientas utilizadas en este proyecto fueron:

1. **Python 3.13**: Este es el lenguaje de programación para escribir las pruebas.
2. **PyTest**: Es el framework de Python para ejecutar las pruebas que llevan como nombre test.
3. **Git**: Es el que gestiona los cambios en el proyecto.
4. **GitHub**: Es la plataforma remota donde se almacena el repositorio del proyecto.
5. **PyCharm**: Es el entorno para editar y ejecutar el proyecto.

