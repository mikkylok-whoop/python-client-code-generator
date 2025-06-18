from typing import Optional

from datadog import DogStatsd
from whoop_service_clients.base.client import BaseApiClient

from data_sci_mdas.models.health_check import HealthCheck


class DefaultApi(BaseApiClient):
    def __init__(self, uri: str, statsd_client: Optional[DogStatsd] = None) -> None:
        self._uri = uri
        super().__init__(service_uri=self._uri, statsd_client=statsd_client)

    def check_health_healthcheck_get(
        self,
    ) -> HealthCheck:
        """ """
        # Process query parameters
        _query_params: list[tuple[str, Any]] = []

        # Process body parameter
        _body_params = None

        # Construct request URL
        request_url = f"{self._uri}/healthcheck"

        # HTTP method selection based on the operation
        return self._get(
            url=request_url,
            return_type=HealthCheck,
            query_params=_query_params,
            data=_body_params,
        )
