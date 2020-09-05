import json
import pprint

pp = pprint.PrettyPrinter(indent=4)

class GetData:

    def __init__(self):

        self.json = self.load_json()


    def load_json(self):
        with open('test.json') as file:
            data = json.load(file)

        return data

    def get_data(self, key:str = None, filter_key:str = None, filter_value:str = None):

        """
        Helper function that retrieves the data from
        the json file that matches a specific key

        Can also take 1 key and 1 value from the nested dicts
        to fetch specific data
        """

        if not any([key, filter_key, filter_value]):
            result = self.json
            return result
        else:
            if key is not None:
                if any([filter_key, filter_value]):
                    new_dict = {info for info in self.json[key] if info[filter_key] == filter_value}
                    return new_dict
                else:
                    result = self.json[key]
                    return result
            else:
                if any([filter_key, filter_value]):
                    new_dict = dict()
                    for key_serie, value_series in self.json.items():
                        empty_list = []
                        for info in value_series:
                            try:
                                if info[filter_key].lower() == filter_value.lower():
                                    new_dict[key_serie] = empty_list
                                    for k,v in new_dict.items():
                                        if k == key_serie:
                                            v.append(info)
                            except KeyError:
                                pass
                        if len(new_dict) == 0:
                            new_dict = {"Message": f"No results found with {filter_key} that has {filter_value} as its value"}
                    return new_dict



    def valid_query(self, query):

        valid_keys = [
                "id",
                "name",
                "user_gender",
                "hair_color",
                "eye_color",
                "stand",
                "stand_type",
                "stand_image",
                "user_image"
                ]

        keys = [k for k in query]
        values = [v for v in query.values()]

        if all(key in valid_keys for key in keys):
            data = self.get_data(None, keys[0], values[0])
            return data

        else:
            return {"Message": f"Filter key: {keys[0]} is not valid"}


    def test(self):
        for i in self.json:
            if 'Gender' not in i:
                pp.pprint(i)


a = GetData()
a.test()
