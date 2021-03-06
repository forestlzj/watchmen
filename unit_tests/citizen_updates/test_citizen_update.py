# Copyright 2017 Insurance Australia Group Limited
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from citizen_updates.update_citizen_stacks.citizen_update \
    import get_citizen_stacks, is_aws_account_id

_single_citizen_stack = [
    {
        'StackId': 'arn:aws:cloudformation:ap-southeast-2:1234567890:stack/Citizen/7851f78f-c79e-4a9a-b9e9-0d975f18f8de',
        'Description': 'Watchmen-Citizen Compliance Rules Version XXX-CITIZEN-VERSION-XXX',
        'StackName': 'Citizen',
        'StackStatus': 'CREATE_COMPLETE'
    }
]

_multiple_stacks_one_citizen = [
    {
        'StackId': 'arn:aws:cloudformation:ap-southeast-2:1234567890:stack/Citizen/7851f78f-c79e-4a9a-b9e9-0d975f18f8de',
        'Description': 'Watchmen-Citizen Compliance Rules Version XXX-CITIZEN-VERSION-XXX',
        'StackName': 'Citizen',
        'StackStatus': 'CREATE_COMPLETE'
    },
    {
        'StackId': 'arn:aws:cloudformation:ap-southeast-2:1234567890:stack/SomeOtherStack/8a972533-dadc-4a75-adae-fcd03e05d31d',
        'Description': 'This is some other stack, it does something else',
        'StackName': 'SomeOtheStack',
        'StackStatus': 'CREATE_COMPLETE'
    }
]

_multiple_stacks_no_citizens = [
    {
        'StackId': 'arn:aws:cloudformation:ap-southeast-2:1234567890:stack/SomeOtherStack/8a972533-dadc-4a75-adae-fcd03e05d31d',
        'Description': 'This is some other stack, it does something else',
        'StackName': 'SomeOtheStack',
        'StackStatus': 'CREATE_COMPLETE'
    },
    {
        'StackId': 'arn:aws:cloudformation:ap-southeast-2:1234567890:stack/AnotherStack/fa1f317f-610b-4d7c-a8fa-5c40f515fb56',
        'Description': 'This is another stack',
        'StackName': 'AnotherStack',
        'StackStatus': 'CREATE_COMPLETE'
    }
]

_no_stacks = []


_valid_aws_account_id = '123456789012'
_invalid_aws_account_id = '123'

class TestCitizenUpdate(object):

    def test_single_citizen_stacks(self):
        stacks = _single_citizen_stack
        citizen_stacks = get_citizen_stacks(stacks, "")
        assert citizen_stacks == [
            {
                'StackName': 'Citizen',
                'StackId': 'arn:aws:cloudformation:ap-southeast-2:1234567890:stack/Citizen/7851f78f-c79e-4a9a-b9e9-0d975f18f8de',
                'Version': 'XXX-CITIZEN-VERSION-XXX',
                'StackStatus': 'CREATE_COMPLETE'
            }
        ]

    def test_multiple_stacks(self):
        stacks = _multiple_stacks_one_citizen
        citizen_stacks = get_citizen_stacks(stacks, "")
        assert citizen_stacks == [
            {
                'StackName': 'Citizen',
                'StackId': 'arn:aws:cloudformation:ap-southeast-2:1234567890:stack/Citizen/7851f78f-c79e-4a9a-b9e9-0d975f18f8de',
                'Version': 'XXX-CITIZEN-VERSION-XXX',
                'StackStatus': 'CREATE_COMPLETE'
            }
        ]

    def test_multiple_stacks_no_citizens(self):
        stacks = _multiple_stacks_no_citizens
        citizen_stacks = get_citizen_stacks(stacks, "")
        assert citizen_stacks == []

    def test_no_stacks(self):
        stacks = _no_stacks
        citizen_stacks = get_citizen_stacks(stacks, "")
        assert citizen_stacks == []

    def test_valid_account_id(self):
        account_id = _valid_aws_account_id
        match = is_aws_account_id(account_id)
        assert match

    def test_invalid_account_id(self):
        account_id = _invalid_aws_account_id
        match = is_aws_account_id(account_id)
        assert match == None