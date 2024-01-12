class CalendarEvent:
    def __init__(self, title, country, date, impact, forecast, previous):
        self.title = title
        self.country = country
        self.date = date
        self.impact = impact
        self.forecast = forecast
        self.previous = previous
       

    def text(self) -> str:
        short_date = self.date.split("T")[0]  # Extracting date part
        
        return f"""事件: {self.title}\n国家: {self.country}\n日期: {short_date}\n影响: {self.impact}\n预测: {self.forecast}\n先前: {self.previous}\n"""