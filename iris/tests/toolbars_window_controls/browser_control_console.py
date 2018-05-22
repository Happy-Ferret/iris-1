# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.


from iris.test_case import *


class Test(BaseTest):

    def __init__(self, app):
        BaseTest.__init__(self, app)
        self.meta = "This is a test case that checks that Browser Control Console work as expected"


    def run(self):

        url = "about:home"

        navigate(url)
        time.sleep(3)

        open_web_console()
        time.sleep(3)
        # get screen Region
        screen = get_screen()
        # from screen region create a region in the left down corner
        left_corner_screen_region = Region(screen.getX(), screen.getH() / 2 - 100, screen.getW() / 3, screen.getH() / 2)
        # search for keyword 'console' in the left corner of the screen with OCR
        element_picker_assert= left_corner_screen_region.exists('browser_control_console_element_picker.png')
        assert_true(self, element_picker_assert, 'Image is present and console is open')

        # open a console from developer tool command line
        console_command = 'window.alert("test alert")'
        type(console_command)
        type(Key.ENTER)
        # create a new region in the center of the screen
        center_screen = Region(0, screen.getH() / 4 , screen.getW() , screen.getH() / 2-100)
        # verify if alert text is displayed
        center_screen_text_assert=center_screen.exists('browser_control_console_test_alert.png')
        assert_true(self, center_screen_text_assert, 'Alert message found')

        # accept the alert message
        type(Key.ENTER)
        logger.debug('Pop up message is closed ')
        open_browser_console()
        logger.debug('Opening browser console with keyboard shortcut ')
        browser_control_console_title_assert=center_screen.exists('browser_control_console_title.png')
        assert_true(self, browser_control_console_title_assert, 'Console is opened')
        expanded_center_region = Region(center_screen.getX(), center_screen.getY(), center_screen.getW() * 1.5,
                                            center_screen.getH())
        expanded_center_region.click('auxiliary_window_close_button.png')
        time.sleep(1)
        close_console_assert = center_screen.exists('auxiliary_window_close_button.png', 5)
        assert_false(self, close_console_assert, 'Console closed')

        open_browser_console()
        auxiliary_window_assert = exists('auxiliary_window_close_button.png', 5)
        assert_true(self, auxiliary_window_assert, 'Console was reopened')

        minimize_button_assert = expanded_center_region.exists('auxiliary_window_minimize.png', 5)
        assert_true(self, minimize_button_assert, 'Minimize button exists')

        expanded_center_region.click('auxiliary_window_minimize.png')
        logger.debug('Browser Console is minimized')
        open_browser_console()
        maximize_button_assert = expanded_center_region.exists('auxiliary_window_maximize.png', 5)
        assert_true(self, maximize_button_assert, 'Maximize button exists')

        expanded_center_region.click('auxiliary_window_maximize.png')
        logger.debug('Browser Console is maximized')
        if Settings.getOS() == Platform.WINDOWS:
            force_close()
