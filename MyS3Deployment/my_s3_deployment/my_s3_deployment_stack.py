#https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.aws_s3_deployment/README.html
#https://aws.amazon.com/getting-started/guides/setup-cdk/
#https://constructs.dev/search?q=AWS&offset=0
#https://docs.aws.amazon.com/cdk/v2/guide/work-with-cdk-python.html
#https://github.com/aws/aws-cdk


# 衍生執行項目
# 1. 文件内容修改
# 2. 檔案位置移動

from aws_cdk import (
    # Duration,
    Stack,
    aws_s3 as s3,
    aws_s3_deployment as s3deploy
)
from constructs import Construct
import aws_cdk

class MyS3DeploymentStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        website_bucket = s3.Bucket(self, "WebsiteBucket",
            website_index_document="index.html",
            public_read_access=True
        )

        s3deploy.BucketDeployment(self, "DeployWebsite",
            sources=[s3deploy.Source.asset("./website-dist")],
            destination_bucket=website_bucket,
            destination_key_prefix="web/static"
        )

