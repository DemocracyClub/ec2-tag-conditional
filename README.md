# EC2 Tag conditionals
[![CircleCI](https://circleci.com/gh/DemocracyClub/ec2-tag-conditional/tree/master.svg?style=svg)](https://circleci.com/gh/DemocracyClub/ec2-tag-conditional/tree/master)
[![Coverage Status](https://coveralls.io/repos/github/DemocracyClub/ec2-tag-conditional/badge.svg?branch=master)](https://coveralls.io/github/DemocracyClub/ec2-tag-conditional?branch=master)

This is a python library and shell command that is designed to be run on AWS's EC2 instances.

It will always fail if it's not on AWS, so tags should only be tested for truthiness, not falseness.

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

