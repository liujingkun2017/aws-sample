package com.aws.sample.chat.dto;

public class ConnectionInfo {

    public ConnectionInfo() {
    }

    public ConnectionInfo(String connectionId) {
        this.connectionId = connectionId;
    }

    private String connectionId;

    public String getConnectionId() {
        return connectionId;
    }

    public void setConnectionId(String connectionId) {
        this.connectionId = connectionId;
    }

}
