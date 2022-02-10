package com.aws.sample.lambda.sample3;

import cn.hutool.json.JSONArray;
import cn.hutool.json.JSONObject;
import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.LambdaLogger;
import com.amazonaws.services.lambda.runtime.RequestHandler;
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;

import java.util.List;
import java.util.Map;


// Handler value: example.Handler
public class Handler implements RequestHandler<Map, String> {

    Gson gson = new GsonBuilder().setPrettyPrinting().create();

    @Override
    public String handleRequest(Map event, Context context) {
        LambdaLogger logger = context.getLogger();
        String response = new String("200 OK -- version 1.0");
        // log execution details
        logger.log("ENVIRONMENT VARIABLES: " + gson.toJson(System.getenv()));
        logger.log("CONTEXT: " + gson.toJson(context));
        logger.log("EVENT TYPE: " + event.getClass().toString());
        // process event
        String eventJson = gson.toJson(event);
        logger.log("EVENT: " + eventJson);
        JSONObject jsonObject = new JSONObject(eventJson);
        JSONArray jaRecords = jsonObject.getJSONArray("Records");
        JSONObject jsonObject0 = (JSONObject) jaRecords.get(0);
        String objectName = jsonObject0.getJSONObject("s3").getJSONObject("object").getStr("key", "no_name");

        logger.log("this process has been done");

        return response + " " + objectName;
    }
}