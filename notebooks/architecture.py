from diagrams import Diagram
from diagrams.custom import Custom

with Diagram("CodeCraft AI Production Architecture", show=False, filename="architecture", outformat="svg"):
    user = Custom("User/API", "../Architecture-Group-Icons_02072025/AWS-Account_32.png")
    alb = Custom("ALB", "../Architecture-Service-Icons_02072025/Arch_Networking-Content-Delivery/Arch_Application-Load-Balancer_48.png")
    ecs = Custom("ECS (Fargate)", "../Architecture-Service-Icons_02072025/Arch_Containers/Arch_Amazon-Elastic-Container-Service_ECS_48.png")
    lam = Custom("Lambda", "../Architecture-Service-Icons_02072025/Arch_Compute/Arch_AWS-Lambda_48.png")
    ecr = Custom("ECR", "../Architecture-Service-Icons_02072025/Arch_Containers/Arch_Amazon-Elastic-Container-Registry_ECR_48.png")
    sm = Custom("SageMaker", "../Architecture-Service-Icons_02072025/Arch_Artificial-Intelligence/Arch_Amazon-SageMaker_48.png")
    s3 = Custom("S3", "../Architecture-Service-Icons_02072025/Arch_Storage/Arch_Amazon-Simple-Storage-Service_S3_48.png")
    secrets = Custom("Secrets Manager", "../Architecture-Service-Icons_02072025/Arch_Security-Identity-Compliance/Arch_AWS-Secrets-Manager_48.png")
    cloudwatch = Custom("CloudWatch", "../Architecture-Service-Icons_02072025/Arch_Monitoring-Management/Arch_Amazon-CloudWatch_48.png")
    iam = Custom("IAM", "../Architecture-Service-Icons_02072025/Arch_Security-Identity-Compliance/Arch_AWS-Identity-Access-Management_IAM_48.png")

    user >> alb >> ecs
    ecs >> [lam, ecr, sm, s3, secrets, cloudwatch, iam]
    lam >> sm
    ecr >> s3
    sm >> cloudwatch
    s3 >> cloudwatch