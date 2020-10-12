from enum import Enum
from t7_smart_vk_api.logger.logger import log
from t7_smart_vk_api.testrail.testrail_client import client, screenshot


def send_results_to_testrail(status, comment, test_id):
    log.debug('Sending results to TestRail')

    add_result = client.send_post(f'add_result/{test_id}', data={
        "status_id": status,
        "comment": comment,
    })

    result_id = add_result['id']
    client.send_post(f'add_attachment_to_result/{result_id}', screenshot)


class ResultStatuses(Enum):
    passed = 1
    failed = 5
