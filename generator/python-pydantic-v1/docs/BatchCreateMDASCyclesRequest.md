# BatchCreateMDASCyclesRequest

All models should inherit from this. If they have special serialization concerns, they can override Config.  >>> class FunTime(WhoopModel): ...     name: str ...     start_time: datetime.datetime ... >>> d = { ... \"name\": \"yay\", ... \"start_time\": datetime.datetime(2020, 1, 1, hour=0, tzinfo=datetime.timezone.utc), ... \"extraBadField\": 3 ... } >>> FunTime(**d).json() '{\"name\": \"yay\", \"start_time\": \"2020-01-01T00:00:00.000+00:00\"}'

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cycles** | [**List[ModelsApiV1CyclesRequestsCreateMDASCycleRequest]**](ModelsApiV1CyclesRequestsCreateMDASCycleRequest.md) |  | 

## Example

```python
from openapi_client.models.batch_create_mdas_cycles_request import BatchCreateMDASCyclesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BatchCreateMDASCyclesRequest from a JSON string
batch_create_mdas_cycles_request_instance = BatchCreateMDASCyclesRequest.from_json(json)
# print the JSON string representation of the object
print BatchCreateMDASCyclesRequest.to_json()

# convert the object into a dict
batch_create_mdas_cycles_request_dict = batch_create_mdas_cycles_request_instance.to_dict()
# create an instance of BatchCreateMDASCyclesRequest from a dict
batch_create_mdas_cycles_request_from_dict = BatchCreateMDASCyclesRequest.from_dict(batch_create_mdas_cycles_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


