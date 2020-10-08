import pytest
from t7_smart_vk_api.browser.browser_factory import Browser
from t7_smart_vk_api.logger.logger import log
from t7_smart_vk_api import CONFIG_DATA
from t7_smart_vk_api.testrail.testrail_client import client, screenshot


@pytest.fixture(params=[CONFIG_DATA["BROWSER"]], scope="session", autouse=True)
def browser(request):
    log.debug('Set-up')
    driver = Browser.get_browser_by_name(request.param)

    log.debug('Maximize browser window')
    driver.maximize_window()

    yield driver

    log.debug('Save screenshot')
    driver.save_screenshot(screenshot)

    log.debug('Tear-down')
    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    setattr(item, "rep_" + rep.when, rep)

@pytest.fixture()
def result(request, tr_test_id):
    yield
    status_id = 0
    comment = ""
    log.debug('Setting result')
    if request.node.rep_call.passed:
        status_id = 1
        comment = "Passed for {}".format(request.node.nodeid)
    if request.node.rep_call.failed:
        status_id = 5
        comment = "Failed for {}".format(request.node.nodeid)
    send_results_to_testrail(status_id, comment, tr_test_id)


def send_results_to_testrail(status, comment, test_id):
    log.debug('Sending results to TestRail')

    add_result = client.send_post(f'add_result/{test_id}', data={
        "status_id": status,
        "comment": comment,
    })

    result_id = add_result['id']
    client.send_post(f'add_attachment_to_result/{result_id}', screenshot)