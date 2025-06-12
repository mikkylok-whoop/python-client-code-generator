# DateRange

This exists and is weird because we have APIs that return ranges as semantic strings, which work with Postgres range types.  For instance, the `during` field in the cycle model is given as  \"['2020-08-17T03:42:01.160Z','2020-08-17T12:16:29.582Z')\"  This model makes it so that you can deserialize fields of this type from those strings. When this class is serialized, the strings will be the same.  I would made this Generic, but Pydantic doesn't work with Generics + Python < 3.7, so this base class has upper and lower bounds of type `Any`. Subclasses can override the `upper` and `lower` fields with more specific types, but the elements will be deserialized using the WhoopModel.Config by default.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lower** | **date** |  | [optional] 
**upper** | **date** |  | [optional] 
**lower_bound_type** | [**BoundType**](BoundType.md) |  | [optional] 
**upper_bound_type** | [**BoundType**](BoundType.md) |  | [optional] 

## Example

```python
from openapi_client.models.date_range import DateRange

# TODO update the JSON string below
json = "{}"
# create an instance of DateRange from a JSON string
date_range_instance = DateRange.from_json(json)
# print the JSON string representation of the object
print DateRange.to_json()

# convert the object into a dict
date_range_dict = date_range_instance.to_dict()
# create an instance of DateRange from a dict
date_range_from_dict = DateRange.from_dict(date_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


