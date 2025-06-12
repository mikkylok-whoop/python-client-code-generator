# ModelsApiV2CyclesResponsesMDASCycle

Data model representing a cycle returned from MDAS APIs

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cycle_id** | **int** |  | 
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

## Example

```python
from openapi_client.models.models_api_v2_cycles_responses_mdas_cycle import ModelsApiV2CyclesResponsesMDASCycle

# TODO update the JSON string below
json = "{}"
# create an instance of ModelsApiV2CyclesResponsesMDASCycle from a JSON string
models_api_v2_cycles_responses_mdas_cycle_instance = ModelsApiV2CyclesResponsesMDASCycle.from_json(json)
# print the JSON string representation of the object
print ModelsApiV2CyclesResponsesMDASCycle.to_json()

# convert the object into a dict
models_api_v2_cycles_responses_mdas_cycle_dict = models_api_v2_cycles_responses_mdas_cycle_instance.to_dict()
# create an instance of ModelsApiV2CyclesResponsesMDASCycle from a dict
models_api_v2_cycles_responses_mdas_cycle_from_dict = ModelsApiV2CyclesResponsesMDASCycle.from_dict(models_api_v2_cycles_responses_mdas_cycle_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


