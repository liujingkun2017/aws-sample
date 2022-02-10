package com.aws.sample.lambda.sample2;

import com.amazonaws.regions.Region;
import com.amazonaws.regions.Regions;
import com.amazonaws.services.dynamodbv2.AmazonDynamoDBClient;
import com.amazonaws.services.dynamodbv2.document.DynamoDB;
import com.amazonaws.services.dynamodbv2.document.Item;
import com.amazonaws.services.dynamodbv2.document.PutItemOutcome;
import com.amazonaws.services.dynamodbv2.document.spec.PutItemSpec;
import com.amazonaws.services.dynamodbv2.model.ConditionalCheckFailedException;
import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.LambdaLogger;
import com.amazonaws.services.lambda.runtime.RequestHandler;
import com.aws.sample.lambda.sample2.dto.PersonRequest;
import com.aws.sample.lambda.sample2.dto.PersonResponse;

import java.util.UUID;


// Handler value: example.Handler
public class Handler implements RequestHandler<PersonRequest, PersonResponse> {

    private DynamoDB dynamoDB;

    private String DYNAMODB_TABLE_NAME = "Person";

    private Regions REGION = Regions.US_EAST_1;

    @Override
    public PersonResponse handleRequest(PersonRequest request, Context context) {

        LambdaLogger logger = context.getLogger();

        this.initDynamoDbClient();

        persistData(request);

        logger.log("this process has been done");
        PersonResponse response = new PersonResponse();
        return response;
    }

    private PutItemOutcome persistData(PersonRequest personRequest) throws ConditionalCheckFailedException {

        personRequest.setId(UUID.randomUUID().toString());

        return this.dynamoDB.getTable(DYNAMODB_TABLE_NAME).putItem(new PutItemSpec()
                .withItem(new Item()
                        .withString("id", personRequest.getId())
                        .withString("name", personRequest.getName())
                        .withString("sex", personRequest.getSex())
                        .withInt("age", personRequest.getAge())));
    }

    private void initDynamoDbClient() {
        AmazonDynamoDBClient client = new AmazonDynamoDBClient();
        client.setRegion(Region.getRegion(REGION));
        this.dynamoDB = new DynamoDB(client);
    }
}