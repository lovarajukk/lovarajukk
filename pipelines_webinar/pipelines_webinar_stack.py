from os import path
from aws_cdk import core
    # aws_sqs as sqs,


# For consistency with other languages, `cdk` is the preferred import name for
# the CDK's core module.  The following line also imports it as `core` for use
# with examples from the CDK Developer's Guide, which are in the process of
# being updated to use `cdk`.  You may delete this import if you don't need it.
from aws_cdk import core
import aws_cdk.aws_lambda as lmb
import aws_cdk.aws_apigateway as apigw
import aws_cdk.aws_codedeploy as codedeploy
class PipelinesWebinarStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # The code that defines your stack goes here
        this_dir=path.dirname(__file__)
        handler=lmb.Function(self,'Handler',
          runtime=lmb.Runtime.PYTHON_3_8,
          handler='handler.handler',
          code=lmb.Code.from_asset(path.join(this_dir,'lambda'))
        )
        gw=apigw.LambdaRestApi(self, 'Gateway',
         description='End point for simple lamda powered webservice',
         handler=handler.current_version)

        self.url_output=core.CfnOutput(self,'url',
         value=gw.url)

        # example resource
        # queue = sqs.Queue(
        #     self, "PipelinesWebinarQueue",
        #     visibility_timeout=cdk.Duration.seconds(300),
        # )
