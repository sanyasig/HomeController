import logging

from entities import tv

def process_message(topic=None, message=None):
 # TODO: need to fix the dynamic loading of modules
    try:
        print("topic: " + topic)
        print("status " + str(message))

        services = {
                   # "ifttt":ifttt,
                  #  "dash":dash,
                   # 'volumio': volumio,
                    #'alerts':alerts,
                    #'audio':audio,
                    'tv':tv,
                    #'trigger': trigger
                    }
        intent = topic.split('/')[1]
        module = services[intent]
        logging.info("calling module " + str(module))
        func = getattr(module, topic.split("/")[2])
        func(topic, message)

    except :
        logging.info("Cannto find service")