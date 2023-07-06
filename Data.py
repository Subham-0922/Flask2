data=[];

def addData(obj):
    data.append(obj)
def removeData(id):
    existingId=None;
    fl=True;
    for i in data:
        if i.get('Id')==id:
            fl=False
            existingId=i;
            data.remove(i)
    if fl:
         'Not Found'
    else:
        return existingId
def isAvailableAndGetIndex(id):
    # print('I m in Data')
    print(data)
    for i in range(len(data)):
        print(i, ' ->  ', id)
        if data[i].get('Id') == id:
            print('found')
            return i
    print('not found')
    return False

