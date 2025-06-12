# ModelsApiV2CyclesRequestsCreateMDASCycleRequest

Representation of a cycle in the MDAS database. Based on https://github.com/WhoopInc/activities-service/blob/4e6bd0353cce859d6923bbb03b53afaf0d075af6/activities-models/src/main/java/com/whoop/activity/model/cycles/CycleIF

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** |  | 
**start_timestamp** | **datetime** |  | 
**end_timestamp** | **datetime** |  | [optional] 
**sleep_need** | **int** |  | [optional] 
**predicted_end** | **datetime** |  | 
**timezone_offset** | **str** |  | 
**start_day** | **date** |  | 
**end_day** | **date** |  | 
**intensity_score** | **float** |  | [optional] 
**data_state** | [**CycleState**](CycleState.md) |  | 
**day_strain** | **float** |  | [optional] 
**day_kilojoules** | **float** |  | [optional] 
**day_avg_heart_rate** | **int** |  | [optional] 
**day_max_heart_rate** | **int** |  | [optional] 
**scaled_strain** | **float** |  | [optional] 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**cycle_id** | **int** |  | 

## Example

```python
from openapi_client.models.models_api_v2_cycles_requests_create_mdas_cycle_request import ModelsApiV2CyclesRequestsCreateMDASCycleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ModelsApiV2CyclesRequestsCreateMDASCycleRequest from a JSON string
models_api_v2_cycles_requests_create_mdas_cycle_request_instance = ModelsApiV2CyclesRequestsCreateMDASCycleRequest.from_json(json)
# print the JSON string representation of the object
print ModelsApiV2CyclesRequestsCreateMDASCycleRequest.to_json()

# convert the object into a dict
models_api_v2_cycles_requests_create_mdas_cycle_request_dict = models_api_v2_cycles_requests_create_mdas_cycle_request_instance.to_dict()
# create an instance of ModelsApiV2CyclesRequestsCreateMDASCycleRequest from a dict
models_api_v2_cycles_requests_create_mdas_cycle_request_from_dict = ModelsApiV2CyclesRequestsCreateMDASCycleRequest.from_dict(models_api_v2_cycles_requests_create_mdas_cycle_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


