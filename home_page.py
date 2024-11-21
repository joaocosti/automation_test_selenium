from selenium.webdriver.common.by import By
from base_page import BasePage

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://tdd-detroid.onrender.com/"
        self.student_name_input = (By.ID, "student-nome")
        self.add_student_button = (By.ID, "student-btn")
        self.course_name_input = (By.ID, "course-nome")
        self.add_course_button = (By.ID, "course-btn")
        self.student_id_input = (By.ID, "student-id")
        self.course_id_input = (By.ID, "course-id")
        self.add_student_to_course_button = (By.CSS_SELECTOR, ".form-group:nth-child(4) > #course-btn")
        self.discipline_name_input = (By.ID, "discipline-nome")
        self.course_discipline_id_input = (By.ID, "course-discipline-id")
        self.add_discipline_button = (By.CSS_SELECTOR, ".form-group:nth-child(5) > #course-btn")
        self.subscribe_student_id_input = (By.ID, "subscribe-student-id")
        self.subscribe_discipline_id_input = (By.ID, "subscribe-discipline-id")
        self.subscribe_button = (By.CSS_SELECTOR, ".form-group:nth-child(6) > #course-btn")
        self.messages = (By.CSS_SELECTOR, ".py-p")
        self.loading_elements = (By.CSS_SELECTOR, ".smooth")

    def open(self):
        self.driver.get(self.url)
        self.driver.set_window_size(1920, 1080)

    def wait_for_page_to_load(self):
        self.wait_for_element(*self.loading_elements)

    def add_student(self, name):
        self.find_element(*self.student_name_input).send_keys(name)
        self.find_element(*self.add_student_button).click()

    def add_course(self, name):
        self.find_element(*self.course_name_input).clear()
        self.find_element(*self.course_name_input).send_keys(name)
        self.find_element(*self.add_course_button).click()

    def add_student_to_course(self, student_id, course_id):
        self.find_element(*self.student_id_input).clear()
        self.find_element(*self.student_id_input).send_keys(student_id)
        self.find_element(*self.course_id_input).clear()
        self.find_element(*self.course_id_input).send_keys(course_id)
        self.find_element(*self.add_student_to_course_button).click()

    def add_discipline_to_course(self, discipline_name, course_id):
        self.find_element(*self.discipline_name_input).clear()
        self.find_element(*self.discipline_name_input).send_keys(discipline_name)
        self.find_element(*self.course_discipline_id_input).clear()
        self.find_element(*self.course_discipline_id_input).send_keys(course_id)
        self.find_element(*self.add_discipline_button).click()

    def subscribe_student_to_discipline(self, student_id, discipline_id):
        self.find_element(*self.subscribe_student_id_input).clear()
        self.find_element(*self.subscribe_student_id_input).send_keys(student_id)
        self.find_element(*self.subscribe_discipline_id_input).clear()
        self.find_element(*self.subscribe_discipline_id_input).send_keys(discipline_id)
        self.find_element(*self.subscribe_button).click()

    def get_messages(self,index = 0):
        return self.find_elements(*self.messages)[index].text
