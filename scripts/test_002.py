import allure


class Test_002:
    def test_add_png(self):
        with open("./scripts/abc.png","rb") as f:
            allure.attach("截图",f.read(),allure.attach_type.PNG)