package com.aws.sample.chat.dto;


public class RequestCliInfo {

    public RequestCliInfo() {
    }

    public RequestCliInfo(ConnectionInfo requestContext) {
        this.requestContext = requestContext;
    }

    private ConnectionInfo requestContext;

    public ConnectionInfo getRequestContext() {
        return requestContext;
    }

    public void setRequestContext(ConnectionInfo requestContext) {
        this.requestContext = requestContext;
    }

}
