# UpdateMDASRecoveryRequestV2

All models should inherit from this. If they have special serialization concerns, they can override Config.  >>> class FunTime(WhoopModel): ...     name: str ...     start_time: datetime.datetime ... >>> d = { ... \"name\": \"yay\", ... \"start_time\": datetime.datetime(2020, 1, 1, hour=0, tzinfo=datetime.timezone.utc), ... \"extraBadField\": 3 ... } >>> FunTime(**d).json() '{\"name\": \"yay\", \"start_time\": \"2020-01-01T00:00:00.000+00:00\"}'

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
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
**algo_version** | **str** |  | [optional] 
**projected_score** | **float** |  | [optional] 
**projected_sleep** | **float** |  | [optional] 
**sleep_consistency** | **float** |  | [optional] 
**skin_temp_celsius** | **float** |  | [optional] 
**spo2** | **float** |  | [optional] 
**total_wake_events** | **int** |  | [optional] 
**optimal_sleep_time_start** | **datetime** |  | [optional] 
**optimal_sleep_time_end** | **datetime** |  | [optional] 
**recovery_score** | **int** |  | [optional] 
**resting_heart_rate** | **int** |  | [optional] 
**hrv_rmssd** | **float** |  | [optional] 
**history_size** | **float** |  | [optional] 
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
from openapi_client.models.update_mdas_recovery_request_v2 import UpdateMDASRecoveryRequestV2

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateMDASRecoveryRequestV2 from a JSON string
update_mdas_recovery_request_v2_instance = UpdateMDASRecoveryRequestV2.from_json(json)
# print the JSON string representation of the object
print UpdateMDASRecoveryRequestV2.to_json()

# convert the object into a dict
update_mdas_recovery_request_v2_dict = update_mdas_recovery_request_v2_instance.to_dict()
# create an instance of UpdateMDASRecoveryRequestV2 from a dict
update_mdas_recovery_request_v2_from_dict = UpdateMDASRecoveryRequestV2.from_dict(update_mdas_recovery_request_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


