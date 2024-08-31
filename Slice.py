def slice(objects, parameters):
    
    if not parameters:
        return objects
    
    if not isinstance(objects, (list, tuple, str)):
        return "TypeError->objects must be a list, tuple, or string"
    
    if isinstance(objects, tuple) or isinstance(objects, str):
        objects = list(objects)
    
    result = []
    
    if len(parameters) == 1:
        st = parameters[0]
        if st < 0:
            st = len(objects) + st
        st = max(st, 0)
        
        for i in range(len(objects)):
            if i >= st:
                result.append(objects[i])
    
    elif len(parameters) == 2:
        st, end = parameters
        if st < 0:
            st = len(objects) + st
        if end < 0:
            end = len(objects) + end
        st = max(st, 0)
        end = min(end, len(objects))
        
        for i in range(len(objects)):
            if st <= i < end:
                result.append(objects[i])
    
    elif len(parameters) == 3:
        st, end, step = parameters
        if step == 0:
            return "ValueError->slice step cannot be zero"
        if st < 0:
            st = len(objects) + st
        if end < 0:
            end = len(objects) + end
        st = max(st, 0)
        end = min(end, len(objects))
        
        if step > 0:
            for i in range(st, end, step):
                result.append(objects[i])
        else:
            for i in range(st, end, step):
                result.append(objects[i])
    
    else:
        return "Invalid parameter"
    
    if isinstance(objects, tuple):
        return tuple(result)
    elif isinstance(objects, str):
        return ''.join(result)
    else:
        return result
