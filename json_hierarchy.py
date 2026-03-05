import json
# import big_o

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
    
    exists = []
    new_paths = []
    for path in paths:
        start = path.find("[")
        if start != -1:
            end = path.find("]", start)
            path = path[:start] + "*"+ path[end+2:]
        if path not in exists:
            new_paths.append(path)
        exists.append(path)
            
    return new_paths


target = "FreeFormNumber"
with open("smt.json", "r") as f:
    json_data = json.load(f)
results = find_json_paths(json_data, target)
for r in results: print(r)


# # 1. Define a data generator that creates a nested dict with N keys
# def json_generator(n):
#     return {f"key_{i}": "value" for i in range(n)}

# # 2. Run the complexity analysis
# # We pass 'key_0' as the target_key to ensure the function has work to do
# best, others = big_o.big_o(
#     lambda data: find_json_paths(data, "key_0"), 
#     json_generator, 
#     max_n=1000, 
#     n_repeats=10
# )

# print(best)