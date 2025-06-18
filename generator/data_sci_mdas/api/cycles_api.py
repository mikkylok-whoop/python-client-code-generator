from datetime import datetime
from typing import Any, List, Optional

from datadog import DogStatsd
from pydantic import StrictInt
from whoop_service_clients.base.client import BaseApiClient

from data_sci_mdas.models.batch_create_mdas_cycles_request import BatchCreateMDASCyclesRequest
from data_sci_mdas.models.models_api_v1_cycles_requests_create_mdas_cycle_request import (
    ModelsApiV1CyclesRequestsCreateMDASCycleRequest,
)
from data_sci_mdas.models.models_api_v1_cycles_requests_update_mdas_cycle_request import (
    ModelsApiV1CyclesRequestsUpdateMDASCycleRequest,
)
from data_sci_mdas.models.models_api_v1_cycles_responses_mdas_cycle import ModelsApiV1CyclesResponsesMDASCycle
from data_sci_mdas.models.models_api_v2_cycles_requests_create_mdas_cycle_request import (
    ModelsApiV2CyclesRequestsCreateMDASCycleRequest,
)
from data_sci_mdas.models.models_api_v2_cycles_requests_update_mdas_cycle_request import (
    ModelsApiV2CyclesRequestsUpdateMDASCycleRequest,
)
from data_sci_mdas.models.models_api_v2_cycles_responses_mdas_cycle import ModelsApiV2CyclesResponsesMDASCycle


