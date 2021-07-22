from example.messages.ender_after_cron_answer_message import EnderAfterCronAnswerMessage
from example.messages.ender_after_cron_input_message import EnderAfterCronInputMessage
from unipipeline.modules.uni_worker import UniWorker
from unipipeline.modules.uni_worker_consumer_message import UniWorkerConsumerMessage

from unipipeline.messages.uni_cron_message import UniCronMessage
from unipipeline.modules.uni_answer_message import UniAnswerMessage


class MySuperCronWorker(UniWorker[UniCronMessage, None]):
    def handle_message(self, msg: UniWorkerConsumerMessage[UniCronMessage]) -> None:
        answ: UniAnswerMessage[EnderAfterCronAnswerMessage] = self.manager.get_answer_from('ender_after_cron_worker', EnderAfterCronInputMessage(value=f'cron>>>{msg.payload.task_name}'))

        print(answ.payload.value)
