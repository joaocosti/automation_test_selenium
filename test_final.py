from selenium import webdriver
from home_page import HomePage

class TestDemo:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.home_page = HomePage(self.driver)

    def teardown_method(self):
        self.driver.quit()

    def test_demo(self):
        self.home_page.open()
        self.home_page.wait_for_page_to_load()

        student_name = "douglas"
        student_id = 1
        course_names = ["mat", "port", "geo"]
        discipline_names = ["mat1", "mat2", "mat3"]
        course_id_for_disciplines = 1

        self.home_page.add_student(student_name)
        assert f"INFO Added student id: 1, Name: {student_name}" in self.home_page.get_messages()

        for idx, course_name in enumerate(course_names, start=1):
            self.home_page.add_course(course_name)
            assert f"INFO Added course id: {idx}, Nome: {course_name}" in self.home_page.get_messages()

        self.home_page.add_student_to_course(student_id, 1)
        assert f"INFO Student id {student_id} subscribed to course id 1" in self.home_page.get_messages()

        for idx, discipline_name in enumerate(discipline_names, start=1):
            self.home_page.add_discipline_to_course(discipline_name, course_id_for_disciplines)
            assert f"INFO Added discipline id: {idx}, Name: {discipline_name}, Course: {course_id_for_disciplines}" in self.home_page.get_messages()

        for idx, discipline_name in enumerate(discipline_names, start=1):
            messageSelectorIndex = 0 if idx == 3 else 1
            self.home_page.subscribe_student_to_discipline(student_id, idx)
            assert f"INFO Student id {student_id}, Name {student_name} subscribed to discipline id {idx}" in self.home_page.get_messages(messageSelectorIndex)