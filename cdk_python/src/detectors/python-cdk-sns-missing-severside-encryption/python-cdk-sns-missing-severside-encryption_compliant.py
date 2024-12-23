# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

# {fact rule=python-cdk-sns-missing-severside-encryption@v1.0 defects=0}
import aws_cdk as cdk
from aws_cdk.aws_sns import Topic, TopicEncryption
from aws_cdk.aws_kms import Key

class CdkStarter(cdk.Stack):
    def __init__(self, scope: cdk.App, id: str):
        super(scope, id)

        # Compliant: SNS topics is encrypted via `master_key`.
        Topic(self, "rTopic", 
            master_key=Key(self, "rKey"),
            encryption=TopicEncryption.KMS
        )
# {/fact}