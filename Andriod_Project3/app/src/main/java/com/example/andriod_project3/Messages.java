package com.example.andriod_project3;

import com.google.gson.annotations.SerializedName;

public class Messages {

    private int messageId;
    private int userId;
    private int parkingId;
    private String message;

    @SerializedName("body")
    private String text;

    public Messages(int messageId, int userId, int parkingId, String message) {
        this.messageId = messageId;
        this.userId = userId;
        this.parkingId = parkingId;
        this.message = message;
    }

    public int getMessageId() {
        return messageId;
    }

    public void setMessageId(int messageId) {
        this.messageId = messageId;
    }

    public int getUserId() {
        return userId;
    }

    public void setUserId(int userId) {
        this.userId = userId;
    }

    public int getParkingId() {
        return parkingId;
    }

    public void setParkingId(int parkingId) {
        this.parkingId = parkingId;
    }

    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }
}
