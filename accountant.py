class Accountant:

    def __init__(self):
        with open('subaccount_data.csv', 'r') as f:
            self.subaccounts = self.organise([x.strip().split(",") for x in f.readlines()])

    def organise(self, data):
        self.headers = data.pop(0)
        return list(map(lambda x: dict(zip(self.headers, x)), data))

    def siblings(self, **data):
        # siblings are self.subaccounts find where parent_account_id = data['parent_account_id']
        if not self.is_full_record(data):
            data = self.details(**data)[0]
        siblings = list(filter(lambda x: x['parent_account_id'] == data['parent_account_id'], self.subaccounts))
        return siblings

    def parent(self, **data):
        # parent is self.subaccounts find where id = data['parent_account_id']
        if not self.is_full_record(data):
            data = self.details(**data)[0]
        parent = list(filter(lambda x: x['id'] == data['parent_account_id'], self.subaccounts))
        return parent

    def children(self, **data):
        # children are self.subaccounts find where parent_id = data['id']
        if not self.is_full_record(data):
            data = self.details(**data)[0]
        children = list(filter(lambda x: x['parent_account_id'] == data['id'], self.subaccounts))
        return children

    def details(self, **data):
        params = data.keys()
        if len(self.headers) == len(self.headers - params):
            exit(f'EXIT: unknown parameter {params}')

        key = list(params)[0]
        value = str(data[key])

        result = list(filter(lambda x: x[key] == value, self.subaccounts))
        if not result:
            return []
        else:
            return result

    def is_full_record(self, data):
        return list(data.keys()) == self.headers


if __name__ == '__main__':
    A = Accountant()
    details = A.details(**dict(name='Kings Meadows High School'))
    print(details)
    children = A.children(**dict(id=364))
    print(children)
    parent = A.parent(**dict(name='Kings Meadows High School'))
    print(parent)
    parent = A.parent(**dict(id=364))
    print(parent)
    siblings = A.siblings(**dict(name='Kings Meadows High School'))
    # print(siblings)

