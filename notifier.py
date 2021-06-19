from notifypy import Notify

notification = Notify()


def show_notification(message: str, title: str = "Slot Available"):
    '''
        Wrapper Function for pushing a notification
        message: The message to show in notification
        title: The title of the notification
    '''
    notification.title = title
    notification.message = message
    notification.send()
