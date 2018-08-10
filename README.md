# EC2 Tag conditionals
[![CircleCI](https://circleci.com/gh/DemocracyClub/ec2-tag-conditional/tree/master.svg?style=svg)](https://circleci.com/gh/DemocracyClub/ec2-tag-conditional/tree/master)
[![Coverage Status](https://coveralls.io/repos/github/DemocracyClub/ec2-tag-conditional/badge.svg?branch=master)](https://coveralls.io/github/DemocracyClub/ec2-tag-conditional?branch=master)



This is a python library and shell command that answers the question:

"Is this instance tagged with the given tag and have a given value"

It is designed to be run on AWS's EC2 instances.

It will always fail if it's not on AWS, so tags should only be tested for
truthiness, not falseness.



## As a Library


```python

from ec2_tag_conditional import InstanceTags

tags = InstanceTags()

if tags['Env'] == 'prod':
    do_prod_thing()
 else:
    do_other_thing()

```


## As a command line script

```shell

> instance-tags "Env=prod"
> echo $?
0

> instance-tags "Madeup=NotThere"
> echo $?
1

> instance-tags "Env=prod" && do_prod_thing

```

## Example use cases

This code was written with the following use case in mind:

You have `n` servers in a auto scaling group, launched from a custom
AMI (golden image). The nature of the application running on the
servers is that, for some functions to work (backup, reporting),
a given set of tasks should only be run by one server.

This server is called a 'controller'. The script that created the ASG
also tags (in the AWS metadata) one (and only one) of the servers
with `controller=True`.

When the AMI is baked, the images don't need to know if they are a
controller or not, as cron tasks can be written like:

`instance-tags "controller=True" && do_controller_only`

Or for controllers in production (rather than dev or staging
environments):

`instance-tags "controller=True" && instance-tags "Env=prod" && do_controller_only`

Because the exit code of the `instance-tags` script is 1 if the tag
with the given value isn't found on the instance, the script wont
run on any server that isn't an EC2 instance with the given values.
