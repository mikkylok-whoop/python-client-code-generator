# ModelsApiV1CyclesRequestsCreateMDASCycleRequest

All models should inherit from this. If they have special serialization concerns, they can override Config.  >>> class FunTime(WhoopModel): ...     name: str ...     start_time: datetime.datetime ... >>> d = { ... \"name\": \"yay\", ... \"start_time\": datetime.datetime(2020, 1, 1, hour=0, tzinfo=datetime.timezone.utc), ... \"extraBadField\": 3 ... } >>> FunTime(**d).json() '{\"name\": \"yay\", \"start_time\": \"2020-01-01T00:00:00.000+00:00\"}'

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scaled_strain** | **float** |  | [optional] 
**during** | [**DateTimeTzRange**](DateTimeTzRange.md) |  | 
**predicted_end** | **datetime** |  | [optional] 
**timezone_offset** | **str** |  | 
**days** | [**DateRange**](DateRange.md) |  | 
**data_state** | [**CycleState**](CycleState.md) |  | 
**day_strain** | **float** |  | [optional] 
**day_kilojoules** | **float** |  | [optional] 
**day_avg_heart_rate** | **int** |  | [optional] 
**day_max_heart_rate** | **int** |  | [optional] 
**user_id** | **int** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**cycle_id** | **int** |  | 

## Example

```python
from openapi_client.models.models_api_v1_cycles_requests_create_mdas_cycle_request import ModelsApiV1CyclesRequestsCreateMDASCycleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ModelsApiV1CyclesRequestsCreateMDASCycleRequest from a JSON string
models_api_v1_cycles_requests_create_mdas_cycle_request_instance = ModelsApiV1CyclesRequestsCreateMDASCycleRequest.from_json(json)
# print the JSON string representation of the object
print ModelsApiV1CyclesRequestsCreateMDASCycleRequest.to_json()

# convert the object into a dict
models_api_v1_cycles_requests_create_mdas_cycle_request_dict = models_api_v1_cycles_requests_create_mdas_cycle_request_instance.to_dict()
# create an instance of ModelsApiV1CyclesRequestsCreateMDASCycleRequest from a dict
models_api_v1_cycles_requests_create_mdas_cycle_request_from_dict = ModelsApiV1CyclesRequestsCreateMDASCycleRequest.from_dict(models_api_v1_cycles_requests_create_mdas_cycle_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


