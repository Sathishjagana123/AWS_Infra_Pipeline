from aws_cdk import (
    Stack,
    aws_s3 as s3,
    RemovalPolicy,
)
from constructs import Construct

class CdkS3BucketStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create S3 bucket with a specific name
        bucket = s3.Bucket(
            self, 
            "MyS3Bucket",
            bucket_name="demo-cdk-code-catalyst-sathish",  
            encryption=s3.BucketEncryption.S3_MANAGED,  # Enable server-side encryption
            block_public_access=s3.BlockPublicAccess.BLOCK_ALL,  # Block all public access
            removal_policy=RemovalPolicy.RETAIN,  # Retain the bucket when stack is destroyed
            enforce_ssl=True  # Enforce SSL when accessing the bucket
        )
