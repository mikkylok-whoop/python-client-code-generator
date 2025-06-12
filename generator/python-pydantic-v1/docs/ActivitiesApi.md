# openapi_client.ActivitiesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**batch_create_activities_data_sci_mdas_v1_activities_batch_post**](ActivitiesApi.md#batch_create_activities_data_sci_mdas_v1_activities_batch_post) | **POST** /data-sci-mdas/v1/activities/batch | Batch Create Activities
[**create_activity_data_sci_mdas_v1_activities_post**](ActivitiesApi.md#create_activity_data_sci_mdas_v1_activities_post) | **POST** /data-sci-mdas/v1/activities | Create Activity
[**create_activity_data_sci_mdas_v2_activities_post**](ActivitiesApi.md#create_activity_data_sci_mdas_v2_activities_post) | **POST** /data-sci-mdas/v2/activities | Create Activity
[**delete_activity_data_sci_mdas_v1_activities_activity_id_delete**](ActivitiesApi.md#delete_activity_data_sci_mdas_v1_activities_activity_id_delete) | **DELETE** /data-sci-mdas/v1/activities/{activity_id} | Delete Activity
[**delete_activity_data_sci_mdas_v2_activities_activity_id_delete**](ActivitiesApi.md#delete_activity_data_sci_mdas_v2_activities_activity_id_delete) | **DELETE** /data-sci-mdas/v2/activities/{activity_id} | Delete Activity
[**get_activities_in_range_for_user_data_sci_mdas_v1_activities_get**](ActivitiesApi.md#get_activities_in_range_for_user_data_sci_mdas_v1_activities_get) | **GET** /data-sci-mdas/v1/activities | Get Activities In Range For User
[**get_activities_in_range_for_user_data_sci_mdas_v2_activities_get**](ActivitiesApi.md#get_activities_in_range_for_user_data_sci_mdas_v2_activities_get) | **GET** /data-sci-mdas/v2/activities | Get Activities In Range For User
[**update_activity_data_sci_mdas_v1_activities_activity_id_put**](ActivitiesApi.md#update_activity_data_sci_mdas_v1_activities_activity_id_put) | **PUT** /data-sci-mdas/v1/activities/{activity_id} | Update Activity
[**update_activity_data_sci_mdas_v2_activities_activity_id_put**](ActivitiesApi.md#update_activity_data_sci_mdas_v2_activities_activity_id_put) | **PUT** /data-sci-mdas/v2/activities/{activity_id} | Update Activity


# **batch_create_activities_data_sci_mdas_v1_activities_batch_post**
> object batch_create_activities_data_sci_mdas_v1_activities_batch_post(batch_create_mdas_activities_request)

Batch Create Activities

POST endpoint to create multiple activity events
Note: This endpoint is for internal application use only. External customers should use the GET endpoints instead.

Args:
    batch_create_activities_request: Multiple activity events
    activities_dao: ActivitiesDAO instance

Returns: None

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.batch_create_mdas_activities_request import BatchCreateMDASActivitiesRequest
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
    api_instance = openapi_client.ActivitiesApi(api_client)
    batch_create_mdas_activities_request = openapi_client.BatchCreateMDASActivitiesRequest() # BatchCreateMDASActivitiesRequest | 

    try:
        # Batch Create Activities
        api_response = api_instance.batch_create_activities_data_sci_mdas_v1_activities_batch_post(batch_create_mdas_activities_request)
        print("The response of ActivitiesApi->batch_create_activities_data_sci_mdas_v1_activities_batch_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivitiesApi->batch_create_activities_data_sci_mdas_v1_activities_batch_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_create_mdas_activities_request** | [**BatchCreateMDASActivitiesRequest**](BatchCreateMDASActivitiesRequest.md)|  | 

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

# **create_activity_data_sci_mdas_v1_activities_post**
> object create_activity_data_sci_mdas_v1_activities_post(models_api_v1_activities_requests_create_mdas_activity_request)

Create Activity

POST endpoint to create a new activity event
Note: This endpoint is for internal application use only. External customers should use the GET endpoints instead.

Args:
    create_activity_request: Activity event data
    activities_dao: ActivitiesDAO instance

Returns: None

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.models_api_v1_activities_requests_create_mdas_activity_request import ModelsApiV1ActivitiesRequestsCreateMDASActivityRequest
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
    api_instance = openapi_client.ActivitiesApi(api_client)
    models_api_v1_activities_requests_create_mdas_activity_request = openapi_client.ModelsApiV1ActivitiesRequestsCreateMDASActivityRequest() # ModelsApiV1ActivitiesRequestsCreateMDASActivityRequest | 

    try:
        # Create Activity
        api_response = api_instance.create_activity_data_sci_mdas_v1_activities_post(models_api_v1_activities_requests_create_mdas_activity_request)
        print("The response of ActivitiesApi->create_activity_data_sci_mdas_v1_activities_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivitiesApi->create_activity_data_sci_mdas_v1_activities_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **models_api_v1_activities_requests_create_mdas_activity_request** | [**ModelsApiV1ActivitiesRequestsCreateMDASActivityRequest**](ModelsApiV1ActivitiesRequestsCreateMDASActivityRequest.md)|  | 

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

# **create_activity_data_sci_mdas_v2_activities_post**
> object create_activity_data_sci_mdas_v2_activities_post(models_api_v2_activities_requests_create_mdas_activity_request)

Create Activity

POST endpoint to create a new activity event
Note: This endpoint is for internal application use only. External customers should use the GET endpoints instead.

Args:
    create_activity_request: Activity event data
    activities_dao: ActivitiesDAO instance

Returns: None

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.models_api_v2_activities_requests_create_mdas_activity_request import ModelsApiV2ActivitiesRequestsCreateMDASActivityRequest
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
    api_instance = openapi_client.ActivitiesApi(api_client)
    models_api_v2_activities_requests_create_mdas_activity_request = openapi_client.ModelsApiV2ActivitiesRequestsCreateMDASActivityRequest() # ModelsApiV2ActivitiesRequestsCreateMDASActivityRequest | 

    try:
        # Create Activity
        api_response = api_instance.create_activity_data_sci_mdas_v2_activities_post(models_api_v2_activities_requests_create_mdas_activity_request)
        print("The response of ActivitiesApi->create_activity_data_sci_mdas_v2_activities_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivitiesApi->create_activity_data_sci_mdas_v2_activities_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **models_api_v2_activities_requests_create_mdas_activity_request** | [**ModelsApiV2ActivitiesRequestsCreateMDASActivityRequest**](ModelsApiV2ActivitiesRequestsCreateMDASActivityRequest.md)|  | 

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

# **delete_activity_data_sci_mdas_v1_activities_activity_id_delete**
> object delete_activity_data_sci_mdas_v1_activities_activity_id_delete(activity_id)

Delete Activity

DELETE endpoint to delete an activity event
Note: This endpoint is for internal application use only. External customers should use the GET endpoints instead.

Args:
    activity_id: ID of the activity event
    activities_dao: ActivitiesDAO instance

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
    api_instance = openapi_client.ActivitiesApi(api_client)
    activity_id = 'activity_id_example' # str | 

    try:
        # Delete Activity
        api_response = api_instance.delete_activity_data_sci_mdas_v1_activities_activity_id_delete(activity_id)
        print("The response of ActivitiesApi->delete_activity_data_sci_mdas_v1_activities_activity_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivitiesApi->delete_activity_data_sci_mdas_v1_activities_activity_id_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activity_id** | **str**|  | 

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

# **delete_activity_data_sci_mdas_v2_activities_activity_id_delete**
> object delete_activity_data_sci_mdas_v2_activities_activity_id_delete(activity_id)

Delete Activity

DELETE endpoint to delete an activity event
Note: This endpoint is for internal application use only. External customers should use the GET endpoints instead.

Args:
    activity_id: ID of the activity event
    activities_dao: ActivitiesDAO instance

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
    api_instance = openapi_client.ActivitiesApi(api_client)
    activity_id = 'activity_id_example' # str | 

    try:
        # Delete Activity
        api_response = api_instance.delete_activity_data_sci_mdas_v2_activities_activity_id_delete(activity_id)
        print("The response of ActivitiesApi->delete_activity_data_sci_mdas_v2_activities_activity_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivitiesApi->delete_activity_data_sci_mdas_v2_activities_activity_id_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activity_id** | **str**|  | 

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

# **get_activities_in_range_for_user_data_sci_mdas_v1_activities_get**
> List[ModelsApiV1ActivitiesResponsesMDASActivity] get_activities_in_range_for_user_data_sci_mdas_v1_activities_get(user_id, start, end)

Get Activities In Range For User

GET endpoint to retrieve all activity events for user during a specified time range
Args:
    user_id: ID of the user
    start: Start of time range to get activity events for
    end: End of time range to get activity events for
    activities_dao: ActivitiesDAO instance

Returns: List of recovery event data

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.models_api_v1_activities_responses_mdas_activity import ModelsApiV1ActivitiesResponsesMDASActivity
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
    api_instance = openapi_client.ActivitiesApi(api_client)
    user_id = 56 # int | 
    start = '2013-10-20T19:20:30+01:00' # datetime | 
    end = '2013-10-20T19:20:30+01:00' # datetime | 

    try:
        # Get Activities In Range For User
        api_response = api_instance.get_activities_in_range_for_user_data_sci_mdas_v1_activities_get(user_id, start, end)
        print("The response of ActivitiesApi->get_activities_in_range_for_user_data_sci_mdas_v1_activities_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivitiesApi->get_activities_in_range_for_user_data_sci_mdas_v1_activities_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 
 **start** | **datetime**|  | 
 **end** | **datetime**|  | 

### Return type

[**List[ModelsApiV1ActivitiesResponsesMDASActivity]**](ModelsApiV1ActivitiesResponsesMDASActivity.md)

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

# **get_activities_in_range_for_user_data_sci_mdas_v2_activities_get**
> List[ModelsApiV2ActivitiesResponsesMDASActivity] get_activities_in_range_for_user_data_sci_mdas_v2_activities_get(user_id, start, end)

Get Activities In Range For User

GET endpoint to retrieve all activity events for user during a specified time range
Args:
    user_id: ID of the user
    start: Start of time range to get activity events for
    end: End of time range to get activity events for
    activities_dao: ActivitiesDAO instance

Returns: List of recovery event data

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.models_api_v2_activities_responses_mdas_activity import ModelsApiV2ActivitiesResponsesMDASActivity
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
    api_instance = openapi_client.ActivitiesApi(api_client)
    user_id = 56 # int | 
    start = '2013-10-20T19:20:30+01:00' # datetime | 
    end = '2013-10-20T19:20:30+01:00' # datetime | 

    try:
        # Get Activities In Range For User
        api_response = api_instance.get_activities_in_range_for_user_data_sci_mdas_v2_activities_get(user_id, start, end)
        print("The response of ActivitiesApi->get_activities_in_range_for_user_data_sci_mdas_v2_activities_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivitiesApi->get_activities_in_range_for_user_data_sci_mdas_v2_activities_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 
 **start** | **datetime**|  | 
 **end** | **datetime**|  | 

### Return type

[**List[ModelsApiV2ActivitiesResponsesMDASActivity]**](ModelsApiV2ActivitiesResponsesMDASActivity.md)

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

# **update_activity_data_sci_mdas_v1_activities_activity_id_put**
> object update_activity_data_sci_mdas_v1_activities_activity_id_put(activity_id, models_api_v1_activities_requests_update_mdas_activity_request)

Update Activity

PUT endpoint to update an activity event
Note: This endpoint is for internal application use only. External customers should use the GET endpoints instead.

Args:
    activity_id: ID of the activity event
    update_activities_request: Activity event data
    activities_dao: ActivitiesDAO instance

Returns: None

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.models_api_v1_activities_requests_update_mdas_activity_request import ModelsApiV1ActivitiesRequestsUpdateMDASActivityRequest
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
    api_instance = openapi_client.ActivitiesApi(api_client)
    activity_id = 'activity_id_example' # str | 
    models_api_v1_activities_requests_update_mdas_activity_request = openapi_client.ModelsApiV1ActivitiesRequestsUpdateMDASActivityRequest() # ModelsApiV1ActivitiesRequestsUpdateMDASActivityRequest | 

    try:
        # Update Activity
        api_response = api_instance.update_activity_data_sci_mdas_v1_activities_activity_id_put(activity_id, models_api_v1_activities_requests_update_mdas_activity_request)
        print("The response of ActivitiesApi->update_activity_data_sci_mdas_v1_activities_activity_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivitiesApi->update_activity_data_sci_mdas_v1_activities_activity_id_put: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activity_id** | **str**|  | 
 **models_api_v1_activities_requests_update_mdas_activity_request** | [**ModelsApiV1ActivitiesRequestsUpdateMDASActivityRequest**](ModelsApiV1ActivitiesRequestsUpdateMDASActivityRequest.md)|  | 

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

# **update_activity_data_sci_mdas_v2_activities_activity_id_put**
> object update_activity_data_sci_mdas_v2_activities_activity_id_put(activity_id, models_api_v2_activities_requests_update_mdas_activity_request)

Update Activity

PUT endpoint to update an activity event
Note: This endpoint is for internal application use only. External customers should use the GET endpoints instead.

Args:
    activity_id: ID of the activity event
    update_activities_request: Activity event data
    activities_dao: ActivitiesDAO instance

Returns: None

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.models_api_v2_activities_requests_update_mdas_activity_request import ModelsApiV2ActivitiesRequestsUpdateMDASActivityRequest
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
    api_instance = openapi_client.ActivitiesApi(api_client)
    activity_id = 'activity_id_example' # str | 
    models_api_v2_activities_requests_update_mdas_activity_request = openapi_client.ModelsApiV2ActivitiesRequestsUpdateMDASActivityRequest() # ModelsApiV2ActivitiesRequestsUpdateMDASActivityRequest | 

    try:
        # Update Activity
        api_response = api_instance.update_activity_data_sci_mdas_v2_activities_activity_id_put(activity_id, models_api_v2_activities_requests_update_mdas_activity_request)
        print("The response of ActivitiesApi->update_activity_data_sci_mdas_v2_activities_activity_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivitiesApi->update_activity_data_sci_mdas_v2_activities_activity_id_put: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activity_id** | **str**|  | 
 **models_api_v2_activities_requests_update_mdas_activity_request** | [**ModelsApiV2ActivitiesRequestsUpdateMDASActivityRequest**](ModelsApiV2ActivitiesRequestsUpdateMDASActivityRequest.md)|  | 

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

