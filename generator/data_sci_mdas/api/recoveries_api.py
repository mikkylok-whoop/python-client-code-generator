from datetime import datetime
from typing import Any, List, Optional

from datadog import DogStatsd
from pydantic import StrictInt, StrictStr
from whoop_service_clients.base.client import BaseApiClient

from data_sci_mdas.models.batch_create_mdas_recoveries_request import BatchCreateMDASRecoveriesRequest
from data_sci_mdas.models.create_mdas_recovery_request import CreateMDASRecoveryRequest
from data_sci_mdas.models.create_mdas_recovery_request_v2 import CreateMDASRecoveryRequestV2
from data_sci_mdas.models.models_api_v1_recoveries_responses_mdas_recovery import (
    ModelsApiV1RecoveriesResponsesMDASRecovery,
)
from data_sci_mdas.models.models_api_v2_recoveries_responses_mdas_recovery import (
    ModelsApiV2RecoveriesResponsesMDASRecovery,
)
from data_sci_mdas.models.update_mdas_recovery_request import UpdateMDASRecoveryRequest
from data_sci_mdas.models.update_mdas_recovery_request_v2 import UpdateMDASRecoveryRequestV2


class RecoveriesApi(BaseApiClient):
    def __init__(self, uri: str, statsd_client: Optional[DogStatsd] = None) -> None:
        self._uri = uri
        super().__init__(service_uri=self._uri, statsd_client=statsd_client)

    def batch_create_recoveries_data_sci_mdas_v1_recoveries_batch_post(
        self, batch_create_mdas_recoveries_request: BatchCreateMDASRecoveriesRequest
    ) -> object:
        """
        POST endpoint to create multiple recovery events Note: This endpoint is for internal application use only. External customers should use the GET endpoints instead.  Args:     batch_create_recoveries_request: Multiple recovery events     recoveries_dao: RecoveriesDAO instance  Returns: None
        """
        # Process query parameters
        _query_params: list[tuple[str, Any]] = []

        # Process body parameter
        _body_params = None
        if batch_create_mdas_recoveries_request is not None:
            _body_params = batch_create_mdas_recoveries_request

        # Construct request URL
        request_url = f"{self._uri}/data-sci-mdas/v1/recoveries/batch"

        # HTTP method selection based on the operation
        return self._post(
            url=request_url,
            return_type=object,
            query_params=_query_params,
            data=_body_params,
        )

    def create_recovery_data_sci_mdas_v1_recoveries_post(
        self, create_mdas_recovery_request: CreateMDASRecoveryRequest
    ) -> object:
        """
        POST endpoint to create a new recovery event Note: This endpoint is for internal application use only. External customers should use the GET endpoints instead.  Args:     create_recovery_request: Recovery event data     recoveries_dao: RecoveriesDAO instance  Returns: None
        """
        # Process query parameters
        _query_params: list[tuple[str, Any]] = []

        # Process body parameter
        _body_params = None
        if create_mdas_recovery_request is not None:
            _body_params = create_mdas_recovery_request

        # Construct request URL
        request_url = f"{self._uri}/data-sci-mdas/v1/recoveries"

        # HTTP method selection based on the operation
        return self._post(
            url=request_url,
            return_type=object,
            query_params=_query_params,
            data=_body_params,
        )

    def create_recovery_data_sci_mdas_v2_recoveries_post(
        self, create_mdas_recovery_request_v2: CreateMDASRecoveryRequestV2
    ) -> object:
        """
        POST endpoint to create a new recovery event Args:     create_recovery_request: Recovery event data     recoveries_dao: RecoveriesDAO instance  Returns: None
        """
        # Process query parameters
        _query_params: list[tuple[str, Any]] = []

        # Process body parameter
        _body_params = None
        if create_mdas_recovery_request_v2 is not None:
            _body_params = create_mdas_recovery_request_v2

        # Construct request URL
        request_url = f"{self._uri}/data-sci-mdas/v2/recoveries"

        # HTTP method selection based on the operation
        return self._post(
            url=request_url,
            return_type=object,
            query_params=_query_params,
            data=_body_params,
        )

    def delete_recovery_data_sci_mdas_v1_recoveries_recovery_id_delete(self, recovery_id: int) -> object:
        """
        DELETE endpoint to delete a recovery event Note: This endpoint is for internal application use only. External customers should use the GET endpoints instead.  Args:     recovery_id: ID of the recovery event     recoveries_dao: RecoveriesDAO instance  Returns: None
        """
        # Process query parameters
        _query_params: list[tuple[str, Any]] = []

        # Process body parameter
        _body_params = None

        # Construct request URL
        request_url = f"{self._uri}/data-sci-mdas/v1/recoveries/{recovery_id}"

        # HTTP method selection based on the operation
        return self._delete(
            url=request_url,
            return_type=object,
            query_params=_query_params,
            data=_body_params,
        )

    def delete_recovery_data_sci_mdas_v2_recoveries_recovery_id_delete(self, recovery_id: str) -> object:
        """
        DELETE endpoint to delete a recovery event Args:     recovery_id: ID of the recovery event     recoveries_dao: RecoveriesDAO instance  Returns: None
        """
        # Process query parameters
        _query_params: list[tuple[str, Any]] = []

        # Process body parameter
        _body_params = None

        # Construct request URL
        request_url = f"{self._uri}/data-sci-mdas/v2/recoveries/{recovery_id}"

        # HTTP method selection based on the operation
        return self._delete(
            url=request_url,
            return_type=object,
            query_params=_query_params,
            data=_body_params,
        )

    def get_recoveries_in_range_for_user_data_sci_mdas_v1_recoveries_get(
        self, user_id: int, start: datetime, end: datetime
    ) -> List[ModelsApiV1RecoveriesResponsesMDASRecovery]:
        """
        GET endpoint to retrieve all recovery events for user during a specified time range Args:     user_id: ID of the user     start: Start of time range to get recovery events for     end: End of time range to get recovery events for     recoveries_dao: RecoveriesDAO instance  Returns: List of recovery event data
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
        request_url = f"{self._uri}/data-sci-mdas/v1/recoveries"

        # HTTP method selection based on the operation
        return self._get(
            url=request_url,
            return_type=List[ModelsApiV1RecoveriesResponsesMDASRecovery],
            query_params=_query_params,
            data=_body_params,
        )

    def get_recoveries_in_range_for_user_data_sci_mdas_v2_recoveries_get(
        self, user_id: int, start: datetime, end: datetime
    ) -> List[ModelsApiV2RecoveriesResponsesMDASRecovery]:
        """
        GET endpoint to retrieve all recovery events for user during a specified time range Args:     user_id: ID of the user     start: Start of time range to get recovery events for     end: End of time range to get recovery events for     recoveries_dao: RecoveriesDAO instance  Returns: List of recovery event data
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
        request_url = f"{self._uri}/data-sci-mdas/v2/recoveries"

        # HTTP method selection based on the operation
        return self._get(
            url=request_url,
            return_type=List[ModelsApiV2RecoveriesResponsesMDASRecovery],
            query_params=_query_params,
            data=_body_params,
        )

    def update_recovery_data_sci_mdas_v1_recoveries_recovery_id_put(
        self, recovery_id: int, update_mdas_recovery_request: UpdateMDASRecoveryRequest
    ) -> object:
        """
        PUT endpoint for updating an existing recovery event Note: This endpoint is for internal application use only. External customers should use the GET endpoints instead.  Args:     recovery_id: ID of the recovery event     update_recoveries_request: Recovery event data     recoveries_dao: RecoveriesDAO instance  Returns: None
        """
        # Process query parameters
        _query_params: list[tuple[str, Any]] = []

        # Process body parameter
        _body_params = None
        if update_mdas_recovery_request is not None:
            _body_params = update_mdas_recovery_request

        # Construct request URL
        request_url = f"{self._uri}/data-sci-mdas/v1/recoveries/{recovery_id}"

        # HTTP method selection based on the operation
        return self._put(
            url=request_url,
            return_type=object,
            query_params=_query_params,
            data=_body_params,
        )

    def update_recovery_data_sci_mdas_v2_recoveries_recovery_id_put(
        self, recovery_id: str, update_mdas_recovery_request_v2: UpdateMDASRecoveryRequestV2
    ) -> object:
        """
        PUT endpoint for updating an existing recovery event Args:     recovery_id: ID of the recovery event     update_recoveries_request: Recovery event data     recoveries_dao: RecoveriesDAO instance  Returns: None
        """
        # Process query parameters
        _query_params: list[tuple[str, Any]] = []

        # Process body parameter
        _body_params = None
        if update_mdas_recovery_request_v2 is not None:
            _body_params = update_mdas_recovery_request_v2

        # Construct request URL
        request_url = f"{self._uri}/data-sci-mdas/v2/recoveries/{recovery_id}"

        # HTTP method selection based on the operation
        return self._put(
            url=request_url,
            return_type=object,
            query_params=_query_params,
            data=_body_params,
        )
