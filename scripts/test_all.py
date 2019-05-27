import allure
import pytest


class Test_allure:
    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    @allure.step(title="测试步骤001")
    def test_001(self):
        print("-->test_001")
        allure.attach('描述', '我是测试步骤001的描述～～～')
        assert 1

    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    @allure.step(title="测试步骤002")
    def test_002(self):
        print("-->test_002")
        allure.attach('用户名', '张三')
        allure.attach('密码','123456')
        assert 0

    @pytest.allure.severity(pytest.allure.severity_level.NORMAL)
    @allure.step(title="测试步骤003")
    def test_003(self):
        print("-->test_003")
        allure.attach('标题', '我是测试步骤003的具体内容～～～')
        assert 1

    @pytest.allure.severity(pytest.allure.severity_level.MINOR)
    @allure.step(title="测试步骤004")
    def test_004(self):
        print("-->test_004")
        allure.attach('标题', '我是测试步骤004的具体内容～～～')
        assert 1

    @pytest.allure.severity(pytest.allure.severity_level.TRIVIAL)
    @allure.step(title="测试步骤005")
    def test_005(self):
        print("-->test_005")
        allure.attach('标题', '我是测试步骤005的具体内容～～～')
        assert 1