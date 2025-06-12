# ModelsApiV2RecoveriesResponsesMDASRecovery

All models should inherit from this. If they have special serialization concerns, they can override Config.  >>> class FunTime(WhoopModel): ...     name: str ...     start_time: datetime.datetime ... >>> d = { ... \"name\": \"yay\", ... \"start_time\": datetime.datetime(2020, 1, 1, hour=0, tzinfo=datetime.timezone.utc), ... \"extraBadField\": 3 ... } >>> FunTime(**d).json() '{\"name\": \"yay\", \"start_time\": \"2020-01-01T00:00:00.000+00:00\"}'

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recovery_id** | **str** |  | 
**user_id** | **int** |  | 
**version** | **int** |  | [optional] 
**cycle_id** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**start_timestamp** | **datetime** |  | 
**end_timestamp** | **datetime** |  | 
**score** | **int** |  | 
**is_normal** | **bool** |  | [optional] 
**quality_duration** | **int** |  | [optional] 
**latency** | **int** |  | [optional] 
**is_significant** | **bool** |  | [optional] 
**debt_pre** | **float** |  | [optional] 
**debt_post** | **float** |  | [optional] 
**need_from_strain** | **float** |  | [optional] 
**sleep_need** | **float** |  | [optional] 
**habitual_sleep_need** | **float** |  | [optional] 
**disturbances** | **int** |  | [optional] 
**time_in_bed** | **float** |  | [optional] 
**light_sleep_duration** | **int** |  | [optional] 
**slow_wave_sleep_duration** | **int** |  | [optional] 
**rem_sleep_duration** | **int** |  | [optional] 
**cycles_count** | **int** |  | [optional] 
**wake_duration** | **int** |  | [optional] 
**arousal_time** | **float** |  | [optional] 
**no_data_duration** | **int** |  | [optional] 
**in_sleep_efficiency** | **float** |  | [optional] 
**credit_from_naps** | **float** |  | [optional] 
**respiratory_rate** | **float** |  | [optional] 
**skin_temp_celsius** | **float** |  | [optional] 
**history_size** | **float** |  | [optional] 
**spo2** | **float** |  | [optional] 
**algo_version** | **str** |  | [optional] 
**projected_score** | **float** |  | [optional] 
**projected_sleep** | **float** |  | [optional] 
**sleep_consistency** | **float** |  | [optional] 
**total_wake_events** | **int** |  | [optional] 
**optimal_sleep_time_start** | **datetime** |  | [optional] 
**optimal_sleep_time_end** | **datetime** |  | [optional] 
**recovery_score** | **int** |  | [optional] 
**resting_heart_rate** | **int** |  | [optional] 
**hrv_rmssd** | **float** |  | [optional] 
**is_calibrating** | **bool** |  | [optional] 
**rhr_component** | **float** |  | [optional] 
**hrv_component** | **float** |  | [optional] 
**recovery_rate** | **float** |  | [optional] 
**hr_baseline** | **float** |  | [optional] 
**score_state** | **str** |  | [optional] 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from openapi_client.models.models_api_v2_recoveries_responses_mdas_recovery import ModelsApiV2RecoveriesResponsesMDASRecovery

# TODO update the JSON string below
json = "{}"
# create an instance of ModelsApiV2RecoveriesResponsesMDASRecovery from a JSON string
models_api_v2_recoveries_responses_mdas_recovery_instance = ModelsApiV2RecoveriesResponsesMDASRecovery.from_json(json)
# print the JSON string representation of the object
print ModelsApiV2RecoveriesResponsesMDASRecovery.to_json()

# convert the object into a dict
models_api_v2_recoveries_responses_mdas_recovery_dict = models_api_v2_recoveries_responses_mdas_recovery_instance.to_dict()
# create an instance of ModelsApiV2RecoveriesResponsesMDASRecovery from a dict
models_api_v2_recoveries_responses_mdas_recovery_from_dict = ModelsApiV2RecoveriesResponsesMDASRecovery.from_dict(models_api_v2_recoveries_responses_mdas_recovery_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


