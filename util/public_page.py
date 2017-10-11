from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import time
import random
import logging
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class PublicPage:

    # location
    pre_button_xpath = '//*[@id="ui-datepicker-div"]/div/a[1]'
    next_button_xpath = '//*[@id="ui-datepicker-div"]/div/a[2]'
    # 日期年下拉 class
    datepicker_year_drop_elem = '.ui-datepicker-year'
    # 日期 月下拉 class
    datepicker_month_drop_elem = 'ui-datepicker-month'

    def __init__(self, driver):
        self.driver = driver
        # self.driver = webdriver.Chrome()

    # 判断元素是否显示
    def is_element_present(self, elem_loc):
        try:
            # self.driver.find_element_by_xpath(elem_loc)
            elem_loc
        except NoSuchElementException as e:
            return False
        return True

    # 判断alert框是否出现
    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    # 关闭alert框，且获取alert内容
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    # 日历
    def select_date(self, calen_xpath, day):
        calen_loc = self.driver.find_element_by_xpath(calen_xpath)
        self.click_elem(calen_loc)
        pre_button = self.driver.find_element_by_xpath(self.pre_button_xpath)
        next_button = self.driver.find_element_by_xpath(self.next_button_xpath)
        time.sleep(2)
        if pre_button:
            return self.driver.find_element_by_link_text(day).click()
        else:
            return False

    # 选择日期
    # year:2017
    # month:一月
    # day：1
    def select_date_by_ymd(self, calen_drop_loc, year, month, day):
        try:
            self.click_elem(calen_drop_loc)
            year_drop_loc = self.driver.find_element_by_css_selector(
                self.datepicker_year_drop_elem)
            self.select_dropdown_item(year_drop_loc, year)
            month_drop_loc = self.driver.find_element_by_css_selector(
                self.datepicker_month_drop_elem)
            self.select_dropdown_item(month_drop_loc, month)
            day_loc = self.driver.find_element_by_link_text(day)
        except Exception as e:
            print(
                '[PublicPage] There was an exception when select_date_by_ymd=>', str(e))

    # 月份选择插件
    def select_month(self, calen_drop_loc, month):
        self.click_elem(calen_drop_loc)
        pre_btn = self.driver.find_element_by_css_selector('.pull-left')
        time.sleep(2)
        if pre_btn:
            return self.driver.find_elements_by_css_selector('.month-button')[month].click()
        else:
            return False

    # 删除日历
    def delete_date(self, elem_xpath):
        del_loc = self.driver.find_element_by_xpath(elem_xpath)
        self.scroll_to_elem(del_loc)
        return del_loc.click()

    # 随机数
    # num: 范围
    def random_num(self, num):
        return random.randrange(0, num)

    # 点击事件
    def click_elem(self, elem_loc):
        try:
            if self.is_element_present(elem_loc):
                self.move_to_element_to_click(elem_loc)
                # elem_loc.click()
            else:
                self.scroll_to_elem(elem_loc)
                elem_loc.click()
        except Exception as e:
            logging.error('There was an exception when click_elem %s', str(e))

    def double_click_elem(self, elem_loc):
        try:
            if self.is_element_present(elem_loc):
                action = ActionChains(self.driver)
                action.move_to_element(elem_loc).double_click()
            else:
                action = ActionChains(self.driver)
                self.scroll_to_elem(elem_loc)
                action.move_to_element(elem_loc).double_click()
        except Exception as e:
            logging.error(
                'There was an exception when double_click_elem %s', str(e))

    # input 框
    def set_value(self, elem_loc, input_value):
        try:
            if self.is_element_present(elem_loc):
                self.move_to_element_to_click(elem_loc)
            else:
                self.scroll_to_elem(elem_loc)
            elem_loc.clear()
            elem_loc.send_keys(input_value)
        except Exception as e:
            logging.error('There was an exception when set_value s%', str(e))

    # input 框
    # 滚动屏幕至元素位置设值
    def scroll_to_set_value(self, elem_loc, input_value):
        try:
            self.is_element_present(elem_loc)
            self.scroll_to_elem(elem_loc)
            elem_loc.clear()
            elem_loc.send_keys(input_value)
        except Exception as e:
            logging.error(
                'There was an exception when scroll_to_set_value s%', str(e))

    # 获取文本值
    def get_value(self, elem_loc):
        try:
            self.scroll_to_elem(elem_loc)
            return elem_loc.text
        except Exception as e:
            logging.error('There was an exception when get_value s%', str(e))

    # 光标移动到元素为止并做点击操作
    def move_to_element_to_click(self, elem_loc):
        # action = webdriver.common.action_chains.ActionChains(self.driver)
        action = ActionChains(self.driver)
        action.move_to_element(elem_loc).click().perform()

    # 将光标定位到元素处
    def scroll_to_elem(self, elem_loc):
        try:
            return self.driver.execute_script('return arguments[0].scrollIntoView();',
                                              elem_loc)
        except Exception as e:
            print('Error scrolling down  web elem ', str(e))

    # 将光标定位到页面顶部
    def scroll_to_top(self):
        return self.driver.execute_script('scroll(250,0)')

    # 将光标定位到页面底部
    def scroll_to_bottom(self):
        return self.driver.execute_script(
            'scroll(0,document.body.scrollHeight)')

    # 获取元素位置坐标
    def get_elem_location(self, elem_loc):
        try:
            location = elem_loc.location
            size = elem_loc.size
            print('location=>', location, '\nsize=>', size)
            return location
        except Exception as e:
            print('[PublicPage]There was an exception when get_elem_location=>', str(e))

    # 选择下拉项
    def select_dropdown_item(self, drop_loc, item_name):
        # self.click_elem(drop_loc)
        # time.sleep(1)
        # item_loc = self.driver.find_element_by_link_text(item_name)
        # self.click_elem(item_loc)
        try:
            self.move_to_element_to_click(drop_loc)
            time.sleep(1)
            item_loc = self.driver.find_element_by_link_text(item_name)
            self.scroll_to_elem(item_loc)
            self.click_elem(item_loc)
        except Exception as e:
            print(
                '[PublicPage]There was an exception when select_dropdown_item=>', str(e))

    # alet
    def get_alert_msg(self):
        alert_msg_array = []
        alert_loc = self.driver.find_element_by_tag_name('alert')
        alert_msg = alert_loc.text
        print('alert_msg type=>', alert_msg)
        alert_msg_array = alert_msg.spilt('\n')
        print('The alert message is ', alert_msg_array[2])
        close_loc = self.driver.find_element_by_css_selector('.close')
        close_loc.click()
        return alert_msg_array[2]

    # danger
    def get_danger_msg(self):
        try:
            danger_loc = self.driver.find_element_by_css_selector(
                '.text-danger')
            self.scroll_to_elem(danger_loc)
            danger_msg = danger_loc.text
            print('The danger message is ', danger_msg)
            return danger_msg
        except Exception as e:
            logging.error('There are an exception %s', str(e))

    # 必填项红框警示
    def has_danger_is_show(self):
        publicPage = PublicPage(self.driver)
        ui_loc = self.driver.find_element_by_css_selector('.has-danger')
        print('publicPage.is_element_present(ui_loc)=>',
              publicPage.is_element_present(ui_loc))
        return publicPage.is_element_present(ui_loc)
