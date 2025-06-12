# openapi_client.CyclesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**batch_create_cycles_data_sci_mdas_v1_cycles_batch_post**](CyclesApi.md#batch_create_cycles_data_sci_mdas_v1_cycles_batch_post) | **POST** /data-sci-mdas/v1/cycles/batch | Batch Create Cycles
[**create_cycle_data_sci_mdas_v1_cycles_post**](CyclesApi.md#create_cycle_data_sci_mdas_v1_cycles_post) | **POST** /data-sci-mdas/v1/cycles | Create Cycle
[**create_cycle_data_sci_mdas_v2_cycles_post**](CyclesApi.md#create_cycle_data_sci_mdas_v2_cycles_post) | **POST** /data-sci-mdas/v2/cycles | Create Cycle
[**delete_cycle_data_sci_mdas_v1_cycles_cycle_id_delete**](CyclesApi.md#delete_cycle_data_sci_mdas_v1_cycles_cycle_id_delete) | **DELETE** /data-sci-mdas/v1/cycles/{cycle_id} | Delete Cycle
[**delete_cycle_data_sci_mdas_v2_cycles_cycle_id_delete**](CyclesApi.md#delete_cycle_data_sci_mdas_v2_cycles_cycle_id_delete) | **DELETE** /data-sci-mdas/v2/cycles/{cycle_id} | Delete Cycle
[**get_cycles_in_range_for_user_data_sci_mdas_v1_cycles_get**](CyclesApi.md#get_cycles_in_range_for_user_data_sci_mdas_v1_cycles_get) | **GET** /data-sci-mdas/v1/cycles | Get Cycles In Range For User
[**get_cycles_in_range_for_user_data_sci_mdas_v2_cycles_get**](CyclesApi.md#get_cycles_in_range_for_user_data_sci_mdas_v2_cycles_get) | **GET** /data-sci-mdas/v2/cycles | Get Cycles In Range For User
[**update_cycle_data_sci_mdas_v1_cycles_cycle_id_put**](CyclesApi.md#update_cycle_data_sci_mdas_v1_cycles_cycle_id_put) | **PUT** /data-sci-mdas/v1/cycles/{cycle_id} | Update Cycle
[**update_cycle_data_sci_mdas_v2_cycles_cycle_id_put**](CyclesApi.md#update_cycle_data_sci_mdas_v2_cycles_cycle_id_put) | **PUT** /data-sci-mdas/v2/cycles/{cycle_id} | Update Cycle


# **batch_create_cycles_data_sci_mdas_v1_cycles_batch_post**
> object batch_create_cycles_data_sci_mdas_v1_cycles_batch_post(batch_create_mdas_cycles_request)

Batch Create Cycles

POST endpoint to create multiple cycle events
Note: This endpoint is for internal application use only. External customers should use the GET endpoints instead.

Args:
    batch_create_cycles_request: Multiple cycle events
    cycles_dao: CyclesDAO instance

Returns: None

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.batch_create_mdas_cycles_request import BatchCreateMDASCyclesRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CyclesApi(api_client)
    batch_create_mdas_cycles_request = openapi_client.BatchCreateMDASCyclesRequest() # BatchCreateMDASCyclesRequest | 

    try:
        # Batch Create Cycles
        api_response = api_instance.batch_create_cycles_data_sci_mdas_v1_cycles_batch_post(batch_create_mdas_cycles_request)
        print("The response of CyclesApi->batch_create_cycles_data_sci_mdas_v1_cycles_batch_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CyclesApi->batch_create_cycles_data_sci_mdas_v1_cycles_batch_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_create_mdas_cycles_request** | [**BatchCreateMDASCyclesRequest**](BatchCreateMDASCyclesRequest.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_cycle_data_sci_mdas_v1_cycles_post**
> object create_cycle_data_sci_mdas_v1_cycles_post(models_api_v1_cycles_requests_create_mdas_cycle_request)

Create Cycle

POST endpoint to create a new cycle event
Note: This endpoint is for internal application use only. External customers should use the GET endpoints instead.

Args:
    create_cycle_request: Cycle event data
    cycles_dao: CyclesDAO instance

Returns: None

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.models_api_v1_cycles_requests_create_mdas_cycle_request import ModelsApiV1CyclesRequestsCreateMDASCycleRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CyclesApi(api_client)
    models_api_v1_cycles_requests_create_mdas_cycle_request = openapi_client.ModelsApiV1CyclesRequestsCreateMDASCycleRequest() # ModelsApiV1CyclesRequestsCreateMDASCycleRequest | 

    try:
        # Create Cycle
        api_response = api_instance.create_cycle_data_sci_mdas_v1_cycles_post(models_api_v1_cycles_requests_create_mdas_cycle_request)
        print("The response of CyclesApi->create_cycle_data_sci_mdas_v1_cycles_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CyclesApi->create_cycle_data_sci_mdas_v1_cycles_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **models_api_v1_cycles_requests_create_mdas_cycle_request** | [**ModelsApiV1CyclesRequestsCreateMDASCycleRequest**](ModelsApiV1CyclesRequestsCreateMDASCycleRequest.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_cycle_data_sci_mdas_v2_cycles_post**
> object create_cycle_data_sci_mdas_v2_cycles_post(models_api_v2_cycles_requests_create_mdas_cycle_request)

Create Cycle

POST endpoint to create a new cycle event
Note: This endpoint is for internal application use only. External customers should use the GET endpoints instead.

Args:
    create_cycle_request: Cycle event data
    cycles_dao: CyclesDAO instance

Returns: None

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.models_api_v2_cycles_requests_create_mdas_cycle_request import ModelsApiV2CyclesRequestsCreateMDASCycleRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CyclesApi(api_client)
    models_api_v2_cycles_requests_create_mdas_cycle_request = openapi_client.ModelsApiV2CyclesRequestsCreateMDASCycleRequest() # ModelsApiV2CyclesRequestsCreateMDASCycleRequest | 

    try:
        # Create Cycle
        api_response = api_instance.create_cycle_data_sci_mdas_v2_cycles_post(models_api_v2_cycles_requests_create_mdas_cycle_request)
        print("The response of CyclesApi->create_cycle_data_sci_mdas_v2_cycles_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CyclesApi->create_cycle_data_sci_mdas_v2_cycles_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **models_api_v2_cycles_requests_create_mdas_cycle_request** | [**ModelsApiV2CyclesRequestsCreateMDASCycleRequest**](ModelsApiV2CyclesRequestsCreateMDASCycleRequest.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_cycle_data_sci_mdas_v1_cycles_cycle_id_delete**
> object delete_cycle_data_sci_mdas_v1_cycles_cycle_id_delete(cycle_id)

Delete Cycle

DELETE endpoint to delete a recovery event
Note: This endpoint is for internal application use only. External customers should use the GET endpoints instead.

Args:
    cycle_id: ID of the cycle event
    cycles_dao: CyclesDAO instance

Returns: None

### Example

```python
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CyclesApi(api_client)
    cycle_id = 56 # int | 

    try:
        # Delete Cycle
        api_response = api_instance.delete_cycle_data_sci_mdas_v1_cycles_cycle_id_delete(cycle_id)
        print("The response of CyclesApi->delete_cycle_data_sci_mdas_v1_cycles_cycle_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CyclesApi->delete_cycle_data_sci_mdas_v1_cycles_cycle_id_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cycle_id** | **int**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_cycle_data_sci_mdas_v2_cycles_cycle_id_delete**
> object delete_cycle_data_sci_mdas_v2_cycles_cycle_id_delete(cycle_id)

Delete Cycle

DELETE endpoint to delete a recovery event
Note: This endpoint is for internal application use only. External customers should use the GET endpoints instead.

Args:
    cycle_id: ID of the cycle event
    cycles_dao: CyclesDAO instance

Returns: None

### Example

```python
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CyclesApi(api_client)
    cycle_id = 56 # int | 

    try:
        # Delete Cycle
        api_response = api_instance.delete_cycle_data_sci_mdas_v2_cycles_cycle_id_delete(cycle_id)
        print("The response of CyclesApi->delete_cycle_data_sci_mdas_v2_cycles_cycle_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CyclesApi->delete_cycle_data_sci_mdas_v2_cycles_cycle_id_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cycle_id** | **int**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cycles_in_range_for_user_data_sci_mdas_v1_cycles_get**
> List[ModelsApiV1CyclesResponsesMDASCycle] get_cycles_in_range_for_user_data_sci_mdas_v1_cycles_get(user_id, start, end)

Get Cycles In Range For User

GET endpoint to retrieve all cycle events for a user during a specified time range
Args:
    user_id: ID of the user
    start: Start of the time range to get cycle events for
    end: End of time range to get cycle events for
    cycles_dao: CyclesDAO instance

Returns: List of cycle event data

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.models_api_v1_cycles_responses_mdas_cycle import ModelsApiV1CyclesResponsesMDASCycle
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CyclesApi(api_client)
    user_id = 56 # int | 
    start = '2013-10-20T19:20:30+01:00' # datetime | 
    end = '2013-10-20T19:20:30+01:00' # datetime | 

    try:
        # Get Cycles In Range For User
        api_response = api_instance.get_cycles_in_range_for_user_data_sci_mdas_v1_cycles_get(user_id, start, end)
        print("The response of CyclesApi->get_cycles_in_range_for_user_data_sci_mdas_v1_cycles_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CyclesApi->get_cycles_in_range_for_user_data_sci_mdas_v1_cycles_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 
 **start** | **datetime**|  | 
 **end** | **datetime**|  | 

### Return type

[**List[ModelsApiV1CyclesResponsesMDASCycle]**](ModelsApiV1CyclesResponsesMDASCycle.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cycles_in_range_for_user_data_sci_mdas_v2_cycles_get**
> List[ModelsApiV2CyclesResponsesMDASCycle] get_cycles_in_range_for_user_data_sci_mdas_v2_cycles_get(user_id, start, end)

Get Cycles In Range For User

GET endpoint to retrieve all cycle events for a user during a specified time range
Args:
    user_id: ID of the user
    start: Start of the time range to get cycle events for
    end: End of time range to get cycle events for
    cycles_dao: CyclesDAO instance

Returns: List of cycle event data

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.models_api_v2_cycles_responses_mdas_cycle import ModelsApiV2CyclesResponsesMDASCycle
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CyclesApi(api_client)
    user_id = 56 # int | 
    start = '2013-10-20T19:20:30+01:00' # datetime | 
    end = '2013-10-20T19:20:30+01:00' # datetime | 

    try:
        # Get Cycles In Range For User
        api_response = api_instance.get_cycles_in_range_for_user_data_sci_mdas_v2_cycles_get(user_id, start, end)
        print("The response of CyclesApi->get_cycles_in_range_for_user_data_sci_mdas_v2_cycles_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CyclesApi->get_cycles_in_range_for_user_data_sci_mdas_v2_cycles_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 
 **start** | **datetime**|  | 
 **end** | **datetime**|  | 

### Return type

[**List[ModelsApiV2CyclesResponsesMDASCycle]**](ModelsApiV2CyclesResponsesMDASCycle.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cycle_data_sci_mdas_v1_cycles_cycle_id_put**
> object update_cycle_data_sci_mdas_v1_cycles_cycle_id_put(cycle_id, models_api_v1_cycles_requests_update_mdas_cycle_request)

Update Cycle

PUT endpoint for updating an existing cycle event
Note: This endpoint is for internal application use only. External customers should use the GET endpoints instead.

Args:
    cycle_id: ID of the cycle event
    update_cycles_request: Cycle event data
    cycles_dao: CyclesDAO instance

Returns: None

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.models_api_v1_cycles_requests_update_mdas_cycle_request import ModelsApiV1CyclesRequestsUpdateMDASCycleRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CyclesApi(api_client)
    cycle_id = 56 # int | 
    models_api_v1_cycles_requests_update_mdas_cycle_request = openapi_client.ModelsApiV1CyclesRequestsUpdateMDASCycleRequest() # ModelsApiV1CyclesRequestsUpdateMDASCycleRequest | 

    try:
        # Update Cycle
        api_response = api_instance.update_cycle_data_sci_mdas_v1_cycles_cycle_id_put(cycle_id, models_api_v1_cycles_requests_update_mdas_cycle_request)
        print("The response of CyclesApi->update_cycle_data_sci_mdas_v1_cycles_cycle_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CyclesApi->update_cycle_data_sci_mdas_v1_cycles_cycle_id_put: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cycle_id** | **int**|  | 
 **models_api_v1_cycles_requests_update_mdas_cycle_request** | [**ModelsApiV1CyclesRequestsUpdateMDASCycleRequest**](ModelsApiV1CyclesRequestsUpdateMDASCycleRequest.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cycle_data_sci_mdas_v2_cycles_cycle_id_put**
> object update_cycle_data_sci_mdas_v2_cycles_cycle_id_put(cycle_id, models_api_v2_cycles_requests_update_mdas_cycle_request)

Update Cycle

PUT endpoint for updating an existing cycle event
Note: This endpoint is for internal application use only. External customers should use the GET endpoints instead.

Args:
    cycle_id: ID of the cycle event
    update_cycles_request: Cycle event data
    cycles_dao: CyclesDAO instance

Returns: None

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.models_api_v2_cycles_requests_update_mdas_cycle_request import ModelsApiV2CyclesRequestsUpdateMDASCycleRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CyclesApi(api_client)
    cycle_id = 56 # int | 
    models_api_v2_cycles_requests_update_mdas_cycle_request = openapi_client.ModelsApiV2CyclesRequestsUpdateMDASCycleRequest() # ModelsApiV2CyclesRequestsUpdateMDASCycleRequest | 

    try:
        # Update Cycle
        api_response = api_instance.update_cycle_data_sci_mdas_v2_cycles_cycle_id_put(cycle_id, models_api_v2_cycles_requests_update_mdas_cycle_request)
        print("The response of CyclesApi->update_cycle_data_sci_mdas_v2_cycles_cycle_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CyclesApi->update_cycle_data_sci_mdas_v2_cycles_cycle_id_put: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cycle_id** | **int**|  | 
 **models_api_v2_cycles_requests_update_mdas_cycle_request** | [**ModelsApiV2CyclesRequestsUpdateMDASCycleRequest**](ModelsApiV2CyclesRequestsUpdateMDASCycleRequest.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

