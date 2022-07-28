import aws_cdk as core
import aws_cdk.assertions as assertions

from my_s3_deployment.my_s3_deployment_stack import MyS3DeploymentStack

# example tests. To run these tests, uncomment this file along with the example
# resource in my_s3_deployment/my_s3_deployment_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = MyS3DeploymentStack(app, "my-s3-deployment")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
