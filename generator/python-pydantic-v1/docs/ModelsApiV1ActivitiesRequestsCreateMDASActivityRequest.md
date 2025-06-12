# ModelsApiV1ActivitiesRequestsCreateMDASActivityRequest

All models should inherit from this. If they have special serialization concerns, they can override Config.  >>> class FunTime(WhoopModel): ...     name: str ...     start_time: datetime.datetime ... >>> d = { ... \"name\": \"yay\", ... \"start_time\": datetime.datetime(2020, 1, 1, hour=0, tzinfo=datetime.timezone.utc), ... \"extraBadField\": 3 ... } >>> FunTime(**d).json() '{\"name\": \"yay\", \"start_time\": \"2020-01-01T00:00:00.000+00:00\"}'

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity_v1_id** | **int** |  | 
**version** | **int** |  | 
**cycle_id** | **int** |  | 
**score_type** | [**ScoreType**](ScoreType.md) |  | 
**user_id** | **int** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**timezone** | **str** |  | [optional] 
**timezone_offset** | **str** |  | [optional] 
**activity_source** | [**ActivitySource**](ActivitySource.md) |  | [optional] 
**score_state** | [**ScoreState**](ScoreState.md) |  | 
**activity_type** | **str** |  | 
**source_id** | **str** |  | [optional] 
**gps_enabled** | **bool** |  | [optional] 
**during** | [**DateTimeTzRange**](DateTimeTzRange.md) |  | 
**activity_id** | **str** |  | 

## Example

```python
from openapi_client.models.models_api_v1_activities_requests_create_mdas_activity_request import ModelsApiV1ActivitiesRequestsCreateMDASActivityRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ModelsApiV1ActivitiesRequestsCreateMDASActivityRequest from a JSON string
models_api_v1_activities_requests_create_mdas_activity_request_instance = ModelsApiV1ActivitiesRequestsCreateMDASActivityRequest.from_json(json)
# print the JSON string representation of the object
print ModelsApiV1ActivitiesRequestsCreateMDASActivityRequest.to_json()

# convert the object into a dict
models_api_v1_activities_requests_create_mdas_activity_request_dict = models_api_v1_activities_requests_create_mdas_activity_request_instance.to_dict()
# create an instance of ModelsApiV1ActivitiesRequestsCreateMDASActivityRequest from a dict
models_api_v1_activities_requests_create_mdas_activity_request_from_dict = ModelsApiV1ActivitiesRequestsCreateMDASActivityRequest.from_dict(models_api_v1_activities_requests_create_mdas_activity_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


