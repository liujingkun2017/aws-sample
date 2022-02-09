package com.aws.sample.chat;

import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.LambdaLogger;
import com.amazonaws.services.lambda.runtime.RequestHandler;
import com.aws.sample.chat.dto.RequestCliInfo;
import com.aws.sample.chat.dto.StatusRes;
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;


public class ConnectHandler implements RequestHandler<RequestCliInfo, StatusRes> {

    Gson gson = new GsonBuilder().setPrettyPrinting().create();

    @Override
    public StatusRes handleRequest(RequestCliInfo input, Context context) {

        LambdaLogger logger = context.getLogger();
//        String response = new String("200 OK -- version 1.0");
        // log execution details
        logger.log("ENVIRONMENT VARIABLES: " + gson.toJson(System.getenv()));
        logger.log("CONTEXT: " + gson.toJson(context));
        // process event
        logger.log("EVENT: " + gson.toJson(input));

        StatusRes statusRes = new StatusRes();

        return statusRes;
    }


}
