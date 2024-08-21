import argparse
import json
import os
from typing import Dict


def get_args():
    parser = argparse.ArgumentParser(
        description="Read a geojson and create from it a create and a modify geojson"
    )
    parser.add_argument("geojson", type=str, help="Path of the input geojson")
    return parser.parse_args()


def get_path(geojson_path: str, action: str):
    """
    Get the path of the action file by suffixing a geojson path by an action
    :param geojson_path: The file which will be suffixed
    :param action: The value of the suffix
    """
    file_and_extension = os.path.basename(geojson_path).split(".")
    new_file = f"{'.'.join(file_and_extension[:-1])}_{action}.{file_and_extension[-1]}"
    return os.path.join(os.path.dirname(geojson_path), new_file)


def extract_subdataset(data: Dict, action: str) -> Dict:
    """
    Extract a new dataset by filtering on properties.action
    :param data: The dataset to filter
    :param action: The value of the properties.action filter
    """
    res = list(filter(lambda e: e["properties"]["action"] == action, data["features"]))
    return {"features": res, "type": "FeatureCollection"}


def split_and_create(geojson_path: str):
    with open(geojson_path, "r") as f:
        data = json.load(f)

    for action in ["create", "modify"]:
        action_path = get_path(geojson_path, action)
        with open(action_path, "w") as f:
            action_dataset = extract_subdataset(data, action)
            json.dump(action_dataset, f, indent=1)
            print(f"{action_path} created ({len(action_dataset['features'])} elements)")


if __name__ == "__main__":
    args = get_args()
    split_and_create(args.geojson)
