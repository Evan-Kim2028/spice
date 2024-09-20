from __future__ import annotations

from typing import Any, Literal, Mapping, Sequence, TypedDict, Union

from typing_extensions import NotRequired

import polars as pl


Query = Union[int, str]

Performance = Literal['medium', 'large']


class Execution(TypedDict):
    execution_id: str
    timestamp: NotRequired[int | None]


class ExecuteKwargs(TypedDict):
    query_id: int | None
    api_key: str | None
    parameters: Mapping[str, Any] | None
    performance: Performance


class PollKwargs(TypedDict):
    api_key: str | None
    poll_interval: float
    verbose: bool


class ResultKwargs(TypedDict):
    limit: int | None
    offset: int | None
    sample_count: int | None
    sort_by: str | None
    columns: Sequence[str] | None
    extras: Mapping[str, Any] | None
    dtypes: Sequence[type[pl.DataType]] | Mapping[str, type[pl.DataType]] | None
    verbose: bool
