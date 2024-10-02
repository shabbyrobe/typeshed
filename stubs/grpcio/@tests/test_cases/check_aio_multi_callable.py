from __future__ import annotations

import typing
from typing_extensions import assert_type

import grpc.aio


class DummyRequest:
    pass


class DummyReply:
    pass


class DummyServiceStub(typing.Protocol):
    UnaryUnary: grpc.aio.UnaryUnaryMultiCallable[DummyRequest, DummyReply]
    UnaryStream: grpc.aio.UnaryStreamMultiCallable[DummyRequest, DummyReply]
    StreamUnary: grpc.aio.StreamUnaryMultiCallable[DummyRequest, DummyReply]
    StreamStream: grpc.aio.StreamStreamMultiCallable[DummyRequest, DummyReply]


stub: DummyServiceStub = typing.cast(typing.Any, None)
req = DummyRequest()


async def async_context() -> None:
    assert_type(await stub.UnaryUnary(req), DummyReply)

    async for resp in stub.UnaryStream(req):
        assert_type(resp, DummyReply)

    assert_type(await stub.StreamUnary(iter([req])), DummyReply)

    async for resp in stub.StreamStream(iter([req])):
        assert_type(resp, DummyReply)