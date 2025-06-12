# ModelsApiV2ActivitiesRequestsCreateMDASActivityRequest

Base class for MDA activities request.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** |  | 
**start_timestamp** | **datetime** |  | 
**end_timestamp** | **datetime** |  | 
**timezone** | **str** |  | [optional] 
**timezone_offset** | **str** |  | [optional] 
**source** | [**ActivitySource**](ActivitySource.md) |  | 
**score_state** | [**ScoreState**](ScoreState.md) |  | 
**type** | **str** |  | 
**score_type** | [**ScoreType**](ScoreType.md) |  | 
**source_id** | **str** |  | [optional] 
**version** | **int** |  | 
**cycle_id** | **int** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**activity_id** | **str** |  | 

## Example

```python
from openapi_client.models.models_api_v2_activities_requests_create_mdas_activity_request import ModelsApiV2ActivitiesRequestsCreateMDASActivityRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ModelsApiV2ActivitiesRequestsCreateMDASActivityRequest from a JSON string
models_api_v2_activities_requests_create_mdas_activity_request_instance = ModelsApiV2ActivitiesRequestsCreateMDASActivityRequest.from_json(json)
# print the JSON string representation of the object
print ModelsApiV2ActivitiesRequestsCreateMDASActivityRequest.to_json()

# convert the object into a dict
models_api_v2_activities_requests_create_mdas_activity_request_dict = models_api_v2_activities_requests_create_mdas_activity_request_instance.to_dict()
# create an instance of ModelsApiV2ActivitiesRequestsCreateMDASActivityRequest from a dict
models_api_v2_activities_requests_create_mdas_activity_request_from_dict = ModelsApiV2ActivitiesRequestsCreateMDASActivityRequest.from_dict(models_api_v2_activities_requests_create_mdas_activity_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


