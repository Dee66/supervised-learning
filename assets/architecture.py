from diagrams import Diagram, Cluster
from diagrams.aws.compute import Lambda, ECS, EC2ContainerRegistry as ECR
from diagrams.aws.ml import Sagemaker
from diagrams.aws.storage import S3
from diagrams.aws.security import IAM, SecretsManager, KMS
from diagrams.aws.management import Cloudwatch, SystemsManagerParameterStore
from diagrams.aws.network import ALB, VPC
from diagrams.aws.general import User

with Diagram(
    "CodeCraft AI Production Architecture",
    show=False,
    filename="assets/architecture",
    outformat="png",
    direction="LR",
    graph_attr={
        "dpi": "240",
        "fontname": "Arial",
        "ranksep": "2.0",
        "nodesep": "2.2",   # Increased for more horizontal gap between clusters
        "margin": "0.7",
        "pad": "0.9",
    },
    node_attr={
        "fontname": "Arial",
        "fontsize": "20",
        "margin": "0.6,1.2",
        "labelloc": "b",
    }
):
    user = User("User/API\n")
    alb = ALB("ALB\n")
    vpc = VPC("VPC\n")

    # Main ML & Data pipeline
    with Cluster("ML & Data Pipeline", graph_attr={"labeljust": "c", "fontsize": "26"}):
        ecs = ECS("ECS (Fargate)\n")
        lam = Lambda("Lambda\n")
        sm = Sagemaker("SageMaker\n")
        s3 = S3("S3\n")
        ecr = ECR("ECR\n")
        ecs >> [lam, sm, s3, ecr]
        s3 >> sm
        sm >> ecr

    # Add invisible node to force a gap between clusters
    from diagrams.aws.storage import S3 as S3Spacer
    gap = S3Spacer("", style="invis")
    sm >> gap  # Connect last ML node to invisible node (no effect on logic, just layout)

    # Security & Config (supporting, not main flow)
    with Cluster("Security & Config", graph_attr={"margin": "32", "fontsize": "26"}):
        secrets = SecretsManager("Secrets Manager\n")
        ssm = SystemsManagerParameterStore("SSM Param Store\n")
        iam = IAM("IAM\n")
        kms = KMS("KMS\n")
        [secrets, ssm, iam, kms] >> ecs

    # Observability (supporting)
    with Cluster("Observability", graph_attr={"margin": "32", "fontsize": "26"}):
        cloudwatch = Cloudwatch("CloudWatch\n")
        [ecs, lam, sm, s3] >> cloudwatch

    # Main user/API flow
    user >> alb >> vpc >> ecs