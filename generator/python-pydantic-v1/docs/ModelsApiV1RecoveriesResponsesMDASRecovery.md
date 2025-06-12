# ModelsApiV1RecoveriesResponsesMDASRecovery

All models should inherit from this. If they have special serialization concerns, they can override Config.  >>> class FunTime(WhoopModel): ...     name: str ...     start_time: datetime.datetime ... >>> d = { ... \"name\": \"yay\", ... \"start_time\": datetime.datetime(2020, 1, 1, hour=0, tzinfo=datetime.timezone.utc), ... \"extraBadField\": 3 ... } >>> FunTime(**d).json() '{\"name\": \"yay\", \"start_time\": \"2020-01-01T00:00:00.000+00:00\"}'

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recovery_id** | **int** |  | 
**quality_duration** | **int** |  | [optional] 
**sleep_score** | **int** |  | [optional] 
**is_nap** | **bool** |  | [optional] 
**var_date** | **datetime** |  | 
**user_id** | **int** |  | 
**sleep_id** | **int** |  | 
**cycle_id** | **int** |  | [optional] 
**recovery_score** | **int** |  | [optional] 
**resting_heart_rate** | **int** |  | [optional] 
**hrv_rmssd** | **float** |  | [optional] 
**activity_state** | [**ActivityState**](ActivityState.md) |  | [optional] 
**is_calibrating** | **bool** |  | [optional] 
**prod_covid** | **float** |  | [optional] 
**hr_baseline** | **float** |  | [optional] 
**skin_temp_celsius** | **float** |  | [optional] 
**spo2** | **float** |  | [optional] 
**algo_version** | **str** |  | [optional] 
**rhr_component** | **float** |  | [optional] 
**hrv_component** | **float** |  | [optional] 
**is_normal** | **bool** |  | [optional] 
**history_size** | **float** |  | [optional] 
**recovery_rate** | **float** |  | [optional] 
**kilojoules** | **float** |  | [optional] 
**during** | [**DateTimeTzRange**](DateTimeTzRange.md) |  | 
**timezone_offset** | **str** |  | [optional] 
**timezone** | **str** |  | [optional] 
**survey_response_id** | **int** |  | [optional] 
**percent_recorded** | **float** |  | [optional] 
**is_responded** | **bool** |  | [optional] 
**activity_source** | [**ActivitySource**](ActivitySource.md) |  | [optional] 
**score** | **int** |  | 
**latency** | **int** |  | [optional] 
**is_significant** | **bool** |  | [optional] 
**debt_pre** | **float** |  | [optional] 
**debt_post** | **float** |  | [optional] 
**need_from_strain** | **float** |  | [optional] 
**sleep_need** | **float** |  | [optional] 
**habitual_sleep_need** | **float** |  | [optional] 
**disturbances** | **float** |  | [optional] 
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
**sleep_consistency** | **float** |  | [optional] 
**projected_score** | **float** |  | [optional] 
**projected_sleep** | **float** |  | [optional] 
**optimal_sleep_times** | [**DateTimeTzRange**](DateTimeTzRange.md) |  | [optional] 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from openapi_client.models.models_api_v1_recoveries_responses_mdas_recovery import ModelsApiV1RecoveriesResponsesMDASRecovery

# TODO update the JSON string below
json = "{}"
# create an instance of ModelsApiV1RecoveriesResponsesMDASRecovery from a JSON string
models_api_v1_recoveries_responses_mdas_recovery_instance = ModelsApiV1RecoveriesResponsesMDASRecovery.from_json(json)
# print the JSON string representation of the object
print ModelsApiV1RecoveriesResponsesMDASRecovery.to_json()

# convert the object into a dict
models_api_v1_recoveries_responses_mdas_recovery_dict = models_api_v1_recoveries_responses_mdas_recovery_instance.to_dict()
# create an instance of ModelsApiV1RecoveriesResponsesMDASRecovery from a dict
models_api_v1_recoveries_responses_mdas_recovery_from_dict = ModelsApiV1RecoveriesResponsesMDASRecovery.from_dict(models_api_v1_recoveries_responses_mdas_recovery_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


