from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class UrbanRoutesPage:
    txt_from = (By.ID, "from")
    txt_to = (By.ID, "to")
    btn_get_car = (By.CSS_SELECTOR, "button.button.round")
    btn_comfort = (By.CSS_SELECTOR, ".tcard:nth-child(5)")
    btn_phone_number = (By.CLASS_NAME, "np-text")
    txt_field_phone_number = (By.ID, "phone")
    btn_submit_phone_number = (By.XPATH, "//div[@class='section active']//button[@type='submit']")
    txt_code_number = (By.ID, "code")
    btn_submit_code = (By.CSS_SELECTOR, 'div.section.active button.button.full:nth-child(1)')
    txt_credit_card = (By.CLASS_NAME, 'pp-text')
    type_of_payment = (By.XPATH, '//div[div[@class= "pp-title" and contains(text(),"Agregar tarjeta")]]')
    txt_card_number = (By.ID, 'number')
    txt_card_code_number = (By.XPATH, '//input[@name="code"]')
    click_around_page_card = (By.CSS_SELECTOR, '.card-wrapper')
    btn_add_credit_card = (By.XPATH, '//div[@class= "pp-buttons"]//button[@type= "submit"]')
    choose_payment_method = (By.XPATH, '//div[div[@class= "pp-title" and contains(text(),"Tarjeta")]]')
    close_window_payment = (By.CSS_SELECTOR, 'div.payment-picker div.modal div.section.active  button.close-button')
    message_to_driver = (By.ID, "comment")
    click_request_tissue = (By.CSS_SELECTOR, 'div.r-type-switch:nth-child(1) div.r-sw-container div.r-sw div.switch span.slider.round')
    click_get_ice_cream = (By.XPATH, '//div[div[@class= "r-counter-label" and contains(text(),"Helado")]]//div[@class="counter-plus"]')
    ice_cream_counter = (By.XPATH, '//div[div[@class= "r-counter-label" and contains(text(),"Helado")]]//div[@class="r-counter"]//div[@class="counter"]//div[@class="counter-value"]')
    click_find_taxi = (By.CLASS_NAME, 'smart-button')


    #constructor
    def __init__(self, driver):
        self.driver = driver

#////////////////////////// punto #1 //////////////////////////////////
    #Rellenar el campo desde        #txt_from = (By.ID, "from")
    def set_from_field(self, field_from):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.txt_from)).send_keys(field_from) #colocar en la mayoria de campos para que cargue y lo encuentre

    def get_from_field(self):
        return self.driver.find_element(*self.txt_from).get_property('value')

    #Rellenar campo hasta           #txt_to = (By.ID, "to")
    def set_to_field(self, field_to):
        WebDriverWait(self.driver,5).until(EC.visibility_of_element_located(self.txt_to)).send_keys(field_to)

    def get_to_field(self):
        return self.driver.find_element(*self.txt_to).get_property('value')

    #Hacer clic en boton 'pedir un taxi'            # btn_get_car = (By.CSS_SELECTOR, "button.button.round")
    def click_in_btn_taxi(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.btn_get_car)).click()
     #   self.driver.find_element(*self.btn_get_car).click()

    def check_button_find_taxi(self):
        btn_taxi = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.btn_get_car))
        return btn_taxi.is_enabled()

    def start_search(self,field_from,field_to):
        self.set_from_field(field_from)
        self.set_to_field(field_to)

#//////////////////////// punto #2 //////////////////////////////////

    #Seleccionar tarifa comfort         #btn_comfort = (By.CSS, "tcard:nth-child(5)")
    def click_in_btn_comfort(self):
        WebDriverWait(self.driver,5).until(EC.element_to_be_clickable(self.btn_comfort)).click()

    def check_btn_comfort(self):
        return WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(self.btn_comfort)).is_enabled() #extraer texto y verificar

#//////////////////////// punto #3 //////////////////////////////////

    #Click en el campo número de teléfono           # btn_phone_number = (By.CLASS_NAME, "np-text")
    def click_on_field_phone_number(self):
        WebDriverWait(self.driver,5).until(EC.presence_of_element_located(self.btn_phone_number)).click()

    #Llenar el campo con número de telefono             #txt_field_phone_number = (By.ID, "phone")
    def setup_field_phone_number(self, phone_number):
        WebDriverWait(self.driver,5).until(EC.visibility_of_element_located(self.txt_field_phone_number)).send_keys(phone_number)

    def get_phone_number(self):
        return self.driver.find_element(self.txt_field_phone_number).get_property('value')

      #Clic en el boton siguiente para enviar el número de teléfono                 #  btn_submit_phone_number = (By.XPATH, "//div[@class='section active']//button[@type='submit']")
    def submit_phone_number(self):
        WebDriverWait(self.driver,5).until(EC.element_to_be_clickable(self.btn_submit_phone_number)).click()

    def check_btn_submit_phone_number(self):
        return self.driver.find_element(*self.btn_submit_phone_number).is_enabled()

    #Introducir el código
    def setup_code_number(self,code):
        WebDriverWait(self.driver,5).until(EC.visibility_of_element_located(self.txt_code_number)).send_keys(code)

    def get_code_number(self):
        return self.driver.find_element(*self.txt_code_number).get_property('value')

    #clic en el boton confirmar para enviar codigo          #btn_submit_code = (By.CSS, 'div.section.active button.button.full:nth-child(1)')
    def click_submit_code(self):
        WebDriverWait(self.driver,5).until(EC.element_to_be_clickable(self.btn_submit_code)).click()

    def check_btn_submit_code(self):
        return self.driver.find_element(*self.btn_submit_code).is_enabled()

    #verificar el # de telefono este en el campo
    def confirm_phone_number(self):
        confirm_phone =WebDriverWait(self.driver,5).until(EC.presence_of_element_located(self.btn_phone_number)).text
        return confirm_phone.strip()

