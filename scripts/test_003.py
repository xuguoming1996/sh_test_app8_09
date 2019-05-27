import allure

class Test_003:
    @allure.step(title="测试步骤001")
    def test_001(self):
        print("-->test_01")
        allure.attach('描述', '我是测试步骤001的描述～～～')
        assert 1
