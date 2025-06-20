# coding: utf-8

"""
    FastAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations

from datetime import datetime
from typing import Optional, Union

from pydantic import Field, StrictBool, StrictFloat, StrictInt, StrictStr
from whoopcommons.model.whoop_model import WhoopModel

from data_sci_mdas.models.activity_source import ActivitySource
from data_sci_mdas.models.activity_state import ActivityState
from data_sci_mdas.models.date_time_tz_range import DateTimeTzRange


class UpdateMDASRecoveryRequest(WhoopModel):
    """
    All models should inherit from this. If they have special serialization concerns, they can override Config.  >>> class FunTime(WhoopModel): ...     name: str ...     start_time: datetime.datetime ... >>> d = { ... \"name\": \"yay\", ... \"start_time\": datetime.datetime(2020, 1, 1, hour=0, tzinfo=datetime.timezone.utc), ... \"extraBadField\": 3 ... } >>> FunTime(**d).json() '{\"name\": \"yay\", \"start_time\": \"2020-01-01T00:00:00.000+00:00\"}'  # noqa: E501
    """

    quality_duration: Optional[StrictInt] = None
    sleep_score: Optional[StrictInt] = None
    is_nap: Optional[StrictBool] = None
    var_date: datetime = Field(default=..., alias="date")
    user_id: StrictInt = Field(...)
    sleep_id: StrictInt = Field(...)
    cycle_id: Optional[StrictInt] = None
    recovery_score: Optional[StrictInt] = None
    resting_heart_rate: Optional[StrictInt] = None
    hrv_rmssd: Optional[Union[StrictFloat, StrictInt]] = None
    activity_state: Optional[ActivityState] = None
    is_calibrating: Optional[StrictBool] = None
    prod_covid: Optional[Union[StrictFloat, StrictInt]] = None
    hr_baseline: Optional[Union[StrictFloat, StrictInt]] = None
    skin_temp_celsius: Optional[Union[StrictFloat, StrictInt]] = None
    spo2: Optional[Union[StrictFloat, StrictInt]] = None
    algo_version: Optional[StrictStr] = None
    rhr_component: Optional[Union[StrictFloat, StrictInt]] = None
    hrv_component: Optional[Union[StrictFloat, StrictInt]] = None
    is_normal: Optional[StrictBool] = None
    history_size: Optional[Union[StrictFloat, StrictInt]] = None
    recovery_rate: Optional[Union[StrictFloat, StrictInt]] = None
    kilojoules: Optional[Union[StrictFloat, StrictInt]] = None
    during: DateTimeTzRange = Field(...)
    timezone_offset: Optional[StrictStr] = None
    timezone: Optional[StrictStr] = None
    survey_response_id: Optional[StrictInt] = None
    percent_recorded: Optional[Union[StrictFloat, StrictInt]] = None
    is_responded: Optional[StrictBool] = None
    activity_source: Optional[ActivitySource] = None
    score: StrictInt = Field(...)
    latency: Optional[StrictInt] = None
    is_significant: Optional[StrictBool] = None
    debt_pre: Optional[Union[StrictFloat, StrictInt]] = None
    debt_post: Optional[Union[StrictFloat, StrictInt]] = None
    need_from_strain: Optional[Union[StrictFloat, StrictInt]] = None
    sleep_need: Optional[Union[StrictFloat, StrictInt]] = None
    habitual_sleep_need: Optional[Union[StrictFloat, StrictInt]] = None
    disturbances: Optional[Union[StrictFloat, StrictInt]] = None
    time_in_bed: Optional[Union[StrictFloat, StrictInt]] = None
    light_sleep_duration: Optional[StrictInt] = None
    slow_wave_sleep_duration: Optional[StrictInt] = None
    rem_sleep_duration: Optional[StrictInt] = None
    cycles_count: Optional[StrictInt] = None
    wake_duration: Optional[StrictInt] = None
    arousal_time: Optional[Union[StrictFloat, StrictInt]] = None
    no_data_duration: Optional[StrictInt] = None
    in_sleep_efficiency: Optional[Union[StrictFloat, StrictInt]] = None
    credit_from_naps: Optional[Union[StrictFloat, StrictInt]] = None
    respiratory_rate: Optional[Union[StrictFloat, StrictInt]] = None
    sleep_consistency: Optional[Union[StrictFloat, StrictInt]] = None
    projected_score: Optional[Union[StrictFloat, StrictInt]] = None
    projected_sleep: Optional[Union[StrictFloat, StrictInt]] = None
    optimal_sleep_times: Optional[DateTimeTzRange] = None
    created_at: datetime = Field(...)
    updated_at: datetime = Field(...)
