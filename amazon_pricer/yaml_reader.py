import yaml


class YamlReader:
    def __init__(self, pathfile: str):
        self.source = pathfile

    def reader(self):
        with open(self.source, "r") as yamlfile:
            data = yaml.load(yamlfile, Loader=yaml.FullLoader)
        return data

    def get_elements(self):
        all_items = []
        data = self.reader()
        for item in data:
            item_dict = list(item.values())[0]
            item_dict["name"] = list(item.keys())[0]
            all_items.append(item_dict)
        return all_items

    def add_new_prices(self, price: float, idx: int):
        data = self.reader()
        if price is not None:
            for _, value in data[idx].items():
                value["current_price"] = price

        with open(self.source, "w") as f:
            yaml.dump(data, f)
