package com.aws.sample.lambda.sample5;

import com.amazonaws.client.builder.AwsClientBuilder;
import com.amazonaws.regions.Regions;
import com.amazonaws.services.dynamodbv2.AmazonDynamoDB;
import com.amazonaws.services.dynamodbv2.AmazonDynamoDBClientBuilder;
import com.amazonaws.services.dynamodbv2.model.ListTablesResult;
import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.LambdaLogger;
import com.amazonaws.services.lambda.runtime.RequestHandler;
import com.amazonaws.services.lambda.runtime.events.APIGatewayV2HTTPEvent;
import com.amazonaws.services.lambda.runtime.events.APIGatewayV2HTTPResponse;
import com.amazonaws.services.s3.AmazonS3;
import com.amazonaws.services.s3.AmazonS3ClientBuilder;
import com.amazonaws.services.s3.model.Bucket;
import com.aws.sample.lambda.sample5.dto.ResponseDTO;
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.dynamodb.DynamoDbClient;

import java.util.List;
import java.util.Map;


// Handler value: example.Handler
public class Handler implements RequestHandler<APIGatewayV2HTTPEvent, APIGatewayV2HTTPResponse> {

    Gson gson = new GsonBuilder().setPrettyPrinting().create();

    @Override
    public APIGatewayV2HTTPResponse handleRequest(APIGatewayV2HTTPEvent event, Context context) {
        LambdaLogger logger = context.getLogger();

//        String response = new String("200 OK -- version 1.0");
        // log execution details
        logger.log("ENVIRONMENT VARIABLES: " + gson.toJson(System.getenv()));
        logger.log("CONTEXT: " + gson.toJson(context));
        // process event
        logger.log("EVENT: " + gson.toJson(event));
        logger.log("EVENT TYPE: " + event.getClass().toString());

        logger.log("this process has been done");


//        AwsClientBuilder.EndpointConfiguration configuration =
//                new AwsClientBuilder.EndpointConfiguration("s3.us-east-1.amazonaws.com", "us-east-1");
//        AmazonS3 s3 = AmazonS3ClientBuilder.standard()
//                .withEndpointConfiguration(configuration)
//                .build();
//
//        List<Bucket> buckets = s3.listBuckets();
//        logger.log("Your Amazon S3 buckets are:");
//        for (Bucket b : buckets) {
//            logger.log("* " + b.getName());
//        }


//        DynamoDbClient ddb = DynamoDbClient.builder().region(Region.US_EAST_1).build();

        AwsClientBuilder.EndpointConfiguration configuration = new AwsClientBuilder.EndpointConfiguration("dynamodb.us-east-1.amazonaws.com", "us-east-1");

        AmazonDynamoDB client = AmazonDynamoDBClientBuilder.standard().withEndpointConfiguration(configuration).build();

        ListTablesResult result = client.listTables();


        APIGatewayV2HTTPResponse response = new APIGatewayV2HTTPResponse();
        response.setStatusCode(200);
        response.setBody("200 OK -- version 1.0 size" + result.getTableNames());

        return response;
    }
}