import config


class HomeService:

    def get_config(self, service_name):
        all_keys = dir(config)
        if service_name in all_keys:
            return getattr(config,service_name)
        else:
            raise AttributeError("Service name not found in config")