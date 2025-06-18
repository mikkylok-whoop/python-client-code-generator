from datetime import datetime
from typing import Any, List, Optional

from datadog import DogStatsd
from pydantic import StrictInt, StrictStr
from whoop_service_clients.base.client import BaseApiClient

from data_sci_mdas.models.batch_create_mdas_activities_request import BatchCreateMDASActivitiesRequest
from data_sci_mdas.models.models_api_v1_activities_requests_create_mdas_activity_request import (
    ModelsApiV1ActivitiesRequestsCreateMDASActivityRequest,
)
from data_sci_mdas.models.models_api_v1_activities_requests_update_mdas_activity_request import (
    ModelsApiV1ActivitiesRequestsUpdateMDASActivityRequest,
)
from data_sci_mdas.models.models_api_v1_activities_responses_mdas_activity import (
    ModelsApiV1ActivitiesResponsesMDASActivity,
)
from data_sci_mdas.models.models_api_v2_activities_requests_create_mdas_activity_request import (
    ModelsApiV2ActivitiesRequestsCreateMDASActivityRequest,
)
from data_sci_mdas.models.models_api_v2_activities_requests_update_mdas_activity_request import (
    ModelsApiV2ActivitiesRequestsUpdateMDASActivityRequest,
)
from data_sci_mdas.models.models_api_v2_activities_responses_mdas_activity import (
    ModelsApiV2ActivitiesResponsesMDASActivity,
)


