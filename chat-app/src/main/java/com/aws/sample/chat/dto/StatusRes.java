package com.aws.sample.chat.dto;

public class StatusRes {

    public StatusRes() {
    }

    private Integer statusCode = 200;

    public Integer getStatusCode() {
        return statusCode;
    }

    public void setStatusCode(Integer statusCode) {
        this.statusCode = statusCode;
    }
}
