#!/usr/bin/env python
# -*- coding: utf-8 -*-


from aws_cdk import core
from aws_cdk import aws_codepipeline as codepipeline


class DemoStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Pipeline to connect to sample repo
        # Pull code and build a docker image
        pipeline = codepipeline.Pipeline(
            self,
            id="pipeline",
            pipeline_name="demo_pipeline",
            restart_execution_on_update=True,
        )