class CyclesApi(BaseApiClient):
    def __init__(self, uri: str, statsd_client: Optional[DogStatsd] = None) -> None:
        self._uri = uri
        super().__init__(service_uri=self._uri, statsd_client=statsd_client)

    def batch_create_cycles_data_sci_mdas_v1_cycles_batch_post(
        self, batch_create_mdas_cycles_request: BatchCreateMDASCyclesRequest
    ) -> object:
        """
        POST endpoint to create multiple cycle events Note: This endpoint is for internal application use only. External customers should use the GET endpoints instead.  Args:     batch_create_cycles_request: Multiple cycle events     cycles_dao: CyclesDAO instance  Returns: None
        """
        # Process query parameters
        _query_params: list[tuple[str, Any]] = []

        # Process body parameter
        _body_params = None
        if batch_create_mdas_cycles_request is not None:
            _body_params = batch_create_mdas_cycles_request

        # Construct request URL
        request_url = f"{self._uri}/data-sci-mdas/v1/cycles/batch"

        # HTTP method selection based on the operation
        return self._post(
            url=request_url,
            return_type=object,
            query_params=_query_params,
            data=_body_params,
        )

    def create_cycle_data_sci_mdas_v1_cycles_post(
        self, models_api_v1_cycles_requests_create_mdas_cycle_request: ModelsApiV1CyclesRequestsCreateMDASCycleRequest
    ) -> object:
        """
        POST endpoint to create a new cycle event Note: This endpoint is for internal application use only. External customers should use the GET endpoints instead.  Args:     create_cycle_request: Cycle event data     cycles_dao: CyclesDAO instance  Returns: None
        """
        # Process query parameters
        _query_params: list[tuple[str, Any]] = []

        # Process body parameter
        _body_params = None
        if models_api_v1_cycles_requests_create_mdas_cycle_request is not None:
            _body_params = models_api_v1_cycles_requests_create_mdas_cycle_request

        # Construct request URL
        request_url = f"{self._uri}/data-sci-mdas/v1/cycles"

        # HTTP method selection based on the operation
        return self._post(
            url=request_url,
            return_type=object,
            query_params=_query_params,
            data=_body_params,
        )

    def create_cycle_data_sci_mdas_v2_cycles_post(
        self, models_api_v2_cycles_requests_create_mdas_cycle_request: ModelsApiV2CyclesRequestsCreateMDASCycleRequest
    ) -> object:
        """
        POST endpoint to create a new cycle event Note: This endpoint is for internal application use only. External customers should use the GET endpoints instead.  Args:     create_cycle_request: Cycle event data     cycles_dao: CyclesDAO instance  Returns: None
        """
        # Process query parameters
        _query_params: list[tuple[str, Any]] = []

        # Process body parameter
        _body_params = None
        if models_api_v2_cycles_requests_create_mdas_cycle_request is not None:
            _body_params = models_api_v2_cycles_requests_create_mdas_cycle_request

        # Construct request URL
        request_url = f"{self._uri}/data-sci-mdas/v2/cycles"

        # HTTP method selection based on the operation
        return self._post(
            url=request_url,
            return_type=object,
            query_params=_query_params,
            data=_body_params,
        )

    def delete_cycle_data_sci_mdas_v1_cycles_cycle_id_delete(self, cycle_id: int) -> object:
        """
        DELETE endpoint to delete a recovery event Note: This endpoint is for internal application use only. External customers should use the GET endpoints instead.  Args:     cycle_id: ID of the cycle event     cycles_dao: CyclesDAO instance  Returns: None
        """
        # Process query parameters
        _query_params: list[tuple[str, Any]] = []

        # Process body parameter
        _body_params = None

        # Construct request URL
        request_url = f"{self._uri}/data-sci-mdas/v1/cycles/{cycle_id}"

        # HTTP method selection based on the operation
        return self._delete(
            url=request_url,
            return_type=object,
            query_params=_query_params,
            data=_body_params,
        )

    def delete_cycle_data_sci_mdas_v2_cycles_cycle_id_delete(self, cycle_id: int) -> object:
        """
        DELETE endpoint to delete a recovery event Note: This endpoint is for internal application use only. External customers should use the GET endpoints instead.  Args:     cycle_id: ID of the cycle event     cycles_dao: CyclesDAO instance  Returns: None
        """
        # Process query parameters
        _query_params: list[tuple[str, Any]] = []

        # Process body parameter
        _body_params = None

        # Construct request URL
        request_url = f"{self._uri}/data-sci-mdas/v2/cycles/{cycle_id}"

        # HTTP method selection based on the operation
        return self._delete(
            url=request_url,
            return_type=object,
            query_params=_query_params,
            data=_body_params,
        )

    def get_cycles_in_range_for_user_data_sci_mdas_v1_cycles_get(
        self, user_id: int, start: datetime, end: datetime
    ) -> List[ModelsApiV1CyclesResponsesMDASCycle]:
        """
        GET endpoint to retrieve all cycle events for a user during a specified time range Args:     user_id: ID of the user     start: Start of the time range to get cycle events for     end: End of time range to get cycle events for     cycles_dao: CyclesDAO instance  Returns: List of cycle event data
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
        request_url = f"{self._uri}/data-sci-mdas/v1/cycles"

        # HTTP method selection based on the operation
        return self._get(
            url=request_url,
            return_type=List[ModelsApiV1CyclesResponsesMDASCycle],
            query_params=_query_params,
            data=_body_params,
        )

    def get_cycles_in_range_for_user_data_sci_mdas_v2_cycles_get(
        self, user_id: int, start: datetime, end: datetime
    ) -> List[ModelsApiV2CyclesResponsesMDASCycle]:
        """
        GET endpoint to retrieve all cycle events for a user during a specified time range Args:     user_id: ID of the user     start: Start of the time range to get cycle events for     end: End of time range to get cycle events for     cycles_dao: CyclesDAO instance  Returns: List of cycle event data
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
        request_url = f"{self._uri}/data-sci-mdas/v2/cycles"

        # HTTP method selection based on the operation
        return self._get(
            url=request_url,
            return_type=List[ModelsApiV2CyclesResponsesMDASCycle],
            query_params=_query_params,
            data=_body_params,
        )

    def update_cycle_data_sci_mdas_v1_cycles_cycle_id_put(
        self,
        cycle_id: int,
        models_api_v1_cycles_requests_update_mdas_cycle_request: ModelsApiV1CyclesRequestsUpdateMDASCycleRequest,
    ) -> object:
        """
        PUT endpoint for updating an existing cycle event Note: This endpoint is for internal application use only. External customers should use the GET endpoints instead.  Args:     cycle_id: ID of the cycle event     update_cycles_request: Cycle event data     cycles_dao: CyclesDAO instance  Returns: None
        """
        # Process query parameters
        _query_params: list[tuple[str, Any]] = []

        # Process body parameter
        _body_params = None
        if models_api_v1_cycles_requests_update_mdas_cycle_request is not None:
            _body_params = models_api_v1_cycles_requests_update_mdas_cycle_request

        # Construct request URL
        request_url = f"{self._uri}/data-sci-mdas/v1/cycles/{cycle_id}"

        # HTTP method selection based on the operation
        return self._put(
            url=request_url,
            return_type=object,
            query_params=_query_params,
            data=_body_params,
        )

    def update_cycle_data_sci_mdas_v2_cycles_cycle_id_put(
        self,
        cycle_id: int,
        models_api_v2_cycles_requests_update_mdas_cycle_request: ModelsApiV2CyclesRequestsUpdateMDASCycleRequest,
    ) -> object:
        """
        PUT endpoint for updating an existing cycle event Note: This endpoint is for internal application use only. External customers should use the GET endpoints instead.  Args:     cycle_id: ID of the cycle event     update_cycles_request: Cycle event data     cycles_dao: CyclesDAO instance  Returns: None
        """
        # Process query parameters
        _query_params: list[tuple[str, Any]] = []

        # Process body parameter
        _body_params = None
        if models_api_v2_cycles_requests_update_mdas_cycle_request is not None:
            _body_params = models_api_v2_cycles_requests_update_mdas_cycle_request

        # Construct request URL
        request_url = f"{self._uri}/data-sci-mdas/v2/cycles/{cycle_id}"

        # HTTP method selection based on the operation
        return self._put(
            url=request_url,
            return_type=object,
            query_params=_query_params,
            data=_body_params,
        )
