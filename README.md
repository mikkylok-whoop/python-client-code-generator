# Python client code generator

Templates to generate python client code

# How to run

1. Install OpenAPI Generator (via Homebrew)
```bash
brew install openapi-generator
```
2. Navigate to the project directory and open the `generate_build_client.sh` script
```bash
cd python-client-code-generator/
```
3. Adjust the version number and paths in `generate_build_client.sh` as needed
```bash
VERSION="<Replace with version number>"
WORKSPACE_DIR="<Replace with your own directory>/python-client-code-generator"
PACKAGE_OUTPUT_DIR="<Replace with your own pacakge output directory>"
```
4. Run the generation script
```bash
sh generate_build_client.sh
```
Note: The script performs the following steps:
- Step 1: Generate the client code using OpenAPI Generator
- Step 2: Set up the Poetry environment and install dependencies
- Step 3: Run linters and type checkers
- Step 4: Build the package (.whl)

# Usage of the Generated Client
1. Create a new project and include a `test_client.py` script:
```Python
"""
Test script for the OpenAPI client.
"""
from datetime import datetime, timedelta
from data_sci_mdas.api.activities_api import ActivitiesApi

def main():
    base_uri = "https://api-internal.dev.whoop.com/"
    activities_api = ActivitiesApi(uri=base_uri)

    user_id = 26040355
    start_date = datetime.fromisoformat("2025-04-30T19:02:07.777+00:00")
    end_date = datetime.fromisoformat("2025-06-01T19:02:07.777+00:00")
    
    print(f"Fetching data for user {user_id} from {start_date} to {end_date}")
    
    try:
        print("Fetching activities...")
        activities = activities_api.get_activities_in_range_for_user_data_sci_mdas_v2_activities_get(
            user_id=user_id,
            start=start_date,
            end=end_date
        )
        print(f"Found {len(activities)} activities")
    except Exception as e:
        print(f"Error occurred: {e}")


if __name__ == "__main__":
    main() 
```
2. Navigate to your new project directory
3. (Optional but recommended) Set up a virtual environment:
```bash
python -m venv venv
source venv/bin/activate
```
4. Install the generated Poetry package
```bash
pip install <Replace with your own pacakge output directory>/dist/data_sci_mdas-<VERSION>-py3-none-any.whl
```
3. Run the test script
```bash
python test_client.py
```
