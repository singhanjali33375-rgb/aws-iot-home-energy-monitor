import json
import boto3

cloudwatch = boto3.client("cloudwatch")

def lambda_handler(event, context):
    device_id = event["deviceId"]
    power_usage = event["powerUsage"]

    cloudwatch.put_metric_data(
        Namespace="HomeEnergyMonitor",
        MetricData=[
            {
                "MetricName": "PowerUsage",
                "Dimensions": [
                    {
                        "Name": "DeviceId",
                        "Value": device_id
                    }
                ],
                "Value": power_usage,
                "Unit": "KilowattHours"
            }
        ]
    )

    return {
        "statusCode": 200,
        "message": "Energy data processed successfully"
    }
