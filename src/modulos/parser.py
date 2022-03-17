import numpy as np

def parser(request):
    data = request.get_json(force=True)
    data = dict(data)
    values = []
    for key in data:
        values.append(data[key])
    values = np.array(values).reshape(1, -1) 

    return values