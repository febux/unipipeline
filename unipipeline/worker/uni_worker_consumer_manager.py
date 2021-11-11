from typing import Callable, Union, Type, Any, Optional, Dict, TYPE_CHECKING, TypeVar
from uuid import uuid4, UUID

from unipipeline.answer.uni_answer_message import UniAnswerMessage
from unipipeline.message.uni_message import UniMessage

if TYPE_CHECKING:
    from unipipeline.worker.uni_worker import UniWorker


TInputMessage = TypeVar('TInputMessage', bound=UniMessage)
TAnswMessage = TypeVar('TAnswMessage', bound=UniMessage)


class UniWorkerConsumerManager:
    def __init__(self, send: Callable[[Union[Type['UniWorker[Any, Any]'], str], Union[Dict[str, Any], UniMessage], bool, bool], Optional[UniAnswerMessage[UniMessage]]]) -> None:
        self._send = send
        self._id = uuid4()

    @property
    def id(self) -> UUID:
        return self._id

    def stop_consuming(self) -> None:
        pass  # TODO

    def exit(self) -> None:
        pass  # TODO

    def get_answer_from(self, worker: Union[Type['UniWorker[TInputMessage, TAnswMessage]'], str], data: Union[Dict[str, Any], TInputMessage]) -> UniAnswerMessage[TAnswMessage]:
        return self._send(worker, data, False, True)  # type: ignore

    def send_to(self, worker: Union[Type['UniWorker[Any, Any]'], str], data: Union[Dict[str, Any], UniMessage], alone: bool = False) -> None:
        self._send(worker, data, alone, False)