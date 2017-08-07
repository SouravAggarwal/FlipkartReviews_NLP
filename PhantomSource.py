from selenium import webdriver

class PhantomSource:

    def getSource(self,URL):
        driver =webdriver.PhantomJS(executable_path=r'C:\phantomjs-2.1.1-windows\bin\phantomjs.exe')
        #driver = webdriver.PhantomJS()
        driver.get(URL)
        retval= driver.page_source
        driver.quit()
        return retval

