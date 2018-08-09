import json

import pytest

import ec2_tag_conditional

from tests.mock_data import mock_get_instance_metadata


@pytest.fixture
def FakeEC2Instance(mocker):
    """
    Mock the instance so we get some return values from boto
    """
    mocked_metadata = mocker.patch(
        "ec2_tag_conditional.util.get_instance_metadata"
    )
    mocked_metadata.return_value = json.loads(mock_get_instance_metadata)


@pytest.fixture
def FakeTags(mocker):
    """
    Mock the instance so we get some return values from boto
    """
    mocked_set_tags = mocker.patch(
        "ec2_tag_conditional.util.InstanceTags._get_tags"
    )

    class FakeTag:
        __slots__ = 'name', 'value'

        def __init__(self, name, value):
            self.name = name
            self.value = value

    mocked_set_tags.return_value = [
        FakeTag('Env', 'prod')
    ]

def test_version_string():
    assert type(ec2_tag_conditional.version_info) == tuple
    assert type(ec2_tag_conditional.__version__) == str

def test_running_on_ec2_is_false(mocker):
    mocked_metadata = mocker.patch(
        "ec2_tag_conditional.util.get_instance_metadata"
    )
    mocked_metadata.return_value = {}
    with pytest.raises(ValueError) as excinfo:
        ec2_tag_conditional.util.InstanceTags()
    assert 'Not on an EC2 instance' in str(excinfo.value)



def test_running_on_ec2_is_true(FakeTags, FakeEC2Instance):
    tags = ec2_tag_conditional.util.InstanceTags()
    assert tags._is_on_ec2 == True

def test_keys(FakeEC2Instance, FakeTags):
    tags = ec2_tag_conditional.util.InstanceTags()
    assert 'Env' in tags.keys()
    assert tags['Env'] == 'prod'

def test_command_line(mocker, FakeEC2Instance, FakeTags):
    mocker.patch.object(ec2_tag_conditional.util.sys, 'argv', ['instance-tags', 'Env=prod'])
    with pytest.raises(SystemExit) as excinfo:
        ec2_tag_conditional.util.command_line()
    assert excinfo.type == SystemExit
    assert excinfo.value.code == 0

def test_command_line_fail(mocker, FakeEC2Instance, FakeTags):
    mocker.patch.object(ec2_tag_conditional.util.sys, 'argv', ['instance-tags', 'Fake=tag'])
    with pytest.raises(SystemExit) as excinfo:
        ec2_tag_conditional.util.command_line()
    assert excinfo.type == SystemExit
    assert excinfo.value.code == 1

def test_get_keys(FakeEC2Instance, FakeTags):
    tags = ec2_tag_conditional.util.InstanceTags()
    assert tags['foo'] == False
