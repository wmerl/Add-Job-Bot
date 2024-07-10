import os

from dotenv import load_dotenv
from pyromod.helpers import ikb
from pyromod.helpers import helpers as pyromod_helpers

load_dotenv()


class Consts(object):

    API_ID: int = int(os.environ.get('API_ID'))
    API_HASH: str = os.environ.get('API_HASH')
    BOT_TOKEN: str = os.environ.get('BOT_TOKEN')

    TIMEOUT: int = 60

    JOB_POST: str = """
Job Title: {}
Seniority: {}
Job Link: {}
""".strip()

    ADMIN_IDS = [1752221538, 7018217656]
    PUBLIC_CHANNEL = -1002154219279  # Targeted Channel where will the jobs posted at the final step
    ADMINS_GROUP_ID = -1002091947120  # Admins Group that Varify / Reject The jobs
    GROUP_LINK = 'https://t.me/auto_job_poster'


class Buttons(object):

    ADD_JOB_BUTTONS: pyromod_helpers = ikb(
        [
            [("Add Job", "add_job")],
        ]
    )

    DEV_TYPE_BUTTONS: pyromod_helpers = ikb(
        [
            [("Java Developer", "java_dev")],
            [("iOS Developer", "ios_dev")],
            [("Flutter Developer", "flutter_dev")],
            [("Android Developer", "android_dev")],
            [("QA Engineer", "qa_engineer")],
        ]
    )

    SENIORITY_BUTTONS: pyromod_helpers = ikb(
        [
            [("Intern", "intern")],
            [("Junior", "junior")],
            [("Middle", "middle")],
            [("Senior", "senior")],
            [("Lead", "lead")],
            [("Architect", "architect")],
        ]
    )

    SUBMIT_BUTTONS: pyromod_helpers = ikb(
        [
            [("Submit ✅", "submit")],
            [("Cancel ❌", "cancel")],
        ]
    )

    APPROVING_BUTTONS: pyromod_helpers = ikb(
        [
            [("Varify ✅", "verify")],
            [("Reject ❌", "reject")],
        ]
    )

    JOIN_GROUP_BUTTONS: pyromod_helpers = ikb([
        [('Group', Consts.GROUP_LINK, 'url')],
        [('Joined ✅', 'joined')]

    ])


class Tags(object):

    LIST: dict[str: str] = {
        "java_dev": '#java',
        "ios_dev": '#ios',
        "flutter_dev": '#flutter',
        "android_dev": '#android',
        "qa_engineer": '#qa',
    }