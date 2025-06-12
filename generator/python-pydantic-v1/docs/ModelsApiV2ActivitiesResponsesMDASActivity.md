# ModelsApiV2ActivitiesResponsesMDASActivity

All models should inherit from this. If they have special serialization concerns, they can override Config.  >>> class FunTime(WhoopModel): ...     name: str ...     start_time: datetime.datetime ... >>> d = { ... \"name\": \"yay\", ... \"start_time\": datetime.datetime(2020, 1, 1, hour=0, tzinfo=datetime.timezone.utc), ... \"extraBadField\": 3 ... } >>> FunTime(**d).json() '{\"name\": \"yay\", \"start_time\": \"2020-01-01T00:00:00.000+00:00\"}'

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity_id** | **str** |  | 
**user_id** | **int** |  | 
**start_timestamp** | **datetime** |  | 
**end_timestamp** | **datetime** |  | 
**timezone** | **str** |  | [optional] 
**timezone_offset** | **str** |  | [optional] 
**source** | [**ActivitySource**](ActivitySource.md) |  | 
**score_state** | [**ScoreState**](ScoreState.md) |  | 
**score_type** | [**ScoreType**](ScoreType.md) |  | 
**type** | **str** |  | 
**source_id** | **str** |  | [optional] 
**version** | **int** |  | 
**cycle_id** | **int** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from openapi_client.models.models_api_v2_activities_responses_mdas_activity import ModelsApiV2ActivitiesResponsesMDASActivity

# TODO update the JSON string below
json = "{}"
# create an instance of ModelsApiV2ActivitiesResponsesMDASActivity from a JSON string
models_api_v2_activities_responses_mdas_activity_instance = ModelsApiV2ActivitiesResponsesMDASActivity.from_json(json)
# print the JSON string representation of the object
print ModelsApiV2ActivitiesResponsesMDASActivity.to_json()

# convert the object into a dict
models_api_v2_activities_responses_mdas_activity_dict = models_api_v2_activities_responses_mdas_activity_instance.to_dict()
# create an instance of ModelsApiV2ActivitiesResponsesMDASActivity from a dict
models_api_v2_activities_responses_mdas_activity_from_dict = ModelsApiV2ActivitiesResponsesMDASActivity.from_dict(models_api_v2_activities_responses_mdas_activity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


