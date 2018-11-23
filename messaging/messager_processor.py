import ahlogger

from entities import alerts, dash, audio, ifttt, firetv, tv, volumio


def process_message(topic=None, message=None):
 # TODO: need to fix the dynamic loading of modules
    try:
        ahlogger.log("topic: " + topic)
        ahlogger.log("status " + str(message))

        services = {"ifttt":ifttt,
                    'firetv':firetv,
                    "dash":dash,
                    'volumio': volumio,
                    'alerts':alerts,
                    'audio':audio,
                    'tv':tv
                    }
        intent = topic.split('/')[1]
        module = services[intent]
        #
        # if ("ifttt" in topic):
        #     module = ifttt
        # if ("firetv" in topic):
        #     module = firetv
        # if ("dash" in topic):
        #     module = dash
        # if ("volumio" in topic):
        #     module = volumio
        # if ("alerts" in topic):
        #     module = alerts
        # if ("" in topic):
#            module = audio

        func = getattr(module, topic.split("/")[2])
        func(topic, message)

    except :
        ahlogger.log("Cannto find service")

    # ahlogger.log "mesage: " + message
    # service = Utils.getService(topic)
    # execution = service.get_function(message)
    # execution = service.get_function(message)
    #
    # if(execution != None):
    #     result =  execution()
    #     ahlogger.log result


