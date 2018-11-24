from services import calendar_service

def updateCalendar(topic=None, details=None):
    calendar_service.get_home_controller_events()