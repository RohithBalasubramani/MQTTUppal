from django.apps import AppConfig
import logging
import threading

logger = logging.getLogger(__name__)

def run_management_command():
    from django.core.management import call_command
    try:
        call_command('read_mqtt')
    except Exception as e:
        logger.error(f"Failed to run read_mqtt command: {e}")

class MainConfig(AppConfig):
    name = 'main'
    
    def ready(self):
        # Run the management command in a separate thread
        if not any(thread.name == 'ReadMQTTThread' for thread in threading.enumerate()):
            thread = threading.Thread(target=run_management_command, name='ReadMQTTThread')
            thread.setDaemon(True)
            thread.start()
