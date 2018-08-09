mock_get_instance_metadata = """
{
    "ami-manifest-path": "(unknown)",
    "instance-action": "none",
    "ami-launch-index": "0",
    "instance-type": "t2.small",
    "local-ipv4": "123.45.67.89",
    "services": {
        "domain": "amazonaws.com",
        "partition": "aws"
    },
    "placement": {
        "availability-zone": "eu-west-2a"
    },
    "reservation-id": "r-123456789",
    "instance-id": "i-12345678",
    "profile": "default-hvm",
    "local-hostname": "ip-123-45-67-89.eu-west-2.compute.internal",
    "public-ipv4": "123-45-67-89",
    "mac": "06:01:6e:6b:7c:2a",
    "hostname": "ip-123-45-67-89.eu-west-2.compute.internal",
    "iam": {
        "info": {
            "InstanceProfileArn": "arn:aws:iam::123456789:instance-profile/example-arn",
            "Code": "Success",
            "InstanceProfileId": "ABCDEFGHIJKL",
            "LastUpdated": "2018-08-09T15:42:25Z"
        },
        "security-credentials": {
            "example-arn": {
                "Expiration": "2018-08-09T22:04:44Z",
                "Code": "Success",
                "Type": "AWS-HMAC",
                "SecretAccessKey": "nothing/here",
                "Token": "could/be",
                "LastUpdated": "2018-08-09T15:40:52Z",
                "AccessKeyId": "ABCDEFG"
            }
        }
    },
    "ami-id": "ami-123456",
    "public-hostname": "ec2-12-345-67-89.eu-west-2.compute.amazonaws.com"    
}
"""
