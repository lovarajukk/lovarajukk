from aws_cdk import core
from pipelines_webinar_stack import PipelineWebinarStack
class WebServiceStage(core.Stage):
    def __init__(self, scope: core.Construct, id: str, **kwargs):
      super().__init__(scope,id,**kwargs)

    service = PipelineWebinarStack(self,'webservice')
    self.url_output = self.url_output