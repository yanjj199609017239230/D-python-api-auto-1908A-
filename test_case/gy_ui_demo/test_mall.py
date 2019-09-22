
def test_ui1_shuru(driver):
    # 打开网页
    driver.get("打开登录页面",'http://ui.yansl.com/#/input')

    driver.send_keys("纯输入框",'//input[@name="t1"]','hello,晨曦')

    driver.send_keys("纯密码框", '//input[@name="t2"]', 'xinshoushanglu')

    driver.send_keys("纯文本域", '//textarea[@name="t3"]', '此处为纯文本')

    driver.send_keys("输入框2", '//label[text()="输入框2"]/../div//input', '此处为输入框2')

    driver.send_keys("密码框2", '//input[@name="t5"]', '此处为密码框2')

    driver.send_keys("文本域2", '//textarea[@name="t6"]', '此处为文本域2')

    driver.send_keys("建议框1", '//input[@name="t7"]', '此处为建议框1')

    driver.send_keys("建议框2", '//input[@name="t8"]', '此处为建议框2')


def test_ui1_danxuan(driver):
    # 打开网页
    driver.get("打开登录页面",'http://ui.yansl.com/#/radio')

    driver.click("纯单选框,男",'//input[@value="0"]')

    driver.click("单选框2,备选项1", '//label[text()="单选框2"]/../div//span/span')

    driver.click("单选项3,广州", '//span[text()="广州"]')

def test_ui1_duoxuan(driver):
    # 打开网页
    driver.get("打开登录页面",'http://ui.yansl.com/#/checkbox')

    driver.click("纯多选框,重庆", '(//input[@type="checkbox"])[2]')

    driver.click("纯多选框,河南", '(//input[@type="checkbox"])[3]')

    driver.click("多选框2,mysql", '//span[text()="mysql"]/../span/span')

    driver.click("多选框2,selenium", '//span[text()="selenium"]/../span/span')

    driver.click("多选框3,北京", '//input[@value="广州"]/../span')

    driver.click("多选框3,深圳", '//input[@value="深圳"]/../span')

    driver.click("多选框4,深圳", '(//span[text()="深圳"])[2]')


def test_ui1_xiala(driver):
    # 打开网页
    driver.get("打开登录页面",'http://ui.yansl.com/#/select')

    driver.select_by_index("多选框4,华为", '//select[@name="item1"]',2)

    driver.click("下拉框2,点击框1", '//label[text()="下拉框2"]/../div//input')

    driver.click("下拉框2,点击框2蚵仔煎", '(//span[text()="蚵仔煎"])[last()]')

    driver.click("下拉框6,点击框1", '//label[text()="下拉框6"]/..//input')

    driver.click("下拉框6,龙须面", '(//span[text()="龙须面"])[last()]')
    driver.click("下拉框6,龙须面", '(//span[text()="双皮奶"])[last()]')

















































