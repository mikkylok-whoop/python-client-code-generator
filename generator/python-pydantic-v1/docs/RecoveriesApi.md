# openapi_client.RecoveriesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**batch_create_recoveries_data_sci_mdas_v1_recoveries_batch_post**](RecoveriesApi.md#batch_create_recoveries_data_sci_mdas_v1_recoveries_batch_post) | **POST** /data-sci-mdas/v1/recoveries/batch | Batch Create Recoveries
[**create_recovery_data_sci_mdas_v1_recoveries_post**](RecoveriesApi.md#create_recovery_data_sci_mdas_v1_recoveries_post) | **POST** /data-sci-mdas/v1/recoveries | Create Recovery
[**create_recovery_data_sci_mdas_v2_recoveries_post**](RecoveriesApi.md#create_recovery_data_sci_mdas_v2_recoveries_post) | **POST** /data-sci-mdas/v2/recoveries | Create Recovery
[**delete_recovery_data_sci_mdas_v1_recoveries_recovery_id_delete**](RecoveriesApi.md#delete_recovery_data_sci_mdas_v1_recoveries_recovery_id_delete) | **DELETE** /data-sci-mdas/v1/recoveries/{recovery_id} | Delete Recovery
[**delete_recovery_data_sci_mdas_v2_recoveries_recovery_id_delete**](RecoveriesApi.md#delete_recovery_data_sci_mdas_v2_recoveries_recovery_id_delete) | **DELETE** /data-sci-mdas/v2/recoveries/{recovery_id} | Delete Recovery
[**get_recoveries_in_range_for_user_data_sci_mdas_v1_recoveries_get**](RecoveriesApi.md#get_recoveries_in_range_for_user_data_sci_mdas_v1_recoveries_get) | **GET** /data-sci-mdas/v1/recoveries | Get Recoveries In Range For User
[**get_recoveries_in_range_for_user_data_sci_mdas_v2_recoveries_get**](RecoveriesApi.md#get_recoveries_in_range_for_user_data_sci_mdas_v2_recoveries_get) | **GET** /data-sci-mdas/v2/recoveries | Get Recoveries In Range For User
[**update_recovery_data_sci_mdas_v1_recoveries_recovery_id_put**](RecoveriesApi.md#update_recovery_data_sci_mdas_v1_recoveries_recovery_id_put) | **PUT** /data-sci-mdas/v1/recoveries/{recovery_id} | Update Recovery
[**update_recovery_data_sci_mdas_v2_recoveries_recovery_id_put**](RecoveriesApi.md#update_recovery_data_sci_mdas_v2_recoveries_recovery_id_put) | **PUT** /data-sci-mdas/v2/recoveries/{recovery_id} | Update Recovery


# **batch_create_recoveries_data_sci_mdas_v1_recoveries_batch_post**
> object batch_create_recoveries_data_sci_mdas_v1_recoveries_batch_post(batch_create_mdas_recoveries_request)

Batch Create Recoveries

POST endpoint to create multiple recovery events
Note: This endpoint is for internal application use only. External customers should use the GET endpoints instead.

Args:
    batch_create_recoveries_request: Multiple recovery events
    recoveries_dao: RecoveriesDAO instance

Returns: None

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.batch_create_mdas_recoveries_request import BatchCreateMDASRecoveriesRequest
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
    api_instance = openapi_client.RecoveriesApi(api_client)
    batch_create_mdas_recoveries_request = openapi_client.BatchCreateMDASRecoveriesRequest() # BatchCreateMDASRecoveriesRequest | 

    try:
        # Batch Create Recoveries
        api_response = api_instance.batch_create_recoveries_data_sci_mdas_v1_recoveries_batch_post(batch_create_mdas_recoveries_request)
        print("The response of RecoveriesApi->batch_create_recoveries_data_sci_mdas_v1_recoveries_batch_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecoveriesApi->batch_create_recoveries_data_sci_mdas_v1_recoveries_batch_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_create_mdas_recoveries_request** | [**BatchCreateMDASRecoveriesRequest**](BatchCreateMDASRecoveriesRequest.md)|  | 

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

# **create_recovery_data_sci_mdas_v1_recoveries_post**
> object create_recovery_data_sci_mdas_v1_recoveries_post(create_mdas_recovery_request)

Create Recovery

POST endpoint to create a new recovery event
Note: This endpoint is for internal application use only. External customers should use the GET endpoints instead.

Args:
    create_recovery_request: Recovery event data
    recoveries_dao: RecoveriesDAO instance

Returns: None

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.create_mdas_recovery_request import CreateMDASRecoveryRequest
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
    api_instance = openapi_client.RecoveriesApi(api_client)
    create_mdas_recovery_request = openapi_client.CreateMDASRecoveryRequest() # CreateMDASRecoveryRequest | 

    try:
        # Create Recovery
        api_response = api_instance.create_recovery_data_sci_mdas_v1_recoveries_post(create_mdas_recovery_request)
        print("The response of RecoveriesApi->create_recovery_data_sci_mdas_v1_recoveries_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecoveriesApi->create_recovery_data_sci_mdas_v1_recoveries_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_mdas_recovery_request** | [**CreateMDASRecoveryRequest**](CreateMDASRecoveryRequest.md)|  | 

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

# **create_recovery_data_sci_mdas_v2_recoveries_post**
> object create_recovery_data_sci_mdas_v2_recoveries_post(create_mdas_recovery_request_v2)

Create Recovery

POST endpoint to create a new recovery event
Args:
    create_recovery_request: Recovery event data
    recoveries_dao: RecoveriesDAO instance

Returns: None

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.create_mdas_recovery_request_v2 import CreateMDASRecoveryRequestV2
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
    api_instance = openapi_client.RecoveriesApi(api_client)
    create_mdas_recovery_request_v2 = openapi_client.CreateMDASRecoveryRequestV2() # CreateMDASRecoveryRequestV2 | 

    try:
        # Create Recovery
        api_response = api_instance.create_recovery_data_sci_mdas_v2_recoveries_post(create_mdas_recovery_request_v2)
        print("The response of RecoveriesApi->create_recovery_data_sci_mdas_v2_recoveries_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecoveriesApi->create_recovery_data_sci_mdas_v2_recoveries_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_mdas_recovery_request_v2** | [**CreateMDASRecoveryRequestV2**](CreateMDASRecoveryRequestV2.md)|  | 

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

# **delete_recovery_data_sci_mdas_v1_recoveries_recovery_id_delete**
> object delete_recovery_data_sci_mdas_v1_recoveries_recovery_id_delete(recovery_id)

Delete Recovery

DELETE endpoint to delete a recovery event
Note: This endpoint is for internal application use only. External customers should use the GET endpoints instead.

Args:
    recovery_id: ID of the recovery event
    recoveries_dao: RecoveriesDAO instance

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
    api_instance = openapi_client.RecoveriesApi(api_client)
    recovery_id = 56 # int | 

    try:
        # Delete Recovery
        api_response = api_instance.delete_recovery_data_sci_mdas_v1_recoveries_recovery_id_delete(recovery_id)
        print("The response of RecoveriesApi->delete_recovery_data_sci_mdas_v1_recoveries_recovery_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecoveriesApi->delete_recovery_data_sci_mdas_v1_recoveries_recovery_id_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recovery_id** | **int**|  | 

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

# **delete_recovery_data_sci_mdas_v2_recoveries_recovery_id_delete**
> object delete_recovery_data_sci_mdas_v2_recoveries_recovery_id_delete(recovery_id)

Delete Recovery

DELETE endpoint to delete a recovery event
Args:
    recovery_id: ID of the recovery event
    recoveries_dao: RecoveriesDAO instance

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
    api_instance = openapi_client.RecoveriesApi(api_client)
    recovery_id = 'recovery_id_example' # str | 

    try:
        # Delete Recovery
        api_response = api_instance.delete_recovery_data_sci_mdas_v2_recoveries_recovery_id_delete(recovery_id)
        print("The response of RecoveriesApi->delete_recovery_data_sci_mdas_v2_recoveries_recovery_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecoveriesApi->delete_recovery_data_sci_mdas_v2_recoveries_recovery_id_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recovery_id** | **str**|  | 

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

# **get_recoveries_in_range_for_user_data_sci_mdas_v1_recoveries_get**
> List[ModelsApiV1RecoveriesResponsesMDASRecovery] get_recoveries_in_range_for_user_data_sci_mdas_v1_recoveries_get(user_id, start, end)

Get Recoveries In Range For User

GET endpoint to retrieve all recovery events for user during a specified time range
Args:
    user_id: ID of the user
    start: Start of time range to get recovery events for
    end: End of time range to get recovery events for
    recoveries_dao: RecoveriesDAO instance

Returns: List of recovery event data

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.models_api_v1_recoveries_responses_mdas_recovery import ModelsApiV1RecoveriesResponsesMDASRecovery
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
    api_instance = openapi_client.RecoveriesApi(api_client)
    user_id = 56 # int | 
    start = '2013-10-20T19:20:30+01:00' # datetime | 
    end = '2013-10-20T19:20:30+01:00' # datetime | 

    try:
        # Get Recoveries In Range For User
        api_response = api_instance.get_recoveries_in_range_for_user_data_sci_mdas_v1_recoveries_get(user_id, start, end)
        print("The response of RecoveriesApi->get_recoveries_in_range_for_user_data_sci_mdas_v1_recoveries_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecoveriesApi->get_recoveries_in_range_for_user_data_sci_mdas_v1_recoveries_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 
 **start** | **datetime**|  | 
 **end** | **datetime**|  | 

### Return type

[**List[ModelsApiV1RecoveriesResponsesMDASRecovery]**](ModelsApiV1RecoveriesResponsesMDASRecovery.md)

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

# **get_recoveries_in_range_for_user_data_sci_mdas_v2_recoveries_get**
> List[ModelsApiV2RecoveriesResponsesMDASRecovery] get_recoveries_in_range_for_user_data_sci_mdas_v2_recoveries_get(user_id, start, end)

Get Recoveries In Range For User

GET endpoint to retrieve all recovery events for user during a specified time range
Args:
    user_id: ID of the user
    start: Start of time range to get recovery events for
    end: End of time range to get recovery events for
    recoveries_dao: RecoveriesDAO instance

Returns: List of recovery event data

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.models_api_v2_recoveries_responses_mdas_recovery import ModelsApiV2RecoveriesResponsesMDASRecovery
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
    api_instance = openapi_client.RecoveriesApi(api_client)
    user_id = 56 # int | 
    start = '2013-10-20T19:20:30+01:00' # datetime | 
    end = '2013-10-20T19:20:30+01:00' # datetime | 

    try:
        # Get Recoveries In Range For User
        api_response = api_instance.get_recoveries_in_range_for_user_data_sci_mdas_v2_recoveries_get(user_id, start, end)
        print("The response of RecoveriesApi->get_recoveries_in_range_for_user_data_sci_mdas_v2_recoveries_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecoveriesApi->get_recoveries_in_range_for_user_data_sci_mdas_v2_recoveries_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 
 **start** | **datetime**|  | 
 **end** | **datetime**|  | 

### Return type

[**List[ModelsApiV2RecoveriesResponsesMDASRecovery]**](ModelsApiV2RecoveriesResponsesMDASRecovery.md)

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

# **update_recovery_data_sci_mdas_v1_recoveries_recovery_id_put**
> object update_recovery_data_sci_mdas_v1_recoveries_recovery_id_put(recovery_id, update_mdas_recovery_request)

Update Recovery

PUT endpoint for updating an existing recovery event
Note: This endpoint is for internal application use only. External customers should use the GET endpoints instead.

Args:
    recovery_id: ID of the recovery event
    update_recoveries_request: Recovery event data
    recoveries_dao: RecoveriesDAO instance

Returns: None

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.update_mdas_recovery_request import UpdateMDASRecoveryRequest
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
    api_instance = openapi_client.RecoveriesApi(api_client)
    recovery_id = 56 # int | 
    update_mdas_recovery_request = openapi_client.UpdateMDASRecoveryRequest() # UpdateMDASRecoveryRequest | 

    try:
        # Update Recovery
        api_response = api_instance.update_recovery_data_sci_mdas_v1_recoveries_recovery_id_put(recovery_id, update_mdas_recovery_request)
        print("The response of RecoveriesApi->update_recovery_data_sci_mdas_v1_recoveries_recovery_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecoveriesApi->update_recovery_data_sci_mdas_v1_recoveries_recovery_id_put: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recovery_id** | **int**|  | 
 **update_mdas_recovery_request** | [**UpdateMDASRecoveryRequest**](UpdateMDASRecoveryRequest.md)|  | 

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

# **update_recovery_data_sci_mdas_v2_recoveries_recovery_id_put**
> object update_recovery_data_sci_mdas_v2_recoveries_recovery_id_put(recovery_id, update_mdas_recovery_request_v2)

Update Recovery

PUT endpoint for updating an existing recovery event
Args:
    recovery_id: ID of the recovery event
    update_recoveries_request: Recovery event data
    recoveries_dao: RecoveriesDAO instance

Returns: None

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.update_mdas_recovery_request_v2 import UpdateMDASRecoveryRequestV2
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
    api_instance = openapi_client.RecoveriesApi(api_client)
    recovery_id = 'recovery_id_example' # str | 
    update_mdas_recovery_request_v2 = openapi_client.UpdateMDASRecoveryRequestV2() # UpdateMDASRecoveryRequestV2 | 

    try:
        # Update Recovery
        api_response = api_instance.update_recovery_data_sci_mdas_v2_recoveries_recovery_id_put(recovery_id, update_mdas_recovery_request_v2)
        print("The response of RecoveriesApi->update_recovery_data_sci_mdas_v2_recoveries_recovery_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecoveriesApi->update_recovery_data_sci_mdas_v2_recoveries_recovery_id_put: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recovery_id** | **str**|  | 
 **update_mdas_recovery_request_v2** | [**UpdateMDASRecoveryRequestV2**](UpdateMDASRecoveryRequestV2.md)|  | 

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

