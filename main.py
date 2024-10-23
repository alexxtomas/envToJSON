import json

def convert_env_to_json(env_file_path, json_file_path):
    env_data = {}
    
    # Read the .env file
    with open(env_file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            # Ignore empty lines and comments
            if line.strip() and not line.startswith('#'):
                key, value = line.strip().split('=', 1)
                # Strip double quotes from the value
                if value.startswith('"') and value.endswith('"'):
                    value = value[1:-1]
                env_data[key] = value
    
    # Convert the dictionary to a JSON string
    json_data = json.dumps(env_data, indent=4)
    
    # Write to a JSON file
    with open(json_file_path, 'w') as json_file:
        json_file.write(json_data)
    
    print(f"Conversion complete! JSON file saved to {json_file_path}")

# Usage example
convert_env_to_json('.env', 'env.json')
