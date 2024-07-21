import json


class Results:

    def __str__(self) -> str:
        return self.jsonify(indent=2)

    def __getattr__(self, name):
        return self.find_keys(keys=name)

    def __setitem__(self, key, value):
        self.original_update[key] = value

    def __getitem__(self, key):
        return self.original_update[key]

    def __lts__(self, update: list, *args, **kwargs):
        for index, element in enumerate(update):
            if isinstance(element, list):
                update[index] = self.__lts__(update=element)
            elif isinstance(element, dict):
                update[index] = Results(update=element)
            else:
                update[index] = element
        return update

    def __init__(self, update: dict, *args, **kwargs) -> None:
        self.client = update.get("client")
        self.original_update = update

    def jsonify(self, indent=None) -> str:
        result = self.original_update
        result["original_update"] = "dict{...}"
        return json.dumps(result, indent=indent, ensure_ascii=False, default=lambda value: str(value))

    def find_keys(self, keys, original_update=None, *args, **kwargs):
        if original_update is None:
            original_update = self.original_update

        if not isinstance(keys, list):
            keys = [keys]

        if isinstance(original_update, dict):
            for key in keys:
                try:
                    update = original_update[key]
                    if isinstance(update, dict):
                        update = Results(update=update)
                    elif isinstance(update, list):
                        update = self.__lts__(update=update)
                    return update
                except KeyError:
                    pass
            original_update = original_update.values()

        for value in original_update:
            if isinstance(value, (dict, list)):
                try:
                    return self.find_keys(keys=keys, original_update=value)
                except AttributeError:
                    return None

        return None

    @property
    def to_dict(self) -> dict:
        """
        Return the update as dict
        """
        return self.original_update

    @property
    def id(self):
        return self.find_keys("id")

    @property
    def is_bot(self):
        return self.find_keys("is_bot")

    @property
    def first_name(self):
        return self.find_keys("first_name")

    @property
    def last_name(self):
        return self.find_keys("last_name")

    @property
    def username(self):
        return self.find_keys("username")
