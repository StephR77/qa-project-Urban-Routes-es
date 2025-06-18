from selenium import webdriver
from method import UrbanRoutesPage
import data
from helpers import retrieve_phone_code


class TestUrbanRoutes:
    driver = None

    @classmethod
    def setup_class(cls):
        from selenium.webdriver.chrome.options import Options  # from selenium.webdriver import DesiredCapabilities
        options = Options()  # capabilities = DesiredCapabilities.CHROME
        options.set_capability("goog:loggingPrefs",
                               {"performance": "ALL"})  # capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome(
            options=options)  # cls.driver = webdriver.Chrome(desired_capabilities=capabilities)

    #////////////////////////////// punto #1 //////////////////////////////
    #Iniciar sesion
    def setup_method(self):
        self.start_app = UrbanRoutesPage(self.driver)

    def test_start_app(self):
        self.driver.get(data.urban_routes_url)

        self.start_app.start_search(data.info_from,data.info_to)    #paso
        assert self.start_app.get_from_field() == data.info_from
        assert self.start_app.get_to_field() == data.info_to
        assert self.start_app.check_button_find_taxi() == True
        self.start_app.click_in_btn_taxi()
        self.start_app.click_in_btn_comfort()  #clic conseguir taxi

    #////////////////////////////// punto #2 /////////////////////////

    #Seleccionar la tarifa Comfort
    def test_tariff_comfort(self):
        self.test_start_app()
        assert self.start_app.check_btn_comfort() == True
        self.start_app.click_in_btn_comfort()

    #//////////////////// punto #3 /////////////////////////////

    #Ingresar # de telefono
    def test_input_phone_number(self):
        self.test_start_app()
        self.start_app.click_on_field_phone_number()    #clic en el campo # de telefono

        self.start_app.setup_field_phone_number(data.phone_number)  # llenar el campo # de telefono
        #assert self.start_app.get_phone_number() == data.phone_number

        assert self.start_app.check_btn_submit_phone_number() == True
        self.start_app.submit_phone_number()    #clic boton agregar # de telefono

        code = retrieve_phone_code(self.driver)
        self.start_app.setup_code_number(code)

        self.start_app.click_submit_code()
        assert self.start_app.check_btn_submit_code() == True
        assert self.start_app.confirm_phone_number() == data.phone_number

    #//////////////////// punto #4 /////////////////////////////////

    #Agregar tarjeta de credito
    def test_credit_card(self):
        self.test_start_app()
        self.start_app.click_on_field_payment_method()  #clic en el metodo de pago
        self.start_app.choose_type_of_payment_method()  #escoger el tipo de metodo de pago

        self.start_app.setup_field_credit_card(data.card_number)  # llenar campo # de tarjeta
        assert self.start_app.get_credit_card_numbers() == data.card_number

        self.start_app.setup_field_card_code_number(data.card_code)  # llenar campo codigo
        assert self.start_app.get_card_code_number() == data.card_code

        self.start_app.click_around_page_credit_card()  #clic alrededor de la tarjeta de credito

        assert self.start_app.check_btn_add_credit_card() == True
        self.start_app.click_btn_add_credit_card()  #clic agregar tarjeta de credito

    # //////////////////// punto #5 /////////////////////////////////

    #Escribir mensaje al conductor
    def test_message_driver(self):
        self.test_start_app()
        self.start_app.comment_to_driver(data.message_for_driver)
        assert self.start_app.comment() == data.message_for_driver

    # //////////////////// punto #6 /////////////////////////////////

    #pedir manta
    def test_click_request_tissues(self):
        self.test_start_app()
        assert self.start_app.first_request() == True
        self.start_app.click_first_request()

    # //////////////////// punto #7 /////////////////////////////////

    #pedir helados
    def test_get_ice_cream(self):
        self.test_start_app()
        assert self.start_app.btn_add_ice_cream() == True
        self.start_app.click_btn_add_ice_cream()
        self.start_app.select_quantity_ice_cream()


    # //////////////////// punto #8 /////////////////////////////////

    #pedir taxi
    def test_request_taxi(self):
        self.test_start_app()
        assert self.start_app.get_taxi() == True
        self.start_app.click_get_taxi()


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
