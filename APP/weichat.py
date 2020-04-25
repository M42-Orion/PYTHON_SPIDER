from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

server = "http://localhost:4723/wd/hub"
desired_caps = {
    "platformName": "Android",
    "deviceName": "127.0.0.1:7555",
    "appPackage": "com.tencent.mobileqq",
    "appActivity": "com.tencent.mobileqq.activity.SplashActivity"
}
driver = webdriver.Remote(server, desired_caps)
time.sleep(10)
el1 = driver.find_element_by_id("com.tencent.mobileqq:id/btn_login")
el1.click()
time.sleep(3)
el2 = driver.find_element_by_accessibility_id("请输入QQ号码或手机或邮箱")
el2.click()
time.sleep(3)
el2.send_keys("1821199691")
time.sleep(3)
el3 = driver.find_element_by_accessibility_id("密码 安全")
el3.click()
time.sleep(3)
el3.send_keys("QQmima123!")
time.sleep(3)
el4 = driver.find_element_by_accessibility_id("登 录")
el4.click()
time.sleep(3)
el5 = driver.find_element_by_accessibility_id("同意")
el5.click()
time.sleep(3)
el6 = driver.find_element_by_accessibility_id("去授权按钮")
el6.click()
time.sleep(3)
el7 = driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button")
el7.click()
time.sleep(3)
el8 = driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button")
el8.click()
time.sleep(3)
el9 = driver.find_element_by_accessibility_id("登 录")
el9.click()
while True:
    try:
        time.sleep(10)
        el10 = driver.find_element_by_accessibility_id("稍后处理按钮")
        el10.click()
        break
    except:
        pass
time.sleep(3)
el2 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.TabHost/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.TabWidget/android.widget.FrameLayout[3]")
el2.click()
time.sleep(3)
el3 = driver.find_element_by_id("com.tencent.mobileqq:id/qzone_feed_entry")
el3.click()
time.sleep(3)
# driver.press(x=637, y=843).move_to(x=628, y=326).release().perform()

# 获取屏幕的size
size = driver.get_window_size()
print(size)
# 获取屏幕宽度 width
width = size['width']
print(width)
# 获取屏幕高度 height
height = size['height']
print(height)

# 执行滑屏操作,向下（下拉）滑动
x1 = width*0.5
y1 = height*0.25
y2 = height*0.9
time.sleep(6)
print("滑动前")
driver.swipe(x1,y1,x1,y2)

for i in range(5):
    print("第%d次滑屏"%i)
    time.sleep(3)
    driver.swipe(x1,y2,x1,y1)

ele = driver.find_element_by_id('com.tencent.mobileqq:id/j')
time.sleep(2)
print(ele)
