import json

def find_json_paths(data, target_key : str, current_path : str = "") -> list:
    paths = []
    
    # If the current data is a Dictionary (JSON Object)
    if isinstance(data, dict):
        for key, value in data.items():
            # Build the dot-notation path
            new_path = f"{current_path}.{key}" if current_path else key
            
            # If we found the key, add it to our list
            if key == target_key:
                paths.append(new_path)
                
            # Keep digging deeper
            paths.extend(find_json_paths(value, target_key, new_path))
            
    # If the current data is a List (JSON Array)
    elif isinstance(data, list):
        for index, item in enumerate(data):
            # Use bracket notation for arrays
            new_path = f"{current_path}[{index}]"
            paths.extend(find_json_paths(item, target_key, new_path))
            
    return paths


target = "FreeFormNumber"
with open("smt.json", "r") as f:
    json_data = json.load(f)
results = find_json_paths(json_data, target)

exists = []
for path in results:
    start = path.find("[")
    if start != -1:
        end = path.find("]", start)
        path = path[:start] + "*"+ path[end+2:]
    if path not in exists:
        print(path)
    exists.append(path)


some = "QueryResponse.Customer*Fax.FreeFormNumber"
i, j = some.split("*")
print(i)
print(j)