class ActivitiesApi(BaseApiClient):
    def __init__(self, uri: str, statsd_client: Optional[DogStatsd] = None) -> None:
        self._uri = uri
        super().__init__(service_uri=self._uri, statsd_client=statsd_client)

    def batch_create_activities_data_sci_mdas_v1_activities_batch_post(
        self, batch_create_mdas_activities_request: BatchCreateMDASActivitiesRequest
    ) -> object:
        """
        POST endpoint to create multiple activity events Note: This endpoint is for internal application use only. External customers should use the GET endpoints instead.  Args:     batch_create_activities_request: Multiple activity events     activities_dao: ActivitiesDAO instance  Returns: None
        """
        # Process query parameters
        _query_params: list[tuple[str, Any]] = []

        # Process body parameter
        _body_params = None
        if batch_create_mdas_activities_request is not None:
            _body_params = batch_create_mdas_activities_request

        # Construct request URL
        request_url = f"{self._uri}/data-sci-mdas/v1/activities/batch"

        # HTTP method selection based on the operation
        return self._post(
            url=request_url,
            return_type=object,
            query_params=_query_params,
            data=_body_params,
        )

    def create_activity_data_sci_mdas_v1_activities_post(
        self,
        models_api_v1_activities_requests_create_mdas_activity_request: ModelsApiV1ActivitiesRequestsCreateMDASActivityRequest,
    ) -> object:
        """
        POST endpoint to create a new activity event Note: This endpoint is for internal application use only. External customers should use the GET endpoints instead.  Args:     create_activity_request: Activity event data     activities_dao: ActivitiesDAO instance  Returns: None
        """
        # Process query parameters
        _query_params: list[tuple[str, Any]] = []

        # Process body parameter
        _body_params = None
        if models_api_v1_activities_requests_create_mdas_activity_request is not None:
            _body_params = models_api_v1_activities_requests_create_mdas_activity_request

        # Construct request URL
        request_url = f"{self._uri}/data-sci-mdas/v1/activities"

        # HTTP method selection based on the operation
        return self._post(
            url=request_url,
            return_type=object,
            query_params=_query_params,
            data=_body_params,
        )

    def create_activity_data_sci_mdas_v2_activities_post(
        self,
        models_api_v2_activities_requests_create_mdas_activity_request: ModelsApiV2ActivitiesRequestsCreateMDASActivityRequest,
    ) -> object:
        """
        POST endpoint to create a new activity event Note: This endpoint is for internal application use only. External customers should use the GET endpoints instead.  Args:     create_activity_request: Activity event data     activities_dao: ActivitiesDAO instance  Returns: None
        """
        # Process query parameters
        _query_params: list[tuple[str, Any]] = []

        # Process body parameter
        _body_params = None
        if models_api_v2_activities_requests_create_mdas_activity_request is not None:
            _body_params = models_api_v2_activities_requests_create_mdas_activity_request

        # Construct request URL
        request_url = f"{self._uri}/data-sci-mdas/v2/activities"

        # HTTP method selection based on the operation
        return self._post(
            url=request_url,
            return_type=object,
            query_params=_query_params,
            data=_body_params,
        )

    def delete_activity_data_sci_mdas_v1_activities_activity_id_delete(self, activity_id: str) -> object:
        """
        DELETE endpoint to delete an activity event Note: This endpoint is for internal application use only. External customers should use the GET endpoints instead.  Args:     activity_id: ID of the activity event     activities_dao: ActivitiesDAO instance  Returns: None
        """
        # Process query parameters
        _query_params: list[tuple[str, Any]] = []

        # Process body parameter
        _body_params = None

        # Construct request URL
        request_url = f"{self._uri}/data-sci-mdas/v1/activities/{activity_id}"

        # HTTP method selection based on the operation
        return self._delete(
            url=request_url,
            return_type=object,
            query_params=_query_params,
            data=_body_params,
        )

    def delete_activity_data_sci_mdas_v2_activities_activity_id_delete(self, activity_id: str) -> object:
        """
        DELETE endpoint to delete an activity event Note: This endpoint is for internal application use only. External customers should use the GET endpoints instead.  Args:     activity_id: ID of the activity event     activities_dao: ActivitiesDAO instance  Returns: None
        """
        # Process query parameters
        _query_params: list[tuple[str, Any]] = []

        # Process body parameter
        _body_params = None

        # Construct request URL
        request_url = f"{self._uri}/data-sci-mdas/v2/activities/{activity_id}"

        # HTTP method selection based on the operation
        return self._delete(
            url=request_url,
            return_type=object,
            query_params=_query_params,
            data=_body_params,
        )

    def get_activities_in_range_for_user_data_sci_mdas_v1_activities_get(
        self, user_id: int, start: datetime, end: datetime
    ) -> List[ModelsApiV1ActivitiesResponsesMDASActivity]:
        """
        GET endpoint to retrieve all activity events for user during a specified time range Args:     user_id: ID of the user     start: Start of time range to get activity events for     end: End of time range to get activity events for     activities_dao: ActivitiesDAO instance  Returns: List of recovery event data
        """
        # Process query parameters
        _query_params: list[tuple[str, Any]] = []
        if user_id is not None:
            _query_params.append(("userId", user_id))
        if start is not None:
            if isinstance(start, datetime):
                _query_params.append(("start", self.format_datetime(start)))
            else:
                _query_params.append(("start", start))
        if end is not None:
            if isinstance(end, datetime):
                _query_params.append(("end", self.format_datetime(end)))
            else:
                _query_params.append(("end", end))

        # Process body parameter
        _body_params = None

        # Construct request URL
        request_url = f"{self._uri}/data-sci-mdas/v1/activities"

        # HTTP method selection based on the operation
        return self._get(
            url=request_url,
            return_type=List[ModelsApiV1ActivitiesResponsesMDASActivity],
            query_params=_query_params,
            data=_body_params,
        )

    def get_activities_in_range_for_user_data_sci_mdas_v2_activities_get(
        self, user_id: int, start: datetime, end: datetime
    ) -> List[ModelsApiV2ActivitiesResponsesMDASActivity]:
        """
        GET endpoint to retrieve all activity events for user during a specified time range Args:     user_id: ID of the user     start: Start of time range to get activity events for     end: End of time range to get activity events for     activities_dao: ActivitiesDAO instance  Returns: List of recovery event data
        """
        # Process query parameters
        _query_params: list[tuple[str, Any]] = []
        if user_id is not None:
            _query_params.append(("userId", user_id))
        if start is not None:
            if isinstance(start, datetime):
                _query_params.append(("start", self.format_datetime(start)))
            else:
                _query_params.append(("start", start))
        if end is not None:
            if isinstance(end, datetime):
                _query_params.append(("end", self.format_datetime(end)))
            else:
                _query_params.append(("end", end))

        # Process body parameter
        _body_params = None

        # Construct request URL
        request_url = f"{self._uri}/data-sci-mdas/v2/activities"

        # HTTP method selection based on the operation
        return self._get(
            url=request_url,
            return_type=List[ModelsApiV2ActivitiesResponsesMDASActivity],
            query_params=_query_params,
            data=_body_params,
        )

    def update_activity_data_sci_mdas_v1_activities_activity_id_put(
        self,
        activity_id: str,
        models_api_v1_activities_requests_update_mdas_activity_request: ModelsApiV1ActivitiesRequestsUpdateMDASActivityRequest,
    ) -> object:
        """
        PUT endpoint to update an activity event Note: This endpoint is for internal application use only. External customers should use the GET endpoints instead.  Args:     activity_id: ID of the activity event     update_activities_request: Activity event data     activities_dao: ActivitiesDAO instance  Returns: None
        """
        # Process query parameters
        _query_params: list[tuple[str, Any]] = []

        # Process body parameter
        _body_params = None
        if models_api_v1_activities_requests_update_mdas_activity_request is not None:
            _body_params = models_api_v1_activities_requests_update_mdas_activity_request

        # Construct request URL
        request_url = f"{self._uri}/data-sci-mdas/v1/activities/{activity_id}"

        # HTTP method selection based on the operation
        return self._put(
            url=request_url,
            return_type=object,
            query_params=_query_params,
            data=_body_params,
        )

    def update_activity_data_sci_mdas_v2_activities_activity_id_put(
        self,
        activity_id: str,
        models_api_v2_activities_requests_update_mdas_activity_request: ModelsApiV2ActivitiesRequestsUpdateMDASActivityRequest,
    ) -> object:
        """
        PUT endpoint to update an activity event Note: This endpoint is for internal application use only. External customers should use the GET endpoints instead.  Args:     activity_id: ID of the activity event     update_activities_request: Activity event data     activities_dao: ActivitiesDAO instance  Returns: None
        """
        # Process query parameters
        _query_params: list[tuple[str, Any]] = []

        # Process body parameter
        _body_params = None
        if models_api_v2_activities_requests_update_mdas_activity_request is not None:
            _body_params = models_api_v2_activities_requests_update_mdas_activity_request

        # Construct request URL
        request_url = f"{self._uri}/data-sci-mdas/v2/activities/{activity_id}"

        # HTTP method selection based on the operation
        return self._put(
            url=request_url,
            return_type=object,
            query_params=_query_params,
            data=_body_params,
        )
