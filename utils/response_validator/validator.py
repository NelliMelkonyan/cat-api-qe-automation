from jsonschema import validate
import json

class ResponseValidator():
    def validate_response(self, response, schema_file_path):
        f = open(schema_file_path)
        data = json.load(f)
        f.close()
        validate(instance=response, schema=data)
        