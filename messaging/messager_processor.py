import logging

from entities import alerts, dash, audio, ifttt, firetv, tv, volumio, trigger

def process_message(topic=None, message=None):
 # TODO: need to fix the dynamic loading of modules
    try:
        logging.info("topic: " + topic)
        logging.info("status " + str(message))

        services = {
                    "ifttt":ifttt,
                    'firetv':firetv,
                    "dash":dash,
                    'volumio': volumio,
                    'alerts':alerts,
                    'audio':audio,
                    'tv':tv,
                    'trigger': trigger
                    }
        intent = topic.split('/')[1]
        module = services[intent]
        logging.info("calling module " + str(module))
        func = getattr(module, topic.split("/")[2])
        func(topic, message)

    except :
        logging.info("Cannto find service")

    # service = Utils.getService(topic)
    # execution = service.get_function(message)
    # execution = service.get_function(message)
    #
    # if(execution != None):
    #     result =  execution()


