package com.aws.sample.lambda.sample2.dto;

public class PersonResponse {

    public PersonResponse() {

    }

    private Integer status = 200;
    private String message = "success";

    public Integer getStatus() {
        return status;
    }

    public void setStatus(Integer status) {
        this.status = status;
    }

    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }
}