#////////////////// punto #4 //////////////////////////////////

    #Clic en el metodo de pago          #txt_credit_card = (By.CLASS_NAME, 'pp-text')
    def click_on_field_payment_method(self):
        WebDriverWait(self.driver,5).until(EC.element_to_be_clickable(self.txt_credit_card)).click()

    #Escoger tipo de pago           # type_of_payment = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[2]')
    def choose_type_of_payment_method(self):
        WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(self.type_of_payment)).click()

    #Llenar campo número de tarjeta         #txt_card_number = (By.ID, 'number')
    def setup_field_credit_card(self, credit_card_number):
        WebDriverWait(self.driver,5).until(EC.visibility_of_element_located(self.txt_card_number)).send_keys(credit_card_number)

    def get_credit_card_numbers(self):
        return self.driver.find_element(*self.txt_card_number).get_property('value')

    #Llenar el campo código         #txt_card_code_number = (By.XPATH, '//input[@name="code"]')
    def setup_field_card_code_number(self, card_code_number):
        WebDriverWait(self.driver,5).until(EC.visibility_of_element_located(self.txt_card_code_number)).send_keys(card_code_number)

    def get_card_code_number(self):
        return self.driver.find_element(*self.txt_card_code_number).get_property('value')

    #Click alrededor de la ventana de tarjeta de credito            # click_around_page_card = (By.CLASS_NAME, '.card-wrapper')
    def click_around_page_credit_card(self):
        WebDriverWait(self.driver,5).until(EC.element_to_be_clickable(self.click_around_page_card)).click()

    #Agregar tarjeta de credito         #  btn_add_credit_card = (By.XPATH, '//div[@class= "pp-buttons"]//button[@type= "submit"]')
    def click_btn_add_credit_card(self):
        WebDriverWait(self.driver,5).until(EC.element_to_be_clickable(self.btn_add_credit_card)).click()

    def check_btn_add_credit_card(self):
        return self.driver.find_element(*self.btn_add_credit_card).is_enabled()

    #Escoger metodo de pago         #  choose_payment_method = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[2]')
    def choose_payment_method_type(self):
        WebDriverWait(self.driver,5).until(EC.element_to_be_clickable(self.choose_payment_method)).click()

    def payment_method_type(self):
        return self.driver.find_element(self.choose_payment_method).is_enabled()

    #Cerrar pagina metodo de pago        #close_window_payment = (By.CSS_SELECTOR, 'div.payment-picker div.modal div.section.active  button.close-button')
    def close_window_type_of_payment(self):
        WebDriverWait(self.driver,5).until(EC.visibility_of_element_located(self.close_window_payment)).click()

#////////////////////// punto #5 ////////////////////////

    #Escribir mensaje al conductor          #  message_to_driver = (By.ID, "comment")
    def comment_to_driver(self,comment):
        WebDriverWait(self.driver,5).until(EC.visibility_of_element_located(self.message_to_driver)).send_keys(comment)

    def comment(self):
        return self.driver.find_element(*self.message_to_driver).get_property('value')

#////////////////// punto #6 //////////////////////////////////

    #Click en el botón redondo para obtener manta y panuelos            #click_request_tissue = (By.CSS_SELECTOR, 'div.r-type-switch:nth-child(1) div.r-sw-container div.r-sw div.switch span.slider.round')
    def click_first_request(self):
        element = self.driver.find_element(*self.click_request_tissue)
        self.driver.execute_script("arguments[0].click();", element)

    def first_request(self):
        return self.driver.find_element(*self.click_request_tissue).is_enabled()

        #//////////////////// punto #7 ///////////////////////////////

    #Seleccionar la cantidad de helados          click_get_ice_cream = (By.XPATH, '//div[div[@class= "r-counter-label" and contains(text(),"Helado")]]//div[@class="counter-plus"]')
    def click_btn_add_ice_cream(self):
        element = WebDriverWait(self.driver,5).until(EC.element_to_be_clickable(self.click_get_ice_cream))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        element.click()
        #element = self.driver.find_element(*self.click_get_ice_cream)
        #self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        #self.driver.execute_script("arguments[0]", element)
        #WebDriverWait(self.driver,5).until(EC.element_to_be_clickable(self.click_get_ice_cream)).click()

    def select_quantity_ice_cream(self, times=2):
        ice_cream = WebDriverWait(self.driver,5).until(EC.element_to_be_clickable(self.click_get_ice_cream))
        for i in range(times):
            ice_cream.click()
        #assert ice_cream == 2

    def count_ice_cream(self):
        ice_cream = self.driver.find_element(*self.ice_cream_counter)
        return ice_cream.text

    def btn_add_ice_cream(self):
        return WebDriverWait(self.driver,5).until(EC.element_to_be_clickable(self.click_get_ice_cream)).is_enabled()

#//////////////////// punto #8 //////////////////////////////////

    #Click pedir un taxi            click_find_taxi = (By.CLASS_NAME, 'smart-button')
    def click_get_taxi(self):
        WebDriverWait(self.driver,5).until(EC.element_to_be_clickable(self.click_find_taxi)).click()

    def get_taxi(self):
        return self.driver.find_element(*self.click_find_taxi).is_enabled()


#/////////////////////// automatización ///////////////////////////

