# -*- coding: UTF-8 -*-
try:
    import os
    import requests
    from model.calendar import CalendarEvent
    from bs4 import BeautifulSoup
except ImportError:
    raise ImportError("🥹无法安装配件")
finally:
    pass

class ForexFactory:
    def __init__(self) -> None:
        super(ForexFactory, self).__init__()
        
        self.ffurl :str = "http://www.forexfactory.com/calendar"
        self.format :str = "html5lib"
        self.request_failed :str = "400: 网站无法访问"
        self.red :str = "\u001b[31m"
        self.green :str = "\u001b[32m"
        self.yellow :str = "\u001b[33m"
        self.urgency :list = ["Low", "Medium", "High"]
        
    def get_url(self, url) -> str:
        headers :dict = { 
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"
        }

        response = requests.get(url=self.ffurl, headers=headers)

        if response.status_code == 200:
            soup =  BeautifulSoup(response.content, self.format)
            link = soup.find("div", attrs={ "class" : "darktext" })
            data = soup.find('a', text='JSON')["href"]
            
            return data
        else:
            return self.request_failed

    def get_urgency(self, urgency: int) -> str:
        if urgency == self.urgency[0]: return self.green
        if urgency == self.urgency[1]: return self.yellow
        if urgency == self.urgency[2]: return self.red
        return ""
        
        
    def get_calendar(self):
        try:
            url :str = self.get_url(url=self.ffurl)

            if url == self.request_failed:
                print(self.request_failed, "<<<")
            else:
                response :object = requests.get(url)

                if response.status_code == 200:
                    json_data_list = response.json()

                    for json_data in json_data_list:

                        calendar_data :CalendarEvent = CalendarEvent(
                            title=json_data.get("title", ""),
                            country=json_data.get("country", ""),
                            date=json_data.get("date", ""),
                            impact=json_data.get("impact", ""),
                            forecast=json_data.get("forecast", ""),
                            previous=json_data.get("previous", "")
                        )

                        print(self.get_urgency(urgency=calendar_data.impact) + calendar_data.text());
        except SyntaxError:
            raise SyntaxError("语法错误")
        except KeyError as k:
            raise KeyError(f"未找到{k}")
        except Exception as e:
            raise Exception(str(e))
        
if __name__ == "__main__":
    ffcalendar = ForexFactory()
    ffcalendar.get_calendar()